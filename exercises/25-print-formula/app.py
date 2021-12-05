
D = input()
def QCDH(d):
    C = 50
    H = 30
    Q = ",".join(str(round(((2 * C * float(n)) / H)**0.5)) for n in d.split(","))

    return Q

print(QCDH(D))