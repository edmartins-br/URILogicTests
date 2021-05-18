num = [100, 50, 20, 10, 5, 2, 1]
note = int(input())
print(note)
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
    if num[i] == 1:
        um = (note // 1) 
        note = note - (um*1)         

print('''{} nota(s) de R$ 100,00
{} nota(s) de R$ 50,00
{} nota(s) de R$ 20,00
{} nota(s) de R$ 10,00
{} nota(s) de R$ 5,00
{} nota(s) de R$ 2,00
{} nota(s) de R$ 1,00'''.format(cem, cinquenta, vinte, dez, cinco, dois, um))   