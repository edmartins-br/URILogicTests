#! /usr/bin/python3

ageDays = int(input())

anos = ageDays // 365
ageDays = (ageDays - (anos * 365))

meses = ageDays // 30
ageDays = (ageDays - (meses * 30))

dias = ageDays

print('''{} ano(s)
{} mes(es)
{} dia(s)'''.format(anos, meses, dias))