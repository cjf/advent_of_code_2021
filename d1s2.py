text_file = open("/Users/cj/IdeaProjects/adventofcode2021/d1/input.txt", "r")
lines = text_file.readlines()
text_file.close()

num_larger = 0
previous_line = None

for count in range(0,len(lines)):
    if count+3 >= len(lines):
       break;

    groupA = int(lines[count]) + int(lines[count+1]) + int(lines[count+2])
    groupB = int(lines[count+1]) + int(lines[count+2]) + int(lines[count+3])

    if groupB > groupA:
        num_larger = num_larger + 1

print(num_larger)





