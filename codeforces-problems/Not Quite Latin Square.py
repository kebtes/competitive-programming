results = []
n = int(input())

for i in range(n):
    row_1 = list(input())
    row_2 = list(input())
    row_3 = list(input())

    rows = [row_1,row_2,row_3]

    for i in range(3):
        if "?" in rows[i]:
            for j in range(len(rows[i])):
                if rows[i][j] == "?":
                    column = [row_1[j],row_2[j],row_3[j]]
                    if "A" not in rows[i] and "A" not in column:
                        results.append("A")
                    elif "B" not in rows[i] and "B" not in column:
                        results.append("B")
                    else:
                        results.append("C")
                    break

for r in results:
    print(r)
