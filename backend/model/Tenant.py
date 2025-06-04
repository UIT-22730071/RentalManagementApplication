#TODO ?
import sqlite3
from typing import Dict, Any
db = 'rent_house_database.sqlite'

class Tenant:
    def __init__(self, data: Dict[str, Any]):
        self.tenant_id = data.get('TenantID')
        self.fullname = data.get('Fullname')
        self.birth = data.get('Birth')
        self.cccd = data.get('CCCD')
        self.gender = data.get('Gender')
        self.job_title = data.get('JobTitle')
        self.marital_status = data.get('MaritalStatus')  # 'Married', 'Single', 'Other'
        self.email = data.get('Email')
        self.phone_number = data.get('PhoneNumber')
        self.home_address = data.get('HomeAddress')
        self.rent_start_date = data.get('RentStartDate')
        self.rent_end_date = data.get('RentEndDate')
        self.user_id = data.get('UserID')
        self.username = data.get("Username")

    @staticmethod
    def add_tenant_to_db(userID, full_name, cccd, gender, job_title, marital_status, email, phone_number, home_address):
        try:
            conn = sqlite3.connect(db)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Tenants(UserID, FullName, CCCD, Gender, JobTitle, MaritalStatus, Email, PhoneNumber, HomeAddress)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (userID, full_name, cccd, gender, job_title, marital_status, email, phone_number, home_address))
            tenant_id = cursor.lastrowid
            conn.commit()
            cursor.execute("SELECT * FROM Tenants WHERE TenantID = ?", (tenant_id,))
            row = cursor.fetchone()
            conn.close()
            if row:
                columns = [column[0] for column in cursor.description]
                data = dict(zip(columns, row))
                print(f"Tenant with fullname: '{full_name}' added to database successfully with ID: {tenant_id}")
                return Tenant(data)
            else:
                print("Failed to fetch tenant after insert.")
                return None
        except Exception as e:
            print(e)
            return None

    def to_dict(self):
        """Return tenant information as a dictionary (database field names)"""
        return {
            "TenantID": self.tenant_id,
            "Fullname": self.fullname,
            "Birth": self.birth,
            "CCCD": self.cccd,
            "Gender": self.gender,
            "JobTitle": self.job_title,
            "MaritalStatus": self.marital_status,
            "Email": self.email,
            "PhoneNumber": self.phone_number,
            "HomeAddress": self.home_address,
            "RentStartDate": self.rent_start_date,
            "RentEndDate": self.rent_end_date,
            "UserID": self.user_id
        }
