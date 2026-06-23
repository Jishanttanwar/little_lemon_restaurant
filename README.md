# 🏥 Hospital Appointment Management System Database

## 📌 Overview

The Hospital Appointment Management System Database is a relational database project developed using MySQL to efficiently manage patient records, doctor information, and appointment scheduling. The project demonstrates core database concepts such as normalization, entity relationships, primary and foreign keys, and SQL queries.

This system provides a structured way to store and retrieve healthcare-related data while ensuring data integrity and consistency.

---

## 🎯 Objectives

- Manage patient information efficiently.
- Store doctor details and specializations.
- Schedule and track appointments.
- Demonstrate relational database design concepts.
- Practice SQL CRUD operations and JOIN queries.

---

## 🛠️ Tech Stack

- **Database:** MySQL
- **Language:** SQL
- **Design Tool:** ER Diagram (ERD)
- **Version Control:** Git & GitHub

---

## 📂 Database Structure

### Patients Table

| Column | Type | Description |
|----------|----------|-------------|
| patient_id | INT (PK) | Unique patient ID |
| first_name | VARCHAR(50) | Patient first name |
| last_name | VARCHAR(50) | Patient last name |
| gender | VARCHAR(10) | Gender |
| date_of_birth | DATE | Date of birth |
| phone | VARCHAR(15) | Contact number |
| email | VARCHAR(100) | Email address |

---

### Doctors Table

| Column | Type | Description |
|----------|----------|-------------|
| doctor_id | INT (PK) | Unique doctor ID |
| first_name | VARCHAR(50) | Doctor first name |
| last_name | VARCHAR(50) | Doctor last name |
| specialization | VARCHAR(100) | Medical specialization |
| phone | VARCHAR(15) | Contact number |
| email | VARCHAR(100) | Email address |

---

### Appointments Table

| Column | Type | Description |
|----------|----------|-------------|
| appointment_id | INT (PK) | Unique appointment ID |
| patient_id | INT (FK) | References Patients |
| doctor_id | INT (FK) | References Doctors |
| appointment_date | DATE | Appointment date |
| appointment_time | TIME | Appointment time |
| status | VARCHAR(20) | Scheduled, Completed, Cancelled |

---

## 🔗 Entity Relationships

- One Patient can have multiple Appointments.
- One Doctor can have multiple Appointments.
- Each Appointment is associated with one Patient and one Doctor.

```text
Patients (1)
    |
    |
    |----< Appointments >----|
                             |
                             |
                             |
                         Doctors (1)
```

---

## ⚙️ Features

### Patient Management
- Add patient records
- Update patient details
- Delete patient records
- View patient information

### Doctor Management
- Store doctor information
- Manage doctor specializations
- Update doctor records

### Appointment Management
- Schedule appointments
- Update appointment status
- Track appointment history
- Retrieve appointment details

---

## 📋 Sample Queries

### View All Appointments

```sql
SELECT
    a.appointment_id,
    p.first_name AS patient_name,
    d.first_name AS doctor_name,
    a.appointment_date,
    a.appointment_time,
    a.status
FROM Appointments a
JOIN Patients p ON a.patient_id = p.patient_id
JOIN Doctors d ON a.doctor_id = d.doctor_id;
```

### Count Total Appointments

```sql
SELECT COUNT(*) AS total_appointments
FROM Appointments;
```

### Find Appointments for a Specific Doctor

```sql
SELECT *
FROM Appointments
WHERE doctor_id = 1;
```

### List Doctors by Specialization

```sql
SELECT first_name, last_name, specialization
FROM Doctors;
```

---

## 📚 Concepts Implemented

- Relational Database Design
- Database Normalization
- Primary Keys
- Foreign Keys
- One-to-Many Relationships
- SQL CRUD Operations
- JOIN Operations
- Aggregate Functions
- Data Integrity Constraints

---

## 🚀 Future Improvements

- Department Management
- Prescription Module
- Laboratory Reports
- Billing and Payments
- Electronic Health Records (EHR)
- Django REST API Integration
- Role-Based Access Control

---

## 🎓 Learning Outcomes

This project helped in understanding:

- Real-world database design
- SQL query writing
- Database normalization
- Relationship modeling
- Data consistency and integrity
- Healthcare database workflows

---

## 👨‍💻 Author

**Jishant Tanwar**  
B.Tech CSE (Health Informatics)  
VIT Bhopal University

### Contact

- GitHub: [Jishanttanwar](https://github.com/Jishanttanwar)
- Email: princetanwar995@gmail.com

---

⭐ If you found this project helpful, consider giving it a star on GitHub.
