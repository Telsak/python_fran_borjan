# En kommun har gjort följande prognos för befolkningsutvecklingen
# de närmaste åren:
#
# - Vid början av år 2019 hade kommunen 26000 invånare
# - Antalet födda och avlidna under ett år uppskattas vara 0.7%
#   respektive 0.6% av befolkningen vid årets början.
# - Antalet inflyttade och antalet utflyttade uppskattas till 300
#   respektive 325 varje år.
#
# Skriv ett program som beräknar kommunens uppskattade invånarantal
# i början av ett visst år. Vilket år det gäller ska läsas in som
# indata till programmet.

def year_prognosis(year):
    population = 26000
    for i in range(abs(year-2019)):
        population *= 1.1
        population -= 25
    return int(population)


year = int(input("Ange årtal för prognos (2020 +): "))
pop = year_prognosis(year)
print(f'Det finns {pop} invånare i kommunen år {year}.')
