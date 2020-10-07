'''
Generering av lösenord: Generera n lösenord med tre tecken före och efter som
är bokstäver och 4 tecken i mitten som är slumpade siffror
'''

from random import randint

def slumptext(start_chr):
    triple = ''
    for position in range(1,4):
        triple += chr(randint(start_chr, start_chr+25))
    return triple

def slumpsiffra():
    return str(randint(1000, 10000))

def losenord():
    prefix = slumptext(ord('a'))
    suffix = slumptext(ord('a'))
    nums = slumpsiffra()
    return prefix+nums+suffix

pwds = int(input('Hur många lösenord vill du ha?\n'))
for i in range(1, pwds+1):
    print(losenord())
