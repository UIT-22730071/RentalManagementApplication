

from QLNHATRO.RentalManagementApplication.backend.database.Database import Database
from QLNHATRO.RentalManagementApplication.backend.model.Rooms import Room

db = Database()
class RoomRepository:

    @staticmethod
    def get_room_data_for_invoice_view(room_id):
        """Trả về thông tin phòng từ RoomID dưới dạng dict phục vụ tạo hóa đơn"""
        db.connect()

        query = """
                SELECT * \
                FROM Rooms \
                WHERE RoomID = ? \
                """
        cursor = db.execute(query, (room_id,))
        row = cursor.fetchone()
        db.close()

        if row:
            room = Room(dict(row))  # ✅ chuyển Row -> dict -> Room object
            return {
                'room_name': room.room_name,
                'room_price': room.room_price,
                'electric_price': room.electricity_price,
                'internet_fee': room.internet_price,
                'another_fee': room.other_fees,
                'water_price': room.water_price,
                'garbage_fee': room.garbage_service_price,
            }
        else:
            print(f"[⚠️] RoomID {room_id} không tồn tại. Trả về dữ liệu mẫu.")
            return {
                'room_name': 'Chưa có dữ liệu',
                'room_price': 0,
                'electric_price': 0,
                'internet_fee': 0,
                'another_fee': 0,
                'water_price': 0,
                'garbage_fee': 0,
            }

    @staticmethod
    def get_all_rooms():
        """
        Lấy danh sách tất cả các phòng để hiển thị ở AdminRoomList.
        Trả về list[dict] với các key:
          - room_id       : Mã phòng (RoomID)
          - room_name     : Tên phòng (RoomName)
          - room_style    : Kiểu phòng (RoomType)
          - landlord_name : Tên chủ trọ (Landlords.Fullname)
          - tenant_name   : Tên người thuê (Tenants.Fullname) hoặc '' nếu chưa có tenant
          - address       : Địa chỉ (Rooms.Address)

        Nếu không có bản ghi nào hoặc có lỗi, trả về list trống [].
        """
        try:
            db.connect()
            query = """
                    SELECT r.RoomID   AS room_id, \
                           r.RoomName AS room_name, \
                           r.RoomType AS room_style, \
                           l.Fullname AS landlord_name, \
                           t.Fullname AS tenant_name, \
                           r.Address  AS address
                    FROM Rooms r
                             LEFT JOIN Landlords l ON r.LandlordID = l.LandlordID
                             LEFT JOIN Tenants t ON r.TenantID = t.TenantID
                    ORDER BY r.RoomID ASC \
                    """
            cursor = db.execute(query)
            rows = cursor.fetchall() if cursor else []

            if not rows:
                # Nếu DB rỗng, trả về list rỗng (AdminRoomList sẽ hiện dữ liệu mẫu nếu cần)
                return []

            # Lấy tên cột từ cursor.description để zip thành dict
            columns = [col[0] for col in cursor.description]
            room_list = [dict(zip(columns, row)) for row in rows]
            return room_list

        except Exception as e:
            print(f"[LỖI] RoomRepository.get_all_rooms: {e}")
            return []

        finally:
            db.close()

    @staticmethod
    def get_room_by_id(room_id):
        """Trả về đối tượng Room từ RoomID, hoặc None nếu không có."""
        db.connect()
        query = "SELECT * FROM Rooms WHERE RoomID = ?"
        cursor = db.execute(query, (room_id,))
        row = cursor.fetchone()
        db.close()
        if row:
            return Room(dict(row))
        else:
            print(f"[⚠️] Không tìm thấy RoomID={room_id}, trả về dữ liệu mẫu")
            return Room({
                "RoomID": room_id,
                "RoomName": "Phòng 302 - Chung cư mini",
                "Address": "456 Nguyễn Văn Linh, Quận 7, TP.HCM",
                "RoomType": "Chung cư mini",
                "Status": "Đã thuê",
                "Area": 32.5,
                "Floor": 3,
                "HasLoft": 1,
                "Bathroom": 1,
                "Kitchen": 1,
                "Balcony": 1,
                "Furniture": 1,
                "AirConditioner": 1,
                "Fridge": 0,
                "WashingMachine": 1,
                "Television": 1,
                "Security": 1,
                "FreeWifi": 1,
                "Parking": 0,
                "CurrentElectricityNum": 425,
                "CurrentWaterNum": 70,
                "RoomPrice": 4200000,
                "Deposit": 4200000,
                "ElectricityPrice": 3500,
                "WaterPrice": 60000,
                "InternetPrice": 100000,
                "OtherFees": 20000,
                "GarbageServicePrice": 30000,
                "MaxTenants": 3,
                "PetAllowed": 0,
                "RentalDate": "2025-05-01",
                "Description": "",
                "TenantID": "TNT002",
                "LandlordID": "CT002"
            })

    @staticmethod
    def update_room_tenant(room_id, tenant_id):
        db.connect()
        query = "UPDATE Rooms SET TenantID = ? WHERE RoomID = ?"
        cursor = db.execute(query, (tenant_id, room_id))
        db.close()
        return True if cursor and cursor.rowcount > 0 else False

    @staticmethod
    def update_room_metrics(room_id, electricity_num, water_num):
        """Cập nhật chỉ số điện nước cho phòng."""
        if not db.connect():
            print(f"[LỖI] Không thể kết nối đến cơ sở dữ liệu để cập nhật phòng {room_id}")
            return False

        try:
            query = """
                    UPDATE Rooms
                    SET CurrentElectricityNum = ?, \
                        CurrentWaterNum       = ?
                    WHERE RoomID = ? \
                    """
            cursor = db.execute(query, (electricity_num, water_num, room_id))
            if cursor and cursor.rowcount > 0:
                db.conn.commit()
                print(f"✅ Đã cập nhật chỉ số điện={electricity_num}, nước={water_num} cho phòng {room_id}")
                return True
            else:
                print(f"[CẢNH BÁO] Không tìm thấy phòng có RoomID = {room_id} để cập nhật.")
                return False
        except Exception as e:
            print(f"[LỖI] Khi thực thi UPDATE cho phòng {room_id}: {e}")
            return False
        finally:
            db.close()

    @staticmethod
    def get_infor_number_room_of_tenant(landlord_id):
        try:
            db.connect()
            query = """
                    SELECT r.RoomID AS id_room, \
                           r.RoomName AS room_name, \
                           t.Fullname AS tenant_name, \
                           r.Price AS price_rent, \
                           r.CurrElectric AS number_electric, \
                           r.CurrWater AS number_water, \
                           COALESCE(i.Status, 'Chưa thanh toán') AS status_invoice
                    FROM Rooms r
                             LEFT JOIN Tenants t ON r.TenantID = t.TenantID
                             LEFT JOIN Invoices i ON i.RoomID = r.RoomID AND i.issue_date = (SELECT MAX(issue_date) \
                                                                                             FROM Invoices i2 \
                                                                                             WHERE i2.RoomID = r.RoomID)
                    WHERE r.LandlordID = ? \
                    """
            cursor = db.execute(query, (landlord_id,))
            result = cursor.fetchall()

            # Mapping column names to dictionary keys
            columns = [desc[0] for desc in cursor.description]
            room_list = [dict(zip(columns, row)) for row in result]

            return room_list
        except Exception as e:
            print(f"[LỖI] Truy vấn thông tin phòng thất bại: {e}")
            return [
            {
                'id_room': 'P101',
                'room_name': "Phòng 101",
                'tenant_name': "Nguyen Van A",
                'price_rent': 3500000,
                'number_electric': 25,
                'number_water': 28,
                'status_invoice': 'Chưa thanh toán'
            },
            {
                'id_room': 'P102',
                'room_name': "Phòng 102",
                'tenant_name': "Tran Thi B",
                'price_rent': 3200000,
                'number_electric': 20,
                'number_water': 22,
                'status_invoice': 'Đã thanh toán'
            }
        ]

    @staticmethod
    def create_new_room(id_landlord, room_create_data):
        try:
            db.connect()
            query = """
                    INSERT INTO Rooms (RoomName, MaxPeople, Address, Type, Status, \
                                       Description, Area, Price, ElectricPrice, WaterPrice, \
                                       CurrElectric, CurrWater, LandlordID) \
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) \
                    """
            params = (
                room_create_data['room_name'],
                int(room_create_data['number_people']),
                room_create_data['address'],
                room_create_data['type_room'],
                room_create_data['status'],
                room_create_data['other_infor'],
                float(room_create_data['area']),
                float(room_create_data['price_rent']),
                float(room_create_data['electric_price']),
                float(room_create_data['water_price']),
                int(room_create_data['num_electric']),
                int(room_create_data['num_water']),
                id_landlord
            )

            db.execute(query, params)
            print(f"✅ Đã tạo phòng mới cho landlord {id_landlord}: {room_create_data['room_name']}")
            return True

        except Exception as e:
            print(f"[LỖI] Không thể tạo phòng mới: {e}")
            return False

    @staticmethod
    def get_data_for_handle_room_home(room_id):
        db.connect()

        # Lấy thông tin hiện tại từ Rooms
        query_current = """
                        SELECT CurrentElectricityNum, CurrentWaterNum, ElectricityPrice, WaterPrice
                        FROM Rooms
                        WHERE RoomID = ? \
                        """
        cursor_current = db.execute(query_current, (room_id,))
        current = cursor_current.fetchone() if cursor_current else (0, 0, 0, 0)

        # Lấy thông tin kỳ trước từ Invoices gần nhất
        query_old = """
                    SELECT CurrElectric, CurrWater
                    FROM Invoices
                    WHERE RoomID = ?
                    ORDER BY issue_date DESC LIMIT 1 \
                    OFFSET 1 \
                    """
        cursor_old = db.execute(query_old, (room_id,))
        old = cursor_old.fetchone() if cursor_old else (current[0], current[1])

        db.close()

        data_sample_room_home = {
            'current_electricity': 356,
            'current_water': 20,
            'electricity_price': 3800,
            'water_price': 100000,
            'old_electricity': 256,
            'old_water': 256,
            'old_electricity_price': 3800,
            'old_water_price': 100000,
        }
        if current is None or old is None:
            # Trả về dữ liệu mẫu nếu không có dữ liệu thực
            return data_sample_room_home
        else: # nếu có dữ liệu thực thì trả về dữ liệu thực
            return {
                'current_electricity': current[0],
                'current_water': current[1],
                'electricity_price': current[2],
                'water_price': current[3],
                'old_electricity': old[0],
                'old_water': old[1],
                'old_electricity_price': current[2],  # Assume không đổi
                'old_water_price': current[3],  # Assume không đổi
            }

    @staticmethod
    def get_data_for_handle_room_infor(room_id):
        """
        Trả về dict chứa tất cả các trường thông tin phòng (Rooms) và thông tin chủ trọ (Landlords)
        theo room_id. Nếu không tìm thấy, trả về None.
        """
        try:
            db.connect()
            query = """
                    SELECT r.RoomName              AS RoomName, \
                           r.Address               AS Address, \
                           r.RoomType              AS RoomType, \
                           r.Status                AS Status, \
                           r.Area                  AS Area, \
                           r.Floor                 AS Floor, \
                           r.HasLoft               AS HasLoft, \
                           r.Bathroom              AS Bathroom, \
                           r.Kitchen               AS Kitchen, \
                           r.Balcony               AS Balcony, \
                           r.Furniture             AS Furniture, \
                           r.FreeWifi              AS FreeWifi, \
                           r.Parking               AS Parking, \
                           r.AirConditioner        AS AirConditioner, \
                           r.Fridge                AS Fridge, \
                           r.WashingMachine        AS WashingMachine, \
                           r.Television            AS Television, \
                           r.Security              AS Security, \
                           r.CurrentElectricityNum AS CurrentElectricityNum, \
                           r.CurrentWaterNum       AS CurrentWaterNum, \
                           r.RoomPrice             AS RoomPrice, \
                           r.Deposit               AS Deposit, \
                           r.ElectricityPrice      AS ElectricityPrice, \
                           r.WaterPrice            AS WaterPrice, \
                           r.InternetPrice         AS InternetPrice, \
                           r.OtherFees             AS OtherFees, \
                           r.GarbageServicePrice   AS GarbageServicePrice, \
                           r.MaxTenants            AS MaxTenants, \
                           r.PetAllowed            AS PetAllowed, \
                           r.RentalDate            AS RentalDate, \
                           r.Description           AS Description, \
                           l.Fullname              AS Fullname, \
                           l.PhoneNumber           AS PhoneNumber, \
                           l.Email                 AS Email
                    FROM Rooms r
                             LEFT JOIN Landlords l ON r.LandlordID = l.LandlordID
                    WHERE r.RoomID = ? \
                    """
            cursor = db.execute(query, (room_id,))
            row = cursor.fetchone() if cursor else None

            if not row:
                data = {
                    "RoomName": "P302",
                    "Address": "456 Đường Nguyễn Văn Linh, Quận 7, TP.HCM",
                    "RoomType": "Chung cư mini",
                    "Status": "Đã thuê",
                    "Area": 32.5,

                    "Floor": 3,
                    "HasLoft": 1,
                    "Bathroom": 1,
                    "Kitchen": 1,
                    "Balcony": 1,
                    "Furniture": 1,

                    # Thiết bị điện & tiện ích (dạng cờ bit 0/1)
                    "AirConditioner": 1,
                    "Fridge": 0,
                    "WashingMachine": 1,
                    "Television": 1,
                    "Security": 1,
                    "FreeWifi": 1,
                    "Parking": 0,

                    "CurrentElectricityNum": 425,
                    "CurrentWaterNum": 70,
                    "RoomPrice": 4200000,
                    "Deposit": 4200000,
                    "ElectricityPrice": 3500,
                    "WaterPrice": 60000,
                    "InternetPrice": 100000,
                    "GarbageServicePrice": 30000,
                    "OtherFees": 20000,

                    "MaxTenants": 3,
                    "PetAllowed": 0,
                    "RentalDate": "2025-05-01",
                    "Description": "Phòng view đẹp, có ban công rộng, gần trung tâm mua sắm",
                    # trích từ lanlord data
                    "Fullname": "Anh Tuấn",
                    "PhoneNumber": "0909 123 456",
                    "Email": "tuan.chutro@gmail.com"
                }
                return data

            # Lấy danh sách tên cột (cursor.description trả về list of tuples (col_name, ...))
            column_names = [desc[0] for desc in cursor.description]
            result_dict = dict(zip(column_names, row))
            return result_dict

        except Exception as e:
            print(f"[LỖI] Truy vấn thông tin phòng thất bại: {e}")
            return None

        finally:
            db.close()

    @staticmethod
    def update_tenant_rent_room(room_id, tenant_id):
        #TODO Tao hàm truy vấn update data
        print(f"✅ Cập nhật người thuê {tenant_id} vào phòng {room_id}")
        return True

    @staticmethod
    def get_list_room_by_id_landlord(id_landlord):
        """Cập nhật thông tin phòng"""
        db.connect()
        query = """
        SELECT RoomID, RoomName FROM Rooms WHERE LandlordID = ?
        """
        cursor = db.execute(query, (id_landlord,))
        rooms = cursor.fetchall() if cursor else [
        {"RoomID": 1, "RoomName": "Phòng A1"},
        {"RoomID": 2, "RoomName": "Phòng B2"}
        ]
        db.close()

        ''' trả về 1 danh sách các tên phòng kèm RoomID để hiển thị trên giao diện tìm người'''
        return rooms

    @staticmethod
    def delete_room(room_id):
        from QLNHATRO.RentalManagementApplication.frontend.Component.ErrorDialog import ErrorDialog
        db.connect()
        try:
            query = "DELETE FROM Rooms WHERE RoomID = ?"
            cursor = db.execute(query, (room_id,))
            if cursor and cursor.rowcount > 0:
                msg = {'success': True, 'message': 'Đã xóa phòng thành công'}
            else:
                msg = {'success': False, 'message': 'Không tìm thấy phòng để xóa'}
        except Exception as e:
            msg = {'success': False, 'message': f'Lỗi: {str(e)}'}
        finally:
            db.close()
        return msg

    @staticmethod
    def get_room_monthly_stats(room_id):
        db.connect()
        query = """
                SELECT strftime('%m/%Y', issue_date) AS month,
                    (CurrElectric - PreElectric) AS num_electricity,
                    (CurrWater - PreWater) AS num_water,
                    (TotalElectronicCost + TotalWaterCost + TotalRoomPrice + InternetFee + TotalGarbageFee + TotalAnotherFee - Discount) AS total
                FROM Invoices
                WHERE RoomID = ?
                ORDER BY issue_date DESC
                    LIMIT 12 \
                """

        cursor = db.execute(query, (room_id,))
        rows = cursor.fetchall() if cursor else []
        db.close()

        result = []
        for row in rows:
            result.append({
                "month": row[0],
                "num_electricity": row[1],
                "num_water": row[2],
                "total": row[3]
            })
        if result is None :
            data = [
            {"month": "01/2024", "num_electricity": 120, "num_water": 15, "total": 700000},
            {"month": "02/2024", "num_electricity": 150, "num_water": 17, "total": 730000},
            {"month": "03/2024", "num_electricity": 130, "num_water": 16, "total": 720000},
            {"month": "04/2024", "num_electricity": 140, "num_water": 18, "total": 750000},
            {"month": "05/2024", "num_electricity": 160, "num_water": 20, "total": 800000},
            {"month": "06/2024", "num_electricity": 170, "num_water": 22, "total": 850000},
            {"month": "07/2024", "num_electricity": 180, "num_water": 25, "total": 900000},
            {"month": "08/2024", "num_electricity": 190, "num_water": 27, "total": 950000},
            {"month": "09/2024", "num_electricity": 200, "num_water": 30, "total": 1000000},
            {"month": "10/2024", "num_electricity": 210, "num_water": 32, "total": 1050000},
            {"month": "11/2024", "num_electricity": 220, "num_water": 35, "total": 1100000},
            {"month": "12/2024", "num_electricity": 230, "num_water": 37, "total": 1150000}
            ]
            return data
        else:
            return result

