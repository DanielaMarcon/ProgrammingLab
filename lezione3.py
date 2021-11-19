# inizializzo una lista vuota per salvare i valori
values = []

# apro e leggo il file
my_file = open('sales.csv', 'r')
# riga per riga faccio lo split sulla virgola
for line in my_file:
  elements = line.split(',')
  # tolgo l'intestazione e salvo le date e i valori
  if elements[0] != 'Date':
    date = elements[0]
    value = elements[1]
    # aggiungo i valori alla lista vuota inizializzata
    values.append(float(value))
# chiudo il file
my_file.close()

# definisco la funzione per sommare i valori della lista
def sum_values(values):
  somma = 0
  for item in values:
    somma += item
  print(somma)

sum_values(values)