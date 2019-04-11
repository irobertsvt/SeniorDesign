import board
import digitalio
import busio

print("Hello blinka!")

# Try to great a Digital input
pin = digitalio.DigitalInOut(board.D4)
print("Digital IO ok!")

# Try to create an I2C device
i2c = busio.I2C(board.SCL, board.SDA)
print("I2C ok!")

# Try to create an SPI device
spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
print("SPI ok!")
print("SCLK:", board.SCK)
print("MOSI:", board.MOSI)
print("MISO:", board.MISO)
print("Pi.D5:", board.D5 )
print("busio:", spi);

print("done!")
