from odoo import api, fields, models, _


class TeacherDetails(models.Model):

    _name = 'teacher.details'

    name=fields.Char('Name')
    age=fields.Integer('Age')
    dept=fields.Selection([('a', 'Computer'),('b','IT'),('c','EXTC')])
    payment = fields.Selection([('a', 'Online'),('b','Cash'),('c','Transfer')])
    html_wid = fields.Html()
    dept_id = fields.One2many('teacher.details.line', 'teacher_id', "Department Type")

class TeacherDetailsLine(models.Model):

    _name = 'teacher.details.line'

    teacher_id = fields.Many2one('teacher.details', "Teacher")
    teacher_dept = fields.Selection([('dept_1', 'Computer'), ('dept_2', 'EXTC')], "Department")
    ds = fields.Char('Data Structure')
    maths = fields.Char('Maths')


