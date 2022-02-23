from pyfirmata import Arduino
import pyfirmata
import time
from mido.sockets import connect, PortServer
import mido



port = "/dev/ttyACM0"
board = Arduino(port)
output = connect('192.168.0.7', 8080)
# activa una nota que luego definire con una variable recogida del sensor
msg = mido.Message('note_on')

pin1 = board.get_pin('a:2:i')

it = pyfirmata.util.Iterator(board)
it.start()
notas = [52,55,57,60,62,64,67,69]

def tocarNota(nota):
    msg.note = nota
    output.send(msg)
    board.digital[12].write(1)
    time.sleep(0.1)
    board.digital[12].write(0)
    print(f'nota on {msg}')

while True:
    analog_value = pin1.read()
    analogFL = float(analog_value or 0)
    analogINT = int(round(analogFL,3)*1000)
    if analogINT < 127 and analogINT > 110:
        tocarNota(notas[7])
    elif analogINT <= 110 and analogINT > 100:
        tocarNota(notas[6])        
    elif analogINT <= 100 and analogINT > 80:
        tocarNota(notas[5])
    elif analogINT <= 80 and analogINT > 60:
        tocarNota(notas[4])
    elif analogINT <= 60 and analogINT > 40:
        tocarNota(notas[3])
    elif analogINT <= 40 and analogINT > 30:
        tocarNota(notas[2])
    elif analogINT <= 30 and analogINT > 20:
        tocarNota(notas[1])
    elif analogINT <= 20:
        tocarNota(notas[0])    
    print(f"-- valor pin: {analog_value} -- valor entero: {analogINT}",end="\r")
    time.sleep(0.1)