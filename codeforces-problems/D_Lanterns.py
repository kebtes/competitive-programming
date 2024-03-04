from collections import defaultdict
def solve():
    n = int(input())
    counter = 0

    dicts = defaultdict(list)

    for _ in range(n):
        a, b = map(int, input().split())
        dicts[a].append(b)

    for i, j in dicts.items():
        j.sort(reverse=True)

        counter += sum(j[:i])

    print(counter)


if __name__ == '__main__':
    for _ in range(int(input())):
        solve()