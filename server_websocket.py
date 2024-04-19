import asyncio
import random
import time

import websockets
import websockets.server
import datetime
from socket import *





user = {}
user_ip_all = []
def ip_user(websocet):
    try:
        if user[websocet.remote_address[0]]:
            user[websocet.remote_address[0]] = websocet
            print("сокет обновлен")
            return user
    except:
        user[websocet.remote_address[0]] = websocet
        print("сокет создан")
        user_ip_all.append(websocet.remote_address[0])
        return user

async def send_messange(user,ip,msg):
   await user[ip].send(msg)


def read_messange(websocet,arg):
     ip = arg[:arg.index("=")]
     messange = arg[arg.index("=")+1:]
     key = websocet.remote_address[0]+'server?'+messange
     return [ip,key]

async def test(websocet,path):
    print(websocet.remote_address,websocet.port)
    ip =  ip_user(websocet)
    print(user_ip_all)


    if(len(user)>1):
        ip_all = ''
        for k in user:

            await user[k].send(str(user_ip_all))

    while 1:
        dt =  datetime.datetime.now()
        mes = dt.strftime("%b")
        try:
            ms = await websocet.recv()
            print(ms)
            data_value = read_messange(websocet,ms)
            await send_messange(user,data_value[0],data_value[1])

        except:
            pass
            print("await")
        await asyncio.sleep(random.random()*3)


start_server = websockets.serve(test,'192.168.0.104',1235) #127.0.0.1

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

