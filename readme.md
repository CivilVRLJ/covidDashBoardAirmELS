<h1>Covid Dashboard</h1>

---
Deze applicatie is bedoeld om inzicht te geven in het aantal besmettingen in de regio's van italië.
Per regio wordt er gekeken naar het aantal besmettingen per dag en het totale aantal besmettingen
Daarnaast worden de besmettingen per dag vergeleken met het aantal besmettingen dat er in een zone mag gebeuren.
Deze zones worden bepaald via <a href='https://www.ticonsiglio.com/colori-regioni-regole-governo/'>deze link</a> en
<a href='https://www.governo.it/it/articolo/domande-frequenti-sulle-misure-adottate-dal-governo/15638#zone'> deze link</a>


---
<h2>Install</h2>
Deze applicatie is gemaakt in python (<a href='https://www.python.org/downloads/'>install python</a>) en gebruikt een paar libaries. En kunnen geïnstalleerd worden met pip.

- numpy (pip install numpy)
- pandas (pip install pandas)
- json (pip install json5)
- plotly (pip install plotly)
- dash (pip install dash)

---
<h2>Run</h2>
Run het bestand
```
main.py
 ``` 
en klik op de link die ontstaat.

<h2>Data</h2>
Voor deze applicatie wordt er gebruik gemaakt van verschillende JSON links
https://github.com/pcm-dpc/COVID-19/blob/master/dati-json/dpc-covid19-ita-regioni-latest.json
https://github.com/pcm-dpc/COVID-19/blob/master/dati-json/dpc-covid19-ita-regioni.json

Alle data wordt op gehaald van dit GitHub account: https://github.com/owid/covid-19-data/tree/master/public/data/
