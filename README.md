# News Sentiment Analysis – Natural Language Processing mit Transformern

## Einleitung
Mit der zunehmend zur Verfügung stehenden Masse an Daten, insbesondere Textdaten, ist Natural Language Processing zu einem vielversprechenden Ansatz in der Datenanalyse geworden. Neben der Anwendung in kommerziellen Bereichen ist ebenfalls die Anwendung im Bereich der Forschung interessant.

In unserer Arbeit vergleichen wir das Sentiment aus verschiedenen Nachrichtenquellen im Zeitraum vom 01.12.21-31.12.21. Als Ursprung für die Daten stehen uns zwei verschiede Quellen zur Verfügung: zum einen Nachrichtenartikel aus diversen (Online-)Zeitungen sowie Tweets aus dem sozialen Netzwerk StockTwits. Aus den Nachrichtenartikeln lässt sich ein allgemeines Sentiment herleiten und aus den Tweets das Sentiment an der Börse. Dabei beschränken wir uns auf Tweets, die in Verbindung mit den beiden gesellschaftliche relevanten Firmen BioNTech und Apple stehen.

Unser Ziel ist es das allgemeine Sentiment mit dem Sentiment an der Börse zu vergleichen.

Sowohl die Nachrichtenartikel als auch die Tweets haben wir für den Zeitraum selbst gescraped und gelabelt. Das Label der Tweets ist durch die entsprechenden Hashtags an dem jeweiligen Tweet entstanden. Wurde #bearish benutzt, so wurde dies mit dem Sentiment negativ als Label gleichgesetzt, wohingegen #bullish mit positiv gleichgesetzt wurde. Die entsprechenden Hashtags wurden im Anschluss entfernt. Die Nachrichtenartikel wurden manuell auf Basis des Textes und dem subjektiven Eindruck gelabelt.

Hinsichtlich der Methodik war der Blick vor allem auf die Nutzung von Transformer Modellen gerichtet. Dafür wurden BERT sowohl mit als auch ohne Finetuning  genutzt. Beide Modelle werden als state of the art Modelle gesehen. Die Ergebnisse vergleichen wir anschließend mit traditionellen NLP Modellen.

## Daten
Für die Firma BioNTech konnten 6799 Tweets gescraped und 3990 gelabelt werden. Die meisten Tweets sind zwischen 58 und 241 Zeichen lang. Die Daten sind sehr unausgewogen: nur knapp 4% der Daten haben ein negatives Sentiment. Entsprechend wurden folgende class weights eingeführt: 0.52 für Klasse 0 und 13.54 für Klasse 1.

Für die Firma Apple konnten 47521 Tweets gescraped werden und 25026 gelabelt. Die meisten Tweets sind zwischen 33 und 118 Zeichen lang. Dieser Datensatz ist zwar ebenfall nicht ausgeglichen, hier macht der Anteil der Tweets mit negativem Sentiment jedoch immerhin knapp 30% der Daten aus. Die class weights sind 0.71 für Klasse 0 und 1.68 für Klasse 1.

Die Nachrichtenartikel wurden ebenfalls gescraped. Insgesamt konnten so 1256 Artikel von Zeitungen bzw. Online News Anbietern gesammelt werden. Zu den Anbietern der Artikel gehören Focus, Süddeutsche, t-online, FAZ, Spiegel, Tagesschau und die Welt. Von den 1256 Artikel hatten 107 Artikel einen Wirtschaftsbezug und konnten manuell gelabelt werden. Die Label die hier verwendet wurden waren negativ, neutral und positiv.
Um noch eine größere Datenbasis hinsichtlich Nachrichtenartikeln zu haben, wurde noch auf den Datensatz Sentiment Analysis for Financial News zurück gegriffen, der online frei zugänglich ist. Dieser beinhaltet 4837 Titel wovon 59% neutral sind, 28% positiv und 12% negativ.


## Baseline
Als Baseline verwenden wir die zwei gängigen Ansätze term-frequency-inverse document frequency (tf-idf) und valence aware dictionary and sentiment reasoner (VADER).
Aus den Ergebnissen des tf-idf Modells lässt sich festhalten, dass die Klassifizierung der positiven Tweets deutlich besser funktioniert als die der negativen und dass das Modell bei Apple besser funktioniert als bei BioNTech. Dies ist nicht überraschen, das sowohl der Apple Datensatz deutlich größer ist als der von BioNTech und auch die positiven Tweets in der Mehrheit sind.
Die Ergebnisse des VADER Modells sind etwas schwieriger zu vergleichen, da es drei Klassen gibt. Der Großteil der Tweets wird neutral bewertet und Positive besser klassifiziert als Negative. Dennoch bildet VADER den tatsächlichen Verlauf des Sentiments gut ab.

Die Ergebnisse der Baselinemodelle auf Basis der Nachrichtenartikel sind wenig zufriedenstellend. VADER klassifiziert sowohl den Titel als auch den Nachrichtentext größtenteils falsch und bei tf-idf werden alle Artikel positiv klassifiziert.

## Modelle
Das BERT Modell ohne Finetuning hat bei beiden Datensätzen -BioNTech und Apple- eine erschreckend schlechte Performance. Es klassifiziert alle Tweets ausschließlich zu negativem Sentiment und weist somit eine deutlich schlechtere Performance auf als die Baselinemodelle. 

Dagegen hat das BERT Modell mit Finetuning eine deutlich bessere Performance. Im Falle von BioNTech erreicht es eine Accuracy von immerhin 77.63%. Außerdem erkennt das Modell trotz der ungleichen Verteilung der Klassen 8 der insgesamt 15 negativen Tweets, was darauf hinweist, dass es nicht einfach lernt, alle Tweets als positiv zu klassifizieren. Dies ist möglicherweise auch durch die Einführung der class weights begründet. Die ungleiche Verteilung der Klassen erschwert die Klassifizierung dennoch.

In Bezug auf die Apple Daten liefert das BERT Modell mit Finetuning mit 81.42% richtig klassifizierter Tweets ein besseres Ergebnisse als die Baselinemodelle, hier liegt das tf-idf bei 77.8% richtig klassifizierter Tweets. Von den insgesamt 744 negativen Tweets erkennt das BERT Modell 570, was ebenfalls zeigt, dass das Modell sinvoll zu lernen scheint. Gerade die Klassifizierung von negativen Tweets ist in Bezug auf Volatilitätsvohersagen für Finanzmärkten relevant, da negatives Sentiment in der Regel einen stärkeren Effekt auf Preisschwenkung hat als positives Sentiment. 

Die Nachrichtenartikel sollten als Testdatensatz dienen. Hier stellte sich jedoch heraus, dass es insgesamt zu wenig Erwähnungen von den Firmen Apple oder BioNTech gab und die Erkennung daher nur mittelmäßig ausfiel. Möglicherweise liegt es daran, dass die Artikel für den spezifischen Use-Case nicht optimal sind.
Im Hinblick auf die Klassifizierung der Titel hat das finetuned German Sentiment BERT die höchste Accuracy mit 47%, bei den Texten das NLPTown Multilingual Sentiment mit 54%.


## Fazit
Insgesamt lässt sich festhalten, dass es kaum bis keine (frei zugänglichen) Trainingsdaten für Sentiment Analysen gibt mit Ausnahme von einigen Social Media Datensätzen. Diese sind jedoch nicht mit Nachrichtendatensätzen zu vergleichen.

Darüber hinaus ist es sehr schwierig das Sentiment eines Textes zu beziehen. Dies gilt vor allem dann, wenn nicht bekannt ist aus welchem Blickwinkel der Text als positiv oder negativ bewertet werden soll. Häufig ist ein Sachverhalt für Entität A positiv, während der gleiche Sachverhalt für Entität negativ ist. Des Weiteren stellt sich die Frage wie man mit verschiedenen Sätzen in einem Paragraph umgeht, die möglicherweise unterschiedliches Sentiment beinhalten.

Zu den weiteren Herausforderungen gehören, dass Colab memory Probleme hat bei vielen und langen Texten. Dass die maximale Input Größe bei BERT 512 Charakter beträgt, ist ebenfalls schwierig. 

Da die Accuracy bereits auf den Testdaten sehr niedrig ist, dürfte auch die Anwendung in der Realität sehr schwer werden.
