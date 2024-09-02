import websocket # you will have to install websocket and websocket-client (windows prompts = [pip install websocket] and [pip install websocket-client])
import json
import threading

# Initialize variables
latestPrices = {}
allowedSymbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]

'''Socket managing functions'''
# processing entering messages
def on_message(ws, messsage):
    json_message = json.loads(messsage)
    symbol = json_message['s'].lower()
    price = float(json_message['c'])
    latestPrices[symbol] = price
    print(f"{symbol.upper()} Price: {price}")

# processing ocurred errors
def on_error(ws, error):
    print(f"Error: {error}")

# properly closing the connection
def on_close(ws):
    print("--- CONNECTION CLOSED ---")

# opening the connection
def on_open(ws):
    def run(*args):
        subscribe_message = {
            "method": "SUBSCRIBE",
            "params": [f"{symbol.lower()}@ticker" for symbol in allowedSymbols],
            "id": 1
        }
        ws.send(json.dumps(subscribe_message))
    threading.Thread(target=run).start()

# binance specific websocket connection url
socketUrl = "wss://stream.binance.com:9443/ws" 

# configuring websocket object with the url and its methods
ws = websocket.WebSocketApp(socketUrl,
                            on_open = on_open,
                            on_message = on_message,
                            on_error = on_error,
                            on_close = on_close)

# running a thread 
wst = threading.Thread(target=ws.run_forever())
wst.daemon = True
wst.start()

try:
    while True:
        pass
except:
    ws.close()