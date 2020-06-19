userpass = {
  "Nesh" : "Ne$h",
  "Roblox": "r0blox",
  "Saver" : "$@ver"
}

username = input("Enter your name:  ")

if username in "Nesh" or username in "R0blox" or username in "Saver":
  def password_manager():
    password = input('Enter your password:  ')
    if password in "Ne$h" or password in "r0blox" or password in "$@ver":
      print("Yahoo")
    else:
      print("OOF")
  password_manager()
else:
  print('bad')