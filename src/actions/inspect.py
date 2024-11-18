import json

def load_command_synonyms():
    with open('data/actions/commands.json') as f:
        commands = json.load(f)
        return commands['inspect_synonyms']
    
def is_inspection_command(command):
    synonyms = load_command_synonyms()
    return any(command.startswith(syn) for syn in synonyms)

def handle_inspection(command, room):
    for syn in load_command_synonyms():
        if command.startswith(syn):
            item_name = command[len(syn):].strip()
            break

    for item in room['interactables']:
        if item['name'].lower() in item_name.lower():
            return item['interaction']
        
    return "You don't see anything like that here."    
          
        
                
            