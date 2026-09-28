ljst = [0,6,5,3,4,6]
lenh = len(ljst) // 2

def merge_sort(lijst):
	i = 0
	links = []
	rechts = []
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
	while rechts == [] and links == []:
		if links[1] < rechts[1]:
			resultaat.append(links.pop[1])
		else:
			resultaat.append(rechts.pop[1])
	resultaat.append(links)
	resultaat.append(rechts)
	return resultaat
merge_sort(ljst)
print(resultaat)
