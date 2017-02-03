#!/usr/bin/python
def quicksort(A, l, r):
	if l < r:
		qone, qtwo = partition(A, l, r)
		quicksort(A, l, qone - 1)
		quicksort(A, qone + 1, qtwo - 1)
		quicksort(A, qtwo + 1, r)

def partition(A, l, r):
	qone = l
	qtwo = r
	if(A[qone] > A[qtwo]):
		A[qone], A[qtwo] = A[qtwo], A[qone]
	i = l

	for j in range(l + 1, r):
		if A[j] <= A[qtwo]:
			i = i + 1
			A[i], A[j] = A[j], A[i]
	qtwo = i + 1
	A[qtwo], A[r] = A[r], A[qtwo]

	i = l
	for j in range(l + 1, qtwo):
		if A[j] <= A[qone]:
			i = i + 1
			A[i], A[j] = A[j], A[i]

	qone = i
	A[qone], A[l] = A[l], A[qone]
	return qone, qtwo

if __name__ == '__main__':
	inputlist = [8,7,11,16,2,5,3,1,12]
	print("List: ", inputlist)
	quicksort(inputlist, 0, len(inputlist) - 1)
	print("Sorted list:", inputlist)

