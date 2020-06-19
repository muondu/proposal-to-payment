earlycamp = {("earlycampAdmin") : "ec12!"}
azizi = {("azizAdmin") : "9934"}
twitter = {("twitterAdmin") : "t956"}
def start()
a = input("Hi. Are you an (a) employer or b(employee):  ")
if a == "a":
  b = input("Input your username here:  ")
  c = input("Enter your password:  ")
  if (b == earlycamp and c == earlycamp) or (b == azizi and c == azizi) or (b ==  twitter and c == twitter):
    print("Welcome")
  else:
    print()
elif a == "b":
  print("We will come back to you latter.")