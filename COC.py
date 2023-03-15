import serial


ser = serial.Serial(port="/dev/ttyUSB0", baudrate=115200, bytesize=8, timeout=0)

# wave = amount one
wave = 121 #adjustment of amount one (63-188)
wave0 = 121 #store previous value of wave
c1 = 0 # variables for CRC
end1 = 0
binary1 = 0
c2 = 0
binary2 = 0
end2 = 0

while True:
    coc = [0xff, 0xff, 0x02, 0x03, 0x17, 0, 0] #CountofCycle周期數; cycle(default = 20) c1, end1
    amount = [0xff, 0xff, 0x02, 0x03, 0x0d, 0, 0] #c2, end2

    wave = int(input("Enter your amount: "))
    diff = abs(wave - wave0)*10

    if (wave <= 188) & (wave >= 63):
        wave0 = wave

        c1 = hex(0x02 + 0x03 + 0x17 + diff)
        binary1 = bin(int((c1[0:2] + c1[-2:]), 0))[2:]
        end1 = hex(255 - int(binary1, 2))
        coc[5] = diff
        coc[6] = int(end1, 16)
        ser.write(serial.to_bytes(coc))

        c2 = hex(0x02 + 0x03 + 0x0d + wave)
        binary2 = bin(int((c2[0:2] + c2[-2:]), 0))[2:]  #start from second digit([-8:]which is incorrect)
        end2 = hex(255 - int(binary2, 2)) #1,0 reverse
        amount[5] = wave  #change variables in command
        amount[6] = int(end2, 16)  #verification byte
        ser.write(serial.to_bytes(amount))
        print(amount)  #checking
        print(coc)

    else:
        print("Wrong amount input")

ser.close()