import os
if os.path.exists("123.txt"):
  os.remove("123.txt")
else:
   print("The file is not  exist!")

try:
  os.rmdir("123")
except:
  print("The folder is not empty or the folder is not exists!")
