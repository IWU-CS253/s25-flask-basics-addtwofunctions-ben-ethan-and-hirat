def average_length(user_string):
    words = user_string.split()
    if words:  # Ensure the string is not empty
        avg = sum(len(word) for word in words) / len(words)
    else:
        avg = 0
    return avg

def total_words(user_string):
    words = user_string.split()
    total_w = len(words)
    return total_w

def total_chars(user_string):
    words = user_string.split()
    total_c = 0
    for word in words:
        total_c += len(word)
    return total_c

def initials(user_string):
    init_str = ""
    words = user_string.split()
    for word in words:
        init_str += word[0]
    return init_str



