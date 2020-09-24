import math
class Rectangle(object):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def set_width (self, newWidth):
        self.width = newWidth
    def set_height (self, newHeight):
        self.height = newHeight
    def get_area(self):
        area = self.width * self.height
        return area 
    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter
    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal
    def get_picture(self):
        '''
        Returns a string that represents the shape using lines of "*". The number of lines should be equal to the height and the number of "*" in each line should be equal to the width. 
        There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.".
        '''
        row = ''
        shape = ''
        if (self.width or self.height) >= 50:
            shape = 'Too big for picture.'
        else:
            for h in range(self.height):
                for w in range(self.width):
                    row = row + '*'
                shape = shape + row + '\n'
                row = ''
        return shape
    def get_amount_inside(self, shape): 
        '''
        Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). 
        For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
        '''
        NumTimes=999
        w = shape.width
        h = shape.height
        checkWidth = self.width/w
        checkHeight = self.height/h
        if (checkWidth or checkHeight) < 1:
            NumTimes=0
        elif (checkWidth or checkHeight) == 1:
            if checkHeight > checkWidth:
                NumTimes = math.floor(checkHeight)
            else:
                NumTimes = math.floor(checkWidth)
        else:
                NumTimes = math.floor(checkHeight) * math.floor(checkWidth) 
     
        return NumTimes
    def __str__(self):
        # Additionally, if an instance of a Rectangle is represented as a string, it should look like: Rectangle(width=5, height=10)
            return 'Rectangle(width='+str(self.width)+', height='+str(self.height)+')'
  
class Square(Rectangle):
    def __init__(self,length):
        self.width = length
        self.height = length   
    def set_side (self, newLength):
        self.width = newLength
        self.height = newLength 
    def set_width (self, newWidth):
        self.width = newWidth
        self.height = newWidth
    def set_height (self, newHeight):
        self.height = newHeight
        self.width = newHeight
    def __str__(self):
        # If an instance of a Square is represented as a string, it should look like: Square(side=9)
        return 'Square(side='+str(self.width)+')'
