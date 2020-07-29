from math import pi
from pcinput import getFloat, getInteger

print ("**************************************")
print ("*** Calculator voor               ****")
print ("*** Metrische schroefdraad (ISO)  ****")
print ("**************************************")
print ("\n"*1) 
print ("Voer voor metrisch schroefdraad volgende gegevens in.")
print()

diameter = getInteger("Geef de diameter:> ")
spoed = getFloat( "Geef de spoed:> " )

d = diameter
p = spoed

h3 = 0.6134*p       # Bout snede diepte
H1 = 0.5413*p       # Moer snede diepte
R  = 0.1443*p       # Afronding
d2 = d-0.6495*p     # Flanken diameter
d3 = d-1.2269*p     # Kern van moer
D1 = d-1.0825*p     # Kern van Bout
boor = d-p          # Boor diameter
hoek = 60           # Tophoek
doorsnede_volume = (pi/4)*pow(((d2+d3)/2), 2)

print("\n"*2)
print("**************************************")
print("*** Schroefdraad M %3.0f x %2.2f      ***" % (d, p))
print("***                                ***")
print("*** Bout snede diepte h3= %8.3f ***" % (h3))
print("*** Moer snede diepte H1= %8.3f ***" % (H1))
print("*** Afronding         R = %8.3f ***" % (R))
print("*** Flanken diameter  d2= %8.3f ***" % (d2))
print("*** Kern van moer     d3= %8.3f ***" % (d3))
print("*** Kern van bout     D1= %8.3f ***" % (D1))
print("*** Boor diameter     ø = %8.3f ***" % (boor))
print("*** Doorsnede volume    = %8.3f ***" % (doorsnede_volume))
print("**************************************")
print("\n"*2)
