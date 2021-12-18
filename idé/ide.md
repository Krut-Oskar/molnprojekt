# Idé till projektarbete

## Bakgrund

Idén är att bygga en applikation som kan underlätta beslutet mellan att ta cykel eller kollektivtrafik när jag/sambon ska till jobb/skola osv. Det kan vara en liten skärm som sitter i hallen eller en hemsida/app. Detta för att underlätta beslutet på morgonen och spara tid.

Applikationen kommer hämta data från temperatur sensor, SMHI api samt SLs API. Detta för att kunna avgöra om det är värt att cykla, är det inte det kan applikationen visa avgångstider för tunnelbanan så man kan planera sin morgon.

Bakgrunden till idén kommer från att vi cyklar relativt ofta men ibland hamnar i regn/andra oväder på vägen hem. Samt att när man väl har valt att ta kollektivtrafiken istället har det varit förseningar som gjort att vi borde tagit cykeln istället. Om vi skulle kunna få en överblick över hur det ser ut på morgonen både gällande väder och kollektivtrafik skulle beslutet bli enklare och man kan bli bättre på att optimera sin tid på morgonen.

## Data

- Temperatur sensor:  Placeras utanför hemmet t.ex DHT sensor eller motsvarande som klarar av utomhusbruk. Kan eventuellt bli simulerad data för att testa olika värden.
- SMHI väder API: För att kolla vädret över dagen, t.ex. om det kommer regna på eftermiddagen så kan det vara relevant för om man tar cykeln eller ej. 
- SL API: Kan nås genom trafiklab för att få tillgång till avgångstider för tunnelbanestationen närmast hemmet. Även störningsinformation kan vara relevant, är det stop i tunnelbanan kan det vara bättre att ta cykeln.

## Effekt/nytta

Den här idén kan användas av många för att optimera sin resväg til jobb/skola eller vart man nu vill åka. Genom att ha tillgång till både väder och kollektivtrafiksdata kan applikationen ge ett bra underlag till vilket färdmedel som passar bäst för dagen. Den första prototypen kommer vara anpassad efter mitt eget användningsområde men planen är att göra den mer flexibel så att du kan ställa in området du bor i och vilka stationer/tågavgångar du vill att den ska kolla. På så sätt blir målgruppen större och den kan användas av alla möjliga för att motverka en del av den stress som många har på morgonen när man ska ta sig till jobb/skola. 

## Hur ska det uppnås

Det kommer uppnås genom att ha en sensor kopplad till en microkontroller som skickar data till en kö i molnet (t.ex. IoT-Hub i azure). I molntjänsten kommer även datat från API:er tas in och presentera den samlade datan på ett snyggt sätt för användaren. Om tid finns kan även applikationen programmeras för att rekommendera ett beslut till användaren. En första iteration på detta hade kunnat vara att sätta egna gränsvärden för när man vill cykla (t.ex. om det är under 10 grader rekommenderas tåg). Alternativt kan man träna en machine learning modell genom att logga användares val och på så sätt skapa en personligare rekommendering.
