from model.model import Model
from view.view import View
from datetime import date



class Controller:
    """
    *******************************
    * A controller for a store DB *
    *******************************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        self.view.start()
        self.main_menu()

    """
    ***********************
    * General controllers *
    ***********************
    """
    def main_menu(self):
        o = '0'
        while o != '3':
            self.view.main_menu()
            self.view.option('3')
            o = input()
            if o == '1':
                self.contacts_menu()
            elif o == '2':
                self.appointments_menu()
            elif o == '3':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    def update_lists(self, fs, vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields,vals


    """
    ****************************
    * Controllers for contacts *
    ****************************
    """

    def contacts_menu(self):
        o = '0'
        while o != '7':
            self.view.contacts_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_contact()
            elif o == '2':
                self.read_a_contact()
            elif o == '3':
                self.read_all_contacts()
            elif o == '4':
                self.read_contact_name()
            elif o == '5':
                self.update_contact()
            elif o == '6':
                self.delete_contact()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_contact(self):
        self.view.ask('Nombre: ')
        name = input()
        self.view.ask('Telefono: ')
        phone = input()
        self.view.ask('Correo: ')
        email = input()
        self.view.ask('Dirección: ')
        direction = input()
        return [name,phone,email,direction]

    def create_contact(self):
        name, phone, email, direction = self.ask_contact()
        out = self.model.create_contact(name, phone, email, direction)
        if out == True:
            self.view.ok(name+' '+phone, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL CONTACTO. REVISA.')
        return

    def read_a_contact(self):
        self.view.ask('ID Contacto: ')
        id_contact = input()
        contact = self.model.read_a_contact(id_contact)
        if type(contact) == tuple:
            self.view.show_contact_header(' Datos del contacto '+id_contact+' ')
            self.view.show_a_contact(contact)
            self.view.show_contact_midder()
            self.view.show_contact_footer()
        else:
            if contact == None:
                self.view.error('EL CONTACTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL CONTACTO. REVISA.')
        return

    def read_all_contacts(self):
        contacts = self.model.read_all_contacts()
        if type(contacts) == list:
            self.view.show_contact_header(' Todos los contactos ')
            for contact in contacts:
                self.view.show_a_contact(contact)
                self.view.show_contact_midder()
            self.view.show_contact_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS CONTACTOS. REVISA.')
        return

    def read_contact_name(self):
        self.view.ask('Nombre: ')
        name = input()
        contacts = self.model.read_contact_name(name)
        if type(contacts) == list:
            self.view.show_contact_header(' Contacto con nombre: '+name+' ')
            for contact in contacts:
                self.view.show_a_contact(contact)
                self.view.show_contact_midder()
            self.view.show_contact_footer()
        else:
            if contact == None:
                self.view.error('EL CONTACTO NO EXISTE')
            else:    
                self.view.error('PROBLEMA AL LEER EL CONTACTO. REVISA.')
        return

    def update_contact(self):
        self.view.ask('ID de contacto a modificar: ')
        id_contact = input()
        contact = self.model.read_a_contact(id_contact)
        if type(contact) == tuple:
            self.view.show_contact_header(' Datos del contacto '+id_contact+' ')
            self.view.show_a_contact(contact)
            self.view.show_contact_midder()
            self.view.show_contact_footer()
        else:
            if contact == None:
                self.view.error('EL CONTACTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL CONTACTO. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_contact()
        fields, vals = self.update_lists(['nombre','telefono','correo', 'direccion'], whole_vals)
        vals.append(id_contact)
        vals = tuple(vals)
        out = self.model.update_contact(fields, vals)
        if out == True:
            self.view.ok(id_contact, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL CONTACTO. REVISA.')
        return

    def delete_contact(self):
        self.view.ask('Id de contacto a borrar: ')
        id_contact = input()
        count = self.model.delete_contact(id_contact)
        if count != 0:
            self.view.ok(id_contact, 'borro')
        else:
            if count == 0:
                self.view.error('EL CONTACTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL CONTACTO. REVISA.')
        return


    """
    ********************************
    * Controllers for appointments *
    ********************************
    """

    def appointments_menu(self):
        o = '0'
        while o != '11':
            self.view.appointments_menu()
            self.view.option('11')
            o = input()
            if o == '1':
                self.create_appointment()
            elif o == '2':
                self.read_a_appointment()
            elif o == '3':
                self.read_all_appointments()
            elif o == '4':
                self.read_appointments_date()
            elif o == '5':
                self.read_appointments_contact()
            elif o == '6':
                self.update_appointment()
            elif o == '7':
                self.add_appointment_details()
            elif o == '8':
                self.update_appointment_details()
            elif o == '9':
                self.delete_appointment_details()
            elif o == '10':
                self.delete_appointment()
            elif o == '11':
                return
            else:
                self.view.not_valid_option()
        return

    def create_appointment(self):
        self.view.ask('Fecha (yyyy/mm/dd): ')
        o_date = input()
        self.view.ask('Hora Inicio (00:00:00): ')
        o_time_i = input()
        self.view.ask('Hora Final (00:00:00): ')
        o_time_f = input()
        self.view.ask('Lugar: ')
        o_place = input()
        self.view.ask('Descripción: ')
        o_description = input()

        id_appointment = self.model.create_appointment( o_date, o_time_i, o_time_f, o_place, o_description)
        if type(id_appointment) == int:
            id_contact = ' '
            while id_contact != '':
                self.view.msg('---- Agrega que contactos asistiran a la cita (deja vacio el id del contacto para salir) ---')
                id_contact = self.create_appointment_details(id_appointment)

        else:
            self.view.error('NO SE PUDO CREAR LA CITA. REVISA.')
        return

    def read_a_appointment(self):
        self.view.ask('ID Cita: ')
        id_appointment = input()
        appointments = self.model.read_a_appointment(id_appointment)
        if type(appointments) == list:
            self.view.show_appointment_header(' Todas las citas ')
            for appointment in appointments:
                id_appointment = appointment[0]
                appointment_details = self.model.read_appointment_details(id_appointment)
                if type(appointment_details) != list and appointment_details != None:
                    self.view.error('PROBLEMA AL LEER LA CITA '+str(id_appointment)+'. REVISA.')
                else:
                    self.view.show_appointment(appointment)
                    self.view.show_appointment_details_header()
                    for appointment_detail in appointment_details:
                        self.view.show_a_appointment_details(appointment_detail)
                    self.view.show_appointment_details_footer()
                    self.view.show_appointment_midder()
            self.view.show_appointment_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS CITAS. REVISA.')
        return


    def read_all_appointments(self):
        appointments = self.model.read_all_appointments()
        if type(appointments) == list:
            self.view.show_appointment_header(' Todas las citas ')
            for appointment in appointments:
                id_appointment = appointment[0]
                appointment_details = self.model.read_appointment_details(id_appointment)
                if type(appointment_details) != list and appointment_details != None:
                    self.view.error('PROBLEMA AL LEER LA CITA '+str(id_appointment)+'. REVISA.')
                else:
                    self.view.show_appointment(appointment)
                    self.view.show_appointment_details_header()
                    for appointment_detail in appointment_details:
                        self.view.show_a_appointment_details(appointment_detail)
                    self.view.show_appointment_details_footer()
                    self.view.show_appointment_midder()
            self.view.show_appointment_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS CITAS. REVISA.')
        return

    def read_appointments_date(self):
        self.view.ask('Fecha: ')
        date = input()
        appointments = self.model.read_appointments_date(date)
        if type(appointments) == list:
            self.view.show_appointment_header(' Citas para la fecha '+date+' ')
            for appointment in appointments:
                id_appointment = appointment[0]
                appointment_details = self.model.read_appointment_details(id_appointment)
                if type(appointment_details) != list and appointment_details != None:
                    self.view.error('PROBLEMA AL LEER LA CITA '+id_appointment+'. REVISA.')
                else:
                    self.view.show_appointment(appointment)
                    self.view.show_appointment_details_header()
                    for appointment_detail in appointment_details:
                        self.view.show_a_appointment_details(appointment_detail)
                    self.view.show_appointment_details_footer()
                    self.view.show_appointment_midder()
            self.view.show_appointment_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS CITAS. REVISA.')
        return

    def read_appointments_contact(self):
        self.view.ask('ID Contacto: ')
        id_contact = input()
        appointments = self.model.read_appointments_contact(id_contact)
        if type(appointments) == list:
            self.view.show_appointment_header(' Citas para el contacto '+id_contact+' ')
            for appointment in appointments:
                id_appointment = appointment[0]
                appointment_details = self.model.read_appointment_details(id_appointment)
                if type(appointment_details) != list and appointment_details != None:
                    self.view.error('PROBLEMA AL LEER LA CITA '+id_appointment+'. REVISA.')
                else:
                    self.view.show_appointment(appointment)
                    self.view.show_appointment_details_header()
                    for appointment_detail in appointment_details:
                        self.view.show_a_appointment_details(appointment_detail)
                    self.view.show_appointment_details_footer()
                    self.view.show_appointment_midder()
            self.view.show_appointment_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS CITAS. REVISA.')
        return

    def update_appointment(self):
        self.view.ask('ID de cita a modificar: ')
        id_appointment = input()
        appointment = self.model.read_a_appointment(id_appointment)
        if type(appointment) == tuple:
            self.view.show_appointment_header(' Datos de la cita '+id_appointment+' ')
            self.view.show_appointment(appointment)
            self.view.show_appointment_footer()
        else:
            if appointment == None:
                self.view.error('LA CITA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA CITA. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        self.view.ask('Fecha (yyyy/mm/dd): ')
        o_date = input()    
        self.view.ask('Hora Inicio (00:00:00): ')
        o_time_i = input()  
        self.view.ask('Hora Final (00:00:00): ')
        o_time_f = input()           
        self.view.ask('Lugar: ')
        o_place = input()
        self.view.ask('Descripcion: ')
        o_description = input()

        whole_vals = [o_date, o_time_i, o_time_f, o_place, o_description]
        fields, vals = self.update_lists(['fecha','hora_inicio','hora_final','lugar','descripcion'], whole_vals)
        vals.append(id_appointment)
        vals = tuple(vals)
        out = self.model.update_appointment(fields, vals)
        if out == True:
            self.view.ok(id_appointment, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA CITA. REVISA.')
        return 

    def delete_appointment(self):
        self.view.ask('Id de cita a borrar: ')
        id_appointment = input()
        count = self.model.delete_appointment(id_appointment)
        if count != 0:
            self.view.ok(id_appointment, 'borro')
        else:
            if count == 0:
                self.view.error('LA CITA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA CITA. REVISA.')
        return

    """
    *********************************
    * Controllers for appointment details *
    *********************************
    """                                 
    def create_appointment_details(self, id_appointment):
        self.view.ask('ID Contacto: ')
        id_contact = input()
        if id_contact != '':
            contact = self.model.read_a_contact(id_contact)
            if type(contact) == tuple:
                self.view.show_contact_header(' Datos del contacto '+id_contact+' ')
                self.view.show_a_contact(contact)
                self.view.show_contact_footer()
                out = self.model.create_appointment_details(id_appointment, id_contact)
                if out == True:
                    self.view.ok(contact[1]+' '+contact[2], 'agrego a la orden')
                else:
                    if out.errno == 1062:
                        self.view.error('EL CONTACTO YA ESTA EN LA CITA')
                    else:
                        self.view.error('NO SE PUDO AGREGAR EL CONTACTO. REVISA.')
            else:
                if contact == None:
                    self.view.error('EL CONTACTO NO EXISTE')
                else:
                    self.view.error('PROBLEMA AL LEER EL CONTACTO. REVISA.')
        return id_contact



    def add_appointment_details(self):
        appointment = self.read_a_appointment()
        if type(appointment) == tuple:
            id_appointment = appointment[0]
            id_contact = ' '
            while id_contact != '':
                self.view.msg('---- Agrega contactos a la cita (deja vacio el id del contacto para salir) ---')
                id_contact = self.create_appointment_details(id_appointment)
                if id_contact == '':
                    break
        return

    def update_appointment_details(self):
        appointment = self.read_a_appointment()
        if type(appointment) == tuple:
            id_appointment = appointment[0]
            id_contact = ' '
            while id_contact != '':
                self.view.msg('---- Modifica contactos de la cita (deja vacio el id del contacto para salir) ---')
                self.view.ask('ID contacto: ')
                id_contact = input()
                if id_contact != '':
                    appointment_detail = self.model.read_a_appointment_details(id_appointment, id_contact)
                    if type(appointment_detail) == tuple:
                        contact = self.model.read_a_contact(id_contact)
                        fields = []
                        whole_vals = []
                        whole_vals.append(id_appointment)
                        whole_vals.append(id_contact)
                        self.model.update_appointment_details(fields, whole_vals)
                        self.view.ok(id_contact, 'actualizo en la orden ')
                    else:
                        if appointment_detail == None:
                            self.view.error('EL CONTACTO NO EXISTE EN LA CITA')
                        else:
                            self.view.error('PROBLEMA AL ACTUALIZAR EL CONTACTO. REVISA.')
        return


    def delete_appointment_details(self):
        appointment = self.read_a_appointment()
        if type(appointment) == tuple:
            id_appointment = appointment[0]
            id_contact = ' '
            while id_contact != '':
                self.view.msg('---- Borra contactos de la orden (deja vacio el id del contacto para salir) ---')
                self.view.ask('ID contacto: ')
                id_contact = input()
                if id_contact != '':
                    appointment_detail = self.model.read_a_appointment_detail(id_appointment, id_contact)
                    count = self.model.delete_appointment_detail(id_appointment, id_contact)
                    if type(appointment_detail) == tuple and count != 0:
                        self.view.ok(id_contact, 'borro de la cita ')
                    else:
                        if appointment_detail == None:
                            self.view.error('EL CONTACTO NO EXISTE EN LA CITA')
                        else:
                            self.view.error('PROBLEMA AL BORRAR EL CONTACTO. REVISA.')
        return

