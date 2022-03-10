def puerta2():
    
    print("")
    print("")
    print ("¡Muy bien aventurero! Pasaste al 2do reto.")
    print("")
    print("")
    print ("¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?")
    print ("              Letras revueltas")
    print("¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?")
    
    
    print("")
    print("")
    print("Adivina adivinador con estas pistas y respuestas desordenadas.")
    print("¿En qué país te encuentras?")
    print("")
  
     
    print("1ra pista:") 
    print ("")
    print("Un humorista y escritor estadounidense utilizó esta expresión para")
    print("identificarme como un país retrasado, empobrecido y con exportaciones")
    print("de bajo valor agregado.")
          
    while (True):
        print ("")
        print("Letras revueltas: aeprlúibc nebarnaa")
        respuesta_usuario = input (("¿Cuál es?: "))
        
        if(respuesta_usuario =="salir"):
            pasalir=True
            return pasalir
        
        if(respuesta_usuario=="república bananera"):
            print("¡Correcto!")
            break
        else:
            print("Intenta de nuevo o tipea salir.")
    
    print ("")
    print ("")                           
    print("2da pista:") 
    print ("")
    print("Soy una unidad de cambio que ayuda a la sociedad en la transferencia de bienes.")
    print("Mi nombre es en honor a un guerrero indígena.")
    
    while (True):
        print ("")
        print("Letras revueltas: miaprel")
        respuesta_usuario = input (("¿Quién soy?: "))

        if(respuesta_usuario =="salir"):
            pasalir=True
            return pasalir
        
        if(respuesta_usuario=="lempira"):
            print("¡Correcto!")
            break
        else:
            print("Intenta de nuevo o tipea salir.")      

    print ("")
    print ("")
    print("3ra pista:") 
    print ("")
    print("Soy la mayor reserva de agua dulce de mi país.")
    print("Y el único lago de origen volcánico.")
    
    while (True):
        print ("")
        print("Letras revueltas: alog ed oyjao")
        respuesta_usuario = input (("¿Cómo me llamo?: "))

        if(respuesta_usuario =="salir"):
            pasalir=True
            return pasalir
        
        if(respuesta_usuario=="lago de yojoa"):
            print("¡Correcto!")
            break
        else:
            print("Intenta de nuevo o tipea salir.")    
            
      
    pasalir=False
    return pasalir