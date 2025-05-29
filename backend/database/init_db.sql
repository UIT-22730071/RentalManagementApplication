CREATE TABLE Users (
    UserID INT AUTOINCREMENT PRIMARY KEY UNIQUE  NOT NULL,
    Username NVARCHAR(30) UNIQUE NOT NULL,
    Password NVARCHAR(255) NOT NULL,
    Role NVARCHAR(12) NOT NULL,
    IsActive BIT DEFAULT 0,
    CONSTRAINT chk_role CHECK (Users.role IN ('admin', 'landlord', 'tenant'))
);

CREATE TABLE Admins (
    AdminID INT AUTOINCREMENT PRIMARY KEY UNIQUE ,
    Fullname NVARCHAR (255) ,
    UserID INT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

CREATE TABLE Landlords (
    LandlordID INT PRIMARY KEY UNIQUE ,
    Fullname NVARCHAR(255),
    Birth Date, -- Lưu ngày sinh dưới dạng chuỗi 'YYYY-MM-DD'
    CCCD NVARCHAR(12) UNIQUE ,
    Gender NVARCHAR(4),
    JobTitle NVARCHAR(255),
    MaritalStatus NVARCHAR (30),
    Email NVARCHAR(30),
    PhoneNumber NVARCHAR(15),
    HomeAddress NVARCHAR(255),
    UserID INT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
    CONSTRAINT chk_martial_status CHECK ( Landlords.MaritalStatus IN ('Married', 'Single','Other') )
);

CREATE TABLE Tenants (
    TenantID INT PRIMARY KEY UNIQUE ,
    Fullname NVARCHAR(255) ,
    Birth Date, -- Lưu ngày sinh dưới dạng chuỗi 'YYYY-MM-DD'
    CCCD NVARCHAR(12) UNIQUE ,
    Gender NVARCHAR(4),
    JobTitle NVARCHAR(255),
    MaritalStatus NVARCHAR(30),
    Email NVARCHAR(30),
    PhoneNumber NVARCHAR(15),
    HomeAddress NVARCHAR(255),
    RentStartDate DATE,
    RentEndDate DATE,
    UserID INT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
    CONSTRAINT chk_martial_tenant_status CHECK ( Tenants.MaritalStatus IN ('Married', 'Single','Other') )
);

CREATE TABLE Rooms (
    RoomID INT PRIMARY KEY UNIQUE,
    RoomName NVARCHAR(100),
    Address NAVARCHAR(255),
    RoomPrice DECIMAL(10,2),
    ElectricityPrice DECIMAL(10,2),
    WaterPrice DECIMAL(10,2),
    GarbageServicePrice DECIMAL(10,2),
    CurrentElectricityNum MEDIUMINT,
    CurrentWaterNum MEDIUMINT,
    TenantID INT,
    LandlordID INT,
    FOREIGN KEY (TenantID) REFERENCES Tenants(TenantID) ON DELETE SET NULL,
    FOREIGN KEY (LandlordID) REFERENCES Landlords(LandlordID) ON DELETE CASCADE
);

CREATE TABLE Invoices (
    InvoiceID INTEGER PRIMARY KEY,
    RoomID INTEGER,
    TenantID INTEGER,
    LandlordID INTEGER,
    Date TEXT,  -- định dạng 'YYYY-MM-DD'
    PrevElectric INTEGER,
    CurrElectric INTEGER,
    PrevWater INTEGER,
    CurrWater INTEGER,
    ElectricPrice INTEGER,
    WaterPrice INTEGER,
    RoomPrice INTEGER,
    InternetFee INTEGER,
    GarbageFee INTEGER,
    OtherFee INTEGER,
    Discount INTEGER DEFAULT 0,
    Status TEXT CHECK (Status IN ('Đã thanh toán', 'Chưa thanh toán')),
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID),
    FOREIGN KEY (TenantID) REFERENCES Tenants(TenantID),
    FOREIGN KEY (LandlordID) REFERENCES Landlords(LandlordID)
);


CREATE TABLE QuangCao (
    id_advertisement INTEGER PRIMARY KEY AUTOINCREMENT,
    RoomID INT,
    Description TEXT,
    Prioritize TEXT,
    Picture TEXT,
    DateCreate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE MaintenanceRequests (
    RequestID INTEGER PRIMARY KEY AUTOINCREMENT,
    TenantID INTEGER,
    RoomID INTEGER,
    Description TEXT,
    Status TEXT CHECK (Status IN ('Pending', 'In Progress', 'Resolved')) DEFAULT 'Pending',
    RequestDate TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (TenantID) REFERENCES Tenants(TenantID),
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID)
);

CREATE TABLE Notifications (
    NotificationID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserID INTEGER,
    Content TEXT,
    IsRead INTEGER DEFAULT 0,
    CreatedAt TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

CREATE TABLE AnalystLanlord (
    idAnalysisLanlord INT PRIMARY KEY unique ,
    NumberRoom DECIMAL (10,2),
    AveragePrice DECIMAL (10,2),
    LandlordID INT,
    FOREIGN KEY (LandlordID) REFERENCES  Landlords (LandlordID) ON DELETE CASCADE
);

CREATE TABLE AnalystTenant(
    ActivityID INTEGER PRIMARY KEY,
    TenantID INTEGER,
    RoomID INTEGER,
    LandlordID INTEGER,
    StartDate TEXT, -- ngày bắt đầu thuê
    EndDate TEXT,   -- ngày kết thúc (có thể NULL nếu còn thuê)
    IsActive INTEGER, -- 1: còn thuê, 0: đã rời đi
    ReasonForLeaving TEXT, -- tuỳ chọn
    IncomeTenant DECIMAL (10,2),
    FOREIGN KEY (TenantID) REFERENCES Tenants(TenantID),
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID)
);

CREATE TABLE InvoiceAnalytics (
    InvoiceID INTEGER PRIMARY KEY,
    LandlordID INTEGER,
    RoomID INTEGER,
    TenantID INTEGER,
    InvoiceDate TEXT, -- YYYY-MM-DD
    RoomPrice INTEGER,
    ElectricityUsed INTEGER,
    ElectricityCost INTEGER,
    WaterUsed INTEGER,
    WaterCost INTEGER,
    InternetFee INTEGER,
    GarbageFee INTEGER,
    OtherFee INTEGER,
    TotalCost INTEGER,
    PaymentStatus TEXT, -- 'Paid' or 'Unpaid'
    FOREIGN KEY (InvoiceID) REFERENCES Invoices(InvoiceID)
);



