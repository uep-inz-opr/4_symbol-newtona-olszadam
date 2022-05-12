import math as math
liczby_spacja = input()

numbers = []
for word in liczby_spacja.split():
   if word.isdigit():
      numbers.append(int(word))

n = numbers[0]
k = numbers[-1]
roznica = n - k

nfactorial = math.factorial(n)
kfactorial = math.factorial(k)
roznicafactorial = math.factorial(roznica)
iloraz = kfactorial * roznicafactorial


print(nfactorial/iloraz)
