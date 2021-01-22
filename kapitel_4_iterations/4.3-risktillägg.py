# På en mycket farlig arbetsplats erbjuds man följande lön: Första
# dagen tjänare man ett öre och sedan fördubblas lönen varje dag.
# Skriv ett program som räknar ut hur länge man behöver arbeta
# för att tjäna ihop 10 miljoner kronor.

salary = 0.001
days = 1
print(days, salary)
while salary < 10000000:
    salary *= 2
    days += 1
    print(days, salary)
print(f'Det tog {days} dagar för att tjäna ihop {int(salary)} SEK!')
