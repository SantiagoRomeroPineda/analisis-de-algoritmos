def posi(suma, numeroSumar,n):
  suma+=numeroSumar
  if suma > n:
    return 0
  if suma ==n:
    print(suma)
    return 1
  return posi(suma,1,n) +posi(suma,3,n) + posi(suma,4,n)

print(posi(0,0,7))