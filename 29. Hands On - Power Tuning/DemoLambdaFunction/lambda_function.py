import json

def lambda_handler(event, context):
   fibonacci_of(25)

def fibonacci_of(n):
   if n in {0, 1}: #Base case
      return n
   return fibonacci_of(n-1) + fibonacci_of(n-2) #Recursive case