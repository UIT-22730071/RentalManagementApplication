SET DATEFORMAT YMD;


-- Table Creating
CREATE TABLE Users (
                       UserID INT PRIMARY KEY IDENTITY(1,1),
                       Username NVARCHAR(30),
                       Password NVARCHAR(255),
                       Role NVARCHAR(12),
                       is_active BIT DEFAULT 0,
                       CONSTRAINT chk_role CHECK (Role IN ('admin', 'chutro', 'nguoithuetro'))
)

CREATE TABLE Admins (
                        AdminID INT PRIMARY KEY IDENTITY(1,1),
                        FullName NVARCHAR(255),
                        Username NVARCHAR(50),
                        Password NVARCHAR(255),
                        IsRoot BIT DEFAULT 0,
                        UserID INT REFERENCES Users(UserID)
);

ALTER TABLE Admins ADD CONSTRAINT FK_Admins_UserID
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE;

CREATE TABLE Chutro (
                        IDChutro INT PRIMARY KEY IDENTITY(1,1),
                        HoTen NVARCHAR(255),
                        CCCD NVARCHAR(12) UNIQUE,
                        Phone NVARCHAR(15),
                        UserID INT REFERENCES Users(UserID)
);

ALTER TABLE Chutro ADD CONSTRAINT FK_Chutro_UserID
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE;

CREATE TABLE NguoiThueTro (
                              IDnguoithue INT PRIMARY KEY IDENTITY(1,1), -- IDnguoithue
                              Hoten NVARCHAR(255),
                              CCCD NVARCHAR(12) UNIQUE,
                              Phone NVARCHAR(15),
                              Ngaybatdauthue DATE,
                              Ngayketthucthue DATE,
                              UserID INT REFERENCES Users(UserID)
);

ALTER TABLE NguoiThueTro ADD CONSTRAINT FK_NguoiThueTro_UserID
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE;

CREATE TABLE TTPhongtro (
                            IDPhong INT PRIMARY KEY IDENTITY(1,1),
                            TenPhong NVARCHAR(100),
                            Address NVARCHAR(255),
                            Giadien DECIMAL(10,2),
                            Gianuoc DECIMAL(10,2),
                            GiaPhong DECIMAL(10,2),
                            Giarac DECIMAL(10,2),
                            Sodienhientai INT,
                            Sonuochientai INT,
                            IDnguoithue INT REFERENCES Nguoithuetro(IDnguoithue),
                            IDChutro INT REFERENCES Chutro(IDChutro)
);

ALTER TABLE TTPhongtro ADD CONSTRAINT FK_TTPhongtro_IDChutro
    FOREIGN KEY (IDChutro) REFERENCES Chutro(IDChutro) ON DELETE SET NULL;

-- Bang chi tiet hoa don
CREATE TABLE CTHoadon (
                          idCTHD INT PRIMARY KEY IDENTITY(1,1),
                          IDPhong INT,
                          SodienUsed INT, -- Số điện tiêu thụ = số hiện tại - số trước
                          SonuocUsed INT,       -- Số nước tiêu thụ = số hiện tại - số trước
                          DaysInMonth INT,     -- Số ngày ở trong tháng
                          Tiennha DECIMAL(10,2), -- Tiền nhà = giá phòng / 30 * số ngày
                          ngaythutiendukien DATE,     -- Ngày kiểm tra số điện nước
                          sodienthangtruoc INT,
                          sonuocthangtruoc INT,
                          Chiphiphatsinh DECIMAL(10,2),  -- Chi phí phát sinh
                          Tienrac DECIMAL(10,2),
                          Giamgia DECIMAL(10,2)
);
ALTER TABLE CTHoadon ADD CONSTRAINT FK_TTPhongtro_CTHoadon
    FOREIGN KEY (IDPhong) REFERENCES TTPhongtro(IDPhong) ON DELETE SET NULL;



CREATE TABLE HoaDon (
                        BillID INT PRIMARY KEY IDENTITY(1,1), -- Mã hóa đơn tự động tăng
                        Tiennha DECIMAL(10,2),               -- Phí thuê nhà hàng tháng
                        Tiendien DECIMAL(10,2),        -- Phí điện
                        Tiennuoc DECIMAL(10,2),              -- Phí nước
                        Tienrac DECIMAL(10,2),              -- Phí rác
                        Chiphikhac DECIMAL(10,2),             -- Các phí khác
                        Giamgia DECIMAL(10,2),              -- Giảm giá
                        Tongchiphi DECIMAL(10,2),           -- Tổng số tiền phải trả
                        Thanhtoan INT,
                        Ngayxuathoadon DATE,                        -- Ngày xuất hóa đơn
                        IDPhong INT REFERENCES TTPhongTro(IDPhong)
);



ALTER TABLE HoaDon ADD idCTHD INT;

ALTER TABLE HoaDon ADD Ghichu NVARCHAR(255) ;

ALTER TABLE HoaDon ADD CONSTRAINT FK_Hoadon_CTHoadon
    FOREIGN KEY (idCTHD) REFERENCES CTHoadon(idCTHD) ON DELETE SET NULL;

ALTER TABLE HoaDon ADD CONSTRAINT FK_HoaDon_IDPhong
    FOREIGN KEY (IDPhong) REFERENCES TTPhongtro(IDPhong) ON DELETE CASCADE;

ALTER TABLE HoaDon ADD CONSTRAINT DF_ThanhToan DEFAULT 0 FOR ThanhToan;

ALTER TABLE HoaDon ADD CONSTRAINT CK_ThanhToan CHECK (ThanhToan IN (0, 1));