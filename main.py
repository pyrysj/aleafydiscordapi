import json
import asyncio
import websockets
import requests

with open ('config.json') as config:
    data = json.load(config)

identity = {
    "op": 2,
    "d":{
        "token": data['token'],
        "intents": 513,
        "properties": {
            "$os": "mac_os",
            "$browser": "my_library",
            "$device": "my_library"
        }
    }
}

async def main():
    r = requests.get('https://discord.com/api/v9/gateway/bot', headers={"Authorization":f"Bot {data['token']}"})
    answer = r.json()

    async with websockets.connect(answer["url"]) as websocket:
        message = await websocket.recv()
        print(message)
        await websocket.send(json.dumps(identity))
        message = await websocket.recv()
        print(message)

asyncio.run(main())