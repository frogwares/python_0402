A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dlin = len(A)
ubiv_vozrost = 0
while ubiv_vozrost == 0:
	for i in range(dlin - 1):
		if A[i] < A[i + 1]:
			ubiv_vozrost = ' Massiv - Vozrostaet'
		else:
			ubiv_vozrost = 0
			break
	if ubiv_vozrost != 0:
		break
	for i in range(dlin - 1):
		if A[i] > A[i + 1]:
			ubiv_vozrost = ' Massiv - Ubyvaet'
		else:
			ubiv_vozrost = 0
			break
	if ubiv_vozrost != 0:
		break
	if ubiv_vozrost == 0:
		ubiv_vozrost = ' Massiv - nesortirovaniy'
print(ubiv_vozrost)
