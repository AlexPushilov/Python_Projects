def convert_to_snake_case(text):
	l = []
	for el, v in enumerate(text):
		if v.isupper() and el != 0:
			l.append("_")
		l.append(v)
	output = "".join(l)
	return output.lower()
string = input()
print(convert_to_snake_case(string))