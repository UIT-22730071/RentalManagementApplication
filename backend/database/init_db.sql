CREATE TABLE Users (
    UserID INT AUTOINCREMENT PRIMARY KEY UNIQUE  NOT NULL,
    Username NVARCHAR(30) UNIQUE NOT NULL,
    Password NVARCHAR(255) NOT NULL,
    Role NVARCHAR(12) NOT NULL,
    IsActive BIT DEFAULT 0,
    CONSTRAINT chk_role CHECK (Users.role IN ('admin', 'landlord', 'tenant'))
);

CREATE TABLE Admins (
    AdminID INT PRIMARY KEY UNIQUE ,
    Fullname NVARCHAR (255) ,
    IsRoot BIT DEFAULT 0,
    UserID INT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

CREATE TABLE Landlords (
    LandlordID INT PRIMARY KEY UNIQUE ,
    Fullname NVARCHAR(255)  ,
    CCCD NVARCHAR(12) UNIQUE ,
    PhoneNumber NVARCHAR(15),
    Job NVARCHAR(30),
    MaritalStatus NVARCHAR (30),
    UserID INT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
    CONSTRAINT chk_martial_status CHECK ( Landlords.MaritalStatus IN ('Married', 'Single') )
);

CREATE TABLE Tenants (
    TenantID INT PRIMARY KEY UNIQUE ,
    UserID INT,
    Fullname NVARCHAR(255) ,
    CCCD NVARCHAR(12) UNIQUE ,
    PhoneNumber NVARCHAR(15) ,
    RentStartDate DATE,
    RentEndDate DATE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
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



