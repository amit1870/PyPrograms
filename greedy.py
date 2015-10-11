
# find minimum time to finish all jobs with given number of assignees

def isPossible(time,K,jobs,n):
	# count is count of current assignees required for jobs 
	count = 1
	curr_time = 0
	i = 0
	while i < n:
		if curr_time + jobs[i] > time:
			curr_time = 0
			count += 1
		else:
			# add time of job to current time and move to next job 
			curr_time += jobs[i]
			i += 1
	# return true if count is <= than K
	return count <= K

# K = number of assignees
# T = time required by every assignee to finish one unit of job 
# N = Number of jobs 

def findMinTime(K, T, jobs):
	# set start and end for binary search 
	# end provides an upper limit for time 
	n = len(jobs)
	start = end = 0
	for i in range(n):
		end += jobs[i]
	answer = end 
	max_of_jobs = max(jobs)
	while start <= end:
		mid = (start+end)/2
		if mid >= max_of_jobs and isPossible(mid,K,jobs,n):
			answer = min(answer,mid)
			end = mid - 1
		else:
			start = mid + 1
	return answer * T

jobs = [10,7,8,12,6,8]
K = 4
T = 5
print findMinTime(K,T,jobs)

# assuming all actvities are sorted initially 
def activitySelection(start,finish):
	i = 0
	activities = [i]
	for j in range(1,len(start)):
		if start[j] >= finish[i]:
			activities.append(j)
			# if the actvity is not selected, then finish time will not get changed
			i = j
	return activities

start = [1,3,0,5,8,5]
finish = [2,4,6,7,9,9]

print activitySelection(start,finish)
