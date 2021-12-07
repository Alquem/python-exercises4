start_point = [0,0]
current_point = [0,0]
movement = " "
while movement:
    movement = input()
    if not(movement):
        break
    move = movement.split()
    if move[0] == "UP":
        current_point[0] += int(move[1])
    elif move[0] == "DOWN":
        current_point[0] -= int(move[1])
    elif move[0] == "LEFT":
        current_point[1] -= int(move[1])
    elif move[0] == "RIGHT":
        current_point[1] += int(move[1])
print(round(((start_point[0] - current_point[0])**2 + (start_point[1] - current_point[1])**2)**0.5))
