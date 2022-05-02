class Parking():
    def __init__(self):
        self.number = 8
        self.floor = 6
        self.total_slots = self.number*self.floor
        self.park_data = [("", "") for i in range(self.total_slots)]
        self.booked = 0

    def park(self, registrationId, color):
        if self.booked < self.total_slots:
            tup = ()
            find = self.park_data.index(("", ""))
            self.park_data[find] = (registrationId, color)
            print(f"vehical is parked at {find}.")
            self.booked = self.booked + 1
        else:
            print("Parking full.")

    def Unparking(self, registrationId):
        out = [slot for slot in self.park_data if slot[0] == registrationId]
        if out:
            self.booked = self.booked - 1
        self.park_data.remove(out[0])

    def search_by_registrationId(self, registrationId):
        out = {slot for slot in self.park_data if slot[0] == registrationId }
        print(f"Parking slot of all vehical of RegistrationId {registrationId} : {out}")

    def search_by_color(self, color):
        out = [slot for slot in self.park_data if slot[1] == color]
        print(f"Parking slot of all vehical of color {color} : {out}")

    def prnt(self):
        print(f"{self.park_data}")


if __name__ == "__main__":
    LLD_system = Parking()
    LLD_system.park("RegId1", "Black")
    LLD_system.prnt()

    LLD_system.park("RegId2", "White")
    LLD_system.prnt()

    LLD_system.park("RegId3", "Green")
    LLD_system.prnt()

    LLD_system.park("RegId4", "Green")
    LLD_system.prnt()

    LLD_system.Unparking("RegId2")
    LLD_system.prnt()

    LLD_system.search_by_registrationId("RegId1")
    LLD_system.prnt()

    LLD_system.search_by_color("Green")
    LLD_system.prnt()
