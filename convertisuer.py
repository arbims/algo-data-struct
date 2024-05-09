x = int(input())

for i in range(x):
    s = input()
    n, u = s.split(' ')
    if (u == 'm'):
        r = float(n) / 0.3048
        print(f"{r:.6f} p")
    if (u == 'g'):
        r = float(n) * 0.002205
        print(f"{r:.6f} l")
    if (u == 'c'):
        r = float(n) * 1.8 + 32
        print(f"{r:.6f} f")