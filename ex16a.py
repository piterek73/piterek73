rom sys import argv

script = argv
prompt = "-->"


print ( "\n", f"""Oto program {script}. Umożliwia on:
* tworzenie plików tekstowych,
* ich zapisywanie
* oraz wyświetlanie ich zawartości.""", "\n")
print ("Podaj nazwę pliku tekstowego, który chesz stworzyć: ", "\n")
namefile = input(prompt).strip()

namefile = namefile + ".txt"
target = open (namefile,'w+')

print ("Teraz zapisz tekst, który ma znaleść sie w Twoim pliku.")

text = input (prompt)

target.write (text)

print ("Oto tekst zapisany w Twoim pliku: ", "\n")
