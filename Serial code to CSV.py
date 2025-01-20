import serial

ser=serial.Serial() #shortens serial function to ser
ser.baudrate=115200 #needed to get correct signal from microbit

ser.port='COM3' #found in command prompt - chgport or device manager

print("Type Ctrl + C to safety exit")
ser.open() #opens serial port

#initialise variables
sound=" "

while True:
    data=str(ser.readline())
    data=data[2:14].replace(" ", "")
    sound=data.replace("Sound:", "")
        
            
    #opening csv file
    file=open("Microbitsound2.csv", "a")
        
    #writing the data
    file.write(sound+",")
    file.close()
        
        
