def get_num_words(content):
    words = content.split()
    return len(words)

def get_frequency_chars(content):
    list_chars = list(content.lower())

    freq_count = {}
    for char in list_chars:
        if freq_count.get(char):
            freq_count[char] += 1
        else:
            freq_count[char] = 1

    return freq_count

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    dict_list = []

    for key in dict:
        temp_dict = {}
        temp_dict["char"] = key
        temp_dict["num"] = dict[key]
        if key.isalpha():
            dict_list.append(temp_dict)
    
    dict_list.sort(reverse = True, key = sort_on)

    return dict_list