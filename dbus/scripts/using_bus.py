from dasbus.connection import SessionMessageBus
bus = SessionMessageBus()

proxy = bus.get_proxy(
    "org.example.Calculator",
    "/org/example/Calculator"
)

print(proxy.Addition(123, 456))
print(proxy.Subtraction(50, 256))
print(proxy.Multiplication(77, 33))
print(proxy.Division(800, 3))
