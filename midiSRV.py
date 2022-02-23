from mido.sockets import PortServer, connect
import mido
import time


outport = mido.open_output()
msg =mido.Message('note_off')

with PortServer('', 8080) as server:
    clients = []
    while True:
        # Handle connections.
        client = server.accept(block=False)
        if client:
            print('Connection from {}'.format(client.name))
            clients.append(client)

        for i, client in reversed(list(enumerate(clients))):
            if client.closed:
                print('{} disconnected'.format(client.name))
                del clients[i]

        # Receive messages.
        for client in clients:
            for message in client.iter_pending():
                print('Received {} from {}'.format(message, client))
                outport.send(message)
                msg.note = message.note
                time.sleep(0.3)
                outport.send(msg)   
                print(f"{msg.note} apagada")
                


