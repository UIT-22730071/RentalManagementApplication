

from QLNHATRO.RentalManagementApplication.backend.database.Database import Database
from QLNHATRO.RentalManagementApplication.backend.model.Landlord import Landlord

db = Database()

class LanlordRepository:

    @staticmethod
    def get_landlord_data_for_invoice_view(id_landlord):
        # TODO: Tao truy vấn SLQ select * from landlords where id
        landlord_data = {
            'id_landlord':1,
            'name': 'Chưa có dữ liệu',
            'cccd': 'Đang cập nhật',
            'address': 'Khu Phố 6, Phường Linh Trung, Thành phố Thủ Đức, TP Hồ Chí Minh',
            'phone': 'Chưa có dữ liệu'
        }
        return landlord_data


    @staticmethod
    def get_all_landlords():
        try:
            db.connect()
            query = """
                    SELECT L.LandlordID, \
                           L.Fullname, \
                           L.Birth, \
                           L.CCCD, \
                           L.Gender, \
                           L.JobTitle, \
                           L.MaritalStatus, \
                           L.Email, \
                           L.PhoneNumber, \
                           L.HomeAddress, \
                           L.UserID, \
                           U.Username, \
                           COUNT(R.RoomID) as so_phong
                    FROM Landlords L
                             LEFT JOIN Users U ON L.UserID = U.UserID
                             LEFT JOIN Rooms R ON L.LandlordID = R.LandlordID
                    GROUP BY L.LandlordID \
                    """
            cursor = db.execute(query)
            data = cursor.fetchall() if cursor else []
            db.close()

            return [Landlord(dict(row)) for row in data]
        except Exception as e:
            print(f"❌ Lỗi get_all_landlords: {e}")
            return []

    @staticmethod
    def get_id_landlord_from_user_id(user_id):
        try:
            db.connect()
            query = "SELECT LandlordID FROM Landlords WHERE UserID = ?"
            cursor = db.execute(query, (user_id,))
            result = cursor.fetchone()
            db.close()

            if result and result[0]:
                return result[0]
            else:
                print("⚠️ Không tìm thấy landlord với user_id:", user_id)
                return None  # hoặc trả về giá trị mặc định nếu cần
        except Exception as e:
            print(f"❌ Lỗi khi truy vấn get_id_landlord_from_user_id: {e}")
            return None

    #-------------Lanlord Home --------------
    #TODO: sau khi có dữ liệu ảo thống kê sẽ vẽ biểu đồ
    '''return của hàm sẽ là 1 char'''
    @staticmethod
    def get_chart_income_month(id_landlord):
        chart = "0"
        return chart

    @staticmethod
    def get_total_income_from_all_of_rooms(id_landlord):
        db.connect()
        query = """
                SELECT SUM(TotalRoomPrice + TotalElectronicCost + TotalWaterCost +
                           InternetFee + TotalGarbageFee + TotalAnotherFee - Discount)
                FROM Invoices
                WHERE LandlordID = ? \
                """
        cursor = db.execute(query, (id_landlord,))

        if cursor is None:
            print("⚠️ [Fallback] Không thể truy vấn bảng Invoices. Trả về sample mẫu.")
            db.close()
            return 50_000_000  # SAMPLE

        result = cursor.fetchone()
        db.close()
        if not result or result[0] is None:
            print("⚠️ [Sample] Không có dữ liệu, trả về tổng thu nhập mẫu.")
            return 50_000_000  # sample

        return result[0]


    @staticmethod
    def get_total_income_last_month(id_landlord):
        db.connect()
        query = """
                SELECT SUM(TotalRoomPrice + TotalElectronicCost + TotalWaterCost +
                           InternetFee + TotalGarbageFee + TotalAnotherFee - Discount)
                FROM Invoices
                WHERE LandlordID = ? \
                  AND strftime('%m-%Y', issue_date) = strftime('%m-%Y', date('now','start of month','-1 month')) \
                """
        cursor = db.execute(query, (id_landlord,))
        result = cursor.fetchone()
        db.close()

        if not result or result[0] is None:
            print("⚠️ [Sample] Không có dữ liệu thu nhập tháng trước, trả về mẫu.")
            return 45_000_000  # sample

        return result[0]

    @staticmethod
    def get_data_for_handel_percent_income(id_landlord):
        db.connect()
        query = """
                SELECT SUM(CASE \
                               WHEN strftime('%m-%Y', issue_date) = strftime('%m-%Y', date('now','start of month','-1 month')) \
                                   THEN TotalRoomPrice + TotalElectronicCost + TotalWaterCost + InternetFee + \
                                        TotalGarbageFee + TotalAnotherFee - Discount \
                               ELSE 0 END) AS last_month, \
                       SUM(CASE \
                               WHEN strftime('%m-%Y', issue_date) = strftime('%m-%Y', date('now','start of month','-2 month')) \
                                   THEN TotalRoomPrice + TotalElectronicCost + TotalWaterCost + InternetFee + \
                                        TotalGarbageFee + TotalAnotherFee - Discount \
                               ELSE 0 END) AS month_before
                FROM Invoices
                WHERE LandlordID = ? \
                """
        cursor = db.execute(query, (id_landlord,))
        result = cursor.fetchone()
        db.close()
        """if not result or result[0] is None or result[1] is None:
            print("⚠️ [Sample] Không có dữ liệu hai tháng gần nhất, trả mẫu.")
            return (30_000_000, 28_000_000)"""

        return result
        #return income_last_month,income_last_month_sub_1

    @staticmethod
    def get_total_number_room_have_invoice_not_complete(id_landlord):
        db.connect()
        query = """
                SELECT COUNT(*)
                FROM Invoices
                WHERE LandlordID = ? \
                  AND Status = 'Chưa thanh toán' \
                """
        cursor = db.execute(query, (id_landlord,))
        total_current = cursor.fetchone()[0] if cursor else 0

        query_last_month = """
                           SELECT COUNT(*)
                           FROM Invoices
                           WHERE LandlordID = ? \
                             AND Status = 'Chưa thanh toán'
                             AND strftime('%m-%Y', issue_date) = strftime('%m-%Y', date('now','start of month','-1 month')) \
                           """
        cursor = db.execute(query_last_month, (id_landlord,))
        total_last = cursor.fetchone()[0] if cursor else 0

        db.close()
        """if total_current == 0 and total_last == 0:
            print("⚠️ [Sample] Không có hóa đơn chưa thanh toán, trả về mẫu.")
            return 3, 2"""

        return total_current, total_last
       # return total_number_invoice,total_number_invoice_last_month
    @staticmethod
    def get_to_total_number_not_tenant(id_landlord):
        db.connect()

        # Phòng hiện tại không có người thuê
        query = """
                SELECT COUNT(*) \
                FROM Rooms
                WHERE LandlordID = ? \
                  AND TenantID IS NULL \
                """
        cursor = db.execute(query, (id_landlord,))
        total_current = cursor.fetchone()[0] if cursor else 0

        # Phòng tháng trước cũng trống: RentalDate là NULL hoặc đã từng null trong tháng trước
        # Lấy số phòng mà:
        # 1. Hiện tại không có Tenant
        # 2. Và tháng trước vẫn chưa có tenant (RentalDate IS NULL hoặc < đầu tháng hiện tại)
        query_last_month = """
                           SELECT COUNT(*) \
                           FROM Rooms
                           WHERE LandlordID = ?
                             AND TenantID IS NULL
                             AND (
                               RentalDate IS NULL OR
                               strftime('%Y-%m', RentalDate) <= strftime('%Y-%m', date('now', 'start of month', '-1 month'))
                               ) \
                           """
        cursor = db.execute(query_last_month, (id_landlord,))
        total_last = cursor.fetchone()[0] if cursor else 0

        db.close()

        """# Nếu không có dữ liệu, trả về dữ liệu mẫu để test
        if total_current == 0 and total_last == 0:
            print("⚠️ [Sample] Không có phòng trống, trả về dữ liệu mẫu.")
            return 2, 3"""

        return total_current, total_last

        #return total_number_room_not_teant,total_rooms_not_tenant_last_month
    # -------------Lanlord Infor --------------
    @staticmethod
    def get_infor_lanlord(id_landlord):
        #TODO tạo 1 hàm select infor lanlord gom cac thong tin
        infor_lanlord = {
            'name': 'Nguyễn Văn A',
            'birth':'13/12/1998',
            'cccd': '012345678901',
            'sex': 'Nam',
            'job': 'Sinh viện',
            'phone': '0901234567',
            'email': "nguyenvanchurtro@gmail.com",
            'marriage': 'Độc thân',
            'password': '**********'}
        return infor_lanlord

    @staticmethod
    def update_field(id_landlord, field, value):
        # TODO: Viết truy vấn SQL update database
        print(f"[Repository] Update field `{field}` = {value} cho landlord {id_landlord}")
        # Ví dụ (giả lập):
        # UPDATE landlords SET field = value WHERE id = id_landlord;

    @staticmethod
    def update_user_info(user_id, data):
        # TODO: Thực hiện truy vấn UPDATE SQL
        print(f"[DB] Đã cập nhật user_id={user_id} với data={data}")

    @staticmethod
    def get_user_id_landlord_from_lanlord_id(lanlord_id):
        #TODO: truy Vấn SQL thực thi lệnh và trả về user id
        user_id = 1
        return user_id

    @staticmethod
    def get_landlord_monthly_income(landlord_id):
        try:
            db.connect()
            query = """
                    SELECT month, year, TotalIncome
                    FROM LandlordAnalytics
                    WHERE LandlordID = ?
                    ORDER BY year DESC, month DESC
                        LIMIT 10 \
                    """
            cursor = db.execute(query, (landlord_id,))
            if cursor is None:
                print("⚠️ Cursor is None, trả về dữ liệu mẫu")
                return [
                    {'month': '01/2024', 'total_income': 5_000_000},
                    {'month': '02/2024', 'total_income': 6_200_000},
                    {'month': '03/2024', 'total_income': 5_800_000},
                    {'month': '04/2024', 'total_income': 7_500_000},
                    {'month': '05/2024', 'total_income': 8_000_000},
                    {'month': '06/2024', 'total_income': 9_200_000}
                ]

            result = cursor.fetchall()
            db.close()

            if not result:
                print("⚠️ Không có dữ liệu từ database")
                return []

            return [
                {'month': f"{str(row[0]).zfill(2)}/{row[1]}", 'total_income': row[2]}
                for row in result[::-1]
            ]
        except Exception as e:
            print(f"❌ Lỗi get_landlord_monthly_income: {e}")
            return []




    @staticmethod
    def get_landlord_analytics_data(id_landlord):
        pass

    @staticmethod
    def get_landlord_name_by_id(landlord_id):
        db = Database()
        db.connect()
        query = "SELECT Fullname FROM Landlords WHERE LandlordID = ?"
        cursor = db.execute(query, (landlord_id,))
        result = db.fetchone()
        db.close()
        return result["Fullname"] if result else "None"

    @staticmethod
    def get_user_id_lanlord_from_lanlord_id(id_lanlord: int):
        """Trả về user_id từ landlord_id"""
        try:
            db.connect()
            query = "SELECT UserID FROM Landlords WHERE LandlordID = ?"
            cursor = db.execute(query, (id_lanlord,))
            row = cursor.fetchone()
            db.close()
            if row:
                return row[0]
            else:
                print(f"⚠️ Không tìm thấy UserID cho LandlordID: {id_lanlord}")
                return None
        except Exception as e:
            print(f"❌ Lỗi khi truy vấn get_user_id_lanlord_from_lanlord_id: {e}")
            return None


