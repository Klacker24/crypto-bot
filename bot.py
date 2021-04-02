import websocket, json, pprint

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m" # Determine symbol and interval time

closes = []

def on_open(ws):
    print("opened connection")

def on_close(ws):
    print("closed connection")

def on_message(ws, message):
    global closes

    json_message = json.loads(message)
    pprint.pprint(json_message)

    candle = json_message['k']

    is_candle_closed = candle['x']
    close = candle['c']

    if is_candle_closed:
        print("candle closed at {}".format(close))
        closes.append(float(close))
        print("CLOSES")
        print(closes)

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message) 

ws.run_forever()