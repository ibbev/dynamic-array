import random

lijst = [random.randint(0,1000) for _ in range(100)]


def merge_sort(lijst):
	i = 0
	links = []
	rechts = []
	lenh = len(lijst) // 2 

	if len(lijst) < 2:
		return lijst
	while i < len(lijst):
		if i < lenh:
			links.append(lijst[i])
		else:
			rechts.append(lijst[i])
		i += 1	

	links = merge_sort(links)
	rechts = merge_sort(rechts)

	resultaat = []

	while len(rechts) > 0 and len(links) > 0:
		if links[0] < rechts[0]:
			resultaat.append(links.pop(0))
		else:
			resultaat.append(rechts.pop(0))
	resultaat.extend(links)
	resultaat.extend(rechts)
	return resultaat
print(merge_sort(lijst))
