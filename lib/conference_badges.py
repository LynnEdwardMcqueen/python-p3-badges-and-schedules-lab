def badge_maker(name):
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    batch_badges = [badge_maker(name) for name in names]

    return batch_badges

def assign_rooms(names):
    i = 1
    room_assignment = []
    for name in names:
        room_assignment.append(f"Hello, {name}! You'll be assigned to room {i}!")
        i += 1
    return room_assignment

def printer(names):
    for name_msg in batch_badge_creator(names):
        print(name_msg)

    for room_msg in assign_rooms(names):
        print(room_msg)
    return None

print(badge_maker("Guido van Rossum"))
print(batch_badge_creator(["Lori", "Lauren", "Linda"]))
print("Hello, Guido! You'll be assigned to room 1!")

printer(["Guido", "Lauren", "Linda", "Paul", "Robbie", "Dave", "James", "Dan"])