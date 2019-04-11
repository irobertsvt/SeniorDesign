#https://github.com/doceme/py-spidev
#https://raspberrypi.stackexchange.com/questions/4884/how-do-i-set-clk-speed-on-spi-for-raspberry-pi
import RPi.GPIO as GPIO
import spidev
import pyaudio
DEBUG=0
spi=spidev.SpiDev()
spi.open(0,0)
#any higher speed dows not make it go faster, just harder to read on the oscilloscope
#this speed refers to the clock speed, but not the sample speed (like if you zoom in on
# one of the clock pulses to get the 3 sets of 8 pulses. those are at 100MHz roughly
spi.max_speed_hz=10000000
#120khz will get  50 ksamp/sec with no delay
#need to figure out how to get rid of this delay

#spi.no_cs=False

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(12, GPIO.OUT)
#p=GPIO.PWM(12,100000)
#p.start(50)

m=open('xfer2.txt', 'w')
def readadc(adcnum):
	#the 120000 is supposed to be the speed, and the 0 is delay in usec
	r=spi.xfer2([1,(8+adcnum)<<4,0],2000000,0)
	adcout=((r[1]&3<<8)+r[2])
	#r=spi.xfer2([1,8<<4,0],2000000,0)
	m.write(str(adcout))
	return adcout

f = open( 'mic_check.txt', 'w' )
while True:
	#readbytes(1)
	#r=spi.xfer2([1,speed_hz=100000,delay_usec=10])
	r=readadc(0)
	#e=readadc(1)
	#d=readadc(2)
	#n=readadc(3)
	#g=readadc(4)
	#h=readadc(5)
	#i=readadc(6)
	#j=readadc(7)
	#print(r,spi.delay_usec,' ',e,' ',d,' ',f,' ',g,' ',h,' ',i,' ',j)
	#print(r,' ')
	f.write(str(r)+' ')
f.close()
