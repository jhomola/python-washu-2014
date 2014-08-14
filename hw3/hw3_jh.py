def selection_sort(unsorted_in):
	# in each run, this will look for the greatest element and move it to the end of the list
	for slot in range(len(unsorted_in)-1, 0, -1):
		maxposition = 0
		for i in range(1, slot+1):
			if unsorted_in[i] > unsorted_in[maxposition]:
				maxposition = i
		temp = unsorted_in[slot]
		unsorted_in[slot] = unsorted_in[maxposition]
		unsorted_in[maxposition] = temp
	return unsorted_in

	

def merge_sort(unsorted_in):
	# this implements the pseudo-code we drafted in class
	# the input is split into halves recursively
	# and then pierced back together starting with the smallest element in each turn
    if len(unsorted_in)>1:
        mid = len(unsorted_in)//2
        left = unsorted_in[:mid]
        right = unsorted_in[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                unsorted_in[k] = left[i]
                i=i+1
            else:
                unsorted_in[k] = right[j]
                j = j+1
            k = k+1

        while i < len(left):
            unsorted_in[k] = left[i]
            i = i+1
            k = k+1

        while j < len(right):
            unsorted_in[k] = right[j]
            j = j+1
            k = k+1
    return unsorted_in



# I am taking the quicksort code for graphing from http://www.pythonschool.net/algorithms_quickSort
def quicksort(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)
    return myList
	
def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right