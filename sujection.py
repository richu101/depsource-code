num_of_inpt = []
num_of_repitation_count = 0
for x in range(0,10):
	c = int(input('enter an num'))	
	num_of_inpt.append(c)
print(num_of_inpt) 
for o in range(0,10): #O = NUM TO BE CHECK
	for a in range(o,10): #NUMBERS TO CHECK 
		if num_of_inpt[o] == num_of_inpt[a]:
			num_of_repitation_count = num_of_repitation_count + 1
			num_of_inpt.delet(a)
	print(f"number_of_repitation_of{num_of_inpt[o]}={num_of_repitation_count} ")
	num_of_repitation_count = 0		
