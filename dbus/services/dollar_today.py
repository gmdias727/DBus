file_handler = open("/home/hansolo/a/pdbus-demo/dasbus/services/org.example.HelloWorld.xml", "r")

xml = file_handler.read()
print(type(file_handler))
print(type(xml))

from dasbus.loop import EventLoop
loop = EventLoop()

from dasbus.connection import SessionMessageBus
session_bus = SessionMessageBus()