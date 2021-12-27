q=int(input("enter the number:"))
result=""
while q>0:
  r=q%2
  result+=str(r)
  q//=2
print(result[::-1])
