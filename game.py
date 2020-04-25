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