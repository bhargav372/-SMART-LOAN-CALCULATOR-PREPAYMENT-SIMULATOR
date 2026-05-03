def emi_calc(p, r, t):
    r, n = r/12/100, t*12
    emi = p/n if r==0 else p*r*(1+r)**n/((1+r)**n-1)
    return round(emi,2), round(emi*n,2), round(emi*n-p,2)


def schedule(p, r, t):
    r, n = r/12/100, t*12
    emi,_,_ = emi_calc(p, r*12*100, t)
    b = p
    for m in range(1,4):  # only first 3 months
        i = round(b*r,2)
        pr = round(emi-i,2)
        b = round(b-pr,2)
        print(m, emi, pr, i, max(b,0))


def prepay(p, r, t, extra):
    r, n = r/12/100, t*12
    emi,_,oi = emi_calc(p, r*12*100, t)
    b, ti, m = p, 0, 0
    while b>0:
        i = b*r
        ti += i
        b -= (emi-i+extra)
        m += 1
    return round(oi-ti,2), n-m


# -------- MAIN --------
p = float(input("Loan: "))
r = float(input("Rate: "))
t = int(input("Years: "))

emi, total, interest = emi_calc(p, r, t)
print("\nEMI:", emi, "Total:", total, "Interest:", interest)

print("\nFirst 3 Months:")
schedule(p, r, t)

extra = float(input("\nExtra Payment: "))
saved_i, saved_m = prepay(p, r, t, extra)

print("Saved Interest:", saved_i, "Months Saved:", saved_m)
