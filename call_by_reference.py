def mutate_list(list):
	print "Got ",list
	# mutate list 
	list.append("Mango")
	print "list changed to " , list

outer_list = ['Apple','Grape']
print "before mutation ", outer_list
mutate_list(outer_list)
print "after mutation ", outer_list



print "------------"


# try to change the reference that was passed in as a paramete
def mutate_reference(list):
	print "Got ",list
	# change reference of list object
	list = ['Apple','Grape','Mango']
	print "list changed to ", list


outer_list = ['Apple','Grape']
print "before mutation ", outer_list
mutate_reference(outer_list)
# after calling mutate_reference(), the reference value is changed not reference 
# i.e so pointer is still pointing to original object which was pass
# inside the method list object reference is changed but still it is not reflected outside.

print "after mutation ", outer_list


def reassign(list):
	list.append(23)

list = [1,2]
reassign(list)
print list
