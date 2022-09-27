

from odoo import models, fields, api

class sube(models.Model):
    _name = 'karavan.sube'
    _description = 'AGD Şube'
    _order = 'name'

    name = fields.Char("Name", required=True)

class ilce(models.Model):
    _name = 'karavan.ilce'
    _description = 'ilce'
    _order = 'name'

    name = fields.Char("Name", required=True)
    il_id = fields.Many2one('karavan.sube', string='İl', required=True)
