# Crossing the road
print("Select the correct answer.")

print("1. Right side")
print("2. Left side")

print("Which side you should look at first when crossing the road?")
answer = input("Enter the correct number for the answer : ")

running = True
if running:
    if answer == '1':
        print("Yes, you are correct.")
        print("Ok, then which side you should look at when crossing the road?")
        a = input("Enter the correct number for the answer : ")
        if a == '2':
            print("Yes, you are correct.")
            print("You can safely cross the road!")
            running = False
        else:
            print("No, you are wrong.")
            print("You can't safely cross the road")
            running = False
    else:
        print("No, you are wrong.")
        print("You can't safely cross the road")
        running = False
