# Part 1 A -- Make a Line
def make_a_line(size, c= "#"):
    line = ""
    for i in range(size):
        line += c
    return line 

print(make_a_line(5))

# Part 1 B -- Make a Square
# create a function using your make_line function to code a square

def make_square(size):
    square = ""
    for i in range(size):
        square += (make_a_line(size) + "\n")
    return square
    
print(make_square(5))

def make_rectangle(width, height):
    rectangle = ""
    for i in range(height):
        rectangle +=(make_a_line(width) + "\n")
    return rectangle 

def make_square(size):
   return make_rectangle(size, size)

print(make_square(5))

# Part 1 C -- Make a Rectangle
def make_rectangle(width, height):
    rectangle = ""
    for i in range(height):
        rectangle +=(make_a_line(width) + "\n")
    return rectangle 

print(make_rectangle(5,3))

# Part 2 A -- Make a Stairs
def make_downward_stairs(height):
    stair = ""
    for i in range(height):
        stair += (make_a_line(i + 1) + "\n")
    return stair

print(make_downward_stairs(5))

# Part 2 B -- Make Space-Line 
def make_space_line(numSpaces, numChar):
   return (make_a_line(numSpaces, " ")) + (make_a_line(numChar, "#")) + (make_a_line(numSpaces, " "))

print(make_space_line(3, 5));

# Part 2 C -- Make Isosceles Triangle
def make_triangle(height):
    triangle = ""
    for i in range(height):
        triangle += (make_space_line(height-i-1, 2*i+1) + "\n")
    return triangle

print(make_triangle(5))

# Part 3 -- Make a Diamond
def make_diamond(height):
    diamond = ""
    triangle = make_triangle(height)
    diamond += triangle[:-1] # skip last new line
    diamond += triangle[::-1] # reverse triangle
    return diamond

print(make_diamond(5))



