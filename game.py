import json

def load_game_data():
    try:
        with open('data/rooms.json') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Could not find rooms.json!")
        return
    
def describe_room(room):
    print(f"You are in {room['name']}.")
    print(room['description'])
    print("Exits:", ", ".join(room['connections'].keys()))
    
    if room['interactables']:
        print("What you can see with a glance:")
        for item in room['interactables']:
            print(f"- {item['name']}: {item['description']}")

if __name__ == "__main__":
    rooms = load_game_data()
    if rooms:
        first_room = rooms[0]
        describe_room(first_room)
    else:
        print("Failed to load game data. Exiting.")
