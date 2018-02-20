# ip = input("Please enter an IP address: ")
# numberSegments = 0
# charsInSegment = 0
# position = 1
#
# if ip != '':
#     print("The IP address {0} contains:".format(ip))
#     for char in ip:
#         if char == '.':
#             if position == 1:
#                 continue
#             else:
#                 numberSegments += 1
#                 print("Segment {0} has {1} chars".format(numberSegments, charsInSegment))
#                 charsInSegment = 0
#         else:
#             charsInSegment += 1
#             if position == len(ip):
#                 numberSegments += 1
#                 print("Segment {0} has {1} chars".format(numberSegments, charsInSegment))
#         position += 1
#
#     print("There are {0} segments".format(numberSegments))
# else:
#     print("There are zero segments")

input_prompt = ("Please enter an IP address. An IP address consists of 4 numbers, "
                "separated from each other with a full stop: ")
ipAddress = input(input_prompt)
if ipAddress[-1] != '.':
    ipAddress += '.'

segment = 1
segment_length = 0

for character in ipAddress:
    if character == '.':
        print("Segment {} contains {} characters".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1
