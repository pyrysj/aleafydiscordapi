import json
import asyncio
import websockets
import requests

# this is basically test code to replicate the basic functionality of discord.js but with python


# not direcrtly necessary, here for testing


with open ('config.json') as config:
    data = json.load(config)

# we can get the application id pretty easily
url = f"https://discord.com/api/v9/applications/{data['appId']}/commands"


# fron the discord documentation
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



class Client:
    def __init__(self) -> None:
        # we want the main loop to 
        asyncio.run(main())
        pass
    def login(self, token):
        r = requests.get('https://discord.com/api/v9/gateway/bot', headers={"Authorization":f"Bot {data['token']}"})
        answer = r.json()
        # login should call a main loop
    def mainLoop(self):
        pass 
        

# might need to consider changing the name 
async def event(intent: str, func):
    def wrapper():
        func()
    return wrapper

# test format from the discord api
testJson = {
    "name": "blep",
    "type": 1,
    "description": "Send a random adorable animal photo",
    "options": [
        {
            "name": "animal",
            "description": "The type of animal",
            "type": 3,
            "required": True,
            "choices": [
                {
                    "name": "Dog",
                    "value": "animal_dog"
                },
                {
                    "name": "Cat",
                    "value": "animal_cat"
                },
                {
                    "name": "Penguin",
                    "value": "animal_penguin"
                }
            ]
        },
        {
            "name": "only_smol",
            "description": "Whether to show only baby animals",
            "type": 5,
            "required": False
        }
    ]
}

async def main():
    # we use the url given
    r = requests.get('https://discord.com/api/v9/gateway/bot', headers={"Authorization":f"Bot {data['token']}"})
    answer = r.json()

    async with websockets.connect(answer["url"]) as websocket:
        # 
        message = await websocket.recv()
        await websocket.send(json.dumps(identity))
        message = await websocket.recv()
        #print(message)

async def registerCommands():
    r = requests.post(url,json=testJson, headers={"Authorization":f"Bot {data['token']}"})
    answer = r.json()
    print(answer)


asyncio.run(main())
# asyncio.run(registerCommands())