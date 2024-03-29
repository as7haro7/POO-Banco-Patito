import json
import time

class persona:
    def __init__(self,codigo_cliente, nombres, apellidos, cedula_identidad, direccion, referencia):
        self.__codigo_cliente = codigo_cliente
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__cedula_identidad = cedula_identidad
        self.__direccion = direccion
        self.__referencia = referencia

#---------------------GETERS------------------------------------

    def get_codigo_cliente(self):
        return self.__codigo_cliente
    
    def get_nombres(self):
        return self.__nombres
    
    def get_apellidos(self):
        return self.__apellidos
    
    def get_cedula_identidad(self):
        return self.__cedula_identidad
    
    def get_direccion(self):
        return self.__direccion
    
    def get_referencia(self):
        return self.__referencia

#--------------------------------------------------------------
#------------------------SETERS--------------------------------        
                        
    def set_nombres(self,new,perma=False):
        variable=self
        new=formato_de_nombre(new)
        variable.__nombres = new 
        prueba=variable.Nombre_Unico()
        if prueba==False: return print(f'EL NOMBRE NO ESTA DISPONIBLE')       
        if perma==True:
            with open('Base_de_datos.json', 'r') as f:
                diccionario=json.loads(f.read())        
            busqueda=self.__dict__
            for i in diccionario:
                if busqueda==i:
                    i["_persona__nombres"]=new
                    break
            with open('Base_de_datos.json','w') as x:
                x.write(json.dumps(diccionario, indent=4))
            

        
    def set_apellidos(self,new,perma=False):
        variable=self
        new=formato_de_nombre(new)  
        variable.__apellidos = new
        prueba=variable.Nombre_Unico()
        if prueba==False: return print(f'EL APELLIDO NO ESTA DISPONIBLE')        
        if perma==True:
            with open('Base_de_datos.json', 'r') as f:
                diccionario=json.loads(f.read())
            busqueda=self.__dict__
            for i in diccionario:
                if busqueda==i:
                    i["_persona__apellidos"]=new
                    break
            with open('Base_de_datos.json','w') as x:
                x.write(json.dumps(diccionario, indent=4))
            

        
    def set_cedula_identidad(self,new,perma=False):
        if perma==True:            
            with open('Base_de_datos.json', 'r') as f:
                diccionario=json.loads(f.read())
            busqueda=self.__dict__
            for i in diccionario:
                if busqueda==i:
                    i["_persona__cedula_identidad"]=new
                    break
            with open('Base_de_datos.json','w') as x:
                x.write(json.dumps(diccionario, indent=4))
            
        self.__cedula_identidad = new
        
    def set_direccion(self,new,perma=False):
        if perma==True:           
            with open('Base_de_datos.json', 'r') as f:
                diccionario=json.loads(f.read())
            busqueda=self.__dict__
            for i in diccionario:
                if busqueda==i:
                    i["_persona__direccion"]=new
                    break
            with open('Base_de_datos.json','w') as x:
                x.write(json.dumps(diccionario, indent=4))
            
        self.__direccion = new
        	
    def set_referencia(self,new,perma=False):
        if perma==True:            
            with open('Base_de_datos.json', 'r') as f:
                diccionario=json.loads(f.read())
            busqueda=self.__dict__
            for i in diccionario:
                if busqueda==i:
                    i["_persona__referencia"]=new
                    break
            with open('Base_de_datos.json','w') as x:
                x.write(json.dumps(diccionario, indent=4))
            
        self.__referencia = new
        	
    def set_codigo_cliente(self):        	
        code_cliente = self.__apellidos[0] + str(next(generador_code_cliente)) + self.__nombres[0]
        self.__codigo_cliente=code_cliente

#--------------------------------------------------------------
#--------------------------ACCIONES----------------------------

    def __str__(self):
        return f'''---------------------------------------------------------
Codigo de cliente : {self.__codigo_cliente}
Nombres : {self.__nombres}
Apellidos : {self.__apellidos}
Cedula de Indentidad : {self.__cedula_identidad}
Direccion : {self.__direccion}
Referencia : {self.__referencia}
---------------------------------------------------------'''



    def Nombre_Unico(self):
        with open('Base_de_datos.json', 'r') as f:
            diccionario=json.loads(f.read())

        usuario=self.get_apellidos()+self.get_nombres()
        for i in diccionario:
            buscando=i["_persona__apellidos"]+i["_persona__nombres"]
            if usuario == buscando: return False
        return True
    


    def enlistar_personas():
        with open('Base_de_datos.json', 'r') as f:
            diccionario=json.loads(f.read())
        lista_de_personas=[]
        for i in diccionario:
            lista_de_personas.append(i["_persona__apellidos"]+' '+i["_persona__nombres"])
        return lista_de_personas



    def nueva_persona():
        USUARIO=persona('none','none','none','none','none','none')
        USUARIO.set_nombres(input(f'INGRESE SUS NOMBRES :\n'))
        USUARIO.set_apellidos(input(f'INGRESE SUS APELLIDOS :\n'))

        comprobar=USUARIO.Nombre_Unico()
        if comprobar==False: return f'>>>>>>>>>>>>>>>>ESTE USUARIO YA EXISTE<<<<<<<<<<<<<<<<'

        USUARIO.set_cedula_identidad(input(f'INSERTAR CEDULA DE IDENTIDAD :\n'))
        USUARIO.set_direccion(input(f'INSERTAR DIRECCION\n'))
        USUARIO.set_referencia(input(f'INSERTAR NUMERO DE REFERENCIA :\n'))
        USUARIO.set_codigo_cliente()
        print(f'ESTE ES SU NUEVO CODIGO DE USUARIO---------->{USUARIO.get_codigo_cliente()}')
        print(f'ESTOS SON LOS DATOS DE LA NUEVA PERSONA')
        print(USUARIO)

        USUARIO.guardar_persona()
        print(f'SE HA GUARDADO CON EXITO')
        return USUARIO



    def guardar_persona(self):

        with open('Base_de_datos.json', 'r') as f:
            diccionario=json.loads(f.read())

        Usuario = self.__dict__
        diccionario.append(Usuario)

        with open('Base_de_datos.json', 'w') as f:
            f.write(json.dumps(diccionario, indent= 4))


    # def actualizar_datos(self,variable):
        

        
    def obtener_persona(apellido,nombre):

        with open('Base_de_datos.json', 'r') as f:
            diccionario=json.loads(f.read())

        apellido=formato_de_nombre(apellido)
        nombre=formato_de_nombre(nombre)
        usuario=apellido+nombre

        for i in diccionario:
            buscando=i["_persona__apellidos"]+i["_persona__nombres"]
            if usuario == buscando: 
                return persona(i["_persona__codigo_cliente"],i["_persona__nombres"],i["_persona__apellidos"],i["_persona__cedula_identidad"],i["_persona__direccion"],i["_persona__referencia"])
        return False

    def obtener_persona_codigo_usuario(codigo):

        with open('Base_de_datos.json', 'r') as f:
            diccionario=json.loads(f.read())

        for i in diccionario:
            if codigo==i["_persona__codigo_cliente"]:
                return persona(i["_persona__codigo_cliente"],i["_persona__nombres"],i["_persona__apellidos"],i["_persona__cedula_identidad"],i["_persona__direccion"],i["_persona__referencia"])

        return False
    
    def ob_per_code(codigo):

        with open('Base_de_datos.json', 'r') as f:
            diccionario=json.loads(f.read())

        for i in diccionario:
            if codigo==i["_persona__codigo_cliente"]:
                return True

        return False
#--------------------------------------------------------------
#-------------------------DEFINICIONES EXTRAS (_FORMATOS_ , y mas)-------------------------------------      	        	
def generar_codigo_cliente():
    ini=11111
    while True:
        yield ini
        ini+=101        	
        	
generador_code_cliente = generar_codigo_cliente()

def formato_de_nombre(n):
    n = n.lower().split()
    nombre=''
    if len(n)==0: return False
    for a in n:
        nombre+=a[0].upper()+a[1:]+' '
    return nombre.strip()










if __name__=='__main__':

    print('\n-----------------------------CREANDO PERSONAS DE PRUEBA--------------------------------------')

    bodoque=persona('3f4gf5hg6','Juan Carlos','Bodoque','4321234','Av.Conejo Rojo','66600666')
    kevin=persona('873D35F', 'Kevin', 'Mc Alister','14141414','Calle falsa 123', '11165422')

    time.sleep(0.3)

    print('-----------------------------IMPRIMIENDO LOS DATOS DE LAS PERSONAS-------------------------------------')

    print(bodoque)
    print(kevin)

    time.sleep(0.3)
    print('\n')
    print('-----------------------------OBTENIENDO CADA DATO DE ELLOS---------------------------------')

    print(bodoque.get_codigo_cliente())
    print(bodoque.get_nombres())
    print(bodoque.get_apellidos())
    print(bodoque.get_cedula_identidad())
    print(bodoque.get_direccion())
    print(bodoque.get_referencia())
    print('\n')
    time.sleep(0.3)

    print(kevin.get_codigo_cliente())
    print(kevin.get_nombres())
    print(kevin.get_apellidos())
    print(kevin.get_cedula_identidad())
    print(kevin.get_direccion())
    print(kevin.get_referencia())

    time.sleep(0.3)

    print('-----------------------------CAMBIANDO DATOS DE CADA UNO DE ELLOS---------------------------------\n\nDE LA PERSONA KEVIN')

    kevin.set_nombres('Jhon')
    kevin.set_apellidos('Mc Clayn')
    kevin.set_cedula_identidad('911911911')
    kevin.set_direccion('reten policial')
    kevin.set_referencia('911')
    print('\n')

    time.sleep(0.3)

    print(kevin.get_codigo_cliente())
    print(kevin.get_nombres())
    print(kevin.get_apellidos())
    print(kevin.get_cedula_identidad())
    print(kevin.get_direccion())
    print(kevin.get_referencia())

    time.sleep(0.3)

    print('-----------------------------GUARDANDO PERSONAS EN BASE DE DATOS---------------------------------')

    kevin.guardar_persona()
    bodoque.guardar_persona()

    print('-----------------------------MOSTRANDO EN LISTA LAS PERSONAS---------------------------------\n')

    print(persona.enlistar_personas())
    print('\n')

    print('-----------------------------ACCEDER A LOS DATOS DE UNA PERSONA---------------------------------')
    
    print(f'\n DONDE ESTA JHON MC CLAYN........')

    usuario=persona.obtener_persona('Mc Clayn','jhon')

    print(usuario)

    print('-----------------------------CREANDO NUEVA PERSONA---------------------------------')

    usuario1=persona.nueva_persona()
    print(usuario1)    
