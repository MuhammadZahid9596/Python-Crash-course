with open('digits.txt') as file_object:
 contents = file_object.read()
 print(contents)
 lines = 0
 for characters in contents:
    if characters == '\n':
        lines +=1
 print(lines)