def calculate(n, Mn, K):

    # G(n)
    c = 300800
    Gn = c+(c*n-Mn)*K

    # T(n)=G(n)/W
    W = 67
    Tn = Gn/W

    # AVR()
    MaxN = 670*10 ^ 6
    ans = (MaxN/Tn*8)/7

    return round(ans, 4)


k = 31  # https://www.timeanddate.com/date/durationresult.html?d1=25&m1=05&y1=2022&d2=&m2=&y2=
n = k-7
Mn = 118968+22886
K = 0.0025  # 1:400
# USD 1:1.4452

print('1 NKT = ', calculate(n, Mn, K))

result = int(input('How many do you have: '))
print(result, ' NKT = ', calculate(n, Mn, K)*result)
