# Decorators


def prefix_decorator(prefix):
    def decorator_function(original_function):
        print("cheezy but great")
        def wrapper_function(*args, **kwargs):
            print(prefix, 'Executed Before', original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, 'Executed After', original_function.__name__, '\n')
            return result
        return wrapper_function
    print("distinct")
    return decorator_function


@prefix_decorator('LOG:')
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('paul', 25)
display_info('chaudhary', 30)