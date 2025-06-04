-- USERS
INSERT INTO Users (Username, Password, Role, IsActive) VALUES
('admin01', 'admin123', 'admin', 1),
('landlord01', 'land123', 'landlord', 1),
('tenant01', 'ten123', 'tenant', 1);

-- ADMINS
INSERT INTO Admins (Fullname, UserID) VALUES
('Nguyễn Quản Trị', 1);

-- LANDLORDS
INSERT INTO Landlords (Fullname, CCCD, PhoneNumber, UserID) VALUES
('Trần Văn Chủ', '123456789012', '0989111222', 2);

-- TENANTS
INSERT INTO Tenants (Fullname, CCCD, PhoneNumber, UserID) VALUES
('Lê Thị Thuê', '987654321098', '0911223344', 3);

-- ROOMS
INSERT INTO Rooms (
    RoomName, Address, RoomType, Status, Area,
    Floor, HasLoft, Bathroom, Kitchen, Furniture, Balcony,
    FreeWifi, Parking, AirConditioner, Fridge, WashingMachine, Security, Television,
    PetAllowed, RoomPrice, ElectricityPrice, WaterPrice, InternetPrice, OtherFees,
    GarbageServicePrice, Deposit, CurrentElectricityNum, CurrentWaterNum,
    MaxTenants, RentalDate, Description, TenantID, LandlordID
) VALUES (
    'Phòng A1', '123 Đường Trọ, Q1, TPHCM', 'Phòng trọ thường', 'Còn trống', 25.0,
    2, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1,
    1, 3000000, 3500, 15000, 100000, 'Phí vệ sinh: 20000 VNĐ',
    20000, 1000000, 50, 10,
    2, '2025-06-01', 'Phòng có đầy đủ tiện nghi.', NULL, 1
);

-- INVOICES
INSERT INTO Invoices (
    RoomID, TenantID, LandlordID, issue_date,
    CurrElectric, CurrWater, PreElectric, PreWater,
    TotalElectronicCost, TotalWaterCost, TotalRoomPrice,
    InternetFee, TotalGarbageFee, TotalAnotherFee, Discount, Status
) VALUES (
    1, 1, 1, '2025-06-01',
    60, 15, 50, 10,
    35000, 75000, 3000000,
    100000, 20000, 50000, 0, 'Chưa thanh toán'
);

-- advertisements
INSERT INTO advertisements (RoomID, description, priority) VALUES
(1, 'Phòng mới xây, đầy đủ nội thất, gần chợ và trường học.', 'Cao');

-- maintenance_requests
INSERT INTO maintenance_requests (
    TenantID, RoomID, issue_type, urgency_level, description,
    contact_phone, available_time, discovery_date, image_path, status
) VALUES (
    1, 1, 'Điện', 'Khẩn cấp', 'Mất điện từ tối qua.',
    '0911223344', 'Chiều sau 5h', '2025-06-01', NULL, 'Pending'
);

-- Notifications
INSERT INTO Notifications (UserID, Content) VALUES
(1, 'Chào mừng bạn đến với hệ thống quản lý nhà trọ!');

-- landlord_analytics
INSERT INTO landlord_analytics (LandlordID, month, year, total_income, number_of_rented_rooms, average_price, growth_rate) VALUES
(1, 6, 2025, 3500000, 1, 3000000, 0.1);

-- tenant_analytics
INSERT INTO tenant_analytics (TenantID, month, year, electricity_cost, water_cost, due_date) VALUES
(1, 6, 2025, 35000, 75000, '2025-06-10');

-- RoomAnalytics
INSERT INTO RoomAnalytics (RoomID, Month, Year, ElectricityCost, WaterCost) VALUES
(1, 6, 2025, 35000, 75000);

-- InvoiceAnalytics
INSERT INTO InvoiceAnalytics (
    InvoiceID, LandlordID, RoomID, TenantID, InvoiceDate,
    RoomPrice, ElectricityUsed, ElectricityCost, WaterUsed, WaterCost,
    InternetFee, GarbageFee, OtherFee, TotalCost, PaymentStatus
) VALUES (
    1, 1, 1, 1, '2025-06-01',
    3000000, 10, 35000, 5, 75000,
    100000, 20000, 50000, 3285000, 'Chưa thanh toán'
);