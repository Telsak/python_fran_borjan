# På ett gym kan man antingen köpa ett årskort eller köpa en biljett vid
# varje besök. Skriv ett program som läser in priset för ett årskort,
# priset för en biljett samt antal gånger man planerar att besöka gymmet
# under ett år. Därefter ska programmet ange om det lönar sig att köpa
# årskort eller inte.

gymkort = int(input('Hur mycket kostar gymkortet? '))
enkelbiljett = int(input('Hur mycket kostar en enkelbiljett? '))
gympass = int(input('Hur många gånger ska du träna? '))

kostnad = enkelbiljett * gympass
if kostnad > gymkort:
    print(f'Att träna {gympass} gånger kostar {kostnad} kr. \
            \nDu sparar pengar om du köper ett gymkort för {gymkort} kr istället.')
elif kostnad == gymkort:
    print('Det kostar lika mycket att köpa enkelbiljetter som ett gymkort.\
            \nKöp ett gymkort dock då det är mer bekvämt att göra så!')
else:
    print(f'Att träna {gympass} gånger kostar {kostnad} kr. \
            \nEtt gymkort kostar {gymkort} kr. \
            \nDu sparar pengar om du köper enkelbiljetter.')

