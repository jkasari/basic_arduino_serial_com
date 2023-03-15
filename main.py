import serial

if __name__ == "__main__":
    print("This assumes a 115200 Baud, send q to quite the program")
    arduino_port = input("Please list the port name of the Arduino")
    port = serial.Serial(f'/dev/{arduino_port}', 115200, timeout=1)
    while True:
        message = input("New Message: ")
        if message == "q":
            break
        port.write(message.encode())
    port.close()