a=input()
a.lower()
b=['a','e','i','o','u']
c="abcdefghijklmnopqrstuvwxyz"
if a in b:
  print("Vowel")
elif a in c:
  print("Consonant")
else:
  print("Invalid")
