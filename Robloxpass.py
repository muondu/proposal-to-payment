data = {
  "Nesh" : "Ne$h",
  "Roblox": "r0blox",
  "Booga Booga" : "$@ver"
}
username = input("Enter your username:  ")
password = input("Enter your password:  ")

if password != data:
  print("Wrong password.")
elif username != data:
  print("Wrong username")
elif password == data[username]:
  print("Welcome.")




