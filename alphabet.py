a=input()
a.lower()
b=['a','e','i','o','u']
if a in b:
  print("Vowel")
elif a not in b:
  print("Consonant")
else:
  print("Invalid")
