# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import datetime

class ReportjtSaleOrderCustomerStatement(models.AbstractModel):

    _name = 'report.customer_statement_sale_orders.action_statement'
    _description = 'SO Customer Statement'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = {}
        partner_ids = data.get('partners') or []
        partners = self.env['res.partner'].browse(partner_ids)
        company = self.env.company
        domain = [('state', 'not in', ('draft', 'cancel')),
                  ('company_id', '=', company.id)]
        if data.get('date_from') and data.get('date_to'):
            domain += [('date_order', '>=', data.get('date_from')),
                       ('date_order', '<=', data.get('date_to'))]
        
        for partner in partners:
            sale = self.env['sale.order'].search(domain + [('partner_id', '=', partner.id)])
            docs[partner] = sale
        values = {
            'doc_ids': partners.ids,
            'doc_model': 'sale.order',
            'data': data,
            'docs': docs,
            'company': company,
        }
        if data.get('date_from'):
            values['dates'] = [datetime.strptime(data.get('date_from'), '%Y-%m-%d %H:%M:%S').date(),
                               datetime.strptime(data.get('date_to'), '%Y-%m-%d %H:%M:%S').date()]
        return values
