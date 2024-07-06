marks1  = int(input(" enter marks 1: "))
marks2  = int(input(" enter marks 2: "))
marks3  = int(input(" enter marks 3: "))

total_percentage = ( marks1 + marks2 + marks3)/300 * 100
if (total_percentage >= 40):
    print("pass" ,total_percentage)
else:
    print( " try again next time", total_percentage)