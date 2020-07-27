# n_digit
def n_digit(num, digit):
    numlist = []
    numdict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while (1):
        num_ = int(num % digit)
        if num_ < 10:
            num_ = str(int(num % digit))
        else:
            num_ = numdict[num_]
        numlist.append(num_)
        num = (num - num % digit) / digit
        if num == 0: break
    numlist.reverse()
    output = "".join(numlist)
    return output


def solution(n, t, m, p):
    numlist = ""
    for i in range(m * t):
        num = n_digit(i, n)
        numlist += num

    answer = ''
    for t_ in range(t):
        answer = answer + numlist[(p - 1) + t_ * m]
    return answer