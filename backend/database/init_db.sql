CREATE TABLE Users (
    user_id INT PRIMARY KEY UNIQUE NOT NULL,
    username NVARCHAR(30) UNIQUE NOT NULL,
    password NVARCHAR(255) NOT NULL,
    role NVARCHAR(12) NOT NULL,
    is_active BIT DEFAULT 0,
    CONSTRAINT chk_role CHECK (Users.role IN ('admin', 'landlord', 'tenant'))
);

CREATE TABLE Admins (
    admin_id INT PRIMARY KEY UNIQUE NOT NULL,
    fullname NVARCHAR (255),
    is_root BIT DEFAULT 0,
    user_id INT REFERENCES Users(user_id)
);

