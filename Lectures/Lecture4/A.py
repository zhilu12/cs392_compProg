p = [2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 43, 47]

count = 0

for num in p:
  print(num, flush=True)
  ans = input()
  if ans == "yes":
    count += 1
    if count == 2:
      break
    
if count == 2:
  print("composite", flush = True)
else:
  print("prime", flush = True)