def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {0}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

##def display():
##    print('display function ran')
##
##decorated_display = decorator_function(display)
##decorated_display()

@decorator_function
def display():
    print('display function ran')

display()

print("\n-----------\n")

@decorator_function
def half(n):
    print(n/2)

half(10)

print("\n-----------\n")

f = half
print(f)
print(f.__name__)
f(100)
