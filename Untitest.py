from . import BattleShip
import pytest


@pytest.mark.parametrize("size, total_ships, p1_ships, p2_ships, p1_shots, p2_shots", [
        ("5 E", 2, 'Q 1 1 A1 B2', 'P 2 1 D4 C3', 'A1 B2 B2 B3', 'A1 B2 B2 B3 A1 B2 B3 A1 D1 E1 D4 D4 D5 D5'),
    ])
def test_Battle_ship(size, total_ships, p1_ships, p2_ships, p1_shots, p2_shots ):

    size_arr = size.split(" ")
    size_width = int(size_arr[0])

    size_height = ord(size_arr[1]) - ord('A') + 1
    BattleShip.input = lambda: size
    # Call the function you would like to test (which uses input)
    height, width = BattleShip.get_size_input()
    assert height == size_height
    assert width == size_width
    BattleShip.input = lambda: total_ships
    ships = BattleShip.get_total_ship_input(height, width)
    assert ships == total_ships

    BattleShip.input = lambda: p1_ships
    player_1_ships = BattleShip.get_p1_ship_info_input()
    assert player_1_ships == p1_ships

    BattleShip.input = lambda: p2_ships
    player_2_ships = BattleShip.get_p2_ship_info_input()
    assert player_2_ships == p2_ships

    BattleShip.input = lambda: p1_shots
    player_1_shots = BattleShip.get_p1_shots_info_input()
    assert player_1_shots == p1_shots

    BattleShip.input = lambda: p2_shots
    player_2_shots = BattleShip.get_p2_shots_info_input()
    assert player_2_shots == p2_shots

