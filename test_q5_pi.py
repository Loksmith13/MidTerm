import serial
import random
from guizero import App,PushButton,TextBox

def button():
    print("sending signal...")
app = App()
Button = PushButton(app, command button)
app.display()



if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    while True:
        number = ser.read()
        if number != b'':
            if int.from_bytes(number, byteorder='big') == 18:
                led_number = random.randint(1,4)
                print("Button has been pressed.")
                print("Sending number " + str(led_number) + " to Arduino.")
                ser.write(str(led_number).encode('utf-8'))