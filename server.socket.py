import asyncio
import websockets

clients = []

async def handle_client(websocket, path):
    clients.append(websocket)
    print("New client connected")

    try:
        async for message in websocket:
            print(f"Received: {message}")
            # Weiterleiten der Nachricht an alle anderen Clients
            for client in clients:
                if client != websocket:
                    await client.send(message)  # Sende die Nachricht weiter
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
    finally:
        clients.remove(websocket)

async def main():
    server = await websockets.serve(handle_client, "Put your ip and port here") #Put your ip and port here
    print("Server started on your ip and port")
    await server.wait_closed()

asyncio.run(main())
