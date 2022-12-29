from turtle import Turtle, Screen
position_snakes = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for pos in position_snakes:
            self.add_snake(pos)

    def add_snake(self, position):
        new_snake = Turtle(shape='square')
        new_snake.penup()
        new_snake.color('orange')
        new_snake.goto(position)
        self.snakes.append(new_snake)

    def extend(self):
        self.add_snake(self.snakes[-1].position())

    def move(self):
        for item in range(len(self.snakes)-1, 0, -1):
            new_x = self.snakes[item - 1].xcor()
            new_y = self.snakes[item - 1].ycor()
            self.snakes[item].goto(x=new_x, y=new_y)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


if __name__ == '__main__':
    screen = Screen()
    snake = Snake()
    snake.move()
    screen.exitonclick()
