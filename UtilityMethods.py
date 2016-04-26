#Print Method
def m(string_toPrint = ""):
	print(str(string_toPrint));

#Prints out any number of passed objects on separate lines
def m(*object_toPrint):
	int_counter = 0;
	for int_n in object_toPrint:
		print(str(object_toPrint[int_counter]));
		int_counter += 1;

#Prints out any number of passed objects on the same line. Removes the parentheses before printing
def mSameLine(*object_toPrint):
	string_str = str(object_toPrint);
	string_str = string_str.replace("(" , "");
	string_str = string_str.replace(")" , "");
	print(str(string_str));