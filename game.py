def checkNumber(x):
    if x.isdigit() and (int(x[0]) != 0):	#проверка строки на числа, ненулевая первая цифра
        for i in x:
            if x.count(i) == 1:		#проверка на повторение цифр
                continue
            else:
                return False
        return True   
    else:
        return False

def gameLow(original, testCase):
	if (checkNumber(original)*checkNumber(testCase) == 1) and (len(original) == len(testCase)):
		out = [0 for i in original]
		for i in range(len(original)):
			if original[i] == testCase[i]:
				out[i] = 1
			elif original.count(testCase[i]) > 0:
				out[i] = 0
			else:
				out[i] = -1
		return out			
	else:
		return ('Input incorrect.')

def gameMedium(original, testCase):
	if (checkNumber(original)*checkNumber(testCase) == 1) and (len(original) == len(testCase)):
		out = [0 for i in original]
		for i in range(len(original)):
			if original[i] == testCase[i]:
				out[i] = 1
			elif original.count(testCase[i]) > 0:
				out[i] = 0
			else:
				out[i] = -1
		return [out.count(1),out.count(0)]			
	else:
		return ('Input incorrect.')

def gameHard(original,testCase):
	if (checkNumber(original)*checkNumber(testCase) == 1) and (len(original) == len(testCase)):
		out = [0 for i in original]
		for i in range(len(original)):
			if original[i] == testCase[i]:
				out[i] = 1
			elif original.count(testCase[i]) > 0:
				out[i] = 0
			else:
				out[i] = -1
		return [out.count(1)]			
	else:
		return ('Input incorrect.')		