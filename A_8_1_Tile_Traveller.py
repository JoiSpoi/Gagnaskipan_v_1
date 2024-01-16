def move_player(position: tuple, move: str) -> tuple:
    vect_move = directoin_to_vector[move]
    return (position[0] + vect_move[0], position[1] + vect_move[1])


def print_acceptable_moves(position: tuple):
    possible_moves = list(map[position[0]][position[1]])
    result = []
    for move in possible_moves:
        result.append(direction_to_words[move])
        result.append(" or ")
    result.pop(-1)

    print("You can travel: ", end="")
    for i in result:
        print(i, end="")
    print(".")



map = [ # [x][y]
    [("N"), ("N", "E", "S"), ("E", "S")],
    [("N"), ("S", "W"), ("E", "W")],
    [("N"), ("N", "S"), ("S", "W")]
]

directoin_to_vector = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0)
}
direction_to_words = {
    "N": "(N)orth",
    "E": "(E)ast",
    "S": "(S)outh",
    "W": "(W)est"
}

WINNING_TILE = (2, 0)


player_pos = (0, 0) # (x, y)

while player_pos != WINNING_TILE:

    print_acceptable_moves(player_pos)

    move = input("Direction: ").upper()

    if not move in map[player_pos[0]][player_pos[1]]:
        print("Not a valid direction!")
        continue

    player_pos = move_player(player_pos, move)

else:
    print("Victory!")