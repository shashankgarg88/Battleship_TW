from constants import ShipContants as constants


class Cell:
    """
    This class represents a cell on the board.
    A cell will have following properties:
        - row: row number of the cell
        - column: column number of the cell
        - occupied: True if cell is occupied, False is not
        - mark: Represents the different symbols in diferent cases
                - X : Occupied by a ship alread hit once
                - # : Occupied by a destroyed ship
                - . : Empty cell
                - * : Occupied by an active ship
                - - : A shot has already been fired at this cell marking at miss
         - hit_count : represent how many times the cell has been fired upon
         - ship: reference to the ship occupying the cell
    """
    def __init__(self, row=None, column=None, mark=None):
        """
        Constructor method to initialize the cell object
        :param row:
        :param column:
        :param mark:
        """
        self.row = row
        self.column = column
        self.occupied = False
        self.mark = mark
        self.hit_count = 0
        self.ship = None

    def flush_cell(self):
        self.occupied = False
        self.mark = constants.EMPTY_CELL_MARK
        self.hit_count = 0
        self.ship = None

    def is_occupied(self):
        """
        Method to check if the cell is occupied or not
        :return: True/False
        """
        return self.occupied

    def has_destroyed_ship(self):
        """
        Method to check whether a cell has a destroyed ship or not.
        :return: True/False
        """
        if self.mark == constants.DEAD_SHIP_MARK:
            return True
        return False

    def has_active_ship(self):
        """
        Method to check whether a cell has a active ship or not.
        :return: True/False
        """
        if self.mark in (constants.ACTIVE_SHIP_MARK, constants.HIT_SHIP_MARK):
            return True
        return False

    def process_shot(self):
        """
        Method to process the shot fired on the cell. It checks whether the cell is occupied by a
         ship or not and then marks the cell as per state.
        :return:
        """
        if self.has_active_ship():
            self.mark = constants.HIT_SHIP_MARK
            self.hit_count += 1
            if self.hit_count == self.ship.power:
                self.mark = constants.DEAD_SHIP_MARK
                return constants.KILL
            else:
                return constants.HIT
        elif not self.occupied or self.mark == constants.MISS_HIT_MARK:
            self.mark = constants.MISS_HIT_MARK
            return constants.MISS


class Board:
    """
    This class represents the board where the ships will be placed for the game. By default the
    board has a size of 9 X 26 but can be modified as per input
    """
    def __init__(self, rows=9, columns=26):
        """
        Constructor method to initialize the board object.
        :param rows:
        :param columns:
        """
        self.rows = rows
        self.columns = columns
        self.grid = [[Cell(j, i, constants.EMPTY_CELL_MARK) for i in range(rows)] for j in range(
            columns)]
        self.total_ships = 0
        self.active_ships = 0
        self.destroyed_ships = 0

    def process_shot(self, coordinate):
        """
        Method to process a shot fired on a cell.
        :param coordinate:
        :return:
        """
        row_num = ord(coordinate[:1]) - ord('A')
        column_num = int(coordinate[1:]) - 1
        target_cell = self.grid[row_num][column_num]
        result = target_cell.process_shot()
        if result == constants.KILL:
            self.destroyed_ships += 1
        return result

    def get_active_ships_count(self):
        """
        Method to get the count of active ships on the board
        :return:
        """
        active_ship_count = 0
        for row_index in range(self.rows):
            for column_index in range(self.columns):
                cell = self.grid[row_index][column_index]
                if cell.has_active_ship():
                    active_ship_count += 1

        return active_ship_count

    def get_destroyed_ships_count(self):
        """
        Method to get the count of destroyed ships on board
        :return:
        """
        destroyed_ships_count = 0
        for row_index in range(self.rows):
            for column_index in range(self.columns):
                cell = self.grid[row_index][column_index]
                if cell.has_destroyed_ship():
                    destroyed_ships_count += 1

        return destroyed_ships_count

    def print_board(self):
        """
        Method to print board.
        :return:
        """
        for row_index in range(self.rows):
            for column_index in range(self.columns):
                cell = self.grid[row_index][column_index]
                print(cell.mark, end=' ')
            print()

