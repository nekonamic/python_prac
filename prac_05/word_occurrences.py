text_string = input("Text: ")
text_list = text_string.split()
words_dict = {}
for word in text_list:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1
sorted(words_dict)
for key, value in sorted(words_dict.items()):
    print("{:<12}:{}".format(key, value))
