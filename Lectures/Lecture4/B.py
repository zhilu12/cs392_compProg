l, r = 1, 10**9

while l != r:
  guess = (l + r) // 2
  print("?", guess, flush = True)
  ans = input()
  
  if ans == "YES":
    l = guess + 1
  else:
    r = guess
    

print("!", r, flush = True)