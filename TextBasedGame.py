import sys
rooms = {
    'H1': {'West': 'H2'},
    'H2': {'West': 'H3', 'East': 'H1'},
    'H3': {'South': 'H4', 'East': 'H2'},
    'H4': {'East': 'H5', 'North': 'H3', 'South': 'H7'},
    'H5': {'East': 'H6', 'West': 'H4'},
    'H6': {'West': 'H5'},
    'H7': {'North': 'H4', 'East': 'H8'},
    'H8': {'East': 'H9', 'West': 'H7'},
    'H9': {'West': 'H8'}


}
items = {
    'H1': '',
    'H2': 'Water',
    'H3': 'Chew Toy',
    'H4': 'Ball',
    'H5': 'Bambam',
    'H6': '',
    'H7': 'Dog Treat',
    'H8': 'Dog Food',
    'H9': 'Bone'

    
}
state = 'H1'
inventory = []
def get_new_state(state, direction):
    new_state = state  
    for i in rooms:  
        if i == state:  
            if direction in rooms[i]:  
                new_state = rooms[i][direction]  
    return new_state  
while 1:  
    print('Hello you are at', state)  
    if state == 'H5':
        print ('Battling with the Bambam', end = '')
        for i in range (50):
            for j in range (1000000):
                pass
            print (".", end = '', flush = True)
        print ()
        if len (inventory) == 6:
            print ('Congratulations! You have collected all items and defeated the Bambam!\nThanks for playing the game. Hope you enjoyed it. ')
        else:
            print ('NOM NOM...GAME OVER!\nThanks for playing the game. Hope you enjoyed it.')
        break
    
    print ('Available to you in this room is', items[state])
    print ('You currently have', inventory)
    direction = input('Add item you want OR direction to go OR exit to give up: ')  
    if direction.lower() == items[state].lower():
        if items[state] not in inventory:
            inventory.append(items[state])
        continue
    direction = direction.capitalize()  
    if direction == 'Exit':  
        sys.exit(0)  
    if direction == 'East' or direction == 'West' or direction == 'North' or direction == 'South':  
        new_state = get_new_state(state, direction)  
        if new_state == state:  
            print('There is a fearsome darkness in that direction quickly enter other direction!')  
        else:
            state = new_state  
    else:
        print('Invalid direction!!')  