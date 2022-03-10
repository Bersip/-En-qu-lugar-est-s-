def introduccion():
    print("")
    print ("¡Bienvenido aventurero! En el mundo hay 195 países")
    print ("y tu tienes que averiguar ¿En dónde estás?")
    
    while (True): 
        jugar = input ("Si quierés continuar la aventura tipea si. En caso contrario, tipea salir: ")
        
        if(jugar =="salir"):
            pasalir=True
            return pasalir
     
        if(jugar =="si"):      
            print("")
            print("A jugar...")
            break
        else:
            print("")
            print("Debes escribir si o salir.")
  
    