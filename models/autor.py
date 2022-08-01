from odoo import models, fields

class Autor(models.Model):
    _name = 'autor'
    _rec_name = 'last_name'

    name = fields.Char(string="Nombre del Autor", required=True)
    last_name = fields.Char(string="Apellido")