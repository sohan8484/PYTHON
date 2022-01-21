weight = float(input("weight: "))
unit = input("(K)gm or (L)bs ")
if unit.upper() == "K":
    converted = weight/0.45
    print("weight in lbs "+ str(converted))
elif unit.upper() == "L":
    converted = weight*0.45
    print("weight in kgs "+ str(converted))
else:
    print("please enter only k or l")