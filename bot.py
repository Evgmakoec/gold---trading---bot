import requests

url = "https://query1.finance.yahoo.com/v8/finance/chart/XAUUSD=X?interval=15m&range=1d"

response = requests.get(url, timeout=10)
data = response.json()

result = data["chart"]["result"][0]

prices = result["indicators"]["quote"][0]["close"]

latest_price = prices[-1]

print("XAUUSD M15")
print("LATEST GOLD PRICE:", latest_price)
