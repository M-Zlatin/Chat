import asyncio #importiert asyncio
import websockets#importiert weboskets

clients = [] #hier werden alle lezte gespeichert die neu joinen

async def handle_client(websocket, path): #code welcher sich um leute kümmert die neu dazu joinen
    clients.append(websocket) #fügt den client hinzu
    print("New client connected") # ansage das jemand neu dauz gekommen ist

    try:
        async for message in websocket: 
            print(f"Received: {message}")
            # Weiterleiten der Nachricht an alle anderen Clients
            for client in clients:
                #if client != websocket:
                    await client.send(message)  # Sende die Nachricht weiter
    except websockets.exceptions.ConnectionClosed: # client disconectet
        print("Client disconnected") # ansage
    finally:
        clients.remove(websocket) # remove client

async def main(): #server starten def
    server = await websockets.serve(handle_client, "127.0.0.1", 5555) #meine ip 
    print("Server started on ws://127.0.0.1:5555") # ansage
    await server.wait_closed()

asyncio.run(main()) #sever starten wurde in line 22-25 beschriben
