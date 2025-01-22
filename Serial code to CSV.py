import serial

ser=serial.Serial() #shortens serial function to ser
ser.baudrate=115200 #needed to get correct signal from microbit

ser.port='COM6' #found in command prompt - chgport or device manager

print("Type Ctrl + C to safety exit")
ser.open() #opens serial port

#initialise variables
temperature=" "

while True:
    data=str(ser.readline())
    data=data[2:14].replace(" ", "")
    sound=data.replace("Temperature:", "")
        
            
    #opening csv file
    file=open("Microbittemprature.csv", "a")
        
    #writing the data
    file.write(temperature+",")
    file.close()
        
        
