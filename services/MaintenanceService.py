import datetime
from typing import List, Dict, Optional

from QLNHATRO.RentalManagementApplication.Repository.MaintenanceRepository import MaintenanceRepository
from QLNHATRO.RentalManagementApplication.backend.model.MaintenanceRequest import MaintenanceRequest


class MaintenanceService:
    @staticmethod
    def create_request(room_id, tenant_id, description, image_path):
        request = MaintenanceRequest(room_id, tenant_id, description, image_path)
        MaintenanceRepository.save_request(request)
        return request

    @staticmethod
    def get_requests_by_room_id(room_id):
        return MaintenanceRepository.get_requests_by_room_id(room_id)

    @staticmethod
    def get_maintenance_list(landlord_id: int) -> List[Dict]:
        """
        Lấy danh sách yêu cầu bảo trì cho landlord

        Args:
            landlord_id: ID của landlord

        Returns:
            List[Dict]: Danh sách yêu cầu bảo trì đã được format
        """
        try:
            '''Phần này lỗi ====> toàn bộ id sẽ chuyển INT hoặc TEXT hết'''
            #if not landlord_id or landlord_id <= 0:
                #print("❌ Landlord ID không hợp lệ")
                #return []

            # Lấy dữ liệu từ repository
            maintenance_requests = MaintenanceRepository.get_maintenance_requests_by_landlord(landlord_id)

            # Format dữ liệu cho UI
            formatted_requests = []
            for request in maintenance_requests:
                formatted_request = MaintenanceService._format_maintenance_request(request)
                formatted_requests.append(formatted_request)

            print(f"✅ Lấy được {len(formatted_requests)} yêu cầu bảo trì cho landlord {landlord_id}")
            return formatted_requests

        except Exception as e:
            print(f"❌ Lỗi trong MaintenanceService.get_maintenance_list: {e}")
            return []

    @staticmethod
    def _format_maintenance_request(request: Dict) -> Dict:
        """
        Format maintenance request để hiển thị trên UI

        Args:
            request: Raw data từ database

        Returns:
            Dict: Formatted data
        """
        try:
            # Format ngày tháng
            created_at = request.get('created_at', '')
            if created_at:
                try:
                    # Chuyển đổi format ngày nếu cần
                    dt = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
                    formatted_date = dt.strftime('%d/%m/%Y')
                except:
                    formatted_date = created_at[:10]  # Lấy phần ngày
            else:
                formatted_date = 'N/A'

            # Format trạng thái
            status = request.get('status', 'Unknown')
            status_mapping = {
                'Pending': '⏳ Chờ xử lý',
                'In Progress': '🔄 Đang xử lý',
                'Resolved': '✅ Đã hoàn thành',
                'Đang xử lý': '🔄 Đang xử lý',
                'Đã hoàn thành': '✅ Đã hoàn thành'
            }
            formatted_status = status_mapping.get(status, status)

            # Format mức độ khẩn cấp
            urgency = request.get('urgency_level', 'Bình thường')
            urgency_mapping = {
                'Khẩn cấp': '🚨 Khẩn cấp',
                'Bình thường': '📝 Bình thường',
                'Thấp': '🔻 Thấp'
            }
            formatted_urgency = urgency_mapping.get(urgency, urgency)

            # Format loại sự cố
            issue_type = request.get('issue_type', '')
            issue_type_mapping = {
                'Điện': '⚡ Điện',
                'Nước': '💧 Nước',
                'Cấu trúc': '🏗️ Cấu trúc',
                'Điều hòa': '❄️ Điều hòa',
                'Khác': '🔧 Khác'
            }
            formatted_issue_type = issue_type_mapping.get(issue_type, f"🔧 {issue_type}")

            return {
                'stt': request.get('stt', 0),
                'request_id': request.get('request_id'),
                'room_id': request.get('room_id'),
                'room_name': request.get('room_name', 'N/A'),
                'tenant_id': request.get('tenant_id'),
                'tenant_name': request.get('tenant_name', 'N/A'),
                'tenant_phone': request.get('tenant_phone', ''),
                'issue_type': formatted_issue_type,
                'urgency_level': formatted_urgency,
                'description': request.get('description', ''),
                'contact_phone': request.get('contact_phone', request.get('tenant_phone', 'N/A')),
                'available_time': request.get('available_time', ''),
                'discovery_date': request.get('discovery_date', ''),
                'image_path': request.get('image_path', ''),
                'status': formatted_status,
                'created_at': formatted_date,
                # Raw values cho việc xử lý
                'raw_status': request.get('status'),
                'raw_urgency': request.get('urgency_level'),
                'raw_issue_type': request.get('issue_type')
            }

        except Exception as e:
            print(f"❌ Lỗi format maintenance request: {e}")
            return request

    @staticmethod
    def get_maintenance_detail(request_id: int) -> Optional[Dict]:
        """
        Lấy thông tin chi tiết một yêu cầu bảo trì

        Args:
            request_id: ID của yêu cầu bảo trì

        Returns:
            Optional[Dict]: Thông tin chi tiết hoặc None
        """
        try:
            if not request_id or request_id <= 0:
                print("❌ Request ID không hợp lệ")
                return None

            # Lấy dữ liệu từ repository
            request_detail = MaintenanceRepository.get_maintenance_request_by_id(request_id)

            if request_detail:
                return MaintenanceService._format_maintenance_request(request_detail)

            return None

        except Exception as e:
            print(f"❌ Lỗi trong MaintenanceService.get_maintenance_detail: {e}")
            return None

    @staticmethod
    def update_maintenance_status(request_id: int, new_status: str) -> Dict:
        """
        Cập nhật trạng thái yêu cầu bảo trì
        Returns:
            Dict: {'success': bool, 'message': str}
        """
        # Validate input đầu vào
        if not request_id or request_id <= 0:
            return {'success': False, 'message': 'ID yêu cầu không hợp lệ'}
        if not new_status:
            return {'success': False, 'message': 'Trạng thái không được để trống'}
        valid_statuses = ['Pending', 'In Progress', 'Resolved', 'Đang xử lý', 'Đã hoàn thành']
        if new_status not in valid_statuses:
            return {'success': False, 'message': f'Trạng thái không hợp lệ. Chỉ chấp nhận: {", ".join(valid_statuses)}'}

        # Thực hiện update DB, bắt exception rõ ràng
        try:
            success = MaintenanceRepository.update_maintenance_status(request_id, new_status)
            if success:
                return {'success': True, 'message': f'Đã cập nhật trạng thái thành "{new_status}" thành công'}
            return {'success': False, 'message': 'Không thể cập nhật trạng thái. Vui lòng thử lại.'}
        except Exception as e:
            # Có thể log lỗi chi tiết ở đây
            return {'success': False, 'message': f'Lỗi hệ thống: {str(e)}'}

    @staticmethod
    def create_maintenance_request(tenant_id: int, room_id: int, request_data: Dict) -> Dict:
        """
        Tạo yêu cầu bảo trì mới

        Args:
            tenant_id: ID người thuê
            room_id: ID phòng
            request_data: Dữ liệu yêu cầu bảo trì

        Returns:
            Dict: Kết quả thao tác
        """
        try:
            # Validate required fields
            required_fields = ['issue_type', 'urgency_level', 'description']
            for field in required_fields:
                if not request_data.get(field):
                    return {
                        'success': False,
                        'message': f'Thiếu thông tin bắt buộc: {field}'
                    }

            # Validate values
            valid_issue_types = ['Điện', 'Nước', 'Cấu trúc', 'Điều hòa', 'Khác']
            valid_urgency_levels = ['Khẩn cấp', 'Bình thường', 'Thấp']

            if request_data['issue_type'] not in valid_issue_types:
                return {
                    'success': False,
                    'message': f'Loại sự cố không hợp lệ. Chọn một trong: {", ".join(valid_issue_types)}'
                }

            if request_data['urgency_level'] not in valid_urgency_levels:
                return {
                    'success': False,
                    'message': f'Mức độ khẩn cấp không hợp lệ. Chọn một trong: {", ".join(valid_urgency_levels)}'
                }

            # Tạo yêu cầu trong database
            success = MaintenanceRepository.create_maintenance_request(
                tenant_id=tenant_id,
                room_id=room_id,
                issue_type=request_data['issue_type'],
                urgency_level=request_data['urgency_level'],
                description=request_data['description'],
                contact_phone=request_data.get('contact_phone'),
                available_time=request_data.get('available_time'),
                discovery_date=request_data.get('discovery_date'),
                image_path=request_data.get('image_path')
            )

            if success:
                return {
                    'success': True,
                    'message': 'Đã tạo yêu cầu bảo trì thành công'
                }
            else:
                return {
                    'success': False,
                    'message': 'Không thể tạo yêu cầu bảo trì. Vui lòng thử lại.'
                }

        except Exception as e:
            print(f"❌ Lỗi trong MaintenanceService.create_maintenance_request: {e}")
            return {
                'success': False,
                'message': f'Lỗi hệ thống: {str(e)}'
            }

    @staticmethod
    def get_maintenance_statistics(landlord_id: int) -> Dict:
        """
        Lấy thống kê yêu cầu bảo trì

        Args:
            landlord_id: ID của landlord

        Returns:
            Dict: Thống kê
        """
        try:
            if not landlord_id or landlord_id <= 0:
                print("❌ Landlord ID không hợp lệ")
                return {}

            stats = MaintenanceRepository.get_maintenance_statistics(landlord_id)

            if not stats:
                return {
                    'total_requests': 0,
                    'pending_count': 0,
                    'in_progress_count': 0,
                    'resolved_count': 0,
                    'urgent_count': 0
                }

            return stats

        except Exception as e:
            print(f"❌ Lỗi trong MaintenanceService.get_maintenance_statistics: {e}")
            return {}

    @staticmethod
    def delete_maintenance_request(request_id: int) -> Dict:
        """
        Xóa yêu cầu bảo trì

        Args:
            request_id: ID của yêu cầu bảo trì

        Returns:
            Dict: Kết quả thao tác
        """
        try:
            if not request_id or request_id <= 0:
                return {
                    'success': False,
                    'message': 'ID yêu cầu không hợp lệ'
                }

            success = MaintenanceRepository.delete_maintenance_request(request_id)

            if success:
                return {
                    'success': True,
                    'message': 'Đã xóa yêu cầu bảo trì thành công'
                }
            else:
                return {
                    'success': False,
                    'message': 'Không thể xóa yêu cầu bảo trì. Vui lòng thử lại.'
                }

        except Exception as e:
            print(f"❌ Lỗi trong MaintenanceService.delete_maintenance_request: {e}")
            return {
                'success': False,
                'message': f'Lỗi hệ thống: {str(e)}'
            }

    @staticmethod
    def filter_by_status(landlord_id: int, status: str) -> List[Dict]:
        """
        Lọc yêu cầu bảo trì theo trạng thái

        Args:
            landlord_id: ID của landlord
            status: Trạng thái cần lọc

        Returns:
            List[Dict]: Danh sách yêu cầu đã lọc
        """
        try:
            if status == "all":
                return MaintenanceService.get_maintenance_list(landlord_id)

            requests = MaintenanceRepository.get_maintenance_requests_by_status(landlord_id, status)
            return [MaintenanceService._format_maintenance_request(req) for req in requests]

        except Exception as e:
            print(f"❌ Lỗi trong MaintenanceService.filter_by_status: {e}")
            return []

    @staticmethod
    def filter_by_urgency(landlord_id: int, urgency: str) -> List[Dict]:
        """
        Lọc yêu cầu bảo trì theo mức độ khẩn cấp

        Args:
            landlord_id: ID của landlord
            urgency: Mức độ khẩn cấp cần lọc

        Returns:
            List[Dict]: Danh sách yêu cầu đã lọc
        """
        try:
            # Validate input
            if not landlord_id or landlord_id <= 0:
                print("❌ Landlord ID không hợp lệ")
                return []

            # Nếu lọc tất cả, trả về toàn bộ danh sách
            if urgency == "all":
                return MaintenanceService.get_maintenance_list(landlord_id)

            # Validate urgency level
            valid_urgency_levels = ['Khẩn cấp', 'Bình thường', 'Thấp']
            if urgency not in valid_urgency_levels:
                print(f"❌ Mức độ khẩn cấp không hợp lệ: {urgency}")
                return []

            # Lấy danh sách yêu cầu theo mức độ khẩn cấp
            requests = MaintenanceRepository.get_maintenance_requests_by_urgency(landlord_id, urgency)

            # Format dữ liệu
            formatted_requests = []
            for request in requests:
                formatted_request = MaintenanceService._format_maintenance_request(request)
                formatted_requests.append(formatted_request)

            print(
                f"✅ Lọc được {len(formatted_requests)} yêu cầu bảo trì với mức độ khẩn cấp '{urgency}' cho landlord {landlord_id}")
            return formatted_requests

        except Exception as e:
            print(f"❌ Lỗi trong MaintenanceService.filter_by_urgency: {e}")
            return []