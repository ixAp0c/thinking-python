# 2. Modify do_twice so that it takes two arguments, a function object and a value,
# and calls the function twice, passing the value as an argument.

def do_twice(f, v):
    f(v)
    f(v)

def print_twice(bruce):
    print(bruce)
    print(bruce)

def print_spam():
    print('spam')

# 5. Define a new function called do_four that takes a function object and a value
# and calls the function four times, passing the value as a parameter. These should
# be only two statements in the body of this function, not four.

def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)

# 4. Use the modified version of do_twice to call print_twice twice, passing 'spam'
# as an argument.

do_twice(print_twice, 'spam')

do_four(print_twice, 'spam')
