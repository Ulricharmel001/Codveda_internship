import os
# use to split sentences into words
with open("Word_counter/text.txt") as  file:
    content = file.read()
    number_of_words = content.split()
    print("number words is:", len(number_of_words))
    