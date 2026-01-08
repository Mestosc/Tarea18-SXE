# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class gestion_hospital(models.Model):
#     _name = 'gestion_hospital.gestion_hospital'
#     _description = 'gestion_hospital.gestion_hospital'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class paciente(models.Model):
    _name = 'gestion_hospital.paciente'
    _description = 'gestion_hospital.paciente'

    nombre = fields.Char()
    sintomas = fields.Char()

class medico(models.Model):
    _name = 'gestion_hospital.medico'
    _description = 'gestion_hospital.medico'

    nombre = fields.Char()
    numero_colegiado = fields.Char(size=9)

class diagnostico(models.Model):
    _name = 'gestion_hospital.diagnostico'
    _description = 'gestion_hospital.diagnostico'
    medicos_ids = fields.Many2many('gestion_hospital.medico')
    pacientes_ids = fields.Many2many('gestion_hospital.paciente')

    


