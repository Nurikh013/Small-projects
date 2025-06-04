import urllib.request
import json

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.frankfurter.app/latest?from={base_currency}&to={target_currency}"
    
  
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data['rates'][target_currency]
    except Exception as e:
        print(f"Error: {e}")
        return None

def convert_currency(amount, base_currency, target_currency):
    rate = get_exchange_rate(base_currency, target_currency)
    if rate:
        converted_amount = amount * rate
        return converted_amount
    return None


try:
    amount = float(input("Enter amount: "))
    from_currency = input("From currency (3-letter code): ").upper()
    to_currency = input("To currency (3-letter code): ").upper()

    result = convert_currency(amount, from_currency, to_currency)
    if result:
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
    else:
        print("Conversion failed")
except Exception as e:
    print(f"Input error: {e}")
