from pathlib import Path
from halo import Halo
from sys import exit

from dasbus.connection import SessionMessageBus
from dasbus.loop import EventLoop
from bs4 import BeautifulSoup

import os
import time
import requests

spinner = Halo(
    spinner='dots',
    color='green',
    text_color='green',
    placement='right',
)

BASE_DIR = Path(__file__).parent.parent

spinner.start(text='The Service is starting... ')
time.sleep(3)

spinner.start('Validating provided XML file... ')
time.sleep(2)

provided_file = BASE_DIR/'data/dollar.quote.Today.xml'

if(os.path.exists(provided_file) == False):
    spinner.fail(text="The provided file doesn't exist... ")
    time.sleep(2)
    spinner.fail(text="The program will stop... ")
    time.sleep(2)
    spinner.stop()
    exit()
    
spinner.succeed('XML file successfully validated... ')
time.sleep(2)

try:
    spinner.start(text="Opening provided XML file... ")
    time.sleep(2)
    opening_file = open(provided_file, "r")
    spinner.succeed('XML file successfully opened... ')
    spinner.start('Reading provided XML file... ')
    time.sleep(2)
    reading_file = opening_file.read()
    spinner.succeed('XML file successfully readed... ')


except IOError as exception:
    spinner.fail(text="An error ocurred during the process... ")
    print(f'Error: {exception}')
    time.sleep(2)
    exit()

xml = reading_file

spinner.start('Starting service loop event... ')
time.sleep(2)

service_loop_event = EventLoop()

spinner.start('Choosing the correct Bus for your service ... ')
time.sleep(2)

session_bus = SessionMessageBus()

spinner.succeed('Success... ')
time.sleep(2)

spinner.start('Building your service... ')
time.sleep(2)

class DollarToday(object):
    __dbus_xml__ = xml

    def TodaysDollarToBRL(self):
        url = 'https://dolarhoje.com/'
        html = requests.get(url)
        element = BeautifulSoup(html.content, 'html.parser')
        value = element.find(id='nacional').get('value') 
        return value


spinner.succeed('Service builded successfully... ')
time.sleep(2)

spinner.start('Publishing your service into D-Bus daemon... ')
time.sleep(2)

session_bus.publish_object("/dollar/quote/DollarToday", DollarToday())

spinner.succeed('Successfully published... ')
time.sleep(2)

spinner.start('Registering your service into D-Bus daemon... ')
time.sleep(2)

session_bus.register_service("dollar.quote.DollarToday")

spinner.succeed('Successfully registered... ')
time.sleep(2)

spinner.start('Service is now up and running, to stop the service type CTRL + C')
service_loop_event.run()