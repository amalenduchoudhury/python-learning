import sys

print(sys.version)
print(sys.executable)

who_we_greet = input("Your Name? ")
def greet(who_we_greet):
    greeting = 'Hello, {}'.format(who_we_greet)
    return greeting
greet(who_we_greet)