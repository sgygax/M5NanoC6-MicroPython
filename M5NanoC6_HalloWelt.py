#--------------------------------------------------
# Für sleep() das Modul time importieren
import time

i = 0

#--------------------------------------------------
# Endlose Wiederholungen
while True:
  # Ausgabe auf der Konsole
  i = i + 1
  print('Hallo Welt ', i)
  
  # Pause 1 Sekunde
  time.sleep(1)