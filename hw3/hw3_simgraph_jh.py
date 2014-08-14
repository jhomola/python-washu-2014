from hw3_jh import *
from random import *
import timeit
import matplotlib.pyplot as plt

def sim_time(maxn):
	time_selection = []
	time_merge = []
	time_quick = []
	
	for iter in range(1,maxn+1): 	
		if iter%10 == 0: print iter
	# creates maxn lists of random numbers of lengths 1-maxn
	# sorts every list with all three different methods 100 times each
	# takes time at beginning, between sorts, and at the end and calculates average runtimes
		temp1 = []
		temp2 = []
		temp3 = []
		for j in range(1,101):
			time1 = timeit.time.clock()
			unsorted = [uniform(-1000,1000) for i in xrange(iter)]
			selection_sort(unsorted)
			time2 = timeit.time.clock()
			unsorted = [uniform(-1000,1000) for i in xrange(iter)]
			merge_sort(unsorted)
			time3 = timeit.time.clock()
			unsorted = [uniform(-1000,1000) for i in xrange(iter)]
			quicksort(unsorted, 0, iter-1)
			time4 = timeit.time.clock()
			temp1.append((time2 - time1)*1)
			temp2.append((time3 - time2)*1)
			temp3.append((time4 - time3)*1)
		time_selection.append([sum(temp1)/100])
		time_merge.append([sum(temp2)/100])
		time_quick.append([sum(temp3)/100])
		
	return [time_selection, time_merge, time_quick]

a = sim_time(1000)

plt.plot(a[0], label="Selection Sorting") 		# complexity: n^2
plt.plot(a[1], "g-", label="Merge Sorting")		# complexity: [n*]log(n)
plt.plot(a[2], "r-", label="Quick Sorting")		# complexity: log(n)
plt.ylabel("Time")
plt.xlabel("Length of list to sort")
plt.legend(loc=2)
#plt.show()						# to display figure in gui
plt.savefig('hw3_jh.png')			# to save figure
plt.savefig('hw3_jh.pdf')			# to save figure