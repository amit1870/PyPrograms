# there will be some sort string error 
# just put this file outside somewhere and will be done
from xlrd import open_workbook
from xlwt import Workbook
from xlutils.copy import copy

rb = open_workbook("contacts.xls")
wb = copy(rb)
s = wb.get_sheet(1)
header = ['name','number','age']
data = {'amit':[920193993,34],'ravi':[920193993,34],'shanu':[920193993,34],'kristy':[920193993,34],'mm':[920193993,34],'jambo':[920193993,34]}

i = 0
j = 0
for item in header:

	s.write(i,j,item)
	j += 1
i = 1

for key,value in data.iteritems():
	s.write(i,0,key)
	s.write(i,1,value[0])
	s.write(i,2,value[1])
	i += 1


# s.write(0,10,'This data is written')
wb.save('contacts.xls')