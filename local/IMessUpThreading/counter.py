from collections import Counter
colors = ['blue', 'blue', 'blue', 'red', 'red']
counter = Counter(colors)
counter['yellow'] += 1
d = counter.most_common()[0]
print(d)