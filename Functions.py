# Function to calculate the area of a circle
def circle_area(pi, radius):
    return round(pi * radius ** 2, 2)

# Function to calculate total due with tax
def total_due(money, tax_rate):
    # Convert percentage string to decimal
    if isinstance(tax_rate, str) and tax_rate.endswith('%'):
        tax_rate = float(tax_rate.strip('%')) / 100
    return round(money + (money * tax_rate), 2)

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * (5 / 9), 5)

# Main program
import math

# --- Circle Area ---
radius = float(input("Enter the radius of the circle: "))
area = circle_area(math.pi, radius)
print("Area of the circle:", area)

# --- Total Due with Tax ---
money = float(input("Enter the amount of money: "))
tax_rate = input("Enter the tax rate (e.g., 6%): ")
total = total_due(money, tax_rate)
print("Total due:", total)

# --- Fahrenheit to Celsius ---
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print("Temperature in Celsius:", celsius)
