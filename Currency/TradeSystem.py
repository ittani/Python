def display_welcome():
    print("\nWelcome to the Trade Centre!\n")
    print("Available currencies:\n")
    print("1. USD - United States Dollar")
    print("2. EUR - Euro")
    print("3. GBP - British Pound")
    print("4. ZAR - South African Rand")
    print("5. JPY - Japanese Yen")
    print("6. CNY - Chinese Yuan\n")

def get_amount():
    while True:
        try:
            amount = float(input("Please enter the amount you want to trade: "))
            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_currency(prompt, valid_currencies):
    while True:
        currency = input(prompt).strip().upper()
        if currency in valid_currencies:
            return currency
        else:
            print("Invalid currency code. Please try again.")

def trade_currency(amount, from_currency, to_currency, exchange_rates):
    if from_currency == to_currency:
        return amount
    elif to_currency in exchange_rates.get(from_currency, {}):
        rate = exchange_rates[from_currency][to_currency]
        return amount * rate
    else:
        raise ValueError("Trade rate not available for the specified currencies.")

def main():
    exchange_rates = {
        'USD': {'EUR': 0.85, 'GBP': 0.75, 'ZAR': 14.50, 'JPY': 110.00, 'CNY': 6.50},
        'EUR': {'USD': 1.18, 'GBP': 0.88, 'ZAR': 17.00, 'JPY': 130.00, 'CNY': 7.70},
        'GBP': {'USD': 1.33, 'EUR': 1.14, 'ZAR': 22.00, 'JPY': 150.00, 'CNY': 9.00},
        'ZAR': {'USD': 0.069, 'EUR': 0.059, 'GBP': 0.045, 'JPY': 6.80, 'CNY': 0.35},
        'JPY': {'USD': 0.0091, 'EUR': 0.0077, 'GBP': 0.0067, 'ZAR': 0.15, 'CNY': 0.06},
        'CNY': {'USD': 0.15, 'EUR': 0.13, 'GBP': 0.11, 'ZAR': 2.85, 'JPY': 16.50}
    }

    valid_currencies = list(exchange_rates.keys())

    display_welcome()
    amount = get_amount()
    from_currency = get_currency("Enter the currency you want to trade from (e.g., USD, EUR, GBP): ", valid_currencies)
    to_currency = get_currency("Enter the currency you want to trade to (e.g., USD, EUR, GBP): ", valid_currencies)

    try:
        traded_amount = trade_currency(amount, from_currency, to_currency, exchange_rates)
        print(f"\n{amount} {from_currency} is equal to {traded_amount:.2f} {to_currency}.")
    except ValueError as e:
        print(f"\nError: {e}")

    print("\nThank you for using the Trade Centre!")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()