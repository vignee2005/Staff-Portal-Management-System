# Staff-Portal-Management-System

The **Staff Portal Management System** is a **comprehensive, web-based application** developed to efficiently manage and maintain staff records in an organization. This system provides **separate login roles** for **Administrators** and **Staff Members**, ensuring secure access and data integrity.

The primary goal of the system is to **centralize staff-related information** in a secure relational database, eliminating paperwork, reducing redundancy, and providing an easy way to view, update, and maintain staff records.

---

### 🔹 Objectives of the System

* **Centralized Record-Keeping:** Store all staff-related details in one unified system.
* **Ease of Access:** Provide secure and quick access to staff records for both employees and administrators.
* **Data Accuracy:** Maintain up-to-date and accurate records through editable forms.
* **Document Management:** Allow uploading and storing important documents securely.
* **User-Friendly Interface:** Provide a clean and responsive UI for smooth navigation.

---

### ✨ Core Features

#### 🛡 Authentication & Security

* **Admin Login:** Full control over staff records, ability to add, update, and view all employee details.
* **Staff Login:** Restricted access to personal profile with the ability to edit and update their own data.
* **Password Protection:** Secure login credentials stored in an encrypted format.

#### 📂 Staff Information Management

* **Personal Details:** Name, DOB, age, gender, contact info, religion, community, salary, experience, etc.
* **Family Details:** Parents' names and occupations, spouse details, emergency contacts.
* **Educational Details:** UG, PG, PhD degrees with college names, years, and specializations.
* **Address Details:** Permanent and communication addresses.
* **Bank Details:** PAN, account number, bank name, branch, IFSC code.
* **Document Uploads:** Profile photo, signature, voter ID, and driving license.

#### 📑 Data Handling

* Pre-filled forms to display existing information upon login.
* Edit and save functionality to update only the required fields.
* All updates are reflected immediately in the database.

---

### 🗄 Database Design Overview

The database uses **MySQL** with multiple interconnected tables to maintain data consistency and normalization.

* **`admin_login`** → Stores admin usernames and passwords.
* **`user_login`** → Stores staff usernames and passwords.
* **`personal_details`** → Personal information, employment details, and document file paths.
* **`family_details`** → Family and emergency contact information.
* **`educational_details`** → Academic history (UG, PG, PhD).
* **`address_details`** → Communication and permanent addresses.
* **`bank_details`** → Bank and financial details.

**Relationships:**

* One **admin** can manage multiple **users**.
* One **user** can have one set of personal, educational, family, address, and bank details.

---

### 🛠 Tech Stack

* **Frontend:** HTML, CSS, Bootstrap (responsive design)
* **Backend:** Python (Flask)
* **Database:** MySQL
* **Additional:** JavaScript for form validation & dynamic interactivity

---

### 🚀 Workflow of the System

1. **Login Phase**

   * Admin logs in with credentials → Redirects to Admin Dashboard.
   * Staff logs in with credentials → Redirects to Staff Dashboard.

2. **Data Management**

   * **Admin:** Can create new staff records, view all details, and update existing records.
   * **Staff:** Can view pre-filled details and update their information.

3. **Document Handling**

   * Staff uploads supporting documents.
   * File paths are stored in the database for retrieval.

4. **Viewing Information**

   * Staff can view all stored data in a clean, formatted view.
   * Admin can retrieve any employee’s details for HR purposes.

---

### 📌 Benefits

* Eliminates paper-based staff record-keeping.
* Improves accuracy and reduces redundancy in data entry.
* Enhances data security and controlled access.
* Provides an intuitive interface for both technical and non-technical users.
* Ensures quick retrieval of staff details for HR and administrative needs.

---

### 💼 Potential Use Cases

* Schools, Colleges, and Universities (faculty record management).
* Corporates and Companies (employee data management).
* NGOs and Government Offices (staff profile maintenance).

