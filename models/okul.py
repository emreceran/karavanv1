# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import pytz
from datetime import datetime, time
from dateutil.rrule import rrule, DAILY
from random import choice
from string import digits
from werkzeug.urls import url_encode
from dateutil.relativedelta import relativedelta
from collections import defaultdict

from odoo import api, fields, models, _
from odoo.osv.query import Query
from odoo.exceptions import ValidationError, AccessError, UserError
from odoo.osv import expression
from odoo.tools.misc import format_date


class karavanokul(models.Model):

    _name = "karavan.okul"
    _description = "Okul"
    _order = 'name'
    # _inherit = ['hr.employee.base', 'mail.thread', 'mail.activity.mixin', 'resource.mixin', 'avatar.mixin']
    # _mail_post_access = 'read'

    # resource and user
    # required on the resource, make sure required="True" set in the view
    # name = fields.Char(string="Sube İsim", related='resource_id.name', store=True, readonly=False, tracking=True)
    name = fields.Char(string="Okul İsim", store=True, readonly=False, tracking=True)
    # user_id = fields.Many2one('res.users', 'User', related='resource_id.user_id', store=True, readonly=False)

    ilce_id = fields.Many2one('karavan.ilce', 'İlçe', store=True, readonly=False)
    sube_id = fields.Char(related='ilce_id.sube_id  ', store=True)




#
# class karavantakim(models.Model):
#
#     _name = "karavan.takim"
#     _description = "TAKIM"
#     _order = 'name'
#     # _inherit = ['hr.employee.base', 'mail.thread', 'mail.activity.mixin', 'resource.mixin', 'avatar.mixin']
#     # _mail_post_access = 'read'
#
#     # resource and user
#     # required on the resource, make sure required="True" set in the view
#     # name = fields.Char(string="Sube İsim", related='resource_id.name', store=True, readonly=False, tracking=True)
#     name = fields.Char(string="Takım İsim", store=True, readonly=False, tracking=True)
#     user_id = fields.Many2one('res.users', 'User', store=True, readonly=False)
#
#     okul_id = fields.Many2one('karavan.okul', 'Okul', store=True, readonly=False)
#     ilce_id = fields.Many2one("karavan.ilce", string='İlçe', ondelete='restrict',
#                                related="okul_id.ilce_id")
