from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'app/index.html')

#  <=====================================Events=================================================>
"""
Connect - recieve event
------------------------
sent to the appication when the client initially opens a connection 
and is about to finish the web socket

"type":"websocket.connect"
~
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

#  <===========================================Websocket===============================================>
"""
The Websocket object provides the API for creating and managing a websocket
connection to a server,as well as for sending and receiving data on the connection
Websocket()
Eg:-
var ws = new Websocket('ws://127.0.0.1:8000/ws/sc/');
"""
#  <===========================================Websocket Properties===============================================>
"""
onopen - The Websocket.onopen property is an event handler that is called when the 
         Websocket connection's ready State changes to 1;this indicates that the connection is 
         ready to send and receive data.It is called with an event.
Eg:-
    ws.onopen = function(event){
        console.log("Websocket Connection Open",event);
    };
---------------------------------------------------------------------------------------------------------------
onmessage - The Websocket.onmessage property is an event handler that is called when a message is received
            from the server.It is called with MessageEvent.
Eg:-
    ws.onmessage = function(event){
        console.log("WebSocket message received from server",event);
    };
----------------------------------------------------------------------------------------------------------------
onerror - The Websocket interface's onerror event handler property is a function which gets called when an error 
          occurs on the websocket.

Eg:-
    ws.onerror = function(event){
        console.log("Websocket Error Occured",event);
    };
----------------------------------------------------------------------------------------------------------------
onclose - The Websocket.onclose property is an event handler that is called when the 
          Websocket connection's readyState changes to CLOSED.It is called with a CloseEvent
Eg:-
    ws.onclose = function(event){
        console.log("Websocket Connection Closed",event);
    };
"""

#  <=========================================Websocket Properties =====================================================================>
"""
~ binaryType
~ bufferedAmount
~ extensions
~ protocol
~ readyState
~ url
"""
#  <========================================Events=====================================================================================>
"""
open - The open event is fired when a connection with a Websocket is opened
Eg:-
   ws.addEventListener('open',(event)=>{
     console.log("Websocket Connedct)  
   })
message -  The message event is fired when data is received through a WebSocket
Eg:-
    ws.addEventListener('message',(event)=>{
       console.log('Websocket Message received from server',event); 
    });
error - The error event is fired when a connection with a WebSocket has been closed due to error.
Eg:-
    ws.addEventListener('error',(event)=>{
        console.log("Websocket Error Occured",event);
    });
close - The close event is fired when a connection with a WebSocket is closed.
Eg:-
    ws.addEventListener('close',(event)=>{
        console.log('Websocket connections closed',event);
    });
"""

#  <======================================= Methods =============================================================>
"""
close() - The WebSocket.close() method closes the WebSocket connection or connection attempt,if any.
          If the connection is already CLOSED, this method does nothing
          SYNTAX :- ws.close(code,reason)
                    code - A numeric value indicating the status code explaining why the connection is being closed
                           If this parameter is not specified,a default value of 1005 is assumed.See the list of 
                           status codes of CloseEvent for permitted values.
                    reason - A human-readable string explaining why the connection is closing.This string must be no longer
                             than 123 bytes of UTF-8 text(not characters)

          Eg:- ws.close()
          
send() - The WebSocket.send() method equeues the specifies data to be transmitted tp the server over the Websocket connection
         increasing the value of bufferedAmount by the number of bytes needed to contain data
         If the data can't be sent,the socket will be closed automatically
         The browser will throw an exception if you call send() when the connection is in the CONNECTING state,the browser will 
         silenty discard the data
         Syntax :- ws.send(data)
         Eg:- ws.send("Hello")

"""
# =========================== Python JSON Lib =========================
"""
~ import json
~ json.dumps() - This method is used to convert Python dictionary into json string
~ json.loads() - This method is used to convert json string into Python Dictionary \
"""

#  ========================== JSON =======================
"""
~ JSON.parse() - This method is used to convert json string to JavaScript object
~ JSON.stringify() - This method is used to convert Javascript object into Json string  
"""