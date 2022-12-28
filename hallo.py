import random

AantalPersonen = 10
AantalSpeelDagen = 4
FlightsPerDag = 4
MaximaleFlightGrote = 4
MinimaleFlightGrote = 3

Persoon =[]
FlightIndeling =[]
TestRemain = AantalPersonen % MaximaleFlightGrote
TestDevide = TestRemain / MinimaleFlightGrote

FlightVerdeling=[4,4,3,3] # testing

J = { 
    "nummer" : 1,
    "naam" : "",
    "hcp" : "",
    "email" : "",
    "met_wie_gespeeld" : [],
    "WelkeFlight" : [],
    "WelkeDag" : []
}

P = {
    "Dag" : 0,
    "Flight" : 0,
    "Grote" : 0,
    "Personen" : []
}


def WieOhWie(Dag,lid,nummer, Grote):
    Dag=Dag+1
    FlightIndeling.append(P)
    FlightIndeling[Dag].update({"Dag": Dag})
    FlightIndeling[Dag].update({"Flight": nummer})
    FlightIndeling[Dag].update({"Grote": Grote})
    for i in range(Grote):
        GaDoor = True
        Tijd = 1001
        while GaDoor:
            Kandidaat = random.randint(0, 9)            
            if not Dag in Persoon[Kandidaat]["WelkeDag"]:
                Tijd = Tijd - 1
                if Tijd <= 0:
                    GaDoor = False
                    print("Kandidaat : ", Kandidaat, "niet gelukt in " , FlightIndeling[Dag])
                if not Kandidaat in Persoon[Kandidaat]["met_wie_gespeeld"]:
                    Persoon[Kandidaat]["met_wie_gespeeld"].append(Kandidaat)
                    Persoon[Kandidaat]["WelkeFlight"].append([nummer])
                    Persoon[Kandidaat]["WelkeDag"].append([Dag])
                if not Kandidaat in FlightIndeling[Dag]["Personen"]:
                    FlightIndeling[Dag]["Personen"].append(Kandidaat)
                    GaDoor = False
                #print("Kandidaat : ",Kandidaat)


FlightIndeling.append(P)
Persoon.append(J)
for x in range(AantalPersonen):
    Persoon.append(J)
    Persoon[x].update({"nummer": x})
    Persoon[x].update({"naam": x+1})
#    print("Persoon = ",Persoon[x])

for Dag in range(AantalSpeelDagen ):
    nummer = 0    
    for Grote in FlightVerdeling:    
        nummer = nummer + 1
 #       print("flight z", z , " Aantal in die flight ", Dag + 1)
        for lid in range(Grote):
#            print("Dag: ", Dag ,"flights", z , " Aantal in die flight ", x, "nummer ", nummer)
            WieOhWie(Dag,lid,nummer,Grote)
print(FlightIndeling)








