
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
import time
from adafruit_mcp3xxx.analog_in import AnalogIn
import RPi.GPIO as GPIO


# create the spi bus
board.SCK.speed=200000
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
spi.speed=200000
print(str(board.SCK))

#spi.try_lock()

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
#chan = AnalogIn(mcp, MCP.P0)
chan2=AnalogIn(mcp,MCP.P1)

#print('Raw ADC Value: ', chan.value)
#print('ADC Voltage: ' + str(chan.voltage) + 'V')

f = open('mic_check.txt', 'w')
while True:
   # print('Raw ADC Value: ', chan.value)
   # print(str(chan.voltage)+"\n")
   # time.sleep(0.5)
    f.write(str(chan2.voltage)+'\n') 
f.close()


