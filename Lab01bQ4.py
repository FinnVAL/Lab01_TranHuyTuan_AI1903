#Ý số 1 câu Q4
try:
    a = float(input("Nhập vào một số thực a: "))
    b = float(input("Nhập vào một số thực b: "))
    c = float(input("Nhập vào một số thực c: "))
except:
    print("Hãy nhập vào số thực!")
max = a
if b > max:
    max = b
if c > max:
    max = c
print("Số lớn nhất trong ba số a, b, c là: ", max)
min = a
if b < min:
    min = b
if c < min:
    min = c
print("Số bé nhất trong ba số a, b, c là: ", min)
#Ý số 2 câu Q4
if a <= b <= c:
    print(a, b, c)
elif a <= c <= b:
    print(a, c, b)
elif b <= a <= c:
    print(b, a, c)
elif b <= c <= a:
    print(b, c, a)
elif c <= a <= b:
    print(c, a, b)
else:
    print(c, b, a)