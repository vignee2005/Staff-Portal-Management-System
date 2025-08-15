from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'cat'

# MySQL configuration
db_config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'staff_portal'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM admins WHERE email = %s AND password = %s', (email, password))
        admin = cursor.fetchone()
        conn.close()
        if admin:
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid email or password')
    return render_template('admin_login.html')

@app.route('/user_login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['user_logged_in'] = True
            session['user_id'] = user['id']
            flash('Login successful!')
            return redirect(url_for('user_dashboard'))
        else:
            flash('Invalid email or password.')
    return render_template('user_login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.')
    return redirect(url_for('index'))

@app.route('/user_dashboard')
def user_dashboard():
    if 'user_logged_in' not in session:
        return redirect(url_for('user_login'))
    return render_template('user_dashboard.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    if 'admin_logged_in' not in session:
        return redirect(url_for('admin_login'))
    return render_template('admin_dashboard.html')

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if not email or not password:
            flash('Email and password are required!')
            return redirect(url_for('add_user'))

        connection = get_db_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute('INSERT INTO users (email, password) VALUES (%s, %s)', (email, password))
            connection.commit()
            flash('User added successfully!')
        except mysql.connector.Error as err:
            flash(f'Error: {err}')
        finally:
            cursor.close()
            connection.close()

        return redirect(url_for('admin_dashboard'))

    return render_template('add_user.html')

@app.route('/remove_user', methods=['GET', 'POST'])
def remove_user():
    if request.method == 'POST':
        email = request.form['email']

        if not email:
            flash('Email is required!')
            return redirect(url_for('remove_user'))

        connection = get_db_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute('DELETE FROM users WHERE email = %s', (email,))
            connection.commit()
            
            if cursor.rowcount > 0:
                flash('User removed successfully!')
            else:
                flash('No user found with that email.')
        except mysql.connector.Error as err:
            flash(f'Error: {err}')
        finally:
            cursor.close()
            connection.close()

        return redirect(url_for('admin_dashboard'))

    return render_template('remove_user.html')

@app.route('/staff_information', methods=['GET', 'POST'])
def staff_information():
    if 'user_logged_in' not in session:
        return redirect(url_for('user_login'))

    user_id = session['user_id']
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        data = request.form.to_dict()
        cursor.execute('''
            UPDATE staff_details SET 
                name=%s, designation=%s, department=%s, qualification=%s, dob=%s, age=%s, gender=%s, 
                mother_tongue=%s, mobile=%s, alternate_mobile=%s, personal_email=%s, college_email=%s, 
                nationality=%s, religion=%s, community=%s, caste=%s, salary=%s, experience=%s, 
                doj_designation=%s, doj_institution=%s, blood_group=%s, aadhar=%s, address_comm=%s, 
                address_perm=%s, degree=%s, specialization=%s, college_name=%s, university=%s, 
                year_of_passing=%s, percentage=%s, pan_card=%s, bank_account=%s, bank_name=%s, 
                branch_name=%s, ifsc=%s 
            WHERE user_id=%s
        ''', (
            data.get('name'), data.get('designation'), data.get('department'), data.get('qualification'), 
            data.get('dob'), data.get('age'), data.get('gender'), data.get('mother_tongue'), data.get('mobile'), 
            data.get('alternate_mobile'), data.get('personal_email'), data.get('college_email'), data.get('nationality'), 
            data.get('religion'), data.get('community'), data.get('caste'), data.get('salary'), data.get('experience'), 
            data.get('doj_designation'), data.get('doj_institution'), data.get('blood_group'), data.get('aadhar'), 
            data.get('address_comm'), data.get('address_perm'), data.get('degree'), data.get('specialization'), 
            data.get('college_name'), data.get('university'), data.get('year_of_passing'), data.get('percentage'), 
            data.get('pan_card'), data.get('bank_account'), data.get('bank_name'), data.get('branch_name'), data.get('ifsc'), 
            user_id
        ))
        conn.commit()
        flash('Information updated successfully')
        return redirect(url_for('view_information'))

    cursor.execute('SELECT * FROM staff_details WHERE user_id = %s', (user_id,))
    staff_info = cursor.fetchone()
    conn.close()

    return render_template('staff_information.html', staff_info=staff_info)

@app.route('/family_information', methods=['GET', 'POST'])
def family_information():
    if 'user_logged_in' not in session:
        return redirect(url_for('user_login'))

    user_id = session['user_id']
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        data = request.form.to_dict()
        cursor.execute('''
            UPDATE family_details SET 
                father_name=%s, father_occupation=%s, mother_name=%s, mother_occupation=%s, 
                spouse_name=%s, spouse_phone_number=%s
            WHERE user_id=%s
        ''', (
            data.get('father_name'), data.get('father_occupation'), data.get('mother_name'), 
            data.get('mother_occupation'), data.get('spouse_name'), data.get('spouse_phone_number'), 
            user_id
        ))
        conn.commit()
        flash('Family information updated successfully')
        return redirect(url_for('view_information'))

    cursor.execute('SELECT * FROM family_details WHERE user_id = %s', (user_id,))
    family_info = cursor.fetchone()
    conn.close()

    return render_template('family_information.html', family_info=family_info)

@app.route('/view_information')
def view_information():
    if 'user_logged_in' not in session:
        return redirect(url_for('user_login'))

    user_id = session.get('user_id')
    
    if not user_id:
        flash('User not logged in.')
        return redirect(url_for('user_login'))

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Fetch staff information
        cursor.execute('SELECT * FROM staff_details WHERE user_id = %s', (user_id,))
        staff_info = cursor.fetchone()
        
        # Fetch family information
        cursor.execute('SELECT * FROM family_details WHERE user_id = %s', (user_id,))
        family_info = cursor.fetchone()
        
    except mysql.connector.Error as err:
        flash(f'Database error: {err}')
        return redirect(url_for('user_dashboard'))
    finally:
        cursor.close()
        conn.close()
    
    if not staff_info and not family_info:
        flash('No information found for this user.')
        return redirect(url_for('user_dashboard'))
    
    return render_template('view_information.html', staff_info=staff_info, family_info=family_info)

if __name__ == '__main__':
    app.run(debug=True)
