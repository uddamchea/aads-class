from sys import stdin

while True:
    jack, jill = list(map(int, stdin.readline().split()))
    if jack == 0 and jill == 0:
        break

    n = {}

    for _ in range(jack):
        cat_number = int(stdin.readline())
        n[cat_number] = True

    duplicate = 0

    for _ in range(jill):
        cat_number = int(stdin.readline())
        if cat_number in n:
            duplicate += 1

    print(duplicate)