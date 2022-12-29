import random

AantalPersonen = 14
AantalSpeelDagen = 4
FlightsPerDag = 4
MaximaleFlightGrote = 4
MinimaleFlightGrote = 3

Persoon =[]
FlightIndeling =[]
TestRemain = AantalPersonen % MaximaleFlightGrote
TestDevide = TestRemain / MinimaleFlightGrote

FlightVerdeling=[4,4,3,3] # testing

def AppendFlight():
    FlightIndeling.append({
        "Dag" : 0,
        "Flight" : 0,
        "Grote" : 0,
        "Personen" : []
    })
def AppendPersoon():
    Persoon.append({ 
        "nummer" : 1,
        "naam" : "",
        "hcp" : "",
        "email" : "",
        "met_wie_gespeeld" : [],
        "WelkeFlight" : [],
        "WelkeDag" : []
})

def WieOhWie(Dag,lid,nummer, Grote):
    Dag=Dag+1
    print(Dag,lid,nummer,Grote)
    print("size :   " , len(FlightIndeling))
    if len(FlightIndeling) == Dag:
        AppendFlight()
        FlightIndeling[Dag].update({"Dag": Dag})
        FlightIndeling[Dag].update({"Flight": nummer})
        FlightIndeling[Dag].update({"Grote": Grote})
    GaDoor = True
    Tijd = 1001
    while GaDoor:
        Kandidaat = random.randint(0, 13)            
        if Dag not in Persoon[Kandidaat]["WelkeDag"]:
            Tijd = Tijd - 1
            if Tijd <= 0:
                GaDoor = False
                print("Kandidaat : ", Kandidaat, "niet gelukt in " , FlightIndeling[Dag])
            if Kandidaat not in Persoon[Kandidaat]["met_wie_gespeeld"]:
                Persoon[Kandidaat]["met_wie_gespeeld"].append(Kandidaat)
                Persoon[Kandidaat]["WelkeFlight"].append([nummer])
                Persoon[Kandidaat]["WelkeDag"].append([Dag])
                GaDoor = False
                #print(Persoon)
            if Kandidaat not in FlightIndeling[Dag]["Personen"]:
                FlightIndeling[Dag]["Personen"].append(Kandidaat)
        else:
            print("Kandidaat : ", Kandidaat, "speelt al op die dag" , Dag)           
    print(Dag,lid,nummer,Grote,Kandidaat)        


AppendFlight()
AppendPersoon()
for x in range(AantalPersonen):
    AppendPersoon()
    Persoon[x].update({"nummer": x})
    Persoon[x].update({"naam": x+1})

for Dag in range(AantalSpeelDagen ):
    nummer = 0    
    for Grote in FlightVerdeling:    
        nummer = nummer + 1
 #       print("flight z", z , " Aantal in die flight ", Dag + 1)
        for lid in range(Grote):
#            print("Dag: ", Dag ,"flights", z , " Aantal in die flight ", x, "nummer ", nummer)
            WieOhWie(Dag,lid,nummer,Grote)
print(FlightIndeling)








