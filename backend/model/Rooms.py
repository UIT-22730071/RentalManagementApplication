class Room:
    def __init__(
        self,
        RoomID,
        RoomName,
        Address,
        RoomType,
        Status,
        Area,
        Floor,
        HasLoft,
        Bathroom,
        Kitchen,
        FreeWifi,
        Parking,
        AirConditioner,
        Fridge,
        WashingMachine,
        Security,
        Television,
        Furniture,
        Balcony,
        PetAllowed,
        RoomPrice,
        ElectricityPrice,
        WaterPrice,
        InternetPrice,
        OtherFees,
        GarbageServicePrice,
        Deposit,
        CurrentElectricityNum,
        CurrentWaterNum,
        MaxTenants,
        RentalDate,
        Description,
        TenantID,
        LandlordID,
    ):
        self.RoomID = RoomID
        self.RoomName = RoomName
        self.Address = Address
        self.RoomType = RoomType
        self.Status = Status
        self.Area = Area
        self.Floor = Floor
        self.HasLoft = HasLoft
        self.Bathroom = Bathroom
        self.Kitchen = Kitchen
        self.FreeWifi = FreeWifi
        self.Parking = Parking
        self.AirConditioner = AirConditioner
        self.Fridge = Fridge
        self.WashingMachine = WashingMachine
        self.Security = Security
        self.Television = Television
        self.Furniture = Furniture
        self.Balcony = Balcony
        self.PetAllowed = PetAllowed
        self.RoomPrice = RoomPrice
        self.ElectricityPrice = ElectricityPrice
        self.WaterPrice = WaterPrice
        self.InternetPrice = InternetPrice
        self.OtherFees = OtherFees
        self.GarbageServicePrice = GarbageServicePrice
        self.Deposit = Deposit
        self.CurrentElectricityNum = CurrentElectricityNum
        self.CurrentWaterNum = CurrentWaterNum
        self.MaxTenants = MaxTenants
        self.RentalDate = RentalDate
        self.Description = Description
        self.TenantID = TenantID
        self.LandlordID = LandlordID

    def to_dict(self):
        return self.__dict__
