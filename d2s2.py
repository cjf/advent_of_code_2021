text_file = open("/Users/cj/IdeaProjects/adventofcode2021/d2/input.txt", "r")
lines = text_file.readlines()
text_file.close()

current_depth = 0
current_hor = 0
current_aim = 0

for line in lines:
    line_parts = line.split()
    direction = line_parts[0]
    value = int(line_parts[1])
    
    if direction == 'down':
        current_aim = current_aim + value
    elif direction == 'up':
        current_aim = current_aim - value
    elif direction == 'forward':
        current_hor = current_hor + value
        current_depth = current_depth + (current_aim * value)
    
    print(str(current_depth) + ' - ' + str(current_hor) + ' - ' + str(current_aim))

        
print(current_depth * current_hor)
