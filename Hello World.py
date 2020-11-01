import sys

print(sys.version)
print(sys.executable)

def greet(who_we_greet):
    greeting = 'Hello, {}'.format(who_we_greet)
    return greeting