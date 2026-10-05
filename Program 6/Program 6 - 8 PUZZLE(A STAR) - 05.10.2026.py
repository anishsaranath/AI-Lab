import heapq

def heuristic(state, goal):
    h = 0

    for tile in range(1, 9):
        current = state.index(tile)
        target = goal.index(tile)

        current_row = current // 3
        current_col = current % 3

        target_row = target // 3
        target_col = target % 3

        h += abs(current_row - target_row) + abs(current_col - target_col)

    return h


def generate_successors(state):
    successors = []

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_state = state.copy()

            new_position = new_row * 3 + new_col

            new_state[blank], new_state[new_position] = \
                new_state[new_position], new_state[blank]

            successors.append(new_state)

    return successors


def print_state(state):

    for i in range(0, 9, 3):
        print(state[i:i + 3])

    print()


def print_path(state, parent):

    path = []

    while state is not None:
        path.append(state)
        state = parent[tuple(state)]

    path.reverse()

    for state in path:
        print_state(state)


def a_star(start, goal):

    open_list = []

    g = {}
    parent = {}
    closed = set()

    start_key = tuple(start)

    g[start_key] = 0
    parent[start_key] = None

    h = heuristic(start, goal)

    heapq.heappush(open_list, (h, 0, start))

    while open_list:

        f, current_g, current = heapq.heappop(open_list)

        current_key = tuple(current)

        if current_key in closed:
            continue

        if current == goal:
            print("Solution:")
            print_path(current, parent)
            return

        closed.add(current_key)

        successors = generate_successors(current)

        for successor in successors:

            successor_key = tuple(successor)

            if successor_key in closed:
                continue

            new_g = current_g + 1

            if successor_key not in g or new_g < g[successor_key]:

                g[successor_key] = new_g
                parent[successor_key] = current

                h = heuristic(successor, goal)
                f = new_g + h

                heapq.heappush(
                    open_list,
                    (f, new_g, successor)
                )

    print("No solution exists")


start = list(map(int, input("Enter the initial state: ").split()))

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

a_star(start, goal)
