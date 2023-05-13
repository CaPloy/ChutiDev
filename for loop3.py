#สูตรคูณ 
for x in range(12):
    for i in range(12):
        print(x+1, "X", i+1, "=", (x+1)*(i+1))
    break           #หยุดรอบการทำงานเลยไม่สนหลังจากนี้
for val in "hello":
    if val=="l":
        continue    #คือข้ามรอบการทำงานของ "l" ไปเลย
    print(val)
print("The end")