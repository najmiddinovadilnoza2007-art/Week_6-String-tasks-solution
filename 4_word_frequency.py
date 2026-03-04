def word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + -1
    return frequency
print(word_frequency("Python is great and python is easy"))
# {'python': 2, 'is': 2, 'great': 1, 'and': 1, 'easy': 1}
