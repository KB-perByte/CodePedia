def reverseSting(strn): 
	index = -1
	for i in range(len(strn)-1, int(len(strn)/2), -1): 
		if strn[i].isalpha(): 
			temp = strn[i] 
			while True: 
				index += 1
				if strn[index].isalpha(): 
					strn[i] = strn[index] 
					strn[index] = temp 
					break
	return strn 

stri = "a!!!b.c.d,e'f,ghi"
print ("Input : ", stri) 
stri = reverseSting(list(stri)) 
print ("Output : ", "".join(stri)) 

