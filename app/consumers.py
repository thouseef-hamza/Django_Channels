from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
class MySyncConsumer(SyncConsumer):
    # This Handler is called when client initially opens a connection 
    # and is about to finish the websocket handshake.
    def websocket_connect(self,event):
        print('Websocket Connected............................................',event)
        self.send({
            'type':'websocket.accept',
        }) 
        
    
    # This Handler is called when data recieved from client 
    def websocket_receive(self,event):
        print('Message Recieved...............................................',event)
        print('Message is ',event['text'])
        for i in range(50):
            self.send({
                'type' : 'websocket.send',
                'text' : str(i) 
            })
            sleep(1)
            
        
        
        
    # This handler is called when either connection to  the client is lost,
    # either from the client closing the connection,
    # the server closing the connection or loss of the socket
    def websocket_disconnect(self,event):
        print('Websocket Disconnected.........................................',event)
        raise StopConsumer()
    
        
from channels.consumer import AsyncConsumer
import asyncio
class MyAsyncConsumer(AsyncConsumer):
    # This Handler is called when client initially opens a connection 
    # and is about to finish the websocket handshake.
    async def websocket_connect(self,event):
        print('Websocket Connected............................................',event)
        self.send({
            'type':'websocket.accept'
        })
    
    # This Handler is called when data recieved from client 
    async def websocket_receive(self,event):
        print('Message Recieved...............................................',event)
        print('Message is ',event['text'])
        for i in range(50):
            await self.send({
                'type' : 'websocket.send',
                'text' : str(i) 
            })
            await asyncio.sleep(1)
    # This handler is called when either connection to  the client is lost,
    # either from the client closing the connection,
    # the server closing the connection or loss of the socket
    async def websocket_disconnect(self,event):
        print('Websocket Disconnected.........................................',event)
        raise StopConsumer()