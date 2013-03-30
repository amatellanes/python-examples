# !/usr/bin/env python
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------
# Incluimos los módulos necesarios.
#----------------------------------------------------------------------------
import xmlrpclib


try:
	# Leemos desde teclado la cantidad que se quiere convertir.
	euros = int(raw_input('Introduzca la cantidad en euros (EUR): '))
	# Conectamos con el servidor e invocamos a la función.
	proxy = xmlrpclib.ServerProxy("http://localhost:8000/")
	print "Cantidad en dólares (USD): %s" % str(proxy.euro_to_dollar(euros))

except ValueError:
	# Si la cantidad introducida no es válida finalizamos la ejecución.
	print 'Cantidad incorrecta'
