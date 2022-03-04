from startup import knights, items


# The move_details function shows the knights and item instances moves 
def move_details(move):


    # This is creating an empty list.
    outcomes = []

    # code is assigning from move to Knight_move.
    for knight in knights:
        if move[0] == knight.code:
            Knight_move = knight

    # Assign the item held by the mover to holding.
    holding = Knight_move.item

    # Check if the Knight that move is alive.
    if Knight_move.status == 'ALIVE':

        # Dictionary translating directional letter into instruction list.
        # First item of list is mover's position index to change.
        # Second item of list is direction in which to change position index.
        directions = {'N':[0,-1], 'S':[0,1], 'W':[1,-1], 'E':[1,1]}

        # Iterate through directions dictionary.
        for key, value in directions.items():
            if move[2] == key:
                position_shift = Knight_move.position[value[0]] + value[1]

                # Checking if the knight new position is on the board or has drown.
                if position_shift in range(8):
                    Knight_move.position[value[0]] = position_shift

                    # Check if knight moves onto a square with item on it.
                    for item in items:
                        if item != holding:
                            if item.position == Knight_move.position:

                                # If knight has not item, an item is picked.
                                if holding is None:
                                    item.holder = Knight_move
                                    Knight_move.item = item

                                # Check if new item more valuable than holding.
                                # If so, drop holding item, and pickup new item.
                                elif holding.value < item.value:
                                    item.holder = Knight_move
                                    Knight_move.item = item
                                    holding.holder = None
                                    holding.position = list(Knight_move.position)

                                # item picked is appended to outcomes.
                                outcomes.append('pickup')

                    # Attack triggered if knight moves to other knight's square.
                    for defender in knights:
                        if defender != Knight_move:
                            if defender.status == 'ALIVE':
                                if defender.position == Knight_move.position:

                                    # Total attack, with weapon and surprise.
                                    total_attack = Knight_move.attack + 0.5
                                    for item in items:
                                        if Knight_move.item == item:
                                            total_attack += item.attack

                                    # Total defence, with weapon.
                                    total_defence = defender.defence
                                    for item in items:
                                        if defender.item == item:
                                            total_defence += item.defence

                                    # Determine winner and loser of battle.
                                    # Append winner and loser names to outcomes.
                                    if total_attack > total_defence:
                                        defender.status = 'DEAD'
                                        defender.item = None
                                        outcomes.append([defender.name,
                                            Knight_move.name])
                                    else:
                                        Knight_move.status = 'DEAD'
                                        Knight_move.item = None
                                        outcomes.append([Knight_move.name,
                                            defender.name])

                # Drowning triggered if knight moves to position outside board.
                else:
                    if Knight_move.item is not None:
                        drop = Knight_move.item
                        drop.holder = None
                        drop.position = list(Knight_move.position)
                    Knight_move.status = 'DROWNED'
                    Knight_move.position = None
                    Knight_move.item = None

                    # drowning condition is appended to outcomes.
                    outcomes.append('drown')

    
    return outcomes