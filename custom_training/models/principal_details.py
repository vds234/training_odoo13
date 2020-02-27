from odoo import api, fields, models, _


class PrincipalDetails(models.Model):

    _name = 'principal.details'

    name=fields.Char('Name')
    age=fields.Integer('Age')
    dept=fields.Char('Dept')
    college=fields.Selection([('a', 'SAKEC'),('b','VJTI'),('c','KJ'),('d','SV')])
    dob = fields.Date("DOB")
    panid = fields.Boolean()
    panno = fields.Char('Pan No')
    notes = fields.Text('Terms and Conditions')
    princ_id = fields.One2many('principal.details.line', 'parent_id', "Subject")
    teacher_ids1 = fields.Many2many('teacher.details', "princ_teach_rel", 'princ_id', 'teach_id', "Principal")


class PrincipalDetailsLine(models.Model):

    _name = 'principal.details.line'

    parent_id = fields.Many2one('principal.details', "Principal")
    account= fields.Float("Account")
    payment = fields.Float("Payment")