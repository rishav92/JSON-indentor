#!/usr/bin/python2
#opening the file
with open("raw.txt") as input_file:
    text = input_file.read()#reading the file and storing it in text
istack = []
str_length = 0
indent = 0
current_string = ""
text = text.replace("\n{", "{")#replacing the "\n{" with "{" in entire text
for char in text:#reading character one by one from text
    if char == '\n':   #if "/n" is encountered
        print current_string #print current_string
        current_string = " " * indent  #replacing current value of current_string with intent times space
        str_length = 0
    elif not (char == '{' or char == '}' or char == '[' or char == ']' or char == ','):
        str_length += 1      #if other than "{","}",'[',']',or ',' is encountered the add to current_string
        current_string += char #appending char to current_string
    elif char == '}' or char == ']':  # if closing parenthesis is encountered
        print current_string          #print current_string
        current_string = " " * indent  # add indent to current_string
        print current_string + char     #print current_string and char
        indent = istack.pop()          # indent = last element of istack
        current_string = " " * indent   #replacing current value of current_string with intent times space
    elif char == '{' or char == '[': # if opening parenthesis is encountered
        istack.append(indent)        #adding indent to last of istack
        indent = str_length + istack[-1]
        print current_string + char
        current_string = " " * indent #replacing current value of current_string with intent times space
        str_length = 0
    elif char == ',':  #if "," is encountered
        print current_string + char #print current_string + char
        current_string = " " * indent #replacing current value of current_string with intent times space
        str_length = 0
