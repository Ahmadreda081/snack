from turtle import Turtle

segment_pos = [(0,0),(-20,0),(-40,0)]
move_distance = 20
right = 0
left = 180
up = 90
down = 270


class Snack:

    def __init__(self):
        self.segments = []
        self.create_snack()
        self.head = self.segments[0]

    def create_snack(self):

        for pos in segment_pos:
            self.add_segment(pos)

    def add_segment(self, posstion):
        segment = Turtle('square')
        segment.penup()
        segment.goto(posstion)
        segment.color('white')
        self.segments.append(segment)

    def rest(self):

        for seq in self.segments:
            seq.ht()
        self.segments.clear()
        self.create_snack()
        self.head = self.segments[0]

    def extend(self):
        pos = self.segments[len(self.segments) - 1].pos()
        self.add_segment(pos)

    def move(self):
        for num_seq in range(len(self.segments) - 1, 0, -1):
            prev = self.segments[num_seq - 1].pos()
            self.segments[num_seq].goto(prev)
        self.head.fd(move_distance)

    def Right(self):
        if (self.head.heading() != left):

            self.head.setheading(right)


    def Left(self):
        if (self.head.heading() != right):

            self.head.setheading(left)

    def Up(self):
        if (self.head.heading() != down):

            self.head.setheading(up)


    def Down(self):
        if (self.head.heading() != up):

            self.head.setheading(down)

    # def rest(self):
    #     self.rest()







