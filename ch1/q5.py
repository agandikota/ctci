def q5(str_):
	nstr= ""
	arr = [0] * 256
	for char in str_:
		arr[ord(char)] += 1
	for i in range(256):
		if (arr[i] != 0):
			nstr += chr(i) + str(arr[i])
	if (len(nstr) < len(str_) and len(nstr) != 0):
		return nstr
	else:
		return str_

def main():
	str_ = "aabccd!!!eeeeeeeeaa" * 1
	print q5(str_)
main()