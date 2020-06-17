import load_dict
from collections import Counter

words = load_dict.load("words.txt")
words.append('a')
words.append('i')

words = sorted(words)
num_each_let = Counter(words)

print(num_each_let)
