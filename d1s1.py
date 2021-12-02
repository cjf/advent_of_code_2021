text_file = open("/Users/cj/IdeaProjects/adventofcode2021/d1/input.txt", "r")
lines = text_file.readlines()
text_file.close()

num_larger = 0
previous_line = None

for count in range(0,len(lines)):
    current_line = int(lines[count])
    if previous_line != None:
        if current_line > previous_line:
            num_larger = num_larger + 1
        
    
    previous_line = current_line

print(num_larger)





