# -*- coding: utf-8 -*-
from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(default=False)
    other_field = fields.Boolean(default=True)
    other_field2 = fields.Boolean(default=True)

    session_ids = fields.Many2many('openacademy.session',
        string="Attended Sessions", readonly=True)