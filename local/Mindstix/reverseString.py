def reversingString(str, start, end): 
	
	while (start < end): 
		str = (str[:start] + chr(ord(str[start]) ^ 
								ord(str[end])) +
								str[start + 1:]); 
		str = (str[:end] + chr(ord(str[start]) ^ 
							ord(str[end])) +
							str[end + 1:]); 
		str = (str[:start] + chr(ord(str[start]) ^ 
								ord(str[end])) +
								str[start + 1:]); 

		start += 1; 
		end -= 1; 
	return str; 

s = "GeeksforGeeks"; 
print(reversingString(s, 0, 12)); 

