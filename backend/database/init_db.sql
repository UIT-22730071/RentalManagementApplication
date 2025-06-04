-- XÓA DỮ LIỆU TRƯỚC KHI CHÈN MỚI
DELETE FROM Users;
DELETE FROM Admins;
DELETE FROM Landlords;
DELETE FROM Tenants;
DELETE FROM Rooms;
DELETE FROM Invoices;
DELETE FROM advertisements;
DELETE FROM maintenance_requests;
DELETE FROM Notifications;
DELETE FROM landlord_analytics;
DELETE FROM tenant_analytics;
DELETE FROM RoomAnalytics;
DELETE FROM InvoiceAnalytics;



-- User's table
CREATE TABLE IF NOT EXISTS Users (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Username TEXT UNIQUE NOT NULL,
    Password TEXT NOT NULL,
    Role TEXT NOT NULL CHECK (Role IN ('admin', 'landlord', 'tenant')),
    IsActive INTEGER DEFAULT 0
);

-- Admins table
CREATE TABLE IF NOT EXISTS Admins (
    AdminID INTEGER PRIMARY KEY AUTOINCREMENT,
    Fullname TEXT,
    UserID INTEGER,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Landlord table
CREATE TABLE IF NOT EXISTS Landlords (
    LandlordID INTEGER PRIMARY KEY AUTOINCREMENT,
    Fullname TEXT,
    Birth TEXT, -- 'YYYY-MM-DD'
    CCCD TEXT UNIQUE,
    Gender TEXT,
    JobTitle TEXT,
    MaritalStatus TEXT CHECK (MaritalStatus IN ('Married', 'Single', 'Other')),
    Email TEXT,
    PhoneNumber TEXT,
    HomeAddress TEXT,
    UserID INTEGER,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Tenants table
CREATE TABLE IF NOT EXISTS Tenants (
    TenantID INTEGER PRIMARY KEY AUTOINCREMENT,
    Fullname TEXT,
    Birth TEXT,
    CCCD TEXT UNIQUE,
    Gender TEXT,
    JobTitle TEXT,
    MaritalStatus TEXT CHECK (MaritalStatus IN ('Married', 'Single', 'Other')),
    Email TEXT,
    PhoneNumber TEXT,
    HomeAddress TEXT,
    RentStartDate TEXT,
    RentEndDate TEXT,
    UserID INTEGER,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Rooms table
CREATE TABLE IF NOT EXISTS Rooms (
    RoomID INTEGER PRIMARY KEY AUTOINCREMENT,
    RoomName TEXT,
    Address TEXT,
    RoomType TEXT,              -- Loại phòng: ví dụ "Phòng trọ trong dãy trọ"
    Status TEXT,                -- Trạng thái: "Còn trống" hoặc "Đã thuê"
    Area REAL,                  -- Diện tích (m²)

    Floor INTEGER DEFAULT 0,              -- Tầng
    HasLoft INTEGER DEFAULT 0,            -- Gác lửng: 0 hoặc 1
    Bathroom INTEGER DEFAULT 0,              -- Phòng tắm: "Riêng", "Chung",...
    Kitchen INTEGER DEFAULT 0,              -- Nhà bếp: mô tả
    Furniture INTEGER DEFAULT 0,             -- Nội thất cơ bản
    Balcony INTEGER DEFAULT 0,          -- Ban công   -- Có ban công

    FreeWifi INTEGER DEFAULT 0,             -- Wifi miễn phí 1
    Parking INTEGER DEFAULT 0,              -- Chổ đậu xe  1
    AirConditioner INTEGER DEFAULT 0,       -- Máy điều hòa 1
    Fridge INTEGER DEFAULT 0,               -- Tủ lạnh 1
    WashingMachine INTEGER DEFAULT 0,       -- Máy giặt 1
    Security INTEGER DEFAULT 0,             -- Có bảo vệ 1
    Television INTEGER DEFAULT 0,           -- Có tivi 1

    PetAllowed INTEGER DEFAULT 0,           -- Thú cưng: " 0: không cho phép", "1: cho phép"
    -- giá cả
    RoomPrice REAL,            -- Giá thuê phòng
    ElectricityPrice REAL,      -- Giá điện
    WaterPrice REAL,           -- Giá nước
    InternetPrice REAL,        -- Giá internet
    OtherFees TEXT,            -- Phí khác: "Phí vệ sinh: 20000 VNĐ"
    GarbageServicePrice REAL,  -- Giá dịch vụ rác thải
    Deposit REAL,              -- Tiền cọc // load vào sau
    --  Chỉ số điện
    CurrentElectricityNum INTEGER, -- Số điện hiện tại, được cập nhật khi tạo phòng và tạo Invoice
    CurrentWaterNum INTEGER,       -- Số nước hiện tại, được cập nhật khi tạo phòng và tạo Invoice
    -- Thông tin thêm
    MaxTenants INTEGER,         -- Số người tối đa
    RentalDate Date,            -- Ngày cho thuê (dạng YYYY-MM-DD) được update khi có người thuê trọ
    Description TEXT,           -- Mô tả thêm

    TenantID INTEGER,          -- Người thuê hiện tại (nullable)
    LandlordID INTEGER NOT NULL ,        -- Chủ trọ

    FOREIGN KEY (TenantID) REFERENCES Tenants(TenantID) ON DELETE SET NULL,
    FOREIGN KEY (LandlordID) REFERENCES Landlords(LandlordID) ON DELETE CASCADE
);
-- CurrentE or CUrrentW khi tạo phòng đã phải nhập, vậy khi hoạt động chỉ cần cập nhật cho nó ở Invoices
-- Lưu ý: PreElectricityNum là ở Invoices là số điện hiện tại tức là CurentElectricityNum ở Rooms
    -- Còn CurrentElectroniccityNum ở Invoices là số điện được nhập vào ở tháng hiện tại
-- Invoices table
CREATE TABLE IF NOT EXISTS Invoices (
    InvoiceID INTEGER PRIMARY KEY AUTOINCREMENT,
    RoomID INTEGER,
    TenantID INTEGER,
    LandlordID INTEGER,

    issue_date TEXT NOT NULL,  -- ISO format 'YYYY-MM-DD'              -- Ngày tạo hóa đơn

    CurrElectric INTEGER,   -- Số điện hiện tại được lấy từ form tạo hóa đơn
    CurrWater INTEGER,      -- Số nước hiện tại được lấy từ form tạo hóa đơn
    PreElectric  INTEGER, -- Số điện trước đó (CurrentElectricityNum ở Rooms)
    PreWater  INTEGER,    -- Số nước trước đó (CurrentWaterNum ở Rooms)

    -- Số điện đã sử dụng (CurrElectric - PreElectricityNum)
    --ElectricPrice REAL,   -- Lấy giá từ Rooms
    --WaterPrice REAL,      -- Lấy giá từ Rooms
    --RoomPrice REAL,       -- Lấy giá từ Rooms
    -- InternetFee REAL,     -- Lấy giá từ Rooms
    -- GarbageFee REAL,      -- Lấy giá từ Rooms

    TotalElectronicCost REAL,   -- Current - PreElectricityNum
    TotalWaterCost REAL,    -- Current - PreWaterNum
    TotalRoomPrice REAL,    -- Giá thuê phòng từ Rooms
    InternetFee REAL,       -- Giá internet từ Rooms
    TotalGarbageFee REAL,   -- Giá dịch vụ rác thải từ Rooms
    TotalAnotherFee REAL,   -- Phí khác từ Rooms

    Discount REAL DEFAULT 0,

    Status TEXT DEFAULT 'Chưa thanh toán'CHECK (Status IN ('Đã thanh toán', 'Chưa thanh toán')),

    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID),
    FOREIGN KEY (TenantID) REFERENCES Tenants(TenantID),
    FOREIGN KEY (LandlordID) REFERENCES Landlords(LandlordID)
);


-- QuangCao table
CREATE TABLE IF NOT EXISTS advertisements (
    ad_id INTEGER PRIMARY KEY AUTOINCREMENT,
    RoomID INTEGER NOT NULL,
    description TEXT,
    priority TEXT,
    image_path TEXT DEFAULT 'default_image.png',
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (RoomID) REFERENCES rooms(RoomID) ON DELETE CASCADE
);


-- MaintenanceRequests table
CREATE TABLE IF NOT EXISTS maintenance_requests (
    request_id INTEGER PRIMARY KEY AUTOINCREMENT,
    TenantID INTEGER NOT NULL,
    RoomID INTEGER NOT NULL,

    issue_type TEXT NOT NULL,           -- VD: "Điện", "Nước", "Cấu trúc", v.v.
    urgency_level TEXT NOT NULL,        -- VD: "Bình thường", "Khẩn cấp"
    description TEXT NOT NULL,          -- Nội dung mô tả chi tiết

    contact_phone TEXT,    -- Số điện thoại liên hệ/ nếu không có sẽ tự load số điện thoại của người tạo
    available_time TEXT,   -- Thời gian thuận tiện liên hệ

    discovery_date TEXT,                -- Ngày phát hiện sự cố
    image_path TEXT,                    -- Đường dẫn ảnh minh họa (nếu có)

    status TEXT DEFAULT 'Pending' CHECK (status IN ('Pending', 'In Progress', 'Resolved', 'Đang xử lý', 'Đã hoàn thành')),
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (TenantID) REFERENCES tenants(TenantID),
    FOREIGN KEY (RoomID) REFERENCES rooms(RoomID)
);


-- Notifications table
CREATE TABLE IF NOT EXISTS Notifications (
    NotificationID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserID INTEGER,
    Content TEXT,
    IsRead INTEGER DEFAULT 0,
    CreatedAt TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);


-- AnalystLanlord table
CREATE TABLE IF NOT EXISTS landlord_analytics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    LandlordID INTEGER NOT NULL,
    month INTEGER CHECK (month BETWEEN 1 AND 12),
    year INTEGER CHECK (year >= 2000),
    total_income REAL DEFAULT 0,
    number_of_rented_rooms INTEGER,
    average_price REAL,
    growth_rate REAL DEFAULT 0,
    FOREIGN KEY (LandlordID) REFERENCES landlords(LandlordID) ON DELETE CASCADE,
    UNIQUE (LandlordID, month, year)
);



-- AnalystTenant table
CREATE TABLE IF NOT EXISTS tenant_analytics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    TenantID INTEGER NOT NULL,
    month INTEGER CHECK (month BETWEEN 1 AND 12),
    year INTEGER CHECK (year >= 2000),
    electricity_cost REAL DEFAULT 0,
    water_cost REAL DEFAULT 0,
    total_cost REAL GENERATED ALWAYS AS (electricity_cost + water_cost) VIRTUAL,
    due_date TEXT,
    FOREIGN KEY (TenantID) REFERENCES tenants(TenantID),
    UNIQUE (TenantID, month, year)
);


CREATE TABLE IF NOT EXISTS RoomAnalytics (
    idRoomAnalytics INTEGER PRIMARY KEY AUTOINCREMENT,
    RoomID INTEGER,
    Month INTEGER CHECK (Month BETWEEN 1 AND 12),
    Year INTEGER CHECK (Year >= 2000),
    ElectricityCost REAL DEFAULT 0,     -- Tổng tiền điện
    WaterCost REAL DEFAULT 0,           -- Tổng tiền nước
    TotalCost REAL GENERATED ALWAYS AS (ElectricityCost + WaterCost) VIRTUAL,
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE,
    UNIQUE (RoomID, Month, Year)
);

-- InvoiceAnalytics table
CREATE TABLE IF NOT EXISTS InvoiceAnalytics (
    InvoiceID INTEGER PRIMARY KEY AUTOINCREMENT,
    LandlordID INTEGER,
    RoomID INTEGER,
    TenantID INTEGER,
    InvoiceDate TEXT,
    RoomPrice REAL,
    ElectricityUsed INTEGER,
    ElectricityCost REAL,
    WaterUsed INTEGER,
    WaterCost REAL,
    InternetFee REAL,
    GarbageFee REAL,
    OtherFee REAL,
    TotalCost REAL,
    PaymentStatus TEXT,
    FOREIGN KEY (InvoiceID) REFERENCES Invoices(InvoiceID)
);

-- Dữ liệu mẫu cho bảng Users
INSERT INTO Users (Username, Password, Role, IsActive) VALUES
('admin01', 'hashed_password_1', 'admin', 1),
('landlord01', 'hashed_password_2', 'landlord', 1),
('landlord02', 'hashed_password_3', 'landlord', 1),
('tenant01', 'hashed_password_4', 'tenant', 1),
('tenant02', 'hashed_password_5', 'tenant', 1),
('landlord_main', 'landlord', 'landlord', 1),
('tenant_main', 'tenant', 'tenant', 1),
('admin_main', 'admin', 'admin', 1);

-- Dữ liệu mẫu cho bảng Admins
INSERT INTO Admins (Fullname, UserID) VALUES
('Nguyễn Văn Admin', 1),
('Trần Thị Quản lý', 1),
('Lê Văn Điều hành', 1);

-- Dữ liệu mẫu cho bảng Landlords
INSERT INTO Landlords (Fullname, Birth, CCCD, Gender, JobTitle, MaritalStatus, Email, PhoneNumber, HomeAddress, UserID) VALUES
('Nguyễn Văn Hùng', '1980-05-15', '123456789012', 'Nam', 'Kinh doanh bất động sản', 'Married', 'hung.nguyen@email.com', '0901234567', '123 Đường ABC, Quận 1, TP.HCM', 2),
('Trần Thị Lan', '1975-08-22', '123456789013', 'Nữ', 'Đầu tư bất động sản', 'Single', 'lan.tran@email.com', '0912345678', '456 Đường DEF, Quận 3, TP.HCM', 3),
('Lê Minh Tuấn', '1985-12-10', '123456789014', 'Nam', 'Chủ nhà trọ', 'Married', 'tuan.le@email.com', '0923456789', '789 Đường GHI, Quận 5, TP.HCM', 2),
('Phạm Thị Hoa', '1978-03-18', '123456789015', 'Nữ', 'Kinh doanh nhà trọ', 'Other', 'hoa.pham@email.com', '0934567890', '321 Đường JKL, Quận 7, TP.HCM', 3);

-- Dữ liệu mẫu cho bảng Tenants
INSERT INTO Tenants (Fullname, Birth, CCCD, Gender, JobTitle, MaritalStatus, Email, PhoneNumber, HomeAddress, RentStartDate, RentEndDate, UserID) VALUES
('Võ Thành Nam', '1995-06-20', '987654321012', 'Nam', 'Nhân viên IT', 'Single', 'nam.vo@email.com', '0945678901', '111 Đường MNO, Quận 2, TP.HCM', '2024-01-15', '2024-12-15', 4),
('Đỗ Thị Mai', '1992-09-12', '987654321013', 'Nữ', 'Kế toán', 'Married', 'mai.do@email.com', '0956789012', '222 Đường PQR, Quận 4, TP.HCM', '2024-02-01', '2025-01-31', 5),
('Hoàng Văn Đức', '1990-11-05', '987654321014', 'Nam', 'Giáo viên', 'Single', 'duc.hoang@email.com', '0967890123', '333 Đường STU, Quận 6, TP.HCM', '2023-12-01', '2024-11-30', 4),
('Bùi Thị Linh', '1996-04-25', '987654321015', 'Nữ', 'Nhân viên ngân hàng', 'Single', 'linh.bui@email.com', '0978901234', '444 Đường VWX, Quận 8, TP.HCM', '2024-03-01', '2025-02-28', 5);

-- Dữ liệu mẫu cho bảng Rooms
INSERT INTO Rooms (RoomName, Address, RoomType, Status, Area, Floor, HasLoft, Bathroom, Kitchen, Furniture, Balcony, FreeWifi, Parking, AirConditioner, Fridge, WashingMachine, Security, Television, PetAllowed, RoomPrice, ElectricityPrice, WaterPrice, InternetPrice, OtherFees, GarbageServicePrice, Deposit, CurrentElectricityNum, CurrentWaterNum, MaxTenants, RentalDate, Description, TenantID, LandlordID) VALUES
('Phòng A101', '123 Đường ABC, Quận 1, TP.HCM', 'Phòng trọ trong dãy trọ', 'Đã thuê', 25.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 3500000, 3500, 15000, 100000, 'Phí vệ sinh: 50000 VNĐ', 50000, 7000000, 1250, 45, 2, '2024-01-15', 'Phòng đầy đủ tiện nghi, gần trung tâm', 1, 1),
('Phòng B202', '456 Đường DEF, Quận 3, TP.HCM', 'Phòng trọ trong dãy trọ', 'Đã thuê', 20.0, 2, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 2800000, 3500, 15000, 80000, 'Phí vệ sinh: 40000 VNĐ', 40000, 5600000, 1180, 38, 2, '2024-02-01', 'Phòng thoáng mát, an ninh tốt', 2, 2),
('Phòng C301', '789 Đường GHI, Quận 5, TP.HCM', 'Phòng trọ trong dãy trọ', 'Còn trống', 18.5, 3, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 2200000, 3500, 15000, 60000, 'Phí vệ sinh: 30000 VNĐ', 30000, 4400000, 1050, 32, 1, NULL, 'Phòng cơ bản, giá rẻ', NULL, 3),
('Phòng D102', '321 Đường JKL, Quận 7, TP.HCM', 'Phòng trọ trong dãy trọ', 'Đã thuê', 30.0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4200000, 3500, 15000, 120000, 'Phí vệ sinh: 60000 VNĐ', 60000, 8400000, 1320, 52, 3, '2023-12-01', 'Phòng cao cấp, đầy đủ tiện ích', 3, 4),
('Phòng E203', '555 Đường YZ, Quận 9, TP.HCM', 'Phòng trọ trong dãy trọ', 'Còn trống', 22.0, 2, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 3000000, 3500, 15000, 90000, 'Phí vệ sinh: 45000 VNĐ', 45000, 6000000, 1100, 40, 2, NULL, 'Phòng thoáng, view đẹp', NULL, 1);

-- Dữ liệu mẫu cho bảng Invoices
INSERT INTO Invoices (RoomID, TenantID, LandlordID, issue_date, CurrElectric, CurrWater, PreElectric, PreWater, TotalElectronicCost, TotalWaterCost, TotalRoomPrice, InternetFee, TotalGarbageFee, TotalAnotherFee, Discount, Status) VALUES
(1, 1, 1, '2024-02-01', 1350, 50, 1250, 45, 350000, 75000, 3500000, 100000, 50000, 0, 0, 'Đã thanh toán'),
(2, 2, 2, '2024-03-01', 1280, 43, 1180, 38, 350000, 75000, 2800000, 80000, 40000, 0, 100000, 'Đã thanh toán'),
(4, 3, 4, '2024-01-01', 1420, 57, 1320, 52, 350000, 75000, 4200000, 120000, 60000, 0, 0, 'Chưa thanh toán'),
(1, 1, 1, '2024-03-01', 1450, 55, 1350, 50, 350000, 75000, 3500000, 100000, 50000, 0, 0, 'Đã thanh toán'),
(2, 2, 2, '2024-04-01', 1380, 48, 1280, 43, 350000, 75000, 2800000, 80000, 40000, 0, 0, 'Chưa thanh toán');

-- Dữ liệu mẫu cho bảng advertisements
INSERT INTO advertisements (RoomID, description, priority, image_path, created_at) VALUES
(3, 'Phòng trọ giá rẻ, gần chợ và trường học', 'High', 'room_c301.jpg', '2024-05-01 10:00:00'),
(5, 'Phòng mới, view đẹp, thoáng mát', 'Medium', 'room_e203.jpg', '2024-05-15 14:30:00'),
(3, 'Cho thuê phòng trọ an ninh tốt', 'Low', 'room_c301_2.jpg', '2024-05-20 09:15:00'),
(5, 'Phòng trọ đầy đủ tiện nghi', 'High', 'room_e203_2.jpg', '2024-05-25 16:45:00'),
(3, 'Phòng trống cần thuê gấp', 'Medium', 'room_c301_3.jpg', '2024-06-01 08:00:00');

-- Dữ liệu mẫu cho bảng maintenance_requests
INSERT INTO maintenance_requests (TenantID, RoomID, issue_type, urgency_level, description, contact_phone, available_time, discovery_date, image_path, status, created_at) VALUES
(1, 1, 'Điện', 'Khẩn cấp', 'Cầu dao bị chạm, mất điện toàn phòng', '0945678901', '8:00-18:00', '2024-05-28', 'electric_issue_1.jpg', 'Đang xử lý', '2024-05-28 07:30:00'),
(2, 2, 'Nước', 'Bình thường', 'Vòi nước bị rỉ, cần thay mới', '0956789012', '18:00-22:00', '2024-05-25', 'water_leak_1.jpg', 'Pending', '2024-05-25 19:00:00'),
(3, 4, 'Cấu trúc', 'Khẩn cấp', 'Trần nhà bị nứt, có nguy cơ rơi', '0967890123', 'Bất kỳ lúc nào', '2024-05-30', 'ceiling_crack.jpg', 'In Progress', '2024-05-30 06:00:00'),
(1, 1, 'Khác', 'Bình thường', 'Cửa phòng bị kẹt, khó đóng mở', '0945678901', '12:00-14:00', '2024-06-01', 'door_issue.jpg', 'Resolved', '2024-06-01 12:30:00'),
(2, 2, 'Điện', 'Bình thường', 'Ổ cắm bị lỏng, cần sửa chữa', '0956789012', '19:00-21:00', '2024-06-02', 'socket_issue.jpg', 'Đã hoàn thành', '2024-06-02 20:00:00');

-- Dữ liệu mẫu cho bảng Notifications
INSERT INTO Notifications (UserID, Content, IsRead, CreatedAt) VALUES
(4, 'Hóa đơn tháng 3 đã được tạo. Vui lòng thanh toán trước ngày 10/4.', 1, '2024-04-01 09:00:00'),
(5, 'Yêu cầu sửa chữa của bạn đã được tiếp nhận và đang xử lý.', 1, '2024-05-25 20:00:00'),
(2, 'Có tenant mới quan tâm đến phòng C301 của bạn.', 0, '2024-06-01 10:30:00'),
(4, 'Nhắc nhở thanh toán hóa đơn tháng 4 sắp đến hạn.', 0, '2024-06-03 08:00:00'),
(3, 'Yêu cầu bảo trì khẩn cấp tại phòng D102 cần được xử lý ngay.', 0, '2024-05-30 06:15:00');

-- Dữ liệu mẫu cho bảng landlord_analytics
INSERT INTO landlord_analytics (LandlordID, month, year, total_income, number_of_rented_rooms, average_price, growth_rate) VALUES
(1, 1, 2024, 4075000, 1, 4075000, 0),
(1, 2, 2024, 4075000, 1, 4075000, 0),
(1, 3, 2024, 4075000, 1, 4075000, 0),
(2, 2, 2024, 3345000, 1, 3345000, 0),
(2, 3, 2024, 3345000, 1, 3345000, 0),
(4, 12, 2023, 4805000, 1, 4805000, 0),
(4, 1, 2024, 4805000, 1, 4805000, 0);

-- Dữ liệu mẫu cho bảng tenant_analytics
INSERT INTO tenant_analytics (TenantID, month, year, electricity_cost, water_cost, due_date) VALUES
(1, 2, 2024, 350000, 75000, '2024-03-10'),
(1, 3, 2024, 350000, 75000, '2024-04-10'),
(2, 3, 2024, 350000, 75000, '2024-04-10'),
(2, 4, 2024, 350000, 75000, '2024-05-10'),
(3, 1, 2024, 350000, 75000, '2024-02-10');

-- Dữ liệu mẫu cho bảng RoomAnalytics
INSERT INTO RoomAnalytics (RoomID, Month, Year, ElectricityCost, WaterCost) VALUES
(1, 2, 2024, 350000, 75000),
(1, 3, 2024, 350000, 75000),
(2, 3, 2024, 350000, 75000),
(2, 4, 2024, 350000, 75000),
(4, 1, 2024, 350000, 75000);

-- Dữ liệu mẫu cho bảng InvoiceAnalytics
INSERT INTO InvoiceAnalytics (InvoiceID, LandlordID, RoomID, TenantID, InvoiceDate, RoomPrice, ElectricityUsed, ElectricityCost, WaterUsed, WaterCost, InternetFee, GarbageFee, OtherFee, TotalCost, PaymentStatus) VALUES
(1, 1, 1, 1, '2024-02-01', 3500000, 100, 350000, 5, 75000, 100000, 50000, 0, 4075000, 'Đã thanh toán'),
(2, 2, 2, 2, '2024-03-01', 2800000, 100, 350000, 5, 75000, 80000, 40000, 0, 3245000, 'Đã thanh toán'),
(3, 4, 4, 3, '2024-01-01', 4200000, 100, 350000, 5, 75000, 120000, 60000, 0, 4805000, 'Chưa thanh toán'),
(4, 1, 1, 1, '2024-03-01', 3500000, 100, 350000, 5, 75000, 100000, 50000, 0, 4075000, 'Đã thanh toán'),
(5, 2, 2, 2, '2024-04-01', 2800000, 100, 350000, 5, 75000, 80000, 40000, 0, 3345000, 'Chưa thanh toán');