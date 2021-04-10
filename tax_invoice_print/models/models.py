# -*- coding: utf-8 -*-

from odoo import models, fields, api
from num2words import num2words


class AccounMove(models.Model):
    _inherit = "account.move"


    def _get_amount(self):
        # amt='100000'
        # amount_in_word = num2words().convertNumberToWords(amt)
        amount_in_word = num2words(self.amount_total, lang='en_IN')

        return amount_in_word