import os
path = r'AI'
for root, dirs, files in os.walk(path):
  for file in files:
    print(os.path.join(root,file))
print()



