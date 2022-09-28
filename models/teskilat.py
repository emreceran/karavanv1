# -*- coding: utf-8 -*-



from odoo import api, fields, models, _


class Sube(models.Model):

    _name = "karavan.sube"
    _description = "Sube"
    _order = 'name'



    name = fields.Char(string="Sube İsim", store=True, readonly=False, tracking=True)
    
    user_id = fields.Many2one('res.users', 'User', store=True, readonly=False)
    il_id = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]")
    ulke_id = fields.Many2one('res.country', string='Country', ondelete='restrict', default=224, readonly=True)
    # user_partner_id = fields.Many2one(related='user_id.partner_id', related_sudo=False, string="User's partner")
    active = fields.Boolean('Active', default=True, store=True, readonly=False)



