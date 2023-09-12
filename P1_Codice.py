!pip install folium
# import moduli
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

# import csv
generation_ = pd.read_csv("file/generation.csv", delimiter = ';', dtype={'Telefono': str})
students_ = pd.read_csv("file/studenti.csv", delimiter = ';')
teachers_ = pd.read_csv("file/insegnanti.csv", delimiter = ';')

# Converto il dataframe generation_ in JSON e lo salvo in un file chiamato "generation.json" (la 'w' = write serve per indicare la scrittura o sovrascrittura del file presente)
generation_json = generation_.to_json(orient='records')
with open('file/generation_json.json', 'w') as file:
    file.write(generation_json)

students_json = students_.to_json(orient='records')
with open('file/students_json.json', 'w') as file:
    file.write(students_json)

teachers_json = teachers_.to_json(orient='records')
with open('file/teachers_json.json', 'w') as file:
    file.write(teachers_json)

# import file json
generation_json = js.load(open("file/generation_json.json"))
students_json = js.load(open("file/students_json.json"))
teachers_json = js.load(open("file/teachers_json.json"))

# import coordinate json
coordinate_json = js.load(open("file/italy_geo.json"))

# creazione dataframe
generation = pd.DataFrame(generation_json)
students = pd.DataFrame(students_json)
teachers = pd.DataFrame(teachers_json)
coordinate = pd.DataFrame(coordinate_json)

# creazione copia dei dataframe
generation_1 = generation.copy()
students_1 = students.copy()
teachers_1 = teachers.copy()
coordinate_1 = coordinate.copy()

# Richiesta all'utente di scegliere tra studente, insegnate, generation
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
    
# Creazione di un nuovo dataframe con la nuova riga
df_nuova_riga = pd.DataFrame(nuova_riga, index=[0])

# Concatenazione del dataframe originale con il nuovo dataframe
generation_1 = pd.concat([generation_1, df_nuova_riga], ignore_index=True)
    

# Verifica della scelta dell'utente
if scelta == 'S':
    nuova_riga2['ID'] = nuova_riga['ID']    
    nuova_riga2['Voto_Python'] = int(input("Inserisci il voto di Python: "))
    nuova_riga2['Voto_Soft_Skill'] = int(input("Inserisci il voto di Soft Skill: "))
    nuova_riga2['Voto_Excel'] = int(input("Inserisci il voto di Excel: "))  
    # Creazione di un nuovo dataframe con la nuova riga
    df_nuova_riga2 = pd.DataFrame(nuova_riga2, index=[0])
    
    # Concatenazione del dataframe originale con il nuovo dataframe
    students_1 = pd.concat([students_1, df_nuova_riga2], ignore_index=True)
    
    print("Fine")
    
elif scelta == 'T':
    nuova_riga2['ID'] = nuova_riga['ID']
    nuova_riga2['Materia'] = input("Inserisci la materia: ")
    
    # Creazione di un nuovo dataframe con la nuova riga
    df_nuova_riga2 = pd.DataFrame(nuova_riga2, index=[0])
    
    # Concatenazione del dataframe originale con il nuovo dataframe
    teachers_1 = pd.concat([teachers_1, df_nuova_riga2], ignore_index=True)
    
    print("Fine")
    
else:
    print("Fine")

# merge dei dataframe
students_complete = pd.merge(generation_1, students_1, how ='right', left_on='ID', right_on='ID')
teachers_complete = pd.merge(generation_1, teachers_1, how ='right', left_on='ID', right_on='ID')
generation_complete = pd.merge(generation_1, students_1, how ='left', left_on='ID', right_on='ID')
generation_complete_1 = pd.merge(generation_complete, teachers_1, how = 'left', left_on = 'ID', right_on = 'ID')

# merge dei dataframe con le coordinate
generation_complete_1 = pd.merge(generation_complete_1, coordinate_1, how = 'left', left_on = 'Citta', right_on = 'comune')

# ordiniamo le colonne
generation_complete_1 = generation_complete_1[["ID","Nome","Cognome","Telefono","Colore_occhi","Sesso","Eta","Provenienza","Citta","lng","lat"]]

# nuova colonna con media dei voti di ogni studente
students_complete['Media'] = students_complete[['Voto_Python','Voto_Soft_Skill', 'Voto_Excel']].mean(axis=1).round(2)

# istogramma dei colori degli occhi
sns.countplot(x = 'Colore_occhi', data = generation_1, palette=['green', 'blue', 'brown'], width=0.4)
plt.yticks([0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
plt.show()

# grafico a torta del genere
sex = generation_1.groupby('Sesso').size() 
sex.plot(kind='pie', autopct='%.1f%%', colors=['hotpink', 'turquoise'])
plt.title('Divisione Maschi e Femmine')
plt.legend(loc='lower right')
plt.show()

# grafico scatterplot che confronta voti python e excel in base al sesso
sns.scatterplot(x='Voto_Python',y='Voto_Excel',hue='Sesso',data=students_complete, palette=['red','blue'])
plt.show()

# grafico jointplot che confronta media e età in base al sesso
sns.jointplot(x='Media', y='Eta', hue='Sesso', data=students_complete, palette=['red','blue'])
plt.show()

# bar plot con i voti delle materie in base al sesso
students_group = students_complete.groupby('Sesso')[['Voto_Python', 'Voto_Soft_Skill', 'Voto_Excel']].mean()
# Il DataFrame students_group = students_group.T fa una trasposizione del students_group DataFrame significa che le colonne diventano le righe e le righe, le colonne. 
# In questo caso facendo la trasposizione del DataFrame scambiamo i dati ('Voto Python', 'Voto Soft Skill' e 'Voto Excel') facendoli diventare righe ed il sesso ('M' e 'F') diventano le nostre colonne.
students_group = students_group.T
ax = students_group.plot(kind='bar')
ax.legend(loc='lower right')
plt.show()

# creiamo il grafico a mappa 
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


'''
class Students(Generation): 
    def __init__(self, ID:str, Nome:str, Cognome:str, Telefono:str, Colore_occhi:str, Voti , Media:float) -> None:
        if Voti.size == 0:
            self.Voti = []
            self.Media = 0    
        else:
            self.Voti = Voti
            self.Media = np.mean(Voti)     
        super().__init__(ID,Nome,Cognome,Telefono,Colore_occhi)

    def __str__(self) -> str:
        return f"Si chiama {self.Nome} {self.Cognome}, il suo numero di cellulare è {self.Telefono}, ha gli occhi di colore {self.Colore_occhi}. Ha preso i seguenti voti: {self.Voti}, ottenendo la seguente media: {self.Media}"

def eyes_colors_dict(*args: Generation) -> dict:     
        d = dict()
        for _ in args:
            if _.Colore_occhi in d:
                d[str(_.Colore_occhi)] += 1
            else:
                d[str(_.Colore_occhi)] = 1
        return d        
'''

