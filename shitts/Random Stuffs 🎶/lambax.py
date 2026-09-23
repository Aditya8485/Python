"""Lambda functions are anonymous functions that can be defined in a single line.
 They are often used for short, simple functions 
 that are not reused elsewhere in the code. 
 The syntax for a lambda function is as follows: lambda arguments: expression"""

# Example 1: A lambda function that adds two numbers '''Normal function'''
def add(x, y):
    return x * y

# Example 2: A lambda function that adds two numbers '''Lambda function'''
add_lambda = lambda x, y: x * y