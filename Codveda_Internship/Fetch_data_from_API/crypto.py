import requests

def get_crypto_price(coin_id, currency):
    """Fetches the current price of a cryptocurrency from CoinGecko."""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        if coin_id and coin_symbol in data and currency in data[coin_id]:
            return {data[coin_id][currency], data[coin_symbol][]}
        
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Fetch crypto price in usdt
while True:
        
    user_request = input("Enter the name of the coin you wish to see the current price: \n")
    current_price_usd = get_crypto_price(user_request, "usd")
    if current_price_usd is not None:
        print(f"The current price of {user_request} is {current_price_usd} USD")
    else:
        print(f"Failed to retrieve {user_request} price! Make sure the spelling is correct")