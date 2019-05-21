## This program calculates the sales tax of a purchase.

def main():
    print("This program calculates the sales tax of a purchase.")
    print()
    keep_going = "y"
    while keep_going.lower() == "y":
        purchase = float(input("Enter your purchase amount: "))

        state_tax = calculate_state_tax(purchase)
        county_tax = calculate_county_tax(purchase)
        tax_total = calculate_total_tax(state_tax, county_tax)
        total_sales = purchase + tax_total
            
        print("Total sales: $", format(total_sales, ",.2f"), sep='')
        print()
        keep_going = input("Would you like to enter another amount? (y=yes): ")
              
    print()
    input("Press the Enter key to terminate the program...")
              


def calculate_state_tax(amount):
    tax = amount * 0.05
    print("State sales tax: $", format(tax, ",.2f"))
    return tax

def calculate_county_tax(amount):
    tax = amount * 0.025
    print("County sales tax: $", format(tax, ",.2f"))
    print()
    return tax

def calculate_total_tax(state, county):
    total = state + county
    print("Total sales tax: $", format(total, ",.2f"))
    return total

main()

        

