"""
Key with decorated classes is to define __init__ and __call__ method.
__call__ is actually responsible for 'decorating' function with extra
functionality
"""

class DecoratedClass:
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method this before {0}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)
        
@DecoratedClass
def display():
    print('display function ran')

display()

print("\n-----------\n")

@DecoratedClass
def half(n):
    print(n/2)

half(10)
