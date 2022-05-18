# DasBus Library
from dasbus.connection import SystemMessageBus, SessionMessageBus


system_bus = SystemMessageBus() # system bus init
session_bus = SessionMessageBus() # Session Bus init

print(system_bus)

proxy = session_bus.get_proxy( # specify dbus service name and path
    "org.freedesktop.systemd1",
    "/org/freedesktop/systemd1"
)