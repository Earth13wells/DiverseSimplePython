n = 1
#
text = list((input("Enter Text:")).rstrip())
#
object = object()
text = [object:=v for v in text if object!=v]
#
for i in list(text):
    if i == ' ':
        n += 1
print(n)
#
# REGEX SOLUTION
# import re
# text = input("Enter Text:")
# x = re.findall("(?:\s+|$)", text, flags=0) # find all spaces and end of line
# print(len(x))
