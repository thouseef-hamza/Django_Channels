from channels.consumer import SyncConsumer

class MySyncConsumer(SyncConsumer):
    # This Handler is called when client initially opens a connection 
    # and is about to finish the websocket handshake.
    def websocket_connect(self,event):
        print('Websocket Connected............................................')
    
    # This Handler is called when data recieved from client 
    def websocket_recieve(self,event):
        print('Message Recieved...............................................')
        
    # This handler is called when either connection to  the client is lost,
    # either from the client closing the connection,
    # the server closing the connection or loss of the socket
    def websocket_diconnect(self,event):
        print('Websocket Disconnected.........................................')
    
        
from channels.consumer import AsyncConsumer

class MyAsyncConsumer(AsyncConsumer):
    # This Handler is called when client initially opens a connection 
    # and is about to finish the websocket handshake.
    async def websocket_connect(self,event):
        print('Websocket Connected............................................')
    
    # This Handler is called when data recieved from client 
    async def websocket_recieve(self,event):
        print('Message Recieved...............................................')
        
    # This handler is called when either connection to  the client is lost,
    # either from the client closing the connection,
    # the server closing the connection or loss of the socket
    async def websocket_diconnect(self,event):
        print('Websocket Disconnected.........................................')