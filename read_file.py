# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Podemos leer el fichero de distintas maneras.

#-----------------------------------------------------------------------------
# Lectura completa del fichero.
#-----------------------------------------------------------------------------

# En primer lugar debemos de abrir el fichero que vamos a leer.
# Usa 'rb' en vez de 'r' si se trata de un fichero binario.
infile = open('texto.txt', 'r')
# Mostramos por pantalla lo que leemos desde el fichero
print('>>> Lectura completa del fichero')
print(infile.read())
# Cerramos el fichero.
infile.close()

#-----------------------------------------------------------------------------
# Lectura de una cantidad determinada de bytes.
#-----------------------------------------------------------------------------
# En primer lugar debemos de abrir el fichero que vamos a leer.
# Usa 'rb' en vez de 'r' si se trata de un fichero binario.
infile = open('texto.txt', 'r')
# Mostramos por pantalla lo que leemos desde el fichero
print('>>> Lectura de una cantidad determinada de bytes')
print(infile.read(50) + '\n')
# Cerramos el fichero.
infile.close()

#-----------------------------------------------------------------------------
# Lectura de una línea del fichero.
#-----------------------------------------------------------------------------
# En primer lugar debemos de abrir el fichero que vamos a leer.
# Usa 'rb' en vez de 'r' si se trata de un fichero binario.
infile = open('texto.txt', 'r')
# Mostramos por pantalla lo que leemos desde el fichero
print('>>> Lectura de una línea del fichero')
print(infile.readline())
# Cerramos el fichero.
infile.close()

#-----------------------------------------------------------------------------
# Lectura línea a línea del fichero.
#-----------------------------------------------------------------------------
# En primer lugar debemos de abrir el fichero que vamos a leer.
# Usa 'rb' en vez de 'r' si se trata de un fichero binario.
infile = open('texto.txt', 'r')
# Mostramos por pantalla lo que leemos desde el fichero
print('>>> Lectura del fichero línea a línea')
for line in infile:
	print(line)
# Cerramos el fichero.
infile.close()