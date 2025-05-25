#TODO ?
import sqlite3


class Tenant:
    def __init__(self, id_tenant, full_name, cccd,gender ,phone, address, email, job_title, marital_status):
        self.id_tenant = id_tenant
        self.full_name = full_name
        self.cccd = cccd
        self.gender = gender
        self.phone = phone
        self.address = address
        self.email = email
        self.job_title = job_title
        self.marital_status = marital_status


    @staticmethod
    def add_tenant_to_db(userID, full_name, cccd, gender, job_title, martial_status, email, phone_number, home_address):
        try:
            conn = sqlite3.connect('rentalmanagement,sqlite')
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO Tenants(UserID, FullName, CCCD, Gender, JobTitle, MaritalStatus, Email, PhoneNumber, HomeAddress) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (userID, full_name, cccd, gender, job_title, martial_status, email, phone_number, home_address))
            tenant_id = cursor.lastrowid
            conn.commit()
            conn.close()
            print(f"Tenant with fullname: '{full_name}' added to database successfully with ID: {tenant_id}")
            return Tenant(full_name, cccd, gender, phone_number, home_address, email, job_title, martial_status)
        except Exception as e:
            print(e)

    def to_dict(self):
        """Trả về thông tin người thuê dưới dạng dictionary"""
        return {
            "id": self.id_tenant,
            "ho_ten": self.full_name,
            "cccd": self.cccd,
            "gender":self.gender,
            "sdt": self.phone,
            "email": self.email,
            "so_nguoi": self.marital_status
        }
