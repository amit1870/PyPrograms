original_list = [1,2,3]
new_list = original_list

# here both list will point to the same reference 
# any change in any object will reflect in both 

# if you want to change the new_list only then you 
# have to use copy.copy 

import copy 

new_list = copy.copy(original_list)

# now any change in new list will not reflect to original list 

# same is true for dictionary object not sure about other object like tuple