model = {
    "A": "unknown",
    "B": "unknown"
}

def act(location, status):

    # Update the model
    model[location] = status

    # If current room is dirty, clean it
    if status == "dirty":
        print("Cleaning Room", location)
        model[location] = "clean"
        return "CLEAN"

    # Find the other room
    if location == "A":
        other_room = "B"
    else:
        other_room = "A"

    # If other room is dirty
    if model[other_room] == "dirty":
        print("Moving from", location, "to", other_room)
        return "MOVE " + other_room

    # If other room is unknown
    elif model[other_room] == "unknown":
        print("Moving from", location, "to", other_room)
        return "MOVE " + other_room

    # If both rooms are clean
    else:
        print("Both rooms are clean. STOP")
        return "STOP"


# Get input for first room
location = input("Enter current room (A/B): ").upper()
status = input("Enter status (dirty/clean): ").lower()

act(location, status)

# Enter the second room
location = input("Enter current room (A/B): ").upper()
status = input("Enter status (dirty/clean): ").lower()

act(location, status)

# Enter the final room status
location = input("Enter current room (A/B): ").upper()
status = input("Enter status (dirty/clean): ").lower()

act(location, status)
