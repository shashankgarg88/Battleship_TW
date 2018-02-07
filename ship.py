import abc
from .constants import ShipContants as constants


class Ship:
    """
    Class to represent a Ship.
        - fleet: The fleet to which the ship belongs.
        - cell : The cell on which the ship is placed.
        - power: How many times the Ship to be hit to destroy.

    """
    def __init__(self, fleet=None, cell=None, power=0):
        self.fleet = fleet
        self.cell = cell
        self.power = power


class AbstractFleet(metaclass=abc.ABCMeta):
    """
    Abstract class to represent a fleet of ships
    """
    def __init__(self):
        """
        Constructor to initialize the fleet of ships.
            - total_ships: Count of total ships in the fleet
            - starting_position: The cell from where the fleet positioning starts.
            - total_rows_req: Total rows required by the fleet to position all ships
            - total_column_req: Total columns required by the fleet to position all ships
            - shipList : List containing reference to all the ships in the fleet.

        """
        self.total_ships = 0
        self.starting_position = None
        self.total_rows_req = 0
        self.total_column_req = 0
        self.shipList = []

    @abc.abstractmethod
    def postion_fleet(self, starting_cell, board):
        """
        Abstract class to position ships of the fleet.
        :param starting_cell:
        :param board:
        :return:
        """
        pass

    def get_total_rows_required(self):
        """
        returns the total rows required by the fleet
        :return:
        """
        return self.total_rows_req

    def get_total_columns_required(self):
        """
        returns the total columns required by the fleet
        :return:
        """
        return self.total_column_req

    def get_next_available_cell(self, starting_cell, board):
        """
        This method returns the next available cell on the board after positioning the ships of
        the fleet
        :param starting_cell:
        :param board:
        :return:
        """
        row = starting_cell.row
        column = starting_cell.column + self.total_column_req + 1
        if column >= board.columns:
            row = starting_cell.row + self.total_rows_req + 1
            column = 0

        if row >= board.rows:
            print('Cannot place ship outside board.')
            return None
        return board.grid[row][column]

    def position_ship(self, cell, fleet, hit_power):
        """
        Method to position ship on a cell of the board.
        :param cell:
        :param fleet:
        :param hit_power:
        :return:
        """
        if not cell.occupied:
            ship = Ship(fleet, cell, hit_power)
            cell.occupied = True
            cell.mark = constants.ACTIVE_SHIP_MARK
            cell.ship = ship
            self.shipList.append(ship)
        else:
            # raise ex.CannotPlaceFleetError()
            print("XXXXXX")

    def can_position_fleet(self, starting_cell, board):
        """
        Method to check whether the fleet can be positioned from the input starting cell or not.
        :param starting_cell:
        :param board:
        :return:
        """
        are_rows_available = starting_cell.row + self.total_rows_req <= board.rows
        are_columns_available = starting_cell.column + self.total_column_req <= board.columns
        if are_columns_available and are_rows_available:
            return True
        return False


class PShips(AbstractFleet):
    """
    Extends the AbstractFleet class
    """

    def __init__(self, total_ships=0, total_rows=0, total_column=0):
        super().__init__()
        self.total_ships = total_ships
        self.total_rows_req = total_rows
        self.total_column_req = total_column

    def postion_fleet(self, ships_positions, board):
        """
        Method to position Ships of the fleet on the board.
        :param ships_positions:
        :param board:
        :return:
        """
        for cell in ships_positions:
            row = ord(cell[:1]) - ord('A')
            col = int(cell[1:]) - 1
            for i in range(row, row + self.total_rows_req):
                for j in range(col, col + self.total_column_req):
                        self.position_ship(
                            board.grid[i][j],
                            constants.FLEET_P_CLASS,
                            constants.P_CLASS_HIT_POWER
                        )

class QShips(AbstractFleet):
    """
    Extends the AbstractFleet class
    """

    def __init__(self, total_ships=0, total_rows=0, total_column=0):
        super().__init__()
        self.total_ships = total_ships
        self.total_rows_req = total_rows
        self.total_column_req = total_column

    def postion_fleet(self, ships_positions, board):
        """
        Method to position Ships of the fleet on the board.
        :param starting_cell:
        :param board:
        :return:
        """
        for cell in ships_positions:
            row = ord(cell[:1]) - ord('A')
            col = int(cell[1:]) - 1
            for i in range(row, row + self.total_rows_req):
                for j in range(col, col + self.total_column_req):
                        self.position_ship(
                            board.grid[i][j],
                            constants.FLEET_Q_CLASS,
                            constants.Q_CLASS_HIT_POWER
                        )
