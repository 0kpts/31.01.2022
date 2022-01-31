def reverseWords(teksts: str):
  sar1 = teksts.split()
  if len(sar1) > 1:
    teksts = ""
    for elements in reversed(sar1):
      teksts += elements
  
  else:
    teksts = "Pārāk iss teikums!"
  return teksts

a = reverseWords("Kak Zhitj")
print(a)