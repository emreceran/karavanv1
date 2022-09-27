# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json
import random

from babel.dates import format_date
from datetime import date
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.release import version


class karavanuser(models.Model):
    _inherit = "res.partner"

    okul_id = fields.Many2one(
        'karavan.okul', string='Okul', index=True, domain="[('ilce_id', '=?', ilce_id)]"
    )

    ilce_id = fields.Many2one("karavan.ilce", string='İlçe', ondelete='restrict',
                              # related="okul_id.ilce_id"
                              domain="[('sube_id', '=?', sube_id)]"
                              )

    sube_id = fields.Many2one("karavan.sube", string='Şube', ondelete='restrict',
                               # related="ilce_id.sube_id"
                              )
