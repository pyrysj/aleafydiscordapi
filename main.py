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
        self.gateway = ""
        pass
    # async function for getting our gateway url, can't do anything without it!
    # needs the token, can be given as plaintext or whatever
    async def login(self, token):
        r = requests.get('https://discord.com/api/v9/gateway/bot', headers={"Authorization":f"Bot {token}"})
        self.gateway = r.json()["url"]         

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


# NOTES FOR FUTURE CODE: I am thinking here that we just need a loop that checks what kind of t we receive, and such we can reuse the code 
# for multiple different events ? I am not 100% sure
async def main():
    # we use the url given
    r = requests.get('https://discord.com/api/v9/gateway/bot', headers={"Authorization":f"Bot {data['token']}"})
    answer = r.json()
    # we can tweak this a lot and make the code "better", basically commenting everything here for now for future me
    async with websockets.connect(answer["url"]) as websocket: 
        #returns "heartbeat" interval
        message = await websocket.recv()
        await websocket.send(json.dumps(identity))
        # gives the "ready state" -> iirc, after this we can start heartbeating at the specified interval from above (?)
        message = await websocket.recv()
        # here for debugging purposes
        print(message)


async def registerCommands():
    r = requests.post(url,json=testJson, headers={"Authorization":f"Bot {data['token']}"})
    answer = r.json()
    print(answer)


asyncio.run(main())
# asyncio.run(registerCommands())