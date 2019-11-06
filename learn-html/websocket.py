# 需提前安装库"pip install websockets"

import websockets
import asyncio

class WSserver():
    async def handle(self,websocket,path):
        recv_msg = await websocket.recv()
        print("i received %s" %recv_msg)
        await websocket.send('server send ok')
    def run(self):
        ser = websockets.serve(self.handle,"0.0.0.0","8240")
        asyncio.get_event_loop().run_until_complete(ser)
        asyncio.get_event_loop().run_forever()

ws = WSserver()
ws.run()
