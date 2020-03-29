def dedup(items):
	seen = set()
	for item in items:
		if item not in seen:
			yield item
			seen.add(item)
	print(seen)

list1 = [1,2,3,5,3,1,5,1,35,6,1,3]
s = list(dedup(list1))
print(s)