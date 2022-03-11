from turtle import Turtle, position
SQUARE_POSITIONS = [(0,0) , (-20,0) , (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]
    
    def create_snake(self):

        for position in SQUARE_POSITIONS:
            self.add_squares(position)
    
    def add_squares(self, position):
        square = Turtle(shape='square')
        square.color('white')
        square.penup()
        square.goto(position)
        self.squares.append(square)

    def extend(self):
        self.add_squares(self.squares[-1].position())
    
    def reset(self):
        for sq in self.squares:
            sq.goto(1000,1000)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]

    def move(self):
        for sq in range(len(self.squares) -1,0,-1):
            self.squares[sq].goto(self.squares[sq -1].xcor(),self.squares[sq -1].ycor())

        self.squares[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
