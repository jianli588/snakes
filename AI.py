import math

import Constants


class Hamiltonian:

    def __init__(self):
        # dictionary of coordinates and their respective number in the hamiltonian cycle
        self.grid_number = {}

        # starting location in the dictionary
        transverse = [0, 0]
        numbering = 1

        # generate the dictionary storing the hamiltonian grid path
        # move to the right
        # when reaching right most block
        # move down one block
        # move to the left
        # when reaching second left most block move down
        while transverse != [29, 0]:

            self.grid_number[(transverse[0], transverse[1])] = numbering
            numbering += 1
            # if on even rows, go left
            if transverse[0] % 2 == 0:
                if transverse[1] != 19:
                    transverse[1] += 1

                else:
                    transverse[0] += 1

            else:
                if transverse[1] != 1:
                    transverse[1] -= 1

                elif transverse[0] == 29:
                    transverse[1] -= 1
                else:
                    transverse[0] += 1

        for index in range(0, 29):
            self.grid_number[(transverse[0], transverse[1])] = numbering
            numbering += 1
            transverse[0] -= 1


class Transverse:

    def __init__(self):
        self.path = Hamiltonian()
        self.skip = Constants.GRID_HORIZONTAL*Constants.GRID_VERTICAL
        self.head_location = Constants.SNAKE[0]
        self.direction = Constants.RIGHT
        self.skipped_tiles = list()
        # inserts the starting snake in to the tiles

        third_seg = self.path.grid_number.get((Constants.SNAKE[2][0], Constants.SNAKE[2][1]))
        second_seg = self.path.grid_number.get((Constants.SNAKE[1][0], Constants.SNAKE[1][1]))
        first_seg = self.path.grid_number.get((Constants.SNAKE[0][0], Constants.SNAKE[0][1]))

        self.skip -= second_seg - third_seg
        self.skipped_tiles.insert(0, second_seg - third_seg)

        self.skip -= first_seg - second_seg
        self.skipped_tiles.insert(0, first_seg - second_seg)

    def update_skip(self, current, value, apple_location):

        self.skip -= value
        self.skipped_tiles.insert(0, value)

        if current + value != apple_location:
            self.skip += self.skipped_tiles.pop()
        else:
            print(f"{self.skipped_tiles} {self.skip}")

    @staticmethod
    def check_positions(current, apple, next_value) -> int:

        # increase the value of the number, if the position of the apple is before current grid
        if current > apple:
            apple += 600

        if current > next_value:
            next_value += 600

        if next_value > apple > current:
            return -1

        return next_value - current

    def check_right(self, current, apple) -> int:

        new_cord = self.head_location[0] + 1
        if new_cord == 30:
            return -1

        next_value = self.path.grid_number.get((new_cord, self.head_location[1]))

        return self.check_positions(current, apple, next_value)

    def check_left(self, current, apple) -> int:

        new_cord = self.head_location[0] - 1
        if new_cord == -1:
            return -1

        next_value = self.path.grid_number.get((new_cord, self.head_location[1]))

        return self.check_positions(current, apple, next_value)

    def check_up(self, current, apple) -> int:

        new_cord = self.head_location[1] - 1
        if new_cord == -1:
            return -1

        next_value = self.path.grid_number.get((self.head_location[0], new_cord))

        return self.check_positions(current, apple, next_value)

    def check_down(self, current, apple) -> int:

        new_cord = self.head_location[1] + 1
        if new_cord == 20:
            return -1

        next_value = self.path.grid_number.get((self.head_location[0], new_cord))

        return self.check_positions(current, apple, next_value)

    def move(self, apple) -> str:

        # find the number corresponding to the positions
        current = self.path.grid_number.get((self.head_location[0], self.head_location[1]))
        apple_location = self.path.grid_number.get((math.floor((apple[0])), math.floor((apple[1]))))

        # check all 4 of the directions, seeing how many tiles each one would skip, if it skips over the apple,
        # then the value returned would be -1
        right_value = self.check_right(current, apple_location)
        left_value = self.check_left(current, apple_location)
        up_value = self.check_up(current, apple_location)
        down_value = self.check_down(current, apple_location)

        # after a snake moves pass a tile, it adds back the number of skipped tiles back

        # finds the largest number of tiles skipped, that would not result in the snake bumping into itself
        if self.skip > right_value > max(left_value, up_value, down_value):
            self.update_skip(current, right_value, apple_location)
            return Constants.RIGHT

        if self.skip > left_value > max(up_value, down_value):
            self.update_skip(current, left_value, apple_location)
            return Constants.LEFT

        if self.skip > up_value > down_value:
            self.update_skip(current, up_value, apple_location)
            return Constants.UP

        if self.skip > down_value:
            self.update_skip(current, down_value, apple_location)
            return Constants.DOWN

        print("error")
        self.update_skip(current, right_value, apple_location)
        return Constants.RIGHT
