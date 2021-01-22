# I en triangel kan man beteckna sidorna med a, b och c. Om man känner till längden
# för sidorna a och b samt vinkeln alfa mellan dessa sidor så kan man räkna ut längden
# av sidan c med formeln c = sqrt(a**2 + b**2 - 2*a*b * cos(alfa)). Skriv ett program
# som läser in längderna på två sidor i en triangel och vinkeln mellan sidorna.
# Programmet ska avgöra om triangeln är liksidig (alla sidor lika), likbent (två sidor
# lika) eller oliksidig (inga sidor lika)
# 
# När man jämför float för att se om de är lika bör man inte använda == direkt eftersom
# talen lagras i en approximativ form. Beräkna istället skillnaden mellan talen och
# undersök om absolutvärdet av denna skillnad är mindre än ett litet tal, t.ex 10^-10

from math import cos, radians, sqrt, pow

def compare_floats(a, b):
    if abs(a-b) < 10**-10:
        return True
    else:
        return False

def count_hypotenuse(a, b, angle):
    squarethis = ( a**2 + b**2 ) - (( 2 * a * b ) * cos(radians(angle)))
    return sqrt(squarethis)

# checks two float values and determines if they are essentially the same
# (less than 10^-10 difference)
def compare_sides(a, b):
    state = True if abs(a - b) < pow(10, -10) else False
    return state

def find_triangle_type(a, b, c):
    if compare_sides(a, b) == True:
        if compare_sides(a, c) == True:
            return 'Triangeln är liksidig!'
        else:
            return 'Triangeln är likbent!'
    elif compare_sides(b, c) == True or compare_sides(a, c) == True:
        return 'Triangeln är likbent!'
    else:
        return 'Triangeln är oliksidig'

a = float(input('a: '))
b = float(input('b: '))
alfa = float(input('angle: '))
c = count_hypotenuse(a, b, alfa)
print(find_triangle_type(a, b, c))
