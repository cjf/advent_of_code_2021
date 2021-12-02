text_file = open("/Users/cj/IdeaProjects/adventofcode2021/d2/input.txt", "r")
lines = text_file.readlines()
text_file.close()

current_depth = 0
current_hor = 0

for line in lines:
    line_parts = line.split()
    direction = line_parts[0]
    value = line_parts[1]
    
    if direction == 'down':
        current_depth = current_depth + int(value)
    if direction == 'up':
        current_depth = current_depth - int(value)
    if direction == 'forward':
        current_hor = current_hor + int(value)
        
print(current_depth * current_hor)
