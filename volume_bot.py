import ccxt
import time
import logging
from config import API_KEY, API_SECRET

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize MEXC exchange
exchange = ccxt.mexc({
    'apiKey': API_KEY,
    'secret': API_SECRET,
    'options': {'defaultType': 'spot'}
})

def get_market_data(symbol):
    """Fetch the latest market price for a given trading pair."""
    ticker = exchange.fetch_ticker(symbol)
    return ticker['last']

def place_order(symbol, order_type, side, amount, price=None):
    """Place an order on MEXC."""
    try:
        if order_type == 'limit':
            order = exchange.create_limit_order(symbol, side, amount, price)
        else:
            order = exchange.create_market_order(symbol, side, amount)
        logging.info(f"Order placed: {order}")
    except Exception as e:
        logging.error(f"Error placing order: {e}")

def run_volume_strategy():
    """Basic volume trading logic."""
    symbol = 'BTC/USDT'
    amount = 0.001  # Adjust based on your volume strategy
    interval = 60  # Trade every 60 seconds
    
    while True:
        price = get_market_data(symbol)
        logging.info(f"Current {symbol} price: {price}")
        place_order(symbol, 'market', 'buy', amount)
        time.sleep(interval)

if __name__ == "__main__":
    run_volume_strategy()
