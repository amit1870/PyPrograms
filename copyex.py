import copy
original_list = [1,2,3]
new_list = original_list

# here both list will point to the same reference 
# any change in any object will reflect in both 

# if you want to change the new_list only then you 
# have to use copy.copy 

 

new_list = copy.copy(original_list)

# now any change in new list will not reflect to original list 

# same is true for dictionary object not sure about other object like tuple

def oneDigit(num):
	return num >= 0 and num < 10

def isPallindromUtil(num, dup_num):
	if oneDigit(num):
		return num == (dup_num % 10) 

	print copy.deepcopy(dup_num)
	if not isPallindromUtil(num/10,copy.deepcopy(dup_num)):
		return False

	dup_num /= 10 

	return (num % 10 == ( dup_num ) % 10)

def isPallindrom(num):
	if num < 0 :
		num = - num

	return isPallindromUtil(num, copy.deepcopy(num))

print isPallindrom(1221)