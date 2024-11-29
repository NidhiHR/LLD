class Parking_spot:
    def __init__(self,spot_id,vehicle_type):
        self.spot_id=spot_id
        self.vehicle_type=vehicle_type
        self.has_occupied=False

    def occupy(self):
        self.has_occupied=True

    def vacate(self):
        self.has_occupied=False

class Vehicle:
    def __init__(self,vehicle_type,plate_number):
        self.vehicle_type=vehicle_type
        self.plate_number=plate_number

import datetime

class Ticket:
    def __init__(self,vehicle,spot):
        self.spot=spot
        self.vehicle=vehicle
        self.entry_time=datetime.datetime.now()

    def calculate_duration(self):
        return (datetime.datetime.now()-self.entry_time).total_seconds()/3600
    
    def __str__(self):
        return (f"The {self.vehicle.vehicle_type} with number {self.vehicle.plate_number}"
                f" has been allocated to {self.spot.spot_id} at {self.entry_time}")
    
class Pricing:
    RATES={"MotorCycle":2,"Car":5,"HeavyVehicle":10}

    @staticmethod
    def calculate_price(vehicle_type,duration):
        return Pricing.RATES[vehicle_type]*max(1,int(duration))
    

class Parking_monitor:
    def __init__(self,capacity):
        self.global_id=1
        self.allocated={"MotorCycle":[self.createspace("MotorCycle") for i in range(capacity//2)],
                        "HeavyVehicle":[self.createspace("HeavyVehicle") for i in range(capacity//10)],
                        "Car":[self.createspace("Car") for i in range(capacity//5)]}
        self.occupied={}

    def createspace(self,vehicle_type):
        ticket=Parking_spot(self.global_id,vehicle_type)
        self.global_id+=1
        return ticket

    def has_space(self,vehicle_type):
        return len([spot for spot in self.allocated[vehicle_type] if not spot.has_occupied])>0
    
    def allocated_(self,vehicle):
        allocated=[spot for spot in self.allocated[vehicle.vehicle_type] if not spot.has_occupied]
        if not allocated:
            return 'No Space'
        spot=allocated[0]
        spot.occupy()
        ticket=Ticket(vehicle,spot)
        self.occupied[vehicle.plate_number]=ticket
        return ticket
    
    def deallocated(self,plate_number):
        ticket=self.occupied.pop(plate_number,None)
        if not ticket:
            return "Not a valid ticket"
        spot=ticket.spot
        spot.vacate()
        duration=ticket.calculate_duration()
        amount=Pricing.calculate_price(ticket.vehicle.vehicle_type,duration)
        return amount
    
class Gate:
    def __init__(self,type,monitor):
        self.type=type
        self.monitor=monitor

    def process_entry(self,vehicle):
        if not self.monitor.has_space(vehicle.vehicle_type):
            return "No space"
        ticket=self.monitor.allocated_(vehicle)
        return ticket
    
    def process_exit(self,plate_number):
        return self.monitor.deallocated(plate_number)
    
class Parking:
    def __init__(self,capacity=1000):
        self.monitor=Parking_monitor(capacity)
        self.entry=Gate("entry",self.monitor)
        self.exit=Gate("exit",self.monitor)

    def park(self,vehicle):
        return self.entry.process_entry(vehicle)
    
    def exit_vehicle(self,plate_number):
        amount=self.exit.process_exit(plate_number)
        return amount
    
parking_lot = Parking(1000)

# Vehicle enters
car = Vehicle("Car", "ABC-1234")
ticket = parking_lot.park(car)
print(f"Ticket issued: {ticket}")
# Vehicle exits
amount_due = parking_lot.exit_vehicle("ABC-1234")
print(f"Amount to pay: ${amount_due}")

    