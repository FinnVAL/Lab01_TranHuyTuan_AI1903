#Ý số 1 câu Q3
try:
    a = float(input("Nhập vào số thực a: "))
    b = float(input("Nhập vào số thực b: "))
    c = float(input("Nhập vào số thực c: "))
    x = float(input("Nhập vào số thực x: "))
except:
    print("Hãy nhập vào số thực!")
#Ý số 2 câu Q3
S1 = a*(x**2)+b*x+c
print("S1 = ",S1)
#Ý số 3 câu Q3
import math
if (b**2 - 4*a*c) > 0:
    S2 = math.sqrt(b**2 - 4*a*c)
else:
    S2 = 0
print("S2 = ", S2)
#Ý số 4 câu Q3
try:
    a = float(input("Nhập vào số thực a: "))
    b = float(input("Nhập vào số thực b: "))
    c = float(input("Nhập vào số thực c: "))
except:
    print("Hãy nhập vào số thực!")
if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
    print("3 cạnh a,b,c có thể là 3 cạnh của 1 tam giác!")
else:
    print("3 cạnh a,b,c không thể là 3 cạnh của 1 tam giác!")
#Ý số 5 câu Q3
if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
    ChuVi = a + b +c
    print("Chu vi của tam giác đó là: ", ChuVi)
    p = ChuVi / 2
    DienTich = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Diện tích của tam giác đó là: ",DienTich)