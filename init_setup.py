import serial
import time

ser = serial.Serial(port="/dev/ttyUSB0", baudrate=115200, bytesize=8, timeout=0)

#hex command
pwml = [0xff,0xff,0x02,0x04,0x09,0xe8,0x03,0x05]
pwmh = [0xff,0xff,0x02,0x04,0x0b,0xd0,0x07,0x15]
set = [0xff,0xff,0x02,0x03,0x0d,0x79,0x74] # amount=121等价，电机静止状态



ser.write(serial.to_bytes(pwml)) #setting pwm wave limit
time.sleep(1)
ser.write(serial.to_bytes(pwmh))
time.sleep(1)
ser.write(serial.to_bytes(set)) #reset the propeller
time.sleep(1)

ser.close()
