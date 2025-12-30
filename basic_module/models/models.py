from odoo import models, fields, api
#
#
class Model_parent(models.Model):
    _name = 'model_parent'
    _description = 'model_parent'

    # child_id = fields.Many2one('model_child')
    name = fields.Char()
    value = fields.Integer()
#
#
# class Model_child(models.Model):
#     _name = 'model_child'
#     _description = 'model_child'
#     _inherit = 'model_parent'
#
#     # parent_id = fields.Many2one('model_parent',invisible=True,default=Model_parent)
#     name = fields.Char()
#     value = fields.Integer()