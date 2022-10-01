# -*- coding: utf-8 -*-



from odoo import api, fields, models, _


class Sube(models.Model):

    _name = "karavan.sube"
    _description = "Sube"
    _order = 'name'



    name = fields.Char(string="Sube İsim", store=True, readonly=False, tracking=True)
    
    user_id = fields.Many2one('res.users', 'User', store=True, readonly=False)
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict', default=224, readonly=True)
    
    active = fields.Boolean('Active', default=True, store=True, readonly=False)


class karavanv1ilce(models.Model):

    _name = "karavan.ilce"
    _description = "ilce"
    _order = 'name'

    name = fields.Char(string="ilce İsim", store=True, readonly=False, tracking=True)
    user_id = fields.Many2one('res.users', 'User', store=True, readonly=False,)
    sube_id = fields.Many2one('karavan.sube', 'Sube', store=True, readonly=False)
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                               related="sube_id.state_id")

class karavanokul(models.Model):
    _name = "karavan.okul"
    _description = "Okul"
    _order = 'name'

    name = fields.Char(string="Okul İsim", store=True, readonly=False, tracking=True)
    user_id = fields.Many2one('res.users', 'User', store=True, readonly=False,)

    ilce_id = fields.Many2one('karavan.ilce', 'İlçe', store=True, readonly=False)
    sube_id = fields.Many2one("karavan.sube", string='Şube', store=True, ondelete='restrict',
                   related="ilce_id.sube_id")

class karavantakim(models.Model):
    _name = "karavan.takim"

    _description = "karavan takim"
    _order = "name"

    # description
    name = fields.Char('Takım', required=True, translate=True)
    sequence = fields.Integer('Sequence', default=10)
    active = fields.Boolean(default=True,
                            help="If the active field is set to false, it will allow you to hide the Sales Team without removing it.")
    okul_id = fields.Many2one(
        'karavan.okul', string='Okul', index=True
    )
    ilce_id = fields.Many2one("karavan.ilce", string='İlçe', ondelete='restrict',
                              related="okul_id.ilce_id")

    user_id = fields.Many2one('res.users', 'KAptan', store=True, readonly=False,)

    member_ids = fields.Many2many(
        'res.users', string='Takım Üyeleri',
        domain="[ ('okul_id', '=', okul_id)]"
    )
