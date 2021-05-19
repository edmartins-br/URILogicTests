import math

ammount = input().split('.')

note = int(ammount[0])
inputCoin = (float((ammount[1]))) / 100

print(note)
print(inputCoin)

num = [100, 50, 20, 10, 5, 2]
baseCoins = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

for i in range(0, len(num)):
    if num[i] == 100:
        cem = (note // 100)
        note = note - (cem*100)   

    if num[i] == 50:
        cinquenta = (note // 50)
        note = note - (cinquenta*50)  

    if num[i] == 20:
        vinte = (note // 20)
        note = note - (vinte*20)  
              
    if num[i] == 10:
        dez = (note // 10) 
        note = note - (dez*10)  

    if num[i] == 5:
        cinco = (note // 5)
        note = note - (cinco*5)  
              
    if num[i] == 2:
        dois = (note // 2)
        note = note - (dois*2)     

for c in range (0, len(baseCoins)):
    if baseCoins[c] == 1:
        um = (inputCoin // 1)
        inputCoin = inputCoin - (um * 1)

    if baseCoins[c] == 0.50:
        cinquentaCents = (inputCoin // 0.50)
        inputCoin = inputCoin - (cinquentaCents * 0.50)      
    
    if baseCoins[c] == 0.25:
        vinteCincoCents = (inputCoin // 0.25)
        inputCoin = inputCoin - (vinteCincoCents * 0.25)
    
    if baseCoins[c] == 0.10:
        dezCents = (inputCoin // 0.10)
        inputCoin = inputCoin - (dezCents * 0.10)

    if baseCoins[c] == 0.05:
        cincoCents = (inputCoin // 0.05)
        inputCoin = inputCoin - (cincoCents * 0.05)    
        print(inputCoin)

    if baseCoins[c] == 0.01:
        umCent = (inputCoin // 0.01)   
        print(umCent)           
        inputCoin = inputCoin - (umCent * 0.01)  

print("NOTAS:")
print('''{} nota(s) de R$ 100,00
{} nota(s) de R$ 50,00
{} nota(s) de R$ 20,00
{} nota(s) de R$ 10,00
{} nota(s) de R$ 5,00
{} nota(s) de R$ 2,00'''.format(cem, cinquenta, vinte, dez, cinco, dois))   

print("MOEDAS:")
print('''{} moeda(s) de R$ 1,00
{} moeda(s) de R$ 0.50
{} moeda(s) de R$ 0.25
{} moeda(s) de R$ 0.10
{} moeda(s) de R$ 0.05
{} moeda(s) de R$ 0.01'''.format(int(um), int(cinquentaCents), int(vinteCincoCents), int(dezCents), int(cincoCents), math.ceil(umCent)))  