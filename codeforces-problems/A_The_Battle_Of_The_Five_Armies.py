damage = list(map(int, input().split()))
soldiers = list(map(int, input().split()))

bilbo_side = 0
other_side = 0

for i in range(3):
    bilbo_side += (damage[i]*soldiers[i])

other_side += (damage[-1]*soldiers[-1]) + (damage[-2]*soldiers[-2])

if bilbo_side > other_side:
    print("WIN")
elif bilbo_side < other_side:
    print("LOSE")
else:
    print("DRAW")