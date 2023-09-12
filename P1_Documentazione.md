# <CENTER>PROGETTO DEI ROMANI<CENTER>
Il presente elaborato è stato svolto da Carlotta Mannucci, Gabriele Rocco, Luca Albertini e Susanna Di Giammarco, nel mese di Aprile. Alla prima fase del progetto ha inoltre collaborato Francesco Ragazzo.

La ripartizione dei compiti non è stata predisposta nel primo approccio al progetto, di fatto si è deciso di collaborare simultaneamente alla scrittura del codice. Nel corso dell'elaborazione, tuttavia, si sono definiti specifici ruoli: Carlotta si è occupata della fase organizzativa, creativa e di brainstorming; Luca e Gabriele si sono dedicati all'aspetto tecnico del codice e alla scrittura di questo, nonché alla risoluzione dei problemi presentatisi con la collaborazione di Susanna che ha sintetizzato i risultati ottenuti, producendo la trascrizione dell'elaborato.

## PRIMA FASE

L’obiettivo della prima fase del progetto è stato quello di creare una classe e due sottoclassi rappresentando, in parte, la realtà della fondazione di Generation Italia. In particolare è stato richiesto di creare una classe chiamata _Generation_, la quale doveva contenere due sottoclassi chiamate rispettivamente _Teachers_ e _Students_ per rappresentare sia la figura degli insegnanti che degli studenti.
Per fare ciò è stato utilizzato il linguaggio Python ricorrendo ai software: Thonny, Visual Studio Code e Jupiter Lab.

Per la stesura del codice è stato utilizzato come modello di riferimento l'articolo realizzato da Julian Sequeira: [How to Write a Python Subclass.](https://pybit.es/articles/python-subclasses/)

Teoria
- 

Elementi fondamentali che sono stati usati durante l'elaborazione sono:

- **Classi:** Insieme generico di oggetti e attributi annessi che possono essere modificati attraverso metodi e con cui si possono creare entità.

- **Sottoclassi:** Classe che appartiene ad un'altra classe primaria, ereditandone gli attributi. Il punto caratteristico delle sottoclassi è quindi l'_ereditarietà_.

- **Metodi:** Definito all'interno di una classe al fine di crearne e manipolarne il contenuto. La classe è composta da due metodi principali:

   ​__init__ definisce le proprietà degli oggetti (self) della classe.

   ​__str__ ritorna una rappresentazione sotto forma di stringa dell'oggetto assegnato alla classe.


Codice
- 
Per la creazione della classe primaria _Generation_ è stato inizializzato l'oggetto _self_ con i seguenti attributi: codice identificativo (id), nome (name), cognome (surname), numero di cellulare (cell), colore degli occhi (eye_color).

    class Generation(object):
        def __init__(self, id:str, name:str, surname:str, cell:str, eye_color:str) -> None:
            self.id = id
            self.name = name
            self.surname = surname
            self.cell = cell
            self.eye_color = eye_color

Nella definizione della sottoclasse _Teachers_ è stata aggiunta, ai già ereditati attributi dalla classe _Generation_, la materia (subject), esclusiva degli oggetti che rientrano nella sottoclasse in questione. 

    class Teachers(Generation):
        def __init__(self, id:str, name:str, surname:str, cell:str, eye_color:str, subject: list) -> None:
            self.subject = subject
            super().__init__(id,name,surname,cell,eye_color)

Nella definizione della sottoclasse _Students_ sono stati aggiunti, ai già ereditati attributi dalla classe _Generation_, le seguenti caratteristiche: voti (grades) e media dei voti (average).

Per ottimizzare la sottoclasse _Students_ si è predisposta la possibilità di associare ad uno studente senza voti una media pari a 0, altrimenti calcolare la media dei voti dello studente.

    class Students(Generation):
        def __init__(self, id:str, name:str, surname:str, cell:str, eye_color:str, grades: list, average:float) -> None:
            if grades is None:
                self.grades = []
                self.average = 0
            else:
                self.grades = grades
                self.average = sum(self.grades)/len(self.grades)
            super().__init__(id,name,surname,cell,eye_color)

Successivamente è stato definito, sotto forma di stringa, uno specifico output per ogni classe di riferimento ed i relativi attributi.

        def __str__(self) -> str:
            return f"Si chiama {self.name} {self.surname}, il suo numero di cellulare è {self.cell}, ha gli occhi di colore {self.eye_color} e fa parte di Generation"
    

        def __str__(self) -> str:
            return f"Si chiama {self.name} {self.surname}, il suo numero di cellulare è {self.cell}, ha gli occhi di colore {self.eye_color} e insegna {self.subject}"

        def __str__(self) -> str:
            return f"Si chiama {self.name} {self.surname}, il suo numero di cellulare è {self.cell}, ha gli occhi di colore {self.eye_color}. Ha preso i seguenti voti: {self.grades}, ottenendo la seguente media: {self.average}"

Infine è stato creato un dizionario con l'obiettivo di tenere il conto di quante persone appartenenti a _Generation_ hanno un determinato colore degli occhi, sfruttando la struttura del dizionario _chiave_:_valore_.

    def eyes_colors_dict(*args: Generation) -> dict:
            d = dict()
            for _ in args:
                if _.eye_color in d:
                    d[str(_.eye_color)] += 1
                else:
                    d[str(_.eye_color)] = 1
            return d   

Per testare la funzionalità il codice sono stati creati: Fra, Tano e Claudia.

    Fra = Students('11','Fra','Raga','111','azel',[30,30,30],0)
    Tano = Teachers('02','Gae','Vita','002','brown',"python")
    Claudia = Generation('_0','Cla','Vi_osservo','hihihi','blue')

    print(Fra)
    print(Tano)
    print(Claudia)
    print(eyes_colors_dict(Fra,Tano,Claudia))

Ottenendo il seguente output:

    Si chiama Fra Raga, il suo numero di cellulare è 111, ha gli occhi di colore azel. Ha preso i seguenti voti: [30, 30, 30], ottenendo la seguente media: 30.0

    Si chiama Gae Vita, il suo numero di cellulare è 002, ha gli occhi di colore brown e insegna python

    Si chiama Cla Vi_osservo, il suo numero di cellulare è hihihi, ha gli occhi di colore blue e fa parte di Generation

    {'azel': 1, 'brown': 1, 'blue': 1}

 

Sarebbe ideale avere la possibilità di inserire input esterni, in modo da facilitare la consultazione agli utenti finali poco esperti del linguaggio di programmazione di riferimento, migliorando l'esperienza attraverso l'utilizzo di un'interfaccia grafica semplice ed accattivante.



## SECONDA FASE
L'obiettivo della seconda fase è rimasto invariato rispetto alla prima, tuttavia si è provveduto alla modifica del codice utilizzando le librerie trattate durante le lezioni, al fine di aggiornare e ottimizzare lo stesso.

Teoria
- 
- **NumPy**: consente di lavorare con vettori e matrici in maniera più efficace. Offre, inoltre, una vasta gamma di funzioni e metodi per eseguire operazioni matematiche, algebra lineare, manipolazione dei dati ecc.
NumPy è infine spesso utilizzato come base per molte altre librerie scientifiche in Python.
- **Pandas**: fornisce strumenti e strutture dati per manipolare e analizzare i dati, con un'attenzione particolare alla gestione dei dati tabulari. Gli elementi alla base di questa libreria sono: "Serie" (lista trascritta come colonna con l'automatica aggiunta di indici relativi alle righe) e "DataFrame" (elementi tabulari, trascritti sottoforma di tabelle con tanto di indici relativi alle righe). E' inoltre possibile importare file CSV o Excel per eseguire una serie di operazioni su di essi.
- **Marplotlib**: con questa libreria è possibile creare una vasta gamma di grafici (a linee, a barre, a torta, istogrammi, scatter plot), anche modificandoli per rendere la visualizzazione dei dati più comprensibile ed accattivante.
- **Seaborn**: è basata su Matplotlib e fornisce funzionalità aggiuntive per la visualizzazione dei dati. Seaborn si concentra sulla creazione di grafici statistici e di visualizzazioni più avanzate. Offre una serie di stili predefiniti per i grafici, che possono essere facilmente personalizzati.
- **Json**: viene comunemente utilizzato per memorizzare dati in modo strutturato. È ampiamente utilizzato nel contesto delle API.
- **Folium**: Folium è una libreria Python che permette di creare mappe interattive e visualizzazioni geospaziali utilizzando i dati forniti. Dà la possibilità di creare una mappa Folium specificando le coordinate geografiche centrali, il livello di zoom e il tipo di mappa. Una delle caratteristiche principali di Folium è la sua interattività: è possibile aggiungere interazioni agli elementi della mappa, come cliccare sui punti per visualizzare informazioni aggiuntive.

  Nello specitico, per la creazione di un grafico a mappa è stato necessario usare questa libreria, con l'ausilio dei seguenti link:

  [Folium Mapping: Displaying Markers on a Map](https://towardsdatascience.com/folium-mapping-displaying-markers-on-a-map-6bd56f3e3420)
 
  [Folium: geospatial data python](https://andreaprovino.it/folium-geospatial-data-python/)


        import numpy as np 
        import pandas as pd
        import matplotlib.pyplot as plt
        import seaborn as sns
        import json as js
        import folium


Codice
- 
Come primo step importiamo i file.*CSV* relativi all'insieme `generation` e ai sottoinsiemi di `studenti` e `insegnanti` creando rispettivamente tre oggetti definiti come:

    generation_ = pd.read_csv("file/generation.csv", delimiter = ';', dtype={'Telefono': str})
    students_ = pd.read_csv("file/studenti.csv", delimiter = ';')
    teachers_ = pd.read_csv("file/insegnanti.csv", delimiter = ';')

Trasformo i csv in json e li salvo in locale:

    generation_json = generation_.to_json(orient='records')
    with open('file/generation_json.json', 'w') as file:
        file.write(generation_json)

    students_json = students_.to_json(orient='records')
    with open('file/students_json.json', 'w') as file:
        file.write(students_json)

    teachers_json = teachers_.to_json(orient='records')
    with open('file/teachers_json.json', 'w') as file:
        file.write(teachers_json)

I precedenti file.*CSV* non saranno più necessari in quanto sono stati convertiti in file.*JSON* da cui sono stati poi creati i rispettivi oggetti:

    generation_json = js.load(open("file/generation_json.json"))
    students_json = js.load(open("file/students_json.json"))
    teachers_json = js.load(open("file/teachers_json.json"))

Importiamo il file.*JSON* che contiene le *coordinate* di ogni città italiana necessario per la successiva creazione di un grafico mappa:

    coordinate_json = js.load(open("file/italy_geo.json"))

Creiamo quattro Data Frame rappresentati dai quattro file.*JSON*:

    generation = pd.DataFrame(generation_json)
    students = pd.DataFrame(students_json)
    teachers = pd.DataFrame(teachers_json)
    coordinate = pd.DataFrame(coordinate_json)

Creiamo una copia dei Data Frame per evitare modifiche dirette ai file principali e quindi la perdita di dati:

    generation_1 = generation.copy()
    students_1 = students.copy()
    teachers_1 = teachers.copy()
    coordinate_1 = coordinate.copy()

Abbiamo creato la possibilità di inserire tramite input esterno, nuove persone:

    nuova_riga = {}
    scelta = input("Vuoi inserire uno studente (S), un insegnante (T), o un membro di generation (G): ")
    while scelta != 'S' and scelta != 'T' and scelta != 'G':
        scelta = input("Hai inserito un valore sbagliato. Inserisci 'S' per uno studente, 'T' per un insegnante o 'G' per un membro di generation: ")

    nuova_riga2 = {}
    nuova_riga['Nome'] = input("Inserisci il nome: ")
    nuova_riga['Cognome'] = input("Inserisci il cognome: ")
    nuova_riga['Telefono'] = input("Inserisci il telefono: ")
    nuova_riga['Colore_occhi'] = input("Inserisci il colore degli occhi: ")
    nuova_riga['Sesso'] = input("Inserisci il sesso (M o F): ")
    nuova_riga['Eta'] = int(input("Inserisci l'età: "))
    nuova_riga['Provenienza'] = input("Inserisci la provenienza (Nord, Centro, Sud): ")
    nuova_riga['Citta'] = input("Inserisci la città: ")
    nuova_riga['ID'] = scelta + nuova_riga['Nome'][:1] + nuova_riga['Cognome'][:1] + nuova_riga['Telefono'][:2] + nuova_riga['Provenienza'][:1]

    df_nuova_riga = pd.DataFrame(nuova_riga, index=[0])

    generation_1 = pd.concat([generation_1, df_nuova_riga], ignore_index=True)
        

    if scelta == 'S':
        nuova_riga2['ID'] = nuova_riga['ID']    
        nuova_riga2['Voto_Python'] = int(input("Inserisci il voto di Python: "))
        nuova_riga2['Voto_Soft_Skill'] = int(input("Inserisci il voto di Soft Skill: "))
        nuova_riga2['Voto_Excel'] = int(input("Inserisci il voto di Excel: "))  
        df_nuova_riga2 = pd.DataFrame(nuova_riga2, index=[0])
        students_1 = pd.concat([students_1, df_nuova_riga2], ignore_index=True)
        print("Fine")
        
    elif scelta == 'T':
        nuova_riga2['ID'] = nuova_riga['ID']
        nuova_riga2['Materia'] = input("Inserisci la materia: ")
        df_nuova_riga2 = pd.DataFrame(nuova_riga2, index=[0])
        teachers_1 = pd.concat([teachers_1, df_nuova_riga2], ignore_index=True)
        print("Fine")
        
    else:
        print("Fine")

Facciamo il merge dei file.*JSON* specifici riferiti ai dataset `studenti` e `insegnanti` con il dataset `generation`:

    students_complete = pd.merge(generation_1, students_1, how ='right', left_on='ID', right_on='ID')
    teachers_complete = pd.merge(generation_1, teachers_1, how ='right', left_on='ID', right_on='ID')
    generation_complete = pd.merge(generation_1, students_1, how ='left', left_on='ID', right_on='ID')
    generation_complete_1 = pd.merge(generation_complete, teachers_1, how = 'left', left_on = 'ID', right_on = 'ID')

Completiamo il nostro dataset con le coordinate attraverso il merge:

    generation_complete_1 = pd.merge(generation_complete_1, coordinate_1, how = 'left', left_on = 'Citta', right_on = 'comune')

Visualizziamo il risultato ordinando le colonne nel modo seguente:

    generation_complete_1 = generation_complete_1[["ID","Nome","Cognome","Telefono","Colore_occhi","Sesso","Eta","Provenienza","Citta","lng","lat"]]

    generation_complete_1.head()

Generiamo una nuova colonna riferita a `students_complete` con la media dei voti per ogni studente:

    students_complete['Media'] = students_complete[['Voto_Python','Voto_Soft_Skill', 'Voto_Excel']].mean(axis=1).round(2)
    students_complete.head()

Creiamo un istogramma riferito alla colonna `Colore_occhi`:

    sns.countplot(x = 'Colore_occhi', data = generation_1, palette=['green', 'blue', 'brown'], width=0.4)
    plt.yticks([0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
    plt.show()

[Grafico a barre del colore degli occhi](https://prnt.sc/bavbVbYKXLMl)

Creiamo un grafico a torta secondo il `Sesso`:

    sex = generation_1.groupby('Sesso').size() 
    sex.plot(kind='pie', autopct='%.1f%%', colors=['hotpink', 'turquoise'])
    plt.title('Divisione Maschi e Femmine')
    plt.legend(loc='lower right')
    plt.show()

[Grafico a Torta per la divisione tra maschi e femmine](https://prnt.sc/TNVuGVKUNMbP)

Visualizziamo uno scatterplot con i voti di python e di excel condizionati al genere:

    sns.scatterplot(x='Voto_Python',y='Voto_Excel',hue='Sesso',data=students_complete, palette=['red','blue'])
    plt.show()

[ScatterPlot tra Excel e Python](https://prnt.sc/RHw-pKGJMOY_)

Realizziamo un grafico jointplot per confrontare, distinguendo tra i generi, età e media dei voti:

    sns.jointplot(x='Media', y='Eta', hue='Sesso', data=students_complete, palette=['red','blue'])
    plt.show()

[ScatterPlot Sesso, Età e Media dei Voti](https://prnt.sc/kPk0n5dRJ1fl)

Creiamo bar plot dei voti delle diverse materie rispetto al sesso:

    students_group = students_complete.groupby('Sesso')[['Voto_Python', 'Voto_Soft_Skill', 'Voto_Excel']].mean()
    students_group = students_group.T
    ax = students_group.plot(kind='bar')
    ax.legend(loc='lower right')
    plt.show()

[Istogramma della media dei voti tra Maschi e Femmine](https://prnt.sc/EcqE1sRLZI-v)

In conclusione abbiamo creato un grafico con relativa mappa sulla provenienza delle persone:

    italia = folium.Map(location=[41.87194,12.56738], zoom_start=6, tiles="CartoDB Positron")
    for index, row in generation_complete_1.iterrows():
        if row["Provenienza"] == "Nord":
            coordinate = [row["lat"],row["lng"]]
            folium.Marker(location = coordinate, icon=folium.Icon(color='green', icon='')).add_to(italia)
        elif row["Provenienza"] == "Centro":
            coordinate = [row["lat"],row["lng"]]
            folium.Marker(location = coordinate, icon=folium.Icon(color='lightgray', icon='')).add_to(italia)
        else:
            coordinate = [row["lat"],row["lng"]]
            folium.Marker(location = coordinate, icon=folium.Icon(color='red', icon='')).add_to(italia)

            
    italia

LINK ALLE COORDINATE: 
https://github.com/MatteoHenryChinaski/Comuni-Italiani-2018-Sql-Json-excel/blob/master/create-database-comuni-italiani-2018.sql

[Grafico a Mappa](https://prnt.sc/AfHzNvBKLfjK)


Post Mortem
-
Quando si lavora con una grande quantità di dati strutturati e complessi, conviene utilizzare un database per gestirli in modo efficiente. Lavorando ad esempio con SQL si otterrebbero diversi vantaggi, tra cui:
1. Un database SQL consente di definire tabelle con colonne e relazioni tra di esse. questa struttura ci aiuterebbe a organizzare e mantenere dati in modo più efficiente
2. QWERY: SQL offre un insieme di comandi che consentono di interrogare il database in modo flessibile (si possono eseguire QWERY complesse che coinvolgono operazioni. di join e filtri).
3. Integrità dei dati: un database SQL può applicare regole ed integrità dei dati per garantire che rispettino determinate condizioni.

Al fine di creare un'interfaccia grafica più user-friendly, si rimanda a siti specializzati che permettono la creazione di siti web, tra cui si consiglia [Django](https://www.djangoproject.com/)
