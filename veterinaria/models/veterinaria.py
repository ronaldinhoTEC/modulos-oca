# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Veterinaria(models.Model):
    _name = 'veterinaria'
    # _description = "Veterinaria"
    # _inherit = ["mail.thread", "mail.activity.mixin"]
    # _order = "name"
    
    nombre = fields.Char()
    raza = fields.Char(string="Raza")
    diagnostico_id = fields.Many2one("ficha.diagnostico", string="Ficha de Diagnostico")
    imagen = fields.Image("Imagen de la mascota") 
    
    
    
    