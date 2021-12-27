q=int(input("enter the number:"))
result=""
while q>0:
  r=q%2
  result=str(r)+result
  q//=2
print(result)
