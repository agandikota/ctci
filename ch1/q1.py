# Unique characters

def unique(str):
	if (len(str) > 256):
		return False
	arr = [False] * 256
	for char in str:
		if (arr[ord(char)] == True):
			return False
		else:
			arr[ord(char)] = True
	return True


def main():
	str = "2" * 128 
	print unique(str)
main()