# Lambdacalc-eindopdracht

Huidige succesvolle modules:
Repr, str en init voor alle klassen (nu ook str zonder overbodige haakjes)
fromstr onder LambdaTerm
substitutie van variabele door willekeurige LambdaTerm
substitutie van variabele in abstractie en applicatie
reductie van Applicatie van functie en variabele

Nog te implementeren:
reductie onder LambdaTerm(?)
substitutie onder LambdaTerm (?)
reductie van Applicaties voor Andere mogelijke combinaties (M N)
verwijder reductie onder Variable en Abstraction? dit als we vasthouden aan gegeven template met overkoepelende reductiefunctie
Verslag!

Scrapped:
	>>preventieve Alfa-conversie toevoegen bij initiëren van Applicatie
	>>Note: dit doen we niet om fucntionaliteit te behouden

wanneer we tijd over hebben: 
laat fromstring ook werken voor abbreviated Abstraction Notation
laat str methods abbreviated Abstraction notation
implementeer __eq__ method voor Lambdatermen, door niet de termen zelf te vergelijken maar hun str representations;
	dit is mogelijk door de eigenschap te gebruiken dat de hudige str methods geen onnodige haakjes hebben. Nu hoeven we 
	slechts de symbolen te permuteren en strings te vergelijken tot we een match vinden; of niet.