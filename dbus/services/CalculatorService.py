from pathlib import Path 
from halo import Halo
from sys import exit
from dasbus.connection import SessionMessageBus
from dasbus.loop import EventLoop

import os
import time

spinner = Halo(
    spinner='dots',
    text_color='magenta',
    placement='right',
)

print('''\u001b[35m
8888888b.         888888b.   888     888  .d8888b.  
888  "Y88b        888  "88b  888     888 d88P  Y88b 
888    888        888  .88P  888     888 Y88b.      
888    888        8888888K.  888     888  "Y888b.   
888    888        888  "Y88b 888     888     "Y88b. 
888    888 888888 888    888 888     888       "888 
888  .d88P        888   d88P Y88b. .d88P Y88b  d88P 
8888888P"         8888888P"   "Y88888P"   "Y8888P"  
''')

spinner.start(text='The Service is starting... ')
time.sleep(1)
spinner.start('Validating provided XML file... ')
time.sleep(1)

BASE_DIR = Path(__file__).parent.parent
provided_file = BASE_DIR/'data/org.example.HelloWorld.xml'

if(os.path.exists(provided_file) == False):
    spinner.fail(text="The provided file doesn't exist... ")
    time.sleep(1)
    spinner.fail(text="The program will stop... ")
    time.sleep(1)
    spinner.stop()
    exit()

spinner.succeed('XML file successfully validated... ')
time.sleep(1)

try:
    spinner.start(text="Opening provided XML file... ")
    time.sleep(1)
    opening_file = open(provided_file, "r")
    spinner.succeed('XML file successfully opened... ')
    spinner.start('Reading provided XML file... ')
    time.sleep(1)
    reading_file = opening_file.read()
    spinner.succeed('XML file successfully readed... ')

except IOError as exception:
    spinner.fail(text="An error ocurred during the process... ")
    print(f'Error: {exception}')
    time.sleep(1)
    exit()

xml = reading_file
service_loop_event = EventLoop()
spinner.start('Starting service loop event... ')
time.sleep(1)


session_bus = SessionMessageBus()
spinner.start('Choosing the correct Bus for your service ... ')
time.sleep(1)
spinner.succeed('Success... ')
time.sleep(1)

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

spinner.start('Building your service... ')
time.sleep(1)
spinner.succeed('Service builded successfully... ')
time.sleep(1)

session_bus.publish_object("/org/example/Calculator", Calculator())
spinner.start('Publishing your service into D-Bus daemon... ')
time.sleep(1)
spinner.succeed('Successfully published... ')
time.sleep(1)

session_bus.register_service("org.example.Calculator")
spinner.start('Registering your service into D-Bus daemon... ')
time.sleep(1)
spinner.succeed('Successfully registered... ')
time.sleep(1)
spinner.start('Service is now up and running, to stop the service type CTRL + C.')
service_loop_event.run()