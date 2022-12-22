print("Hallo World")
AantalPersonen = 10
y = [1,2,3,4,5]
fruit = []
fruit.append("een")
fruit.append(2)
fruit.append("drie")
fruit.append(y)
Persoon =[]
print("Dit is mijn eerste variabel")
print("Dus alles wat ik hier doet komt rechts")
for x in fruit:
    print(x)

J = { 
    "nummer" : 1,
    "naam" : "",
    "leeftijd" : "",
    "met_wie_gespeeld" : []
}

Persoon.append(J)
for x in range(AantalPersonen):
    Persoon.append(J)
    Persoon[x].update({"nummer": x})
    print("Persoon 0 = ",Persoon[x])








