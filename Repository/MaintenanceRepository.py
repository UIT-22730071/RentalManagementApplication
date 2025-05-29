import sqlite3
from datetime import datetime
from typing import List, Dict, Optional


class MaintenanceRepository:
    # Dữ liệu yêu cầu sửa chữa giả lập
    requests = []

    @staticmethod
    def save_request(request_data):
        MaintenanceRepository.requests.append(request_data)
        print(f"[DEBUG][Repository] Đã lưu yêu cầu: {request_data}")

    @staticmethod
    def get_all_requests():
        return MaintenanceRepository.requests

    @staticmethod
    def get_requests_by_room_id(room_id):

        maintenance_history = [
            {
                "id": 1,
                "description": "Vòi nước bị rỉ",
                "status": "Đã hoàn thành",
                "date": "01/04/2025"
            },
            {
                "id": 2,
                "description": "Đèn phòng tắm không sáng",
                "status": "Đang xử lý",
                "date": "20/04/2025"
            }
        ]

        return maintenance_history

    @staticmethod
    def get_requests_by_tenant_id(tenant_id):
        return [req for req in MaintenanceRepository.requests if req['tenant_id'] == tenant_id]

    @staticmethod
    def get_database_connection():
        """Lấy kết nối database"""
        try:
            conn = sqlite3.connect('QLNHATRO/RentalManagementApplication/database/database_rental_management.sqlite')
            conn.row_factory = sqlite3.Row  # Cho phép truy cập cột bằng tên
            return conn
        except sqlite3.Error as e:
            print(f"❌ Lỗi kết nối database: {e}")
            return None

    @staticmethod
    def get_maintenance_requests_by_landlord(landlord_id: int) -> List[Dict]:
        """Lấy danh sách yêu cầu bảo trì theo landlord_id"""

        conn = MaintenanceRepository.get_database_connection()
        if conn is None:
            return [
                {
                    "stt": 1,
                    "request_id": 1,
                    "room_name": "Phòng 101",
                    "tenant_name": "Nguyễn Văn A",
                    "issue_type": "Điện",
                    "urgency_level": "Khẩn cấp",
                    "description": "Mất điện toàn bộ phòng",
                    "status": "Pending",
                    "created_at": "2025-01-15",
                    "contact_phone": "0912345678"
                },
                {
                    "stt": 2,
                    "request_id": 2,
                    "room_name": "Phòng 203",
                    "tenant_name": "Trần Thị B",
                    "issue_type": "Nước",
                    "urgency_level": "Bình thường",
                    "description": "Vòi nước bị rỉ nhỏ giọt",
                    "status": "Đang xử lý",
                    "created_at": "2025-01-14",
                    "contact_phone": "0987654321"
                },
                {
                    "stt": 3,
                    "request_id": 3,
                    "room_name": "Phòng 305",
                    "tenant_name": "Lê Văn C",
                    "issue_type": "Cấu trúc",
                    "urgency_level": "Khẩn cấp",
                    "description": "Tường bị nứt, có nguy cơ sập",
                    "status": "Pending",
                    "created_at": "2025-01-13",
                    "contact_phone": "0901234567"
                }
            ]
        try:
            cursor = conn.cursor()

            # Query để lấy yêu cầu bảo trì kèm thông tin phòng và tenant
            query = """
                    SELECT mr.request_id, \
                           mr.issue_type, \
                           mr.urgency_level, \
                           mr.description, \
                           mr.contact_phone, \
                           mr.available_time, \
                           mr.discovery_date, \
                           mr.image_path, \
                           mr.status, \
                           mr.created_at, \
                           r.RoomName    as room_name, \
                           r.RoomID      as room_id, \
                           t.Fullname    as tenant_name, \
                           t.TenantID    as tenant_id, \
                           t.PhoneNumber as tenant_phone
                    FROM maintenance_requests mr
                             JOIN Rooms r ON mr.room_id = r.RoomID
                             JOIN Tenants t ON mr.tenant_id = t.TenantID
                    WHERE r.LandlordID = ?
                    ORDER BY CASE mr.urgency_level \
                                 WHEN 'Khẩn cấp' THEN 1 \
                                 WHEN 'Bình thường' THEN 2 \
                                 ELSE 3 \
                                 END, \
                             mr.created_at DESC \
                    """

            cursor.execute(query, (landlord_id,))
            rows = cursor.fetchall()

            maintenance_requests = []
            for idx, row in enumerate(rows, 1):
                maintenance_requests.append({
                    'stt': idx,
                    'request_id': row['request_id'],
                    'room_id': row['room_id'],
                    'room_name': row['room_name'] or f"Phòng {row['room_id']}",
                    'tenant_id': row['tenant_id'],
                    'tenant_name': row['tenant_name'],
                    'tenant_phone': row['tenant_phone'],
                    'issue_type': row['issue_type'],
                    'urgency_level': row['urgency_level'],
                    'description': row['description'],
                    'contact_phone': row['contact_phone'] or row['tenant_phone'],
                    'available_time': row['available_time'],
                    'discovery_date': row['discovery_date'],
                    'image_path': row['image_path'],
                    'status': row['status'],
                    'created_at': row['created_at']
                })

            return maintenance_requests

        except sqlite3.Error as e:
            print(f"❌ Lỗi truy vấn maintenance requests: {e}")
            return []
        finally:
            conn.close()

    @staticmethod
    def get_maintenance_request_by_id(request_id: int) -> Optional[Dict]:
        """Lấy thông tin chi tiết một yêu cầu bảo trì"""
        conn = MaintenanceRepository.get_database_connection()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()

            query = """
                    SELECT mr.*, \
                           r.RoomName    as room_name, \
                           r.Address     as room_address, \
                           t.Fullname    as tenant_name, \
                           t.PhoneNumber as tenant_phone, \
                           t.Email       as tenant_email
                    FROM maintenance_requests mr
                             JOIN Rooms r ON mr.room_id = r.RoomID
                             JOIN Tenants t ON mr.tenant_id = t.TenantID
                    WHERE mr.request_id = ? \
                    """

            cursor.execute(query, (request_id,))
            row = cursor.fetchone()

            if row:
                return dict(row)
            return None

        except sqlite3.Error as e:
            print(f"❌ Lỗi truy vấn maintenance request: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def update_maintenance_status(request_id: int, new_status: str) -> bool:
        """Cập nhật trạng thái yêu cầu bảo trì"""
        conn = MaintenanceRepository.get_database_connection()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()

            # Kiểm tra status hợp lệ
            valid_statuses = ['Pending', 'In Progress', 'Resolved', 'Đang xử lý', 'Đã hoàn thành']
            if new_status not in valid_statuses:
                print(f"❌ Trạng thái không hợp lệ: {new_status}")
                return False

            query = """
                    UPDATE maintenance_requests
                    SET status     = ?, \
                        created_at = CURRENT_TIMESTAMP
                    WHERE request_id = ? \
                    """

            cursor.execute(query, (new_status, request_id))
            conn.commit()

            if cursor.rowcount > 0:
                print(f"✅ Đã cập nhật trạng thái yêu cầu {request_id} thành '{new_status}'")
                return True
            else:
                print(f"❌ Không tìm thấy yêu cầu với ID: {request_id}")
                return False

        except sqlite3.Error as e:
            print(f"❌ Lỗi cập nhật trạng thái: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()

    @staticmethod
    def create_maintenance_request(tenant_id: int, room_id: int, issue_type: str,
                                   urgency_level: str, description: str,
                                   contact_phone: str = None, available_time: str = None,
                                   discovery_date: str = None, image_path: str = None) -> bool:
        """Tạo yêu cầu bảo trì mới"""
        conn = MaintenanceRepository.get_database_connection()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()

            # Validate input
            if not all([tenant_id, room_id, issue_type, urgency_level, description]):
                print("❌ Thiếu thông tin bắt buộc")
                return False

            # Set default values
            discovery_date = discovery_date or datetime.now().strftime('%Y-%m-%d')

            query = """
                    INSERT INTO maintenance_requests (tenant_id, room_id, issue_type, urgency_level, description, \
                                                      contact_phone, available_time, discovery_date, image_path, status) \
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'Pending') \
                    """

            cursor.execute(query, (
                tenant_id, room_id, issue_type, urgency_level, description,
                contact_phone, available_time, discovery_date, image_path
            ))

            conn.commit()

            if cursor.rowcount > 0:
                print(f"✅ Đã tạo yêu cầu bảo trì mới với ID: {cursor.lastrowid}")
                return True
            else:
                print("❌ Không thể tạo yêu cầu bảo trì")
                return False

        except sqlite3.Error as e:
            print(f"❌ Lỗi tạo yêu cầu bảo trì: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()

    @staticmethod
    def get_maintenance_statistics(landlord_id: int) -> Dict:
        """Lấy thống kê yêu cầu bảo trì theo landlord"""
        conn = MaintenanceRepository.get_database_connection()
        if conn is None:
            return {}

        try:
            cursor = conn.cursor()

            query = """
                    SELECT COUNT(*)                                                                    as total_requests, \
                           SUM(CASE WHEN mr.status = 'Pending' THEN 1 ELSE 0 END)                      as pending_count, \
                           SUM(CASE WHEN mr.status IN ('In Progress', 'Đang xử lý') THEN 1 ELSE 0 END) as in_progress_count, \
                           SUM(CASE WHEN mr.status IN ('Resolved', 'Đã hoàn thành') THEN 1 ELSE 0 END) as resolved_count, \
                           SUM(CASE WHEN mr.urgency_level = 'Khẩn cấp' THEN 1 ELSE 0 END)              as urgent_count
                    FROM maintenance_requests mr
                             JOIN Rooms r ON mr.room_id = r.RoomID
                    WHERE r.LandlordID = ? \
                    """

            cursor.execute(query, (landlord_id,))
            row = cursor.fetchone()

            if row:
                return {
                    'total_requests': row['total_requests'] or 0,
                    'pending_count': row['pending_count'] or 0,
                    'in_progress_count': row['in_progress_count'] or 0,
                    'resolved_count': row['resolved_count'] or 0,
                    'urgent_count': row['urgent_count'] or 0
                }

            return {}

        except sqlite3.Error as e:
            print(f"❌ Lỗi lấy thống kê: {e}")
            return {}
        finally:
            conn.close()

    @staticmethod
    def delete_maintenance_request(request_id: int) -> bool:
        """Xóa yêu cầu bảo trì"""
        conn = MaintenanceRepository.get_database_connection()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()

            query = "DELETE FROM maintenance_requests WHERE request_id = ?"
            cursor.execute(query, (request_id,))
            conn.commit()

            if cursor.rowcount > 0:
                print(f"✅ Đã xóa yêu cầu bảo trì ID: {request_id}")
                return True
            else:
                print(f"❌ Không tìm thấy yêu cầu với ID: {request_id}")
                return False

        except sqlite3.Error as e:
            print(f"❌ Lỗi xóa yêu cầu bảo trì: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()

    @staticmethod
    def get_maintenance_requests_by_status(landlord_id: int, status: str) -> List[Dict]:
        """Lấy danh sách yêu cầu bảo trì theo trạng thái"""
        conn = MaintenanceRepository.get_database_connection()
        if conn is None:
            return []

        try:
            cursor = conn.cursor()

            query = """
                    SELECT mr.request_id, \
                           mr.issue_type, \
                           mr.urgency_level, \
                           mr.description, \
                           mr.status, \
                           mr.created_at, \
                           r.RoomName as room_name, \
                           t.Fullname as tenant_name
                    FROM maintenance_requests mr
                             JOIN Rooms r ON mr.room_id = r.RoomID
                             JOIN Tenants t ON mr.tenant_id = t.TenantID
                    WHERE r.LandlordID = ? \
                      AND mr.status = ?
                    ORDER BY mr.created_at DESC \
                    """

            cursor.execute(query, (landlord_id, status))
            rows = cursor.fetchall()

            return [dict(row) for row in rows]

        except sqlite3.Error as e:
            print(f"❌ Lỗi truy vấn theo trạng thái: {e}")
            return []
        finally:
            conn.close()

    @staticmethod
    def get_maintenance_requests_by_urgency(landlord_id: int, urgency: str) -> List[Dict]:
        """Lấy danh sách yêu cầu bảo trì theo mức độ khẩn cấp"""
        conn = MaintenanceRepository.get_database_connection()
        if conn is None:
            return []

        try:
            cursor = conn.cursor()

            query = """
                    SELECT mr.request_id, \
                           mr.issue_type, \
                           mr.urgency_level, \
                           mr.description, \
                           mr.status, \
                           mr.created_at, \
                           r.RoomName as room_name, \
                           t.Fullname as tenant_name
                    FROM maintenance_requests mr
                             JOIN Rooms r ON mr.room_id = r.RoomID
                             JOIN Tenants t ON mr.tenant_id = t.TenantID
                    WHERE r.LandlordID = ? \
                      AND mr.urgency_level = ?
                    ORDER BY mr.created_at DESC \
                    """

            cursor.execute(query, (landlord_id, urgency))
            rows = cursor.fetchall()

            return [dict(row) for row in rows]

        except sqlite3.Error as e:
            print(f"❌ Lỗi truy vấn theo mức độ khẩn cấp: {e}")
            return []
        finally:
            conn.close()