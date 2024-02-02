def can_sell_ticket(n, bills):
    cash_25 = 0 
    cash_50 = 0

    for b in bills:
        if b == 25:
            cash_25 += 1
        elif b == 50:
            if cash_25 == 0:
                return "NO"
            
            cash_25 -= 1
            cash_50 += 1
        elif b == 100:
            if cash_50 >= 1 and cash_25 >=1:
                cash_50 -= 1
                cash_25 -= 1
            elif cash_25 >= 3:
                cash_25 -= 3
            else:
                return "NO"
    
    return "YES"

n = int(input())
bills = list(map(int,input().split()))

print(can_sell_ticket(n, bills))