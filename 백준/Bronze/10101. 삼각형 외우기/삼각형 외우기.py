tri = [int(input()) for _ in range(3)]

if sum(tri) != 180:
    print("Error")
else:
    if tri[0] == tri[1] == tri[2]:
        print("Equilateral")
    elif tri[0] == tri[1] or tri[0] == tri[2] or tri[1] == tri[2]:
        print("Isosceles")
    else:
        print("Scalene")
