from odoo import models, fields

class Diagnostico(models.Model):
    _name = "ficha.diagnostico"

    name = fields.Char(string="Name", translate=True)
    descripcion = fields.Text(string="Descripcion", translate=True)
    fecha = fields.Date(string="Date")
    
    