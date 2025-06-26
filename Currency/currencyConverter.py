
print("\nWelcome to the Currency Converter!\n")

print("Available currencies:\n")
print("1. USD - United States Dollar")
print("2. EUR - Euro")
print("3. GBP - British Pound")
print("4. ZAR - South African Rand")
print("5. JPY - Japanese Yen")
print("6. CNY - Chinese Yuan\n")  

print("Please enter the amount you want to convert:")
amount = float(input()) 
print("\nPlease enter the currency you want to convert from (e.g., USD, EUR, GBP, ZAR, JPY, CNY):")
from_currency = input().strip().upper()
print("Please enter the currency you want to convert to (e.g., USD, EUR, GBP, ZAR, JPY, CNY):")
to_currency = input().strip().upper()          

# Exchange rates (as of the last known data)
exchange_rates = {
    'USD': {'EUR': 0.85, 'GBP': 0.75, 'ZAR': 14.50, 'JPY': 110.00, 'CNY': 6.50},
    'EUR': {'USD': 1.18, 'GBP': 0.88, 'ZAR': 17.00, 'JPY': 130.00, 'CNY': 7.70},
    'GBP': {'USD': 1.33, 'EUR': 1.14, 'ZAR': 22.00, 'JPY': 150.00, 'CNY': 9.00},
    'ZAR': {'USD': 0.069, 'EUR': 0.059, 'GBP': 0.045, 'JPY': 6.80, 'CNY': 0.35},
    'JPY': {'USD': 0.0091, 'EUR': 0.0077, 'GBP': 0.0067, 'ZAR': 0.15, 'CNY': 0.06},
    'CNY': {'USD': 0.15, 'EUR': 0.13, 'GBP': 0.11, 'ZAR': 2.85, 'JPY': 16.50}
}   
# Function to convert currency
def convert_currency(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return amount
    elif from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        rate = exchange_rates[from_currency][to_currency]
        return amount * rate
    else:
        raise ValueError("Conversion rate not available for the specified currencies.")         
# Perform the conversion
try:
    converted_amount = convert_currency(amount, from_currency, to_currency)
    print(f"\n{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")
except ValueError as e:
    print(f"\nError: {e}. Please check the currency codes and try again.")      
print("\nThank you for using the Currency Converter!")
print("Have a great day!\n")
input("Press Enter to exit...")
# End of currencyConverter.py
# This code is a simple currency converter that allows users to convert between various currencies using predefined exchange rates. 
# It prompts the user for the amount and the currencies they wish to convert from and to, performs the conversion using a dictionary of exchange rates, and displays the result. 
# If the conversion is not possible due to missing exchange rates, it raises an error and informs the user.
# The code is structured to be user-friendly and provides clear instructions and feedback throughout the process.
# The exchange rates are hardcoded for simplicity, but in a real-world application, they would typically be fetched from a live API to ensure accuracy and up-to-date information.
# The code also includes error handling to manage cases where the user inputs invalid currency codes or if the conversion rate is not available.
# The program ends by thanking the user and prompting them to exit, ensuring a smooth user      experience.
# The code is written in Python and is designed to be run in a console or terminal environment.
# It is a straightforward implementation suitable for educational purposes or as a basic utility script.            