name = "Akash"
age = 27
height = 5.9
is_preparing_for_IT = True
print(name,age,height,is_preparing_for_IT)

skills = ["Python", "SQL","ML"]
for skill in skills:
    print("I am Learning",skill) 

# A function that greets the user
def greet(user):
    return f"Welcome, {user}! Let's learn Python."

print(greet("Akash"))

marks = 75
if marks>=60:
    print("You Passed")
else:
    print("Try again")
