from services.dolar import DolarHoje
file_handler = open("/home/hansolo/a/pdbus-demo/dasbus/services/org.example.HelloWorld.xml", "r")

xml = file_handler.read()
# print(type(file_handler))
# print(type(xml))

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
print('SERVIÇO DBUS RODANDO!')
print('SERVIÇO DBUS RODANDO!')
print('SERVIÇO DBUS RODANDO!')
print('SERVIÇO DBUS RODANDO!')
print('SERVIÇO DBUS RODANDO!')
loop.run()
