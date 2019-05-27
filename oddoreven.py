def oddoreven(u):
  if u%2==0:
    return("Even")
  elif u%2!=0:
    return("Odd")
  else:
    return("Invalid Input")
u=int(input())
print(oddoreven(u))
