# This program creates a Car object, a truck object, and an SUV object

import vehicles
import pprint
def main():
    # Create a Car object
    car = vehicles.Car('Bugatti', 'Veyron', 0, 3000000, 2)

    # Create a truck object
    truck = vehicles.Truck('Dodge', 'Power Wagon', 0, 57000, '4WD')

    # Create an SUV object
    suv = vehicles.SUV('Jeep', 'Wrangler', 200000, 5000, 4)

    print('VEHICLE INVENTORY')
    print('=================')

    # Display the vehicles data
    print('\nmake', car.get_make())
    print('model', car.get_model())
    print('mileage', car.get_mileage())
    print(f'price {car.get_price():.2f}')
    print('doors', car.get_doors())

    print('\nmake', truck.get_make())
    print('model', truck.get_model())
    print('mileage', truck.get_mileage())
    print(f'price {truck.get_price():.2f}')
    print('doors',truck.get_drive_type())

    print('\nmake', suv.get_make())
    print('model', suv.get_model())
    print('mileage', suv.get_mileage())
    print(f'price {suv.get_price():.2f}')
    print('doors', suv.get_pass_cap())
    # shows cool info about the things
    # print(help(vehicles.SUV))
    # shows if an object is an instance of a class
    print(isinstance(suv, vehicles.Automobile))
    # shows if an object is a subclass of another
    print(issubclass(vehicles.SUV, vehicles.Automobile))
    # print or set object as the dictionary of the items
    bob = suv.__dict__
    pprint.pprint(bob, sort_dicts = False)

main()