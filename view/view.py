class View:
    """
    *************************
    * A view for a agenda DB *
    *************************
    """
    def start(self):
        print('=================================')
        print('=          Bienvenido           =')
        print('=================================')
    
    def end(self):
        print('=================================')
        print('=             Adios             =')
        print('=================================')

    def main_menu(self):
        print('************************')
        print('* -- Menu Principal -- *')
        print('************************')
        print('1. Contactos')
        print('2. Citas')
        print('3. Salir')

    def option(self, last):
        print('Selecciona una opcion (1-'+last+'): ', end = '')
    
    def not_valid_option(self):
        print('¡Opcion no valida!\nIntenta de nuevo')
    
    def ask(self, output):
        print(output, end = '')

    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))

    def error(self, err):
        print(' ¡ERROR! '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))
    

    """
    **********************
    * Views for contactos *
    **********************
    """
    def contacts_menu(self):
        print('***************************')
        print('* -- Submenu Contactos -- *')
        print('***************************')
        print('1. Agregar contacto')
        print('2. Leer un contacto')
        print('3. Leer todos los contactos')
        print('4. Leer contactos por nombre')
        print('5. Actualizar contacto')
        print('6. Borrar contacto')
        print('7. Regresar')


    def show_a_contact(self, record):
        print('ID: ', record[0])
        print('Nombre: ', record[1])
        print('Telefono: ', record[2])
        print('Correo: ', record[3])
        print('Direccion: ', record[4])


    def show_a_contact_brief(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1])
        print('Telefono:', record[3])




    def show_contact_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def show_contact_midder(self):
        print('-'*48)

    def show_contact_footer(self):
        print('*'*48)


    """
    **********************
    * Views for orders   *
    **********************
    """
    def appointments_menu(self):
        print('*************************')
        print('* -- Submenu Citas -- *')
        print('*************************')
        print('1. Agregar cita')
        print('2. Leer una cita')
        print('3. Leer todas las citas')
        print('4. Leer citas de una fecha')
        print('5. Leer citas de un contacto')
        print('6. Actualizar datos de una cita')
        print('7. Agregar contactos a una cita')
        print('8. Modificar contactos de una cita')
        print('9. Borrar contactos de una cita')
        print('10. Borrar cita')
        print('11. Regresar')

    def show_appointment(self, record):
        print('ID: ', record[0])
        print('Fecha: ', record[1])
        print('Hora Inicio: ', record[2])
        print('Hora Final: ', record[3])
        print('Lugar: ', record[4])
        print('Descripcion: ', record[5])
        #self.show_a_contact_brief(record[6:])
    
    def show_appointment_header(self, header):
        print(header.center(160,'+'))

    def show_appointment_midder(self):
        print('/'*160)
    
    def show_appointment_footer(self):
        print('+'*160)

    """
    **********************************
    * Views for Appointment Details  *
    **********************************
   """
    def show_a_appointment_details(self, record):
        print(f'{record[0]:<5}|{record[1]:<30}|{record[2]:<14}|{record[3]:<14}|{record[4]:<14}|{record[5]:<25}|{record[6]:<30}')

    def show_appointment_details_header(self):
        print('-'*160)
        print('ID'.ljust(5)+'|'+'Nombre'.ljust(30)+'|'+'Fecha'.ljust(14)+'|'+'Hora_Inicio'.ljust(14)+'|'+'Hora_Final'.ljust(14)+'|'+'Lugar'.ljust(25)+'|'+'Descripcion'.ljust(30))
        print('-'*160)

    def show_appointment_details_footer(self):
        print('-'*160)









