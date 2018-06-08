def remove_duplicate(string):
    previous_char = ''
    cur_char = ''
    no_duplicates = ''
    duplicates = ''
    for ch in string:
        if ch == previous_char:
            duplicates += ch
        else:
            no_duplicates += ch
        previous_char = ch

    return no_duplicates, duplicates

print(remove_duplicate("balloons"))
print(remove_duplicate("aabbccddeded"))
print(remove_duplicate("flabby aapples"))