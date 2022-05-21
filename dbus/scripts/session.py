from dasbus.connection import SystemMessageBus, SessionMessageBus

system_bus = SystemMessageBus()
session_bus = SessionMessageBus()

proxy = session_bus.get_proxy(
    "org.freedesktop.systemd1",
    "/org/freedesktop/systemd1"
)

print(proxy)