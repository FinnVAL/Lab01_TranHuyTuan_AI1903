Số_hiện_tại = 0
Số_trước_đó = 0
print('Printing current and previous number sum in a range(10)')
for i in range(0, 10):
    Tổng = Số_hiện_tại + Số_trước_đó
    print("Current number: ", Số_hiện_tại, " Previous number: ", Số_trước_đó, " Sum: ",Tổng)
    Số_trước_đó = Số_hiện_tại
    Số_hiện_tại = i + 1