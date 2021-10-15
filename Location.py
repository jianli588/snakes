import random
import Constants


# this class takes care of moving the snake and extending the snake
class Snake:

    def __init__(self):
        self.segments = []
        for item in Constants.SNAKE:
            self.segments.append(item)

        self.head = self.segments[0]
        self.direction = Constants.RIGHT
        self.point = 0

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num] = [self.segments[seg_num - 1][0], self.segments[seg_num - 1][1]]

        if self.direction == Constants.RIGHT:
            self.head[0] += 1
        elif self.direction == Constants.LEFT:
            self.head[0] -= 1
        elif self.direction == Constants.UP:
            self.head[1] -= 1
        elif self.direction == Constants.DOWN:
            self.head[1] += 1

    def extend(self):
        self.segments.append([self.segments[- 1][0], self.segments[- 1][1]])
        self.point += 1

    def collision(self) -> bool:

        if self.head[0] < 0 or self.head[0] > 30:
            return True
        if self.head[1] < 0 or self.head[1] > 20:
            return True

        for segment in self.segments[1:]:
            if self.head == segment:
                print("hello")
                return True

        return False

    def turn_left(self):
        if self.direction != Constants.RIGHT:
            self.direction = Constants.LEFT

    def turn_up(self):
        if self.direction != Constants.DOWN:
            self.direction = Constants.UP

    def turn_right(self):
        if self.direction != Constants.LEFT:
            self.direction = Constants.RIGHT

    def turn_down(self):
        if self.direction != Constants.UP:
            self.direction = Constants.DOWN


class Food:

    def __init__(self):
        self.coordinates = [random.randint(0, 29) + 0.5, random.randint(0, 19) + 0.5]

    def refresh(self):
        self.coordinates = [random.randint(0, 29) + 0.5, random.randint(0, 19) + 0.5]
