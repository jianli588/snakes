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

    def move(self):

        if self.direction == Constants.RIGHT:
            right_value = self.check_right()
            left_value = self.check_left()
            up_value = self.check_up()
            down_value = self.check_down()

        elif self.direction == Constants.LEFT:
            right_value = self.check_right()
            left_value = self.check_left()
            up_value = self.check_up()
            down_value = self.check_down()

        elif self.direction == Constants.UP:
            right_value = self.check_right()
            left_value = self.check_left()
            up_value = self.check_up()
            down_value = self.check_down()

        elif self.direction == Constants.DOWN:
            right_value = self.check_right()
            left_value = self.check_left()
            up_value = self.check_up()
            down_value = self.check_down()

        pass

    def check_right(self) -> int:
        pass

    def check_left(self) -> int:
        pass

    def check_up(self) -> int:
        pass

    def check_down(self) -> int:
        pass
