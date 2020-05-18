from mysql import connector

class Model:
    """
    *********************************************
    * A data model with MYSQL for a agenda DB *
    *********************************************
    """

    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d
    
    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor() #Para consultas u operaciones en MySQL

    def close_db(self):
        self.cnx.close()



    """
    ********************
    * Contactos methods  *
    ********************
    """

    def create_contact(self, nombre, telefono, correo, direccion):
        try:
            sql = 'INSERT INTO contactos (`nombre`, `telefono`, `correo`, `direccion`) VALUES (%s, %s, %s, %s)'
            vals = (nombre, telefono, correo, direccion)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_contact(self, id_contacto):
        try:
            sql = 'SELECT * FROM contactos WHERE idContacto = %s'
            vals = (id_contacto,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err


    def read_contact_name(self, name):
        try:
            sql = 'SELECT * FROM contactos WHERE nombre = %s'
            vals = (name,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_all_contacts(self): #Caution with large amount of data
        try:
            sql = 'SELECT * FROM contactos'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_contact(self, fields, vals):
        try:
            sql = 'UPDATE contactos SET '+','.join(fields)+' WHERE idContacto = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_contact(self, id_contacto):
        try:
            sql = 'DELETE FROM contactos WHERE idContacto = %s'
            vals = (id_contacto,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


    """
    ********************
    * Citas methods  *
    ********************
    """

    def create_appointment(self, fdate, time_i, time_f, place, description):
        try:
            sql = 'INSERT INTO citas (`fecha`, `hora_inicio`, `hora_final`, `lugar`, `descripcion` ) VALUES (%s, %s, %s, %s, %s)'
            vals = (fdate, time_i, time_f, place, description)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_appointment = self.cursor.lastrowid
            return id_appointment
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_appointment(self, id_cita):
        try:
            sql = 'SELECT citas.*, citas_detalles.*, contactos.* FROM citas JOIN citas_detalles ON citas_detalles.idCita = citas.idCita and citas.idCita = %s JOIN contactos ON contactos.idContacto = citas_detalles.idContacto'
            vals = (id_cita,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_appointments(self): #Caution with large amount of data
        try:
            sql = 'SELECT citas.*, citas_detalles.*, contactos.* FROM citas JOIN citas_detalles ON citas_detalles.idCita = citas.idCita JOIN contactos ON contactos.idContacto = citas_detalles.idContacto'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_appointments_date(self, date):
        try:
            sql = 'SELECT citas.*, citas_detalles.*, contactos.* FROM citas JOIN citas_detalles ON citas_detalles.idCita = citas.idCita and citas.fecha = %s JOIN contactos ON contactos.idContacto = citas_detalles.idContacto'
            vals = (date,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_appointments_contact(self, name):
        try:
            sql = 'SELECT citas.*, citas_detalles.*, contactos.* FROM citas JOIN citas_detalles ON citas_detalles.idCita = citas.idCita JOIN contactos ON contactos.idContacto = citas_detalles.idContacto and contactos.idContacto = %s'
            vals = (name,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def update_appointment(self, fields, vals):
        try:
            sql = 'UPDATE citas SET '+','.join(fields)+' WHERE idCita = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_appointment(self, id_cita):
        try:
            sql = 'DELETE FROM citas WHERE idCita = %s'
            vals = (id_cita,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


    """
    ***************************
    * Order Details methods   *
    ***************************
    """
    
    def create_appointment_details(self, id_cita, id_contacto):
        try:
            sql = 'INSERT INTO citas_detalles (`idCita`, `idContacto`) VALUES (%s, %s)'
            vals = (id_cita, id_contacto)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_appointment_details(self, id_cita, id_contacto):
        try:
            sql = 'SELECT citas.idCita, contactos.nombre,citas.fecha, citas.hora_inicio, citas.hora_final, citas.lugar, citas.descripcion FROM citas_detalles JOIN citas ON citas_detalles.idCita = citas.idCita JOIN contactos ON citas_detalles.idContacto = contactos.idContacto and citas_detalles.idCita = %s and citas_detalles.idContacto = %s'
            vals = (id_cita, id_contacto)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_appointment_details(self, id_cita):
        try:
            sql = 'SELECT citas.idCita, contactos.nombre, citas.fecha, citas.hora_inicio, citas.hora_final, citas.lugar, citas.descripcion FROM citas_detalles JOIN citas ON citas_detalles.idCita = citas.idCita JOIN contactos ON citas_detalles.idContacto = contactos.idContacto and citas_detalles.idCita = %s'
            vals = (id_cita,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err


    def update_appointment_details(self, fields, vals):
        try:
            sql = 'UPDATE cita_detalles SET '+','.join(fields)+' WHERE idCita = %s and idContacto = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_appointment_details(self, id_cita, id_contacto):
        try:
            sql = 'DELETE FROM cita_detalles WHERE idCita = %s and idContacto = %s'
            vals = (id_cita, id_contacto)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err






