# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Veterinaria(models.Model):
    _name = 'veterinaria'
    # _description = "Veterinaria"
    # _inherit = ["mail.thread", "mail.activity.mixin"]
    # _order = "name"
    
    name = fields.Char()
    ref = fields.Char(string="Reference")