def find_occurrences(text, pattern):
    indexes = []
    start = 0
    while True:
        index = text.find(pattern, start)
        if index == - 1:
           break
        indexes.append(index)
        start = index + 1
    return indexes
print(find_occurrences("abracadabra", "abra")) #[0, 7]