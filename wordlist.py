list=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

for i in range(0,26):
 for j in range(0,26):
  for k in range(0,26):
   for l in range(0,26):
    for m in range(0,26):
      r=list[i]+list[j]+list[k]+list[l]+list[m]
      print(r)
