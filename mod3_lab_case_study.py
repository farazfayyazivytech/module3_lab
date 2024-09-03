class Vehicle():
    def __init__(self, type):
        self.type = type

class Automobile (Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    
get_type = input('Enter your vehicle type? (car, truck, plane, boat, or broomstick): ')

get_year = int(input('Enter the year of vehicle: '))
get_make = input('Enter the vehicle make: ')
get_model = input('Enter the vehicle model: ')
get_doors = int(input('Enter the number of doors: '))
get_roof = input('Enter vehicle sun roof information (solid / sun roof): ')

build_vehicle = Automobile(get_type, get_year, get_make, get_model, get_doors, get_roof)

print(f'Vehicle type: {build_vehicle.type}\nYear: {build_vehicle.year}\nMake: {build_vehicle.make}\nModel: {build_vehicle.model}\nNumber of Doors: {build_vehicle.doors}\nType of Roof: {build_vehicle.roof}')
