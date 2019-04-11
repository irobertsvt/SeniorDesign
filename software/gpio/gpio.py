from gpiozero import MCP3008
from time import sleep

mic = MCP3008(channel=0)

while True:
	print(mic.value)
