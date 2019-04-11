#Senior Design 

from gpiozero import MCP3008

pot = MCP3008(0)
pot2 = MCP3008(1)
while True:
    print(pot.value, pot2.value)

