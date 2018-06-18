# -*- coding: utf-8 -*-

from odoo import models, api


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
    _sql_constraints = {
        ('client_order_ref_uniq', 'unique(client_order_ref)', 'Customer Reference không được trùng')
    }