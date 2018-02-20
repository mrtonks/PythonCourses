# jabber = open("C:/Users/jesus vera/Google Drive/Python Exercises/Python Course/FileIO/textfiles/sample.txt", 'r')
# jabber = open("C:\\Users\\jesus vera\\Google Drive\\Python Exercises\\Python Course\\FileIO\\textfiles\\sample.txt")
# jabber = open("textfiles\\sample.txt", 'r')
# for line in jabber:
#     if "somewhere" in line.lower():
#         print(line, end='')
#
# jabber.close()

# with open("textfiles\\sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "SOMEWHERE" in line.upper():
#             print(line, end='')
# with open("textfiles\\sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()
# with open("textfiles\\sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')

# with open("textfiles\\sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines[::-1]:
#     print(line, end='')
with open("textfiles\\sample.txt", 'r') as jabber:
    lines = jabber.read()
print(lines)

for line in lines[::-1]:
    print(line, end='')