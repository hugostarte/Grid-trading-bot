import requests
import time

def main():
  # Définissez votre clé API et votre clé secrète
  api_key = "your_api_key"
  secret_key = "your_secret_key"

  # Définissez votre paire de trading (ex: BTCUSDT) et votre stratégie (ex: grille)
  symbol = "BTCUSDT"
  strategy = "grid"

  # Définissez les paramètres de votre stratégie
  grid_size = 0.01
  buy_level = 9000
  sell_level = 9500

  while True:
    # Récupérez les derniers prix de la paire de trading à l'aide de l'API
    response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}")
    data = response.json()
    price = float(data["price"])

    # Appliquez votre stratégie
    if strategy == "grid":
      if price <= buy_level:
        # Achat de crypto-monnaie
        print(f"Achat de {grid_size} {symbol} à {price}")
        buy_level -= grid_size
        sell_level -= grid_size
      elif price >= sell_level:
        # Vente de crypto-monnaie
        print(f"Vente de {grid_size} {symbol} à {price}")
        buy_level += grid_size
        sell_level += grid_size

    # Définissez la fréquence d'exécution du script (par exemple, toutes les 10 secondes)
    time.sleep(10)

if __name__ == "__main__":
  main()
