from math import pi, sqrt
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

H  = sqrt(.75)*p
h_R=(H/4)/3             #Hoogte van de radius
m_8= H/8                #Hoogte van het snijpuntje moer
m_4= H/4                #Hoogte van het snijpuntje bout
h3 = (17/24)*H          #Bout snede diepte
H1 = (5/8)*H            #Moer snede diepte
R  = H/6                #Afrondings radius
d2 = d-(3/8)*H*2        #Flanken diameter
d3 = d-((H1+h_R)*2)     #Kern van moer
D1 = d-(H1*2)           #Kern van Bout
boor = d-p              #Boor diameter
hoek = 60               #Tophoek
doorsnede_volume = (pi/4)*pow(((d2+d3)/2),2)    #spanningsdoorsnede

print("\n"*2)
print("****************************************")
print("*** Schroefdraad M %3.0f x %2.2f        ***" % (d, p))
print("***                                  ***")
print("*** Bout snede diepte   h3= %8.3f ***" % (h3))
print("*** Moer snede diepte   H1= %8.3f ***" % (H1))
print("*** Afronding           R = %8.3f ***" % (R))
print("*** Flanken diameter d2/D2= %8.3f ***" % (d2))
print("*** Kern van moer       d3= %8.3f ***" % (d3))
print("*** Kern van bout       D1= %8.3f ***" % (D1))
print("*** Boor diameter       ø = %8.3f ***" % (boor))
print("*** Doorsnede volume      = %8.3f ***" % (doorsnede_volume))
print("****************************************")
print("\n"*2)
input("Druk op enter (STOP) >")
