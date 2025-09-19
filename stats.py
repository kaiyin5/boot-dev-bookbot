def get_num_words(s):
    number_of_words = len(s.split())
    return number_of_words

def get_num_chars(s):
    char_list = {}
    for char in s:
        if char.lower() not in char_list:
            char_list[char.lower()] = 1
        else:
            char_list[char.lower()] += 1
    return char_list

def get_char_num_pair(char_dict):
    char_num_list = []
    for char in char_dict:
        if char.isalpha():
            char_num = {"char": char, "num": char_dict[char]}
            char_num_list.append(char_num)
    def sort_on(item):
        return item["num"]
    char_num_list.sort(reverse=True, key=sort_on)
    return char_num_list
    