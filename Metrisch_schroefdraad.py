from math import pi
from pcinput import getFloat, getInteger

print("\n"*5)
print("Voer voor metrisch schroefdraad de gegevens in.")
print()

diameter = getInteger("Geef de diameter: ")
spoed = getFloat( "Geef de spoed: " )

d = diameter
p = spoed

h3 = round(0.6134*p, 2)    # Bout snede diepte
H1 = round(0.5413*p, 2)    # Moer snede diepte
R = round(0.1443*p, 2)     # Afronding
d2 = round(d-0.6495*p, 2)  # Flanken diameter
d3 = round(d-1.2269*p, 2)  # Kern van moer
D1 = round(d-1.0825*p, 2)  # Kern van Bout
boor = d-p                 # Boor diameter
hoek = 60                  # Tophoek
doorsnede_volume = round((pi/4)*pow(((d2+d3)/2), 2), 0)


#print (d,p,d2,d3,D1,h3,H1,R,doorsnede_volume,boor)

print("\n"*2)
print("**************************************")
print("*** Schroefdraad M %3.0f x %2.2f      ***" % (d, p))
print("***                                ***")
print("*** Bout snede diepte h3= %8.2f ***" % (h3))
print("*** Moer snede diepte H1= %8.2f ***" % (H1))
print("*** Afronding         R = %8.2f ***" % (R))
print("*** Flanken diameter  d2= %8.2f ***" % (d2))
print("*** Kern van moer     d3= %8.2f ***" % (d3))
print("*** Kern van bout     D1= %8.2f ***" % (D1))
print("*** Boor diameter       = %8.2f ***" % (boor))
print("*** Doorsnede volume    = %8.2f ***" % (doorsnede_volume))
print("**************************************")
print("\n"*2)
