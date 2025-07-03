import requests
from collections import Counter
from bitstring import BitArray

url = 'http://127.0.0.1:8080/api2.php'

r = requests.get(url)
resp = r.json()

wins = [BitArray(bytes.fromhex(x['winning_number'])) for x in resp]
# print(wins)

mn = float('inf')
for w in wins:
	mn = min(mn, len(w))

# LEN = 408

# wins = [w for w in wins if len(w) == LEN]

lens = list(set([len(w) for w in wins]))

PERCENTAGE = 0.70


final = [None] * max(lens)

for j in lens:
	cols = []
	ws = [w for w in wins if len(w) == j]
	for i in range(j):
		col = Counter([w[i] for w in ws])
		cols.append(col)

	a = 0
	for i, c in enumerate(cols):
		res = c
		if c[True] > len(ws) * PERCENTAGE:
			res = True
		elif c[False] > len(ws) * PERCENTAGE:
			res = False
		else:
			a += 1
		
		if (final[i] == True or final[i] == False) and (res is True or res is False):
			print(i, j, final[i], res)
			assert final[i] == res
		else:
			final[i] = res

	print(len(ws), len(ws) * PERCENTAGE, a)

for i, c in enumerate(final):
	print(i, c)
