'''
Challenge: FizzBuzz
Write a function that prints numbers from 1 to N, following these rules:

If a number is divisible by 3, print "Fizz" instead.
If a number is divisible by 5, print "Buzz" instead.
If a number is divisible by both 3 and 5, print "FizzBuzz".
Otherwise, print the number itself.

Example:
fizz_buzz(15)

Expected Output:
1  
2  
Fizz  
4  
Buzz  
Fizz  
7  
8  
Fizz  
Buzz  
11  
Fizz  
13  
14  
FizzBuzz  
'''

def FizzBuzz(n: int) -> None:
    for i in range(1, n+1):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

FizzBuzz(15)