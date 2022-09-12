from collections import Counter

# Determining the most frequently occured items in a sequence
words =['test', 'test', 'test', 'are', 'is', 'i', 'am']
c = Counter(words)
print(c.most_common())
print(sorted(c))
print(sum(c.values()))