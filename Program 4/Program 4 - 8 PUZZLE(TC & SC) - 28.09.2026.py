import time
import sys

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

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
    if i >= 3:
        moves.append(i - 3)
    if i < 6:
        moves.append(i + 3)
    if i % 3 != 0:
        moves.append(i - 1)
    if i % 3 != 2:
        moves.append(i + 1)
    for m in moves:
        new = list(state)
        new[i], new[m] = new[m], new[i]
        yield tuple(new)

def dfs(start, goal, limit=50):
    stack = [(start, [], 0)]
    visited = set()
    nodes_expanded = 0
    max_memory_nodes = 1  
    
    start_time = time.perf_counter()

    while stack:
        current_memory_nodes = len(stack) + len(visited)
        if current_memory_nodes > max_memory_nodes:
            max_memory_nodes = current_memory_nodes

        state, path, depth = stack.pop()
        if state in visited:
            continue
        visited.add(state)
        nodes_expanded += 1
        
        if state == goal:
            end_time = time.perf_counter()
            return path + [state], nodes_expanded, max_memory_nodes, end_time - start_time
            
        if depth >= limit:
            continue
            
        for nxt in neighbors(state):
            if nxt not in visited:
                stack.append((nxt, path + [state], depth + 1))
                
    end_time = time.perf_counter()
    return None, nodes_expanded, max_memory_nodes, end_time - start_time

def show(state):
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])
    print()

start = get_start()
print("\nStart state:")
show(start)

path, expanded, max_nodes, execution_time = dfs(start, GOAL)

if path:
    cost = len(path) - 1
    print(f"Solved in {cost} moves.")
    print(f"Path cost (each move = 1): {cost}")
    print(f"Nodes expanded: {expanded}")
    print(f"Time Complexity (Execution Time): {execution_time:.6f} seconds")
    print(f"Space Complexity (Peak Node Storage): {max_nodes} nodes (~{max_nodes * sys.getsizeof(tuple()):,} bytes)\n")
    
    for i, step in enumerate(path):
        print(f"Step {i} (cost so far = {i}):")
        show(step)
else:
    print("No solution found within depth limit.")
    print(f"Nodes expanded: {expanded}")
    print(f"Execution Time: {execution_time:.6f} seconds")

