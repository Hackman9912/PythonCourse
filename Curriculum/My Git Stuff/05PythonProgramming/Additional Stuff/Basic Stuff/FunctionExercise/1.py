 # 1. Kilometer ConverterWrite a program that asks the user to enter a distance in kilometers, and then converts that distance to miles. 
 # The conversion formula is as follows:
 # Miles =Kilometers * 0.6214

def main():
    kilo = miley()
    convert(kilo)

def miley():
    return float(input("Enter the number of kilometers that you need converted: "))

def convert(number):
    miles = number * 0.6214
    print(number, "converted to miles is", miles)

main()
