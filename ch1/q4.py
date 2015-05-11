def q4(str):
	i = 0
	while True:
		if (i == len(str)):
			break
		if (str[i] == " "):
			str = str[:i] + "%20" + str[i+1:]
		i += 1
	print str

def main():
	str = "P U A"
	q4(str)
main()