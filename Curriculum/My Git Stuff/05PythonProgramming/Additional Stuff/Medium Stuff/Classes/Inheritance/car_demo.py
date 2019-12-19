# This program demosnstrates the Car class

import vehicles

def main():
    # Create an object from the car class. The car is a 2007 Audi A3 with 12,500
    #  miles and price of 21,500 with 4 doors
    used_car = vehicles.Car('Audi', 'A3', 12500, 21500.00, 4)
    
    # display the car's data
    print('make', used_car.get_make())
    print('model', used_car.get_model())
    print('mileage', used_car.get_mileage())
    print(f'price {used_car.get_price():.2f}')
    print('doors', used_car.get_doors())

main()