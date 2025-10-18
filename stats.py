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