import json
from src.actions.inspect import is_inspection_command, handle_inspection

def load_game_data():
    try:
        with open('data/rooms.json') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Could not find rooms.json!")
        return
    
def describe_room(room):
    print(f"\nYou are in {room['name']}.")
    print(room['description'])
    print("\nExits:", ", ".join(room['connections'].keys()))
    
    if room['interactables']:
        print("\nWhat you can see with a glance:")
        for item in room['interactables']:
            print(f"- {item['name']}: {item['description']}")
            
def main():
    rooms = load_game_data() 
    if not rooms:
        print("\nFailed to load game data!")
        return
    
    current_room = rooms[0]
    
    print("\n=== Welcome to Singed ===\n")  
    
    while True:
        describe_room(current_room)
        
        command = input("\nWhat would you like to do? ").lower().strip()
        
        if command == "quit":
            print("\nThanks for playing!")   
            break
        elif command == "look":
            continue
        elif is_inspection_command(command):
            print(handle_inspection(command, current_room))        
        else:
            print("\nI don't understand that command.") 

if __name__ == "__main__":
    main()
