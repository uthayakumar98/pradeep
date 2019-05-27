def le(ye):
  if ye%400==0 or ye%100!=0 and ye%4==0:
    a="yes"
  return a
  else:
    b="no"
  return b
ye=int(input())
print(le(ye))
