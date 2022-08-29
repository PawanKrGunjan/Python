
def is_valid(ip):
	# Splitting by "."
	ip = ip.split(".")
	# Checking for the corner cases
	for i in ip:
		if (len(i) > 3 or int(i) < 0 or
						int(i) > 255):
			return False
		if len(i) > 1 and int(i) == 0:
			return False
		if (len(i) > 1 and int(i) != 0 and
			i[0] == '0'):
			return False
	return True

def genIp(s):
    # Code Here
	ip = s
	l=[]
	L = len(s)
	if L < 4 or L > 4*3:
		l.append(-1)
	else:
		for i in range(1, L-2):
			for j in range(i+1, L-1):
				for k in range(j+1, L):
					ip = ip[:k] + "." + ip[k:]
					ip = ip[:j] + "." + ip[j:]
					ip = ip[:i] + "." + ip[i:]

					if is_valid(ip):
						l.append(ip)
					ip = s
	return l


print(genIp("25525511135"))
