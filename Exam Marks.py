print("Enter Marks Obtained in 4 subjects:")
Math = int(input("math:"))
English = int(input("English:"))
Science = int(input("Science:"))
Hindi = int(input("Hindi:"))

sum = Math + English + Science + Hindi
perc = (sum/400) * 100
print ("Percentage Score", perc)