def main():
    hours = int(input("Enter the number of hours worked: "))

    while hours <= 55 and hours >= 0:
        pay_rate = float(input("Enter your pay rate: "))
        gross_pay = hours * pay_rate
        print(f"Gross pay is {gross_pay:.2f}")


main()