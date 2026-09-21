rooms = {"A": "Dirty", "B": "Dirty"}
location = "A"
goal = {"A": "Clean", "B": "Clean"}

def goal_reached():
    return rooms == goal

def act():
    global location
    if rooms[location] == "Dirty":
        rooms[location] = "Clean"
        print(f"Location {location}: Dirty -> Suck -> Clean")
    if goal_reached():
        return
    if location == "A" and rooms["B"] == "Dirty":
        location = "B"
        print("Move Right -> B")
    elif location == "B" and rooms["A"] == "Dirty":
        location = "A"
        print("Move Left -> A")

print("Initial:", rooms, "| Vacuum at", location)
while not goal_reached():
    act()
    if goal_reached():
        break

print("Goal achieved. Final:", rooms)
