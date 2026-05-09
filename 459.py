#oops in python
#real world mini project
#cab booking app
class CabBooking:
    def __init__(self,name,pickup,destination):
        self.name=name
        self.pickup=pickup
        self.destination=destination
        self.status="not booking"

    def cab_booking(self):
        self.status="booked"
        print(f"cab has been booked successfully")

    def trip_details(self):
        print(f"trip details:")
        print(f"customer name:{self.name}")
        print(f"pickup location:{self.pickup}")
        print(f"drop location:{self.destination}")
        print(f"booking status:{self.status}")

    def cancel_booking(self):
        self.status="booking cancelled" 
        print(f"booking has been cancelled successfully")

c1=CabBooking("radha","karvenagar","katraj isckon temple") 
c1.cab_booking()
c1.trip_details()
c1.cancel_booking()

