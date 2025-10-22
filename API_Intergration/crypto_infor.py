import requests

def fetch_crypto_info(coin):
    url = f"https://api.coingecko.com/api/v3/coins/{coin.lower()}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.HTTPError:
        print(f"Coin '{coin}' not found or invalid.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    return {}

def display_crypto_info(data):
    if not data:
        print("No data to display.")
        return

    market = data.get("market_data", {})
    print(f"\n{data.get('name')} ({data.get('symbol', '').upper()})")
    print(f"Price: ${market.get('current_price', {}).get('usd', 'N/A'):,}")
    print(f"Market Cap: ${market.get('market_cap', {}).get('usd', 'N/A'):,}")
    print(f"24h High: ${market.get('high_24h', {}).get('usd', 'N/A'):,}")
    print(f"24h Low: ${market.get('low_24h', {}).get('usd', 'N/A'):,}")
    print(f"24h Change: {market.get('price_change_percentage_24h', 'N/A')}%")
    print(f"Volume: ${market.get('total_volume', {}).get('usd', 'N/A'):,}")
    print(f"Last Updated: {data.get('last_updated', 'N/A')}\n")

def main():
    coin = input("Enter cryptocurrency name (e.g., bitcoin, ethereum): ").strip()
    if not coin:
        print("Enter a valid name.")
        return
    data = fetch_crypto_info(coin)
    display_crypto_info(data)

if __name__ == "__main__":
    main()
    
