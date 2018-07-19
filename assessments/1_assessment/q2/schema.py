#!/usr/bin/env python3

import sqlite3


connection = sqlite3.connect('assessment.db', check_same_thread=False)
cursor = connection.cursor()

# 1. A state has many cities and a state has many parks.
# Considering all states are from the same country. Otherwise should add one more column
cursor.execute(
    """CREATE TABLE states(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL,
        acronym VARCHAR(2) UNIQUE NOT NULL
    );"""
)

cursor.execute(
    """CREATE TABLE cities(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL,
        state_id INTEGER NOT NULL,
        FOREIGN KEY(state_id) REFERENCES states(pk)
    );"""
)

# References the table Status, since the problem asks for it, instead of city.
# A state has many cities and a STATE has many PARKS.
cursor.execute(
    """CREATE TABLE parks(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL,
        state_id INTEGER NOT NULL,
        FOREIGN KEY(state_id) REFERENCES states(pk)
    );"""
)


# 2. A doctor has many patients and a patient has many doctors.
# Considering the import thing in this exercise is the relation between tables,
# not the attributes created in each table
cursor.execute(
    """CREATE TABLE doctors(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL,
        specialty VARCHAR(50) NOT NULL
    );"""
)

cursor.execute(
    """CREATE TABLE patients(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL
    );"""
)

cursor.execute(
    """CREATE TABLE doctors_patients(
        doctor_id INTEGER,
        patient_id INTEGER,
        CONSTRAINT PK_Doctor_Patien PRIMARY KEY (doctor_id, patient_id),
        FOREIGN KEY(doctor_id) REFERENCES doctors(pk),
        FOREIGN KEY(patient_id) REFERENCES patients(pk)
    );"""
)


# 3. Have the following in one database:
#     * A user has a name, username, password, email, and many phone numbers.
#     * An admin has a name, username, password, email, and many phone numbers.

# Profile - "A": Admin; "U": Regular User
cursor.execute(
    """CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL,
        username VARCHAR(16) UNIQUE NOT NULL,
        password VARCHAR(32) NOT NULL,
        profile VARCHAR(1) NOT NULL,
        email VARCHAR(100)
    );"""
)


# Considers that a user cannot repeat the same phone number
cursor.execute(
    """CREATE TABLE user_phones(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        phone_number VARCHAR(20) NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(pk),
        CONSTRAINT unique_user_phone UNIQUE (user_id, phone_number)
    );"""
)


cursor.close()
connection.close()
