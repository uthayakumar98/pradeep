def le(ye):
  if ye%400==0 or ye%100!=0 and ye%4==0:
    return("yes")
  else:
    return("no")
ye=int(input())
print(le(ye))
