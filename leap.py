def le(ye):
  if ye%400==0 or ye%100!=0 and ye%4==0:
    print("yes")
  else:
    print("no")
le=int(input())
