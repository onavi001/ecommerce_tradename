# -*- coding: utf-8 -*-

from odoo import models, fields

class ProductTemplateTradename(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'
    
    tradename = fields.Char(string='Tradename', Size=32)