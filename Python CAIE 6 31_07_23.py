# data types
int #  integer 1,2,3
float # float 1.23,2.34
str #string is text


var = "myp3" # variable is a bucket where we put a data (string, number)
print(type(var))

# python is a loosely typed language
print("12.3")
print(type("12.3"))
print(type(12.3))

# binary data types (discuss later)

# condional statements
# ramu wants to have a ps5
marks_ramu=40
if(marks_ramu>90):
    print("Ramu will get a ps5")
elif(marks_ramu<90 and marks_ramu>70):
    print("Ramu will be gifted with a samosa and chutni")
elif(marks_ramu<70 and marks_ramu>50):
    print("Ramu will be eating pizza with only pinapples")
else:
    print("Ramu will be restricted from using electronic devices")

n=20

if(n % 2 == 1): #odd
    print("Weird")
else:
    if(n>2 and n<5):
        print("Not Weird")
    elif(n>6 and n<20):
        print("Weird")
    else:
        print("Not Weird")

print(19/4)




