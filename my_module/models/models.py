# -*- coding: utf-8 -*-

from odoo import models, fields, api


class my_module(models.Model):
    _name = 'my_module.my_module'
    _description = 'my_module.my_module'

    name = fields.Char()