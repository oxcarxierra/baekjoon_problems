import sys
while True:
    try: 
        g,t,a,d = map(int, sys.stdin.readline().split())
        if g <0:
            break
        x = int(g * t * (t-1) / 2)
        z = 1
        while True:
            if z >= g * a + d:
                break
            z *= 2
        x += z - 1
        y = z - g*a - d
        print(f"{g}*{a}/{t}+{d}={x}+{y}")
    except:
        break