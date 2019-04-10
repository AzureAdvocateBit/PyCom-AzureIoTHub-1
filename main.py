import pycom
import _thread
from pysense import Pysense
from SI7006A20 import SI7006A20
from time import sleep

pycom.heartbeat(False)

py = Pysense()
si = SI7006A20(py)

while True:
    pycom.rgbled(0x0000FF)
    temp = si.temperature()
    pybytes.send_signal(0, temp)
    pycom.rgbled(0x000000)
    sleep(5)