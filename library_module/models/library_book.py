from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'A library book'
    _order = 'release_date desc, name'
    _sql_constraints = [
        ('isbn_unique', 'unique(isbn)', "This ISBN value already exists in the database!")
    ]

    name = fields.Char('Title', required=True)
    release_date = fields.Date('Release Date', required=True, )
    isbn = fields.Char('ISBN', required=True,)
    author_ids = fields.Many2many(
        'res.partner',
        string='Authors'
    )
