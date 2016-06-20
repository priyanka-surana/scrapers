import csv


filename = 'items.csv'
reader = csv.reader(open(filename))
#Making it compatible with Python 2.6+
#col = reader.next().index('id')
col = next(reader).index("id")
ids = [line[col] for line in reader]
ids = list(set(ids))
with open('ids.txt', 'w') as f:
    f.write('\n'.join(ids))
