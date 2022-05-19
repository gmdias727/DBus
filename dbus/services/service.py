from dbus.services.dolar import DolarHoje
from pathlib import Path 
import time
from halo import Halo

import os

BASE_DIR = Path(__file__).parent.parent

print(f'printando!!! {BASE_DIR}')

spinner = Halo(
    spinner='dots12',
    text_color='magenta',
    placement='right',
)

spinner.start(text='Service is running')
time.sleep(2)

opening_file = open(BASE_DIR/'data/org.example.HelloWorld.xml', "r")


if(os.path.exists(BASE_DIR/'data/org.example.HelloWorl.xml') == False):
    spinner.fail(text="The provided file doesn't exists...")
    spinner.stop()
    time.sleep(2)
    
xml = opening_file.read()
spinner.succeed(text='Reading provided XML file...')
time.sleep(2)

from dasbus.loop import EventLoop
loop = EventLoop()

from dasbus.connection import SessionMessageBus
session_bus = SessionMessageBus()

class Calculator(object):
    __dbus_xml__ = xml

    def Addition(self, value1, value2):
        return value1 + value2

    def Subtraction(self, value1, value2):
        return value1 - value2

    def Multiplication(self, value1, value2):
        return value1 * value2
    
    def Division(self, value1, value2):
        return value1 / value2
    
    def Dolar(self):
        return DolarHoje()


session_bus.publish_object("/org/example/Calculator", Calculator())
session_bus.register_service("org.example.Calculator")

loop.run()
spinner.stop()