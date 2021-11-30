class CSVFile():
  def __init__(self, name):
    # setto il nome del file
    self.name = name

  def get_data(self):
    # inizializzo una lista vuota per salvare tutti i dati
    data = []
    # apro il file
    my_file = open(self.name, 'r')
    # leggo il file linea per linea
    for line in my_file:
      # faccio lo split di ogni linea sulla virgola
      elements = line.split(',')
      # posso anche pulire il carattere di newline dall'ultimo elemento con la funzione strip()
      elements[-1] = elements[-1].strip()
      # p.s. in realtà strip() toglie anche gli spazi bianchi all'inizio e alla fine di una stringa
      # se non sto processando l'intestazione...
      if elements[0] != 'Date':
        # aggiungo alla lista gli elementi di questa linea
        data.append(elements)
    # chiudo il file
    my_file.close()
    # quando ho processato tutte le righe, ritorno i dati
    return data

mio_file = CSVFile(name='sales.csv')
print('Dati contenuti nel file: "{}"'.format(mio_file.get_data()))