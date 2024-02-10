n, m = map(int, input().split())

ip_names = {}

for _ in range(n):
    name, ip = input().split()
    ip += ';'
    ip_names[ip] = name

for _ in range(m):
    name, ip = input().split()
    print(f"{name} {ip} #{ip_names[ip]}")