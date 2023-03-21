import serial
import keyboard
import time

ser = serial.Serial(port="/dev/ttyUSB0", baudrate=115200, bytesize=8, timeout=0)

# wave = amount one
wave = 121# adjustment of amount one
a = 0
b = 0
c = 0
end = 0
binary = 0

while True:
    vari = [0xff, 0xff, 0x02, 0x03, 0x0d, 0, 0] # 更改电机转速
    if keyboard.is_pressed('w'):
        time.sleep(0.3)
        print('\n w is pressed')
        wave += 1
        a = hex(wave)
        b = int(hex(wave), 0)
        c = hex(0x02 + 0x03 + 0x0d + b)
        binary = bin(int((c[0:2] + c[-2:]), 0))[2:]  #start from second digit([-8:]which is incorrect)
        end = hex(255 - int(binary, 2)) #1,0 reverse
        print(a, binary, end)
        vari[5] = b  #change variables in command
        vari[6] = int(end, 16)  #verification byte
        ser.write(serial.to_bytes(vari))
        print(vari) 
        #checking
    elif keyboard.is_pressed('s'):
        time.sleep(0.3)
        print('\n s is pressed')
        wave -= 1
        a = hex(wave)
        b = int(hex(wave), 0)
        c = hex(0x02 + 0x03 + 0x0d + b)
        binary = bin(int((c[0:2] + c[-2:]), 0))[2:]
        end = hex(255 - int(binary, 2))
        print(a, binary, end)
        vari[5] = b
        vari[6] = int(end, 16)
        ser.write(serial.to_bytes(vari))
        print(vari)



ser.close()
