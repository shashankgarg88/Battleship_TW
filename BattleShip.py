from .board import Board
from .ship import QShips, PShips
from .constants import ShipContants as const


def place_ships(board, total_ships, details):
    """
    Method to place ships on board
    :param board: Board of a player
    :param total_ships: total ships to be placed
    :param details: Details of ship placement
    :return:
    """
    # Get ship type, row, column and ship positions
    ship_type = details[0]
    if ship_type not in (const.FLEET_Q_CLASS, const.FLEET_P_CLASS):
        print("invalid ship type.")
        exit()

    ship_row = int(details[1])
    ship_col = int(details[2])
    ship_positions = details[3:]

    # place ships on the basis of ship type
    if ship_type == const.FLEET_Q_CLASS:
        q_ships = QShips(total_ships, ship_row, ship_col)
        q_ships.postion_fleet(ship_positions, board)
    else:
        p_ships = PShips(total_ships, ship_row, ship_col)
        p_ships.postion_fleet(ship_positions, board)


def process_shots(p1_shots, p2_shots, p1_board, p2_board, is_p1_turn):
    """
    Method to process shots of player 1 and player 2
    :param p1_shots: List of shots by player 1
    :param p2_shots: List of shots by player 2
    :param p1_board: player 1 board
    :param p2_board: player 2 board
    :param is_p1_turn: flag to identify if its player 1 turn or player 2 turn
    :return:
    """
    if is_p1_turn:
        # process shot for player 1 if any shot is left in list of player 1 shots.
        if len(p1_shots) > 0:
            # remove 1st shot from the list and process it.
            p1_shot = p1_shots.pop(0)

            # get result after processing the shot
            result = p2_board.process_shot(p1_shot)

            # print on the basis of result from the processed shot.
            if result in (const.KILL, const.HIT):
                print("Player-1 fires a missile with target {0} which got hit".format(p1_shot))
                # if the shot is a hit, set player 1 as the next turn player
                is_p1_turn = True
            else:
                print("Player-1 fires a missile with target {0} which got miss".format(p1_shot))
                is_p1_turn = False
        else:
            # if there are no shots left for player 1 print no shot left.
            is_p1_turn = False
            print("Player-1 has no more missiles left to launch")
    else:
        # Same logic for player 2
        if len(p2_shots)>0:
            p2_shot = p2_shots.pop(0)
            result = p1_board.process_shot(p2_shot)

            if result in (const.KILL, const.HIT):
                print("Player-2 fires a missile with target {0} which got hit".format(p2_shot))
                is_p1_turn = False
            else:
                print("Player-2 fires a missile with target {0} which got miss".format(p2_shot))
                is_p1_turn = True
        else:
            is_p1_turn = True
            print("Player-2 has no more missiles left to launch")

    # if there are shots left for player 1 or player 2 call recursively
    if len(p1_shots) > 0 or len(p2_shots) > 0:
        process_shots(p1_shots, p2_shots, p1_board, p2_board, is_p1_turn)
    else:
        p1_ship_count = p1_board.get_active_ships_count()
        p2_ship_count = p2_board.get_active_ships_count()
        # else find the winner and print it.
        if p1_ship_count > 0 and p2_ship_count == 0:
            print("Player-1 won the battle")
        elif p2_board.get_active_ships_count() > 0 and p1_ship_count == 0:
            print("Player-2 won the battle")
        else:
            print("Both players have active ships.")
        return


def get_size_input():

    size = input().split(" ")
    # Validate size format
    if len(size) != 2:
        return "Invalid size format."
        # exit()

    # Validate width of board
    if not size[0].isnumeric() or not 1 <= int(size[0]) <= 9:
        return "Invalid width of area. 1<=M<=9"
        # exit()

    # validate height of board.

    if not (size[1].isalpha() and size[1].isupper()) or not ord('A') <= ord(size[1]) <= ord('Z'):
        return "Invalid height of area. A <= Height of Battle area (N’) <= Z"
        # exit()
    width = int(size[0])

    height = ord(size[1]) - ord('A') + 1
    return height, width


def get_total_ship_input(height, width):
    total_ships = int(input())
    if not 1 <= total_ships <= (height * width):
        return "Too many ships. 1 <= Number of battleships <= M’ * N’ "
        # exit()

    return total_ships


def get_p1_ship_info_input():
    return input()


def get_p2_ship_info_input():
    return input()


def get_p1_shots_info_input():
    return input()


def get_p2_shots_info_input():
    return input()


def battle_ship():
    """
    This method performs the following steps
    1. Takes all the user inputs
    2. Creates and initializes Player boards
    3. Process shots fired by player 1 and player 2
    :return:
    """
    # First input to get size of the board
    import pdb
    pdb.set_trace()
    height, width = get_size_input()
    #
    # width = int(size[0])
    #
    # height = ord(size[1]) - ord('A') + 1

    # Create player boards
    p1_board = Board(height, width)
    p2_board = Board(height, width)

    # get total ships
    total_ships = get_total_ship_input(height, width)

    # get player 1 ship details
    p1_ship_details = get_p1_ship_info_input().split(" ")

    # get player 2 ship details
    p2_ship_details = get_p2_ship_info_input().split(" ")

    # get player 1 shots
    p1_shots = get_p1_shots_info_input().split(" ")

    # get player 2 shots
    p2_shots = get_p2_shots_info_input().split(" ")

    # place ships on player 1 and player 2 board
    place_ships(p1_board, total_ships, p1_ship_details)
    place_ships(p2_board, total_ships, p2_ship_details)

    # Process shots of player 1 and player 2 starting with player 1
    process_shots(p1_shots, p2_shots, p1_board, p2_board, True)

    return ""

# print(battle_ship())
