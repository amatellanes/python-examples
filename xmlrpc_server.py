#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------
# Incluimos los módulos necesarios.
#----------------------------------------------------------------------------
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

# Definimos la función que convierte la cantidad de euros en dólares.
def convert_euro_to_dollar(euros):
	# 1.00 EUR	=	1.28225 USD
	# 2013-03-30 15:28 UTC
	return euros * 1.28225

# Abrimos el servidor para que acepte peticiones.
server = SimpleXMLRPCServer(("localhost", 8000))
print "Listening on port 8000..."

# Registramos la función que hemos definido.
server.register_function(convert_euro_to_dollar, "euro_to_dollar")
server.serve_forever()
