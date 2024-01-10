#Ý số 1 câu Q4
try:
    a = float(input("Nhập vào một số thực a: "))
    b = float(input("Nhập vào một số thực b: "))
    c = float(input("Nhập vào một số thực c: "))
except:
    print("Hãy nhập vào số thực!")
x = oct(int(a))
y = oct(int(b))
z = oct(int(c))
print("The octal number of decimal number ",int(a), "is ", x.replace("0o",""))
print("The octal number of decimal number ",int(b), "is ", y.replace("0o",""))
print("The octal number of decimal number ",int(c), "is ", z.replace("0o",""))
#Ý số 2 câu Q4
print("Làm tròn lấy tới chữ số thứ 2 sau dấu phẩy:")
print(round(a,2))
print(round(b,2))
print(round(c,2))