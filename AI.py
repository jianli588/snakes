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
        self.skip = Constants.GRID_HORIZONTAL*Constants.GRID_VERTICAL - len(Constants.SNAKE)
        self.head_location = Constants.SNAKE[0]
        self.direction = Constants.RIGHT
        self.skipped_tiles = list()
        # inserts the starting snake in to the tiles
        self.skipped_tiles.insert(0, 1)
        self.skipped_tiles.insert(0, 1)
        self.skipped_tiles.insert(0, 1)

    def update_skip(self, value):
        self.skip -= value
        self.skipped_tiles.insert(0, value)

    def check_right(self, apple) -> int:
        current = self.transverse
        pass

    def check_left(self, apple) -> int:
        pass

    def check_up(self, apple) -> int:
        pass

    def check_down(self, apple) -> int:
        pass

    def move(self, apple) -> str:

        # check all 4 of the directions, seeing how many tiles each one would skip, if it skips over the apple,
        # then the value returned would be -1
        right_value = self.check_right(apple)
        left_value = self.check_left(apple)
        up_value = self.check_up(apple)
        down_value = self.check_down(apple)

        # after a snake moves pass a tile, it adds back the number of skipped tiles back
        self.skip += self.skipped_tiles.pop()

        # finds the largest number of tiles skipped, that would not result in the snake bumping into itself
        if self.skip >= right_value >= max(left_value, up_value, down_value):
            self.update_skip(right_value)
            self.head[0] += 1
            return Constants.RIGHT

        elif self.skip >= left_value >= max(up_value, down_value):
            self.update_skip(left_value)
            self.head[0] -= 1
            return Constants.LEFT

        elif self.skip >= up_value >= max(down_value):
            self.update_skip(up_value)
            self.head[1] -= 1
            return Constants.UP

        else:
            self.update_skip(down_value)
            self.head[1] += 1
            return Constants.DOWN

