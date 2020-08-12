def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('yes 1')
        print(func(*args, **kwargs))
        print('yes 2')
    return wrapper

@my_decorator
def call_dec(a,  b, c):
    return ('Value I have is', str(a+b+c))

#
# exeD = my_decorator(call_dec(1,2,3))

#print(exeD)

print(call_dec(1,2,3))

