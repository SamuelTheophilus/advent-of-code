"""
Day 4
"""
def read_data():
    with open("day_4.txt", "r") as f:
        data = f.read().strip().split("\n")
        return data, len(data), len(data[0])

gen_array, row_len, col_len = read_data()

def has_xmas(
        i: int,
        j: int,
        direction:tuple,
) -> int:

    x_dir, y_dir = direction
    for idx, char in enumerate("XMAS"):
        x_pos: int = i + idx * x_dir
        y_pos: int = j + idx * y_dir
        if not (0 <= x_pos < row_len and 0 <= y_pos < col_len): return 0
        if gen_array[x_pos][y_pos] != char: return 0
    return 1

def has_diagonal_mas(
        i: int,
        j: int
) -> int:
    if not( 1 <= i < row_len - 1 and 1 <= j < col_len - 1): return 0
    if gen_array[i][j] != "A": return 0

    dg_1 = f"{gen_array[i-1][j-1]}{gen_array[i+1][j+1]}"
    dg_2 = f"{gen_array[i-1][j+1]}{gen_array[i+1][j-1]}"

    return 1 if dg_1 in ['SM', 'MS'] and dg_2 in ['SM', 'MS'] else 0


if __name__ == "__main__":
    coordinates = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x != 0 or y != 0: coordinates.append((x, y))

    sol_1: int = 0
    sol_2: int = 0
    for cor_x in range(row_len):
        for cor_y in range(col_len):
            for coordinate in coordinates:
                sol_1 += has_xmas(cor_x, cor_y, coordinate)
            sol_2 += has_diagonal_mas(cor_x, cor_y)

    print(f"Solution one: {sol_1}")
    print(f"Solution two: {sol_2}")