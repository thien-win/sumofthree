class AddThreeGame:
    """Represents a sum up game for two players, each player can pick 3 distinct numbers from 1 to 9"""

    def __init__(self):
        """Creates a sum up game object with private input numbers"""

        self._first_list = []
        self._second_list = []
        self._first_player = 0
        self._second_player = 0
        self._input_number = []
        self._current_state = "UNFINISHED"

    def get_current_state(self):
        """Returns current state"""
        return self._current_state

    def make_move(self, player, number):
        """Returns player's move"""

        if number not in range(1, 10) or number in self._input_number:
            return False

        if self._current_state != "UNFINISHED":
            return False

        if player == "first":
            # player's inputs will be added into 2 separate lists
            self._input_number.append(number)
            self._first_list.append(number)

            # the Multiplication Rule
            # loop for all elements in first player's list
            for i in range(0, len(self._first_list) - 2):
                for j in range(i + 1, len(self._first_list) - 1):
                    for k in range(j + 1, len(self._first_list)):
                        # if sum of any elements in the list = 15
                        if self._first_list[i] + self._first_list[j] + self._first_list[k] == 15:
                            self._current_state = "FIRST_WON"

        elif player == "second":
            self._input_number.append(number)
            self._second_list.append(number)

            for i in range(0, len(self._second_list) - 2):
                for j in range(i + 1, len(self._second_list) - 1):
                    for k in range(j + 1, len(self._second_list)):
                        if self._second_list[i] + self._second_list[j] + self._second_list[k] == 15:
                            self._current_state = "SECOND_WON"

        if len(self._input_number) == 9:
            self._current_state = "DRAW"

        return True


# test
game = AddThreeGame()
while True:
    input_num = int(input("First player please enter a number from 1 to 9: "))
    while True:
        if game.make_move("first", input_num):
            break
        else:
            input_num = int(
                input("Wrong input, please try a different number: "))

    # check game status after first player's move
    live_game = game.get_current_state()

    if live_game == "FIRST_WON":
        print("First player won this game!")
        break

    elif live_game == "SECOND_WON":
        print("Second player won this game!")
        break

    elif live_game == "DRAW":
        print("Draw game!")
        break

    input_num = int(input("Second player please enter a number from 1 to 9: "))
    while True:
        if game.make_move("second", input_num):
            break
        else:
            input_num = int(
                input("Wrong input, please try a different number: "))

    # check game status after second player's move
    live_game = game.get_current_state()

    if live_game == "UNFINISHED":
        print("We have unfinished business, come back for more")

    elif live_game == "FIRST_WON":
        print("First player won this game!")
        break

    elif live_game == "SECOND_WON":
        print("Second player won this game!")
        break

    elif live_game == "DRAW":
        print("Draw game!")
