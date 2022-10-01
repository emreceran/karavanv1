# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager

from odoo import fields as odoo_fields, http, tools, _, SUPERUSER_ID
from odoo.exceptions import ValidationError, AccessError, MissingError, UserError, AccessDenied
from odoo.http import content_disposition, Controller, request, route
from odoo.tools import consteq
from odoo import  api

class PortalAccountinherited(CustomerPortal):
    MANDATORY_BILLING_FIELDS = ["name", "phone", "email", "street", "city", "country_id", ]
    OPTIONAL_BILLING_FIELDS = ["zipcode", "state_id", "vat", "sube_id", "ilce_id", "okul_id", "company_name"]

    @route(['/my/account'], type='http', auth='user', website=True)
    def account(self, redirect=None, **post):
        values = self._prepare_portal_layout_values()

        partner = request.env.user.partner_id
        values.update({
            'error': {},
            'error_message': [],
        })


        if post and request.httprequest.method == 'POST':
            error, error_message = self.details_form_validate(post)
            values.update({'error': error, 'error_message': error_message})
            values.update(post)
            if not error:
                values = {key: post[key] for key in self.MANDATORY_BILLING_FIELDS}
                values.update({key: post[key] for key in self.OPTIONAL_BILLING_FIELDS if key in post})
                for field in set(['sube_id', 'ilce_id']) & set(values.keys()):
                    try:
                        values[field] = int(values[field])
                    except:
                        values[field] = False
                values.update({'zip': values.pop('zipcode', '')})
                partner.sudo().write(values)
                if redirect:
                    return request.redirect(redirect)
                return request.redirect('/my/home')

        countries = request.env['res.country'].sudo().search([])
        states = request.env['res.country.state'].sudo().search([])
        subeler = request.env['karavan.sube'].sudo().search([])
        ilceler = request.env['karavan.ilce'].sudo().search([])
        okullar = request.env['karavan.okul'].sudo().search([])

        # @api.onchange('sube_id')
        # def _onchange_sube_id(self):
        #     if self.sube_id and self.sube_id != self.ilce_id.sube_id:
        #         self.ilce_id = False
        #
        # @api.onchange('ilce_id')
        # def _onchange_ilce(self):
        #     if self.ilce_id.sube_id:
        #         self.sube_id = self.ilce_id.sube_id

        @api.onchange('sube_id')
        def onchange_subeler(self):
            print("sube değişti")
            self.ilceler = [
                (6, 0, self.ilceler.filtered(lambda ilce: ilce.id in self.subeler.mapped('ilceler').ids).ids)]

        values.update({
            'partner': partner,
            'countries': countries,
            'states': states,
            'okullar': okullar,
            'subeler': subeler,
            'ilceler': ilceler,
            'has_check_vat': hasattr(request.env['res.partner'], 'check_vat'),
            'redirect': redirect,
            'page_name': 'my_details',

        })
        print(values)



        response = request.render("portal.portal_my_details", values)
        response.headers['X-Frame-Options'] = 'DENY'
        return response








class Karavan(http.Controller):
    @http.route('/karavan/karavan', auth='public', website=True)
    def index(self, **kw):
        subeler = http.request.env['karavan.sube']
        return http.request.render('karavan.index', {
            'subeler': subeler.search([])
        })

    # @http.route('/karavan/<name>/', auth='public', website=True)
    # def teacher(self, name):
    #     return '<h1>{}</h1>'.format(name)
    #
    # @http.route('/karavan/<int:id>/', auth='public', website=True)
    # def teacher(self, id):
    #     return '<h1>{} ({})</h1>'.format(id, type(id).__name__)

    @http.route('/karavan/<model("karavan.sube"):sube>/', auth='public', website=True)
    def sube(self, sube):
        return http.request.render('karavan.biography', {
            'sube': sube,
            'il' :sube.state_id
        })

    @http.route('/karavan/karavan/objects', auth='public', website=True)
    def list(self, **kw):
        return http.request.render('karavan.listing', {
            'root': '/karavan/karavan',
            'objects': http.request.env['karavan.sube'].search([]),
        })

    @http.route('/karavan/karavan/objects/<model("karavan.sube"):obj>', auth='public', website=True)
    def object(self, obj, **kw):
        return http.request.render('karavan.object', {
            'object': obj
        })
