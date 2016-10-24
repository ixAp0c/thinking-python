# Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# print('+', end=' ')
# print('-')

def draw_beam():
    print('+', '-', '-', '-', '-', end=' ')

def draw_column():
    print('|', ' ', ' ', ' ', ' ', end=' ')

def do_twice(f):
    f()
    f()

def do_four(f):
    f()
    f()
    f()
    f()

def make_beam():
    do_twice(draw_beam)
    print('+')

def make_column():
    do_twice(draw_column)
    print('|')

def draw_grid():
    make_beam()
    do_four(make_column)
    make_beam()
    do_four(make_column)
    make_beam()

draw_grid()
# 2. Write a function that draws a similar grid with four rows and four columns
def make_big_beam():
    do_four(draw_beam)
    print('+')

def make_big_column():
    do_four(draw_column)
    print('|')

def draw_row_top():
    make_big_beam()
    do_four(make_big_column)

def draw_big_grid():
    do_four(draw_row_top)
    make_big_beam()

draw_big_grid()
