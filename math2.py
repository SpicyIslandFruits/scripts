import math

print("ある数のn乗根を2分探索法で求める関数です。試行回数は最大2000回。")
x = int(input("x : "))
n = int(input("n : "))

y_min = 0
y_max = 10 ** 300

for num in range(0, 2000):
    mid = (y_min + y_max) // 2
    dy = pow(mid, n)
    if dy == x:
        print(mid)
        break
    elif dy > x:
        y_max = mid
        print("大きすぎ")
    elif dy < x:
        y_min = mid
        print("小さすぎ")
    digit = int(math.log10(mid) + 1)
    print(str(num) + ": " + str(digit) + "桁")