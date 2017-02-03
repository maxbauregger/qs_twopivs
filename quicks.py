#!/usr/bin/python
def quicksort(A, l, r):
	if l < r:
		qone, qtwo = partition(A, l, r)
		quicksort(A, l, qone - 1)
		quicksort(A, qone + 1, qtwo - 1)
		quicksort(A, qtwo + 1, r)

def partition(A, l, r):
	x = A[r]
	y = A[l]
	i = l

	for j in range(l + 1, r):
		if A[j] <= x:
			i = i + 1
			A[i], A[j] = A[j], A[i]

	A[i + 1], A[r] = A[r], A[i + 1]

	qtwo = i + 1
	i = l

	for j in range(l + 1, qtwo):
		if A[j] >= y:
			i = i + 1
			A[i], A[j] = A[j], A[i]

	A[i + 1], A[l] = A[l], A[i + 1]
	qone =  i + 1

	return qone, qtwo

if __name__ == '__main__':
	inputlist = [8,7,11,16,2,5,3,1,12]
	print("List: ", inputlist)
	quicksort(inputlist, 0, len(inputlist) - 1)
	print("Sorted list:", inputlist)

