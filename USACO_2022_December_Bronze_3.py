
def solve(d):
    while d and d[0] and d[0][0]:
        sigdig = 0
        char = 0
        for digit in range(len(d[0][0])):
            zero = None
            one = None
            for itm in d:
                if itm[0][digit] == '0':
                    if zero is not False:
                        if not zero:
                            zero = itm[1]
                        elif itm[1] != zero:
                            zero = False
                else:
                    if one is not False:
                        if not one:
                            one = itm[1]
                        elif itm[1] != one:
                            one = False
            if zero:
                sigdig = digit
                char = '0'
                break
            elif one:
                sigdig = digit
                char = '1'
                break
        else:
            return False
        tmp = []
        for itm in d:
            if itm[0][sigdig] != char:
                tmp.append(itm)
        d = tmp
    return True

for tc in range(int(input())):
    input()
    n,m = input().split()
    n,m = int(n),int(m)
    data = [input().split() for k in range(m)]
    data.sort()
    if solve(data):
        print('OK')
    else:
        print('LIE')
