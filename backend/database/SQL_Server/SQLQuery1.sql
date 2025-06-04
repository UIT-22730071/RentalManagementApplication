create database DB_Rental_House

CREATE TABLE Users (
    UserID INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
    Username NVARCHAR(100) UNIQUE NOT NULL,
    Password NVARCHAR(255) NOT NULL,
    Role NVARCHAR(20) NOT NULL CHECK (Role IN ('admin', 'landlord', 'tenant')),
    IsActive BIT DEFAULT 0
);
CREATE TABLE Admins (
    AdminID INT IDENTITY(1,1) PRIMARY KEY,
    Fullname NVARCHAR(255),
    UserID INT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);
CREATE TABLE Landlords (
    LandlordID INT IDENTITY(1,1) PRIMARY KEY,
    Fullname NVARCHAR(255),
    Birth DATE,
    CCCD NVARCHAR(50) UNIQUE,
    Gender NVARCHAR(20),
    JobTitle NVARCHAR(100),
    MaritalStatus NVARCHAR(20) CHECK (MaritalStatus IN ('Married', 'Single', 'Other')),
    Email NVARCHAR(100),
    PhoneNumber NVARCHAR(20),
    HomeAddress NVARCHAR(255),
    UserID INT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);
CREATE TABLE Tenants (
    TenantID INT IDENTITY(1,1) PRIMARY KEY,
    Fullname NVARCHAR(255),
    Birth DATE,
    CCCD NVARCHAR(50) UNIQUE,
    Gender NVARCHAR(20),
    JobTitle NVARCHAR(100),
    MaritalStatus NVARCHAR(20) CHECK (MaritalStatus IN ('Married', 'Single', 'Other')),
    Email NVARCHAR(100),
    PhoneNumber NVARCHAR(20),
    HomeAddress NVARCHAR(255),
    RentStartDate DATE,
    RentEndDate DATE,
    UserID INT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);
CREATE TABLE Rooms (
    RoomID INT IDENTITY(1,1) PRIMARY KEY,
    RoomName NVARCHAR(255),
    Address NVARCHAR(255),
    RoomType NVARCHAR(100),
    Status NVARCHAR(30),
    Area FLOAT,
    Floor INT DEFAULT 0,
    HasLoft BIT DEFAULT 0,
    Bathroom BIT DEFAULT 0,
    Kitchen BIT DEFAULT 0,
    Furniture BIT DEFAULT 0,
    Balcony BIT DEFAULT 0,
    FreeWifi BIT DEFAULT 0,
    Parking BIT DEFAULT 0,
    AirConditioner BIT DEFAULT 0,
    Fridge BIT DEFAULT 0,
    WashingMachine BIT DEFAULT 0,
    Security BIT DEFAULT 0,
    Television BIT DEFAULT 0,
    PetAllowed BIT DEFAULT 0,
    RoomPrice FLOAT,
    ElectricityPrice FLOAT,
    WaterPrice FLOAT,
    InternetPrice FLOAT,
    OtherFees NVARCHAR(255),
    GarbageServicePrice FLOAT,
    Deposit FLOAT,
    CurrentElectricityNum INT,
    CurrentWaterNum INT,
    MaxTenants INT,
    RentalDate DATE,
    Description NVARCHAR(500),
    TenantID INT NULL,
    LandlordID INT NOT NULL,
    FOREIGN KEY (TenantID) REFERENCES Tenants(TenantID),
    FOREIGN KEY (LandlordID) REFERENCES Landlords(LandlordID) ON DELETE CASCADE
);

CREATE TABLE Invoices (
    InvoiceID INT IDENTITY(1,1) PRIMARY KEY,
    RoomID INT,
    TenantID INT,
    LandlordID INT,
    issue_date DATE NOT NULL,
    CurrElectric INT,
    CurrWater INT,
    PreElectric INT,
    PreWater INT,
    TotalElectronicCost FLOAT,
    TotalWaterCost FLOAT,
    TotalRoomPrice FLOAT,
    InternetFee FLOAT,
    TotalGarbageFee FLOAT,
    TotalAnotherFee FLOAT,
    Discount FLOAT DEFAULT 0,
    Status NVARCHAR(30) DEFAULT 'Chưa thanh toán' CHECK (Status IN ('Đã thanh toán', 'Chưa thanh toán')),
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID),
    FOREIGN KEY (TenantID) REFERENCES Tenants(TenantID),
    FOREIGN KEY (LandlordID) REFERENCES Landlords(LandlordID)
);
CREATE TABLE advertisements (
    ad_id INT IDENTITY(1,1) PRIMARY KEY,
    RoomID INT NOT NULL,
    description NVARCHAR(500),
    priority NVARCHAR(50),
    image_path NVARCHAR(255) DEFAULT 'default_image.png',
    created_at DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE
);
CREATE TABLE maintenance_requests (
    request_id INT IDENTITY(1,1) PRIMARY KEY,
    TenantID INT NOT NULL,
    RoomID INT NOT NULL,
    issue_type NVARCHAR(50) NOT NULL,
    urgency_level NVARCHAR(30) NOT NULL,
    description NVARCHAR(500) NOT NULL,
    contact_phone NVARCHAR(20),
    available_time NVARCHAR(50),
    discovery_date DATE,
    image_path NVARCHAR(255),
    status NVARCHAR(30) DEFAULT 'Pending' CHECK (status IN ('Pending', 'In Progress', 'Resolved', N'Đang xử lý', N'Đã hoàn thành')),
    created_at DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (TenantID) REFERENCES Tenants(TenantID),
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID)
);
CREATE TABLE Notifications (
    NotificationID INT IDENTITY(1,1) PRIMARY KEY,
    UserID INT,
    Content NVARCHAR(500),
    IsRead BIT DEFAULT 0,
    CreatedAt DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);
CREATE TABLE landlord_analytics (
    id INT IDENTITY(1,1) PRIMARY KEY,
    LandlordID INT NOT NULL,
    month INT CHECK (month BETWEEN 1 AND 12),
    year INT CHECK (year >= 2000),
    total_income FLOAT DEFAULT 0,
    number_of_rented_rooms INT,
    average_price FLOAT,
    growth_rate FLOAT DEFAULT 0,
    FOREIGN KEY (LandlordID) REFERENCES Landlords(LandlordID) ON DELETE CASCADE,
    CONSTRAINT UQ_landlord_analytics UNIQUE (LandlordID, month, year)
);
CREATE TABLE tenant_analytics (
    id INT IDENTITY(1,1) PRIMARY KEY,
    TenantID INT NOT NULL,
    month INT CHECK (month BETWEEN 1 AND 12),
    year INT CHECK (year >= 2000),
    electricity_cost FLOAT DEFAULT 0,
    water_cost FLOAT DEFAULT 0,
    total_cost AS (electricity_cost + water_cost), -- computed column
    due_date DATE,
    FOREIGN KEY (TenantID) REFERENCES Tenants(TenantID),
    CONSTRAINT UQ_tenant_analytics UNIQUE (TenantID, month, year)
);
CREATE TABLE RoomAnalytics (
    idRoomAnalytics INT IDENTITY(1,1) PRIMARY KEY,
    RoomID INT,
    Month INT CHECK (Month BETWEEN 1 AND 12),
    Year INT CHECK (Year >= 2000),
    ElectricityCost FLOAT DEFAULT 0,
    WaterCost FLOAT DEFAULT 0,
    TotalCost AS (ElectricityCost + WaterCost), -- computed column
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE,
    CONSTRAINT UQ_RoomAnalytics UNIQUE (RoomID, Month, Year)
);
CREATE TABLE InvoiceAnalytics (
    InvoiceID INT IDENTITY(1,1) PRIMARY KEY,
    LandlordID INT,
    RoomID INT,
    TenantID INT,
    InvoiceDate DATE,
    RoomPrice FLOAT,
    ElectricityUsed INT,
    ElectricityCost FLOAT,
    WaterUsed INT,
    WaterCost FLOAT,
    InternetFee FLOAT,
    GarbageFee FLOAT,
    OtherFee FLOAT,
    TotalCost FLOAT,
    PaymentStatus NVARCHAR(50),
    FOREIGN KEY (InvoiceID) REFERENCES Invoices(InvoiceID)
);
