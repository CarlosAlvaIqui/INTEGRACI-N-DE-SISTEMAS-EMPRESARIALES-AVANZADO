# -*- conding: utf-8 -*-
from odoo import models, fields, api

class Series(models.Model):
    _name = 'facturacion.series'
    _description = 'Series de documentos'

    name = fields.Char(string='Nombre de la serie')
    prefix = fields.Char(string='prefijo de la serie')
    document_type = fields.Selection([
        ('01','Factura'),
        ('03','Boleta'),
        ('07','Nota de Credito'),
        ('08','Nota de Debito')
    ])
    active = fields.Boolean(string='Estado de la serie', default=True)