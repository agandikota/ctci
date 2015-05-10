def isPerm(str1, str2):
	if (len(str1) != len(str2)):
		return False
	lis1,lis2 = [0] * 256, [0] * 256
	i = 0 
	while(i < len(str1)):
		lis1[ord(str1[i])] += 1
		lis2[ord(str2[i])] += 1
		i += 1
	return lis1 == lis2

def main():
	str1 = "abcd"
	str2 = "cdba"

	print isPerm(str1,str2)
main()