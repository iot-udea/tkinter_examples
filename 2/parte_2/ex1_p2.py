import os
import subprocess

# os.system('touch xyz')  -- Usado el system

# Forma equivalente usando el popen
x = subprocess.Popen(['touch', 'xyz']) # Creacion un archivo vacio llamado xyz
print(x.poll())
print(x.returncode)
p = subprocess.Popen(['cp','-r', "xyz", "abc"]) # Creacion de una copia (abc) a partir del archivo xyz
# p=subprocess.Popen("cp -r xyz abc", shell=True) --> Imita como el comando anterior se pasa a la terminal

p = subprocess.Popen(['ls','-l'], stdout=subprocess.PIPE)                                              
print(p.stdout.read())