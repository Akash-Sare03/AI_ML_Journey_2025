
age = 20
if age >=20:
    print("You are an Adult.")
else:
    print("You are a minor.")

for i in range(5):
    print("Number:", i)


count = 0
while count < 3:
    print("Count is:", count)
    count += 1

for i in range(10):
    if i==5:
        break
    if i % 2==0:
        continue
    print("Odd Numbers:", i)
    
