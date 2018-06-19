# -*- coding: utf-8 -*-
from odoo import models, api, fields
from odoo.exceptions import ValidationError
from odoo.tools.translate import _


class ReturnPicking(models.TransientModel):
    _inherit = 'stock.return.picking'

    @api.model
    def default_get(self, fields):
        res = super(ReturnPicking, self).default_get(fields)
        if res.get('product_return_moves'):
            for line in res.get('product_return_moves'):
                line[2]['to_refund'] = True
        return res


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    _sql_constraints = [('client_order_ref_uniq', 'unique(client_order_ref)',
                         u'Tham chiếu khách hàng (Customer Reference) không được trùng nhau.')]

    @api.constrains('client_order_ref')
    def _check_client_order_ref(self):
        customer_reference = self.sudo().search([]).mapped('client_order_ref')
        for rec in self:
            if rec.client_order_ref in customer_reference:
                raise ValidationError(_('Tham chiếu khách hàng (Customer Reference) không được trùng nhau.'))

