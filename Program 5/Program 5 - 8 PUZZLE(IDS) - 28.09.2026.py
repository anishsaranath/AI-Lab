GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def get_start():
    print("Enter the 8-puzzle start state (use 0 for blank).")
    print("Enter 9 numbers separated by spaces (row by row):")
    while True:
        try:
            nums = list(map(int, input("> ").split()))
            if sorted(nums) != list(range(9)):
                print("Invalid: must contain 0-8 exactly once. Try again.")
                continue
            return tuple(nums)
        except ValueError:
            print("Invalid input. Enter 9 integers.")

def neighbors(state):
    i = state.index(0)
    moves = []
    if i >= 3: moves.append(i - 3)
    if i < 6:  moves.append(i + 3)
    if i % 3 != 0: moves.append(i - 1)
    if i % 3 != 2: moves.append(i + 1)
    for m in moves:
        new = list(state)
        new[i], new[m] = new[m], new[i]
        yield tuple(new)

def dls(start, goal, limit):
    stack = [(start, [], 0)]
    visited = set()
    nodes_expanded = 0
    while stack:
        state, path, depth = stack.pop()
        if state in visited:
            continue
        visited.add(state)
        nodes_expanded += 1
        if state == goal:
            return path + [state], nodes_expanded
        if depth >= limit:
            continue
        for nxt in neighbors(state):
            if nxt not in visited:
                stack.append((nxt, path + [state], depth + 1))
    return None, nodes_expanded

def ids(start, goal, max_depth=50):
    total_expanded = 0
    for depth in range(max_depth + 1):
        print(f"Depth limit: {depth}")
        path, expanded = dls(start, goal, depth)
        total_expanded += expanded
        if path:
            return path, total_expanded
    return None, total_expanded

def show(state):
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])
    print()

start = get_start()
print("\nStart state:")
show(start)

path, expanded = ids(start, GOAL)

if path:
    cost = len(path) - 1
    print(f"\nSolved in {cost} moves.")
    print(f"Path cost (each move = 1): {cost}")
    print(f"Total nodes expanded: {expanded}\n")
    for i, step in enumerate(path):
        print(f"Step {i} (cost so far = {i}):")
        show(step)
else:
    print("No solution found within max depth.")
print("ANISH SARANATH")
print("1WN24CS041")
