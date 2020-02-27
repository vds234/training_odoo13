from odoo import api, fields, models, _


class StudentDetails(models.Model):

    _name = 'student.details'

    name=fields.Char('Name')
    age=fields.Integer('Age')
    dob = fields.Date("DOB")
    upload_dob = fields.Binary("Upload DOB")
    dob_file_name = fields.Char("Filename")
    select_gender = fields.Selection([('a', 'Male'),('b','Female'),('c','Others')], "Gender", default='a')
    principal_id = fields.Many2one('principal.details', "Principal")
    marks_ids = fields.One2many('student.details.line', 'student_id', "Marks")
    teacher_ids = fields.Many2many('teacher.details', "stud_teach_rel", 'stud_id', 'teach_id', "Teachers")



class StudentDetailsLine(models.Model):

    _name = 'student.details.line'

    student_id = fields.Many2one('student.details', "Student")
    select_sem = fields.Selection([('sem_1', 'Semester 1'), ('sem_2', 'Semester 2')], "Semester")
    english = fields.Float("English")
    math = fields.Float("Maths")



