-- Users table
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

-- Landlords table
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
    Floor INTEGER,              -- Tầng
    HasLoft INTEGER,            -- Gác lửng: 0 hoặc 1
    Bathroom TEXT,              -- Phòng tắm: "Riêng", "Chung",...
    Kitchen TEXT,               -- Nhà bếp: mô tả
    Balcony TEXT,               -- Ban công
    Furniture TEXT,             -- Nội thất cơ bản
    ElectricalDevices TEXT,     -- Thiết bị điện
    Utilities TEXT,             -- Tiện ích khác (Wifi, Camera, ...)
    RoomPrice REAL,            -- Giá thuê phòng
    Deposit REAL,              -- Tiền cọc
    ElectricityPrice REAL,     -- Giá điện
    GarbageServicePrice REAL,  -- Giá dịch vụ rác thải
    CurrentElectricityNum INTEGER, -- Số điện hiện tại
    CurrentWaterNum INTEGER,   -- Số nước hiện tại
    GarbageServicePrice REAL,  -- Giá dịch vụ rác thải
    ElectricityPrice REAL,      -- Giá điện
    WaterPrice REAL,           -- Giá nước
    InternetPrice REAL,        -- Giá internet
    OtherFees TEXT,            -- Phí khác: "Phí vệ sinh: 20000 VNĐ"
    MaxTenants INTEGER,        -- Số người tối đa
    PetAllowed TEXT,           -- Thú cưng: "Có", "Không"
    AvailableFrom TEXT,        -- Ngày có thể thuê (dạng YYYY-MM-DD)
    CurrentElectricityNum INTEGER,
    CurrentWaterNum INTEGER,
    TenantID INTEGER,          -- Người thuê hiện tại (nullable)
    LandlordID INTEGER,        -- Chủ trọ
    FOREIGN KEY (TenantID) REFERENCES Tenants(TenantID) ON DELETE SET NULL,
    FOREIGN KEY (LandlordID) REFERENCES Landlords(LandlordID) ON DELETE CASCADE
);

-- Invoices table
CREATE TABLE IF NOT EXISTS Invoices (
    InvoiceID INTEGER PRIMARY KEY AUTOINCREMENT,
    RoomID INTEGER,
    TenantID INTEGER,
    LandlordID INTEGER,
    Date TEXT,
    PrevElectric INTEGER,
    CurrElectric INTEGER,
    PrevWater INTEGER,
    CurrWater INTEGER,
    ElectricPrice REAL,
    WaterPrice REAL,
    RoomPrice REAL,
    InternetFee REAL,
    GarbageFee REAL,
    OtherFee REAL,
    Discount REAL DEFAULT 0,
    Status TEXT CHECK (Status IN ('Đã thanh toán', 'Chưa thanh toán')),
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID),
    FOREIGN KEY (TenantID) REFERENCES Tenants(TenantID),
    FOREIGN KEY (LandlordID) REFERENCES Landlords(LandlordID)
);

-- QuangCao table
CREATE TABLE IF NOT EXISTS QuangCao (
    id_advertisement INTEGER PRIMARY KEY AUTOINCREMENT,
    RoomID INTEGER,
    Description TEXT,
    Prioritize TEXT,
    Picture TEXT,
    DateCreate TEXT DEFAULT CURRENT_TIMESTAMP
);

-- MaintenanceRequests table
CREATE TABLE IF NOT EXISTS MaintenanceRequests (
    RequestID INTEGER PRIMARY KEY AUTOINCREMENT,
    TenantID INTEGER,
    RoomID INTEGER,
    Description TEXT,
    Status TEXT CHECK (Status IN ('Pending', 'In Progress', 'Resolved')) DEFAULT 'Pending',
    RequestDate TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (TenantID) REFERENCES Tenants(TenantID),
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID)
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
CREATE TABLE IF NOT EXISTS AnalystLanlord (
    idAnalysisLanlord INTEGER PRIMARY KEY AUTOINCREMENT,
    NumberRoom REAL,
    AveragePrice REAL,
    LandlordID INTEGER,
    FOREIGN KEY (LandlordID) REFERENCES Landlords(LandlordID) ON DELETE CASCADE
);

-- AnalystTenant table
CREATE TABLE IF NOT EXISTS AnalystTenant (
    ActivityID INTEGER PRIMARY KEY AUTOINCREMENT,
    TenantID INTEGER,
    RoomID INTEGER,
    LandlordID INTEGER,
    StartDate TEXT,
    EndDate TEXT,
    IsActive INTEGER,
    ReasonForLeaving TEXT,
    IncomeTenant REAL,
    FOREIGN KEY (TenantID) REFERENCES Tenants(TenantID),
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID)
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