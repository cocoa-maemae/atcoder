S = input()
m = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
if S[:2] in m and S[2:] in m:
  print("AMBIGUOUS")
elif S[:2] not in m and S[2:] in m:
  print("YYMM")
elif S[:2] in m and S[2:] not in m:
  print("MMYY")
else:
  print("NA")
