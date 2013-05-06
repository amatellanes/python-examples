# !/usr/bin/env python
# -*- coding: utf-8 -*-

# A la hora de escribir un fichero podemos optar por escribir sobreescribiendo
# el contenido ya existente o añadiendo el texto a continuación del contenido 
# ya existente en el fichero.

#-----------------------------------------------------------------------------
# Escritura de fichero sobreescribiendo su contenido.
#-----------------------------------------------------------------------------
outfile = open('texto.txt', 'w') # Indicamos el valor 'w'.
outfile.write('Fusce vitae leo purus, a tempor nisi.\n')
outfile.close()
# Leemos el contenido para comprobar que ha sobreescrito el contenido.
infile = open('texto.txt', 'r')
print('>>> Escritura de fichero sobreescribiendo su contenido.')
print(infile.read())
# Cerramos el fichero.
infile.close()

#-----------------------------------------------------------------------------
# Escritura de fichero concatenando su contenido.
#-----------------------------------------------------------------------------
outfile = open('texto.txt', 'a') # Indicamos el valor 'w'.
outfile.write('Fusce vitae leo purus, a tempor nisi.\n')
outfile.close()
# Leemos el contenido para comprobar que ha sobreescrito el contenido.
infile = open('texto.txt', 'r')
print('>>> Escritura de fichero concatenando su contenido.')
print(infile.read())
# Cerramos el fichero.
infile.close()