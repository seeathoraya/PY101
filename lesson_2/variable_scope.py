# Question 1
"""
Should print '5' from the global scope
"""

# Question 2
"""
Should print '5' from the global scope since that's where it's called.
"""

# Question 3
"""
Should print '10' because the function reference the global num variable and 
then reassigns it within the function.
"""

# Question 4
"""
Should print 'Hello World' because nested functions can reference 
variables defined in outer scope.
"""

# Question 5
"""
Will throw an error because num is called outside the function 
(where it is not defined).
"""

# Question 6
"""
First x is '15'. In inner_func1 a new variable is defined, shadowing 
the value of x from my_func. Thus, the function fill print 'Inner 1: 25'.
The next function will use the nested value from my_func and will print
'Inner 2: 15'
"""