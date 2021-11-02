# -*- coding: utf-8 -*-

from odoo import models, fields, api


class olamundo(models.Model):
    _name = 'odoo_olamundo.olamundo'
    _description = 'odoo_olamundo.olamundo'

    name = fields.Char(string="Ola Mundo")

