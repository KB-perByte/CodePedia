def first(func):
    print("ABC")
    def second():
        print("DEF")
        return None
    return second

@first
def third(): #call a method but don't call it in python
    print("GHI")

third()

def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper

@run_once
def my_function(foo, bar):
    print("ala")
    return foo+bar

my_function(6, 10)
my_function(6, 10)

from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)