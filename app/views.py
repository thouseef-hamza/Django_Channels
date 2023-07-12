from django.shortcuts import render

# Create your views here.

#  <=====================================Events=================================================>
"""
Connect - recieve event
------------------------
sent to the appication when the client initially opens a connection 
and is about to finish the web socket

"type":"websocket.connect"

Accept - send event
-------------------
Sent by the application when it wishes to accept an incoming connection

"type" : "websocket.accept"
"subprotocol" : None
"headers" : [name,value] Where name is header,name and value us header value

Receive - receive event
-----------------------
Sent to the application when a data message is recieved from the client.

"type" : "websocket.recieve"
"bytes" : None.     The message content,if it was a binary mode, or None.Optional;if missing , it is equivalent to None.
"text" : None.      The message content,if it was a text mode,or None.Optional;if missing , it is equivalent to None.

Send - send event
-----------------
Sent by the application to send a data message to the client
"type" : "websocket.send"
"bytes" : None.     The message content,if it was a binary mode, or None.Optional;if missing , it is equivalent to None.
"text" : None.      The message content,if it was a text mode,or None.Optional;if missing , it is equivalent to None.

Disconnect - receive event
--------------------------
Sent to the application when either connection to the client is lost,either from the client closing the connection,
the server closing the connection,or loss of the socket
"type" : "websocket.disconnect"
"code" : The websocket close code in int,as per the Websocket spec 

Close - send event
------------------
sent by the application to tell the server to close the connection  
"type" : "websocket.close"
"code" : The websocket close code in int, as per the Websocket spec.
        Optional;if missing defaults to 1000.

"reason" : "no need" A reason given for the closure , can be any string .
            Optional; if missing or None default is empty string.

"""