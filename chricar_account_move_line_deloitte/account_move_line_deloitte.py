# -*- coding: utf-8 -*-

#!/usr/bin/python
# -*- encoding: utf-8 -*-
##############################################
#
# ChriCar Beteiligungs- und Beratungs- GmbH
# Copyright (C) ChriCar Beteiligungs- und Beratungs- GmbH
# all rights reserved
# created 2009-10-17 12:10:57+02
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs.
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company.
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/> or
# write to the Free Software Foundation, Inc.,
# 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
###############################################
import time
from osv import fields,osv
import pooler

class chricar_account_move_import_deny(osv.osv):
     _name = "chricar.account_move_import_deny"

     _columns = {
       'company_id'         : fields.many2one('res.company', 'Company'),
       'name'               : fields.char    ('Voucher', size=16, required=True),
       'code'               : fields.char    ('Code', size=8),
       'date_start'         : fields.date    ('Date Start'),
       'date_stop'          : fields.date    ('Date Stop'),
}
     _defaults = {
}
     _order = "code"
chricar_account_move_import_deny()

class chricar_account_tax_code_deloitte(osv.osv):
     _name = "chricar.account_tax_code_deloitte"

     _columns = {
       'company_id'         : fields.many2one('res.company', 'Company'),
       'name'               : fields.char    ('Tax Name', size=32, required=True),
       'code'               : fields.char    ('Code', size=8, required=True),
       'account_id'         : fields.many2one('account.account','Tax Account',required=True),
       'percent'            : fields.float   ('Percent', digits=(8,4), required=True, help=""),
}
     _order = "code"
chricar_account_tax_code_deloitte()

class chricar_account_opening_deloitte(osv.osv):
     _name = "chricar.account_opening_deloitte"

     _columns = {
       'company_id'         : fields.many2one('res.company', 'Company'),
       'account'            : fields.char    ('Account', size=8, required=True),
       'amount'             : fields.float   ('Amount', required=True, digits=(16,2)),
       'name'               : fields.char    ('Account Name', size=64, required=True),
       'date'               : fields.char    ('Date', size=16, required=True),
}
     _order = "account"

chricar_account_opening_deloitte()


class chricar_account_move_line_deloitte(osv.osv):
     _name = "chricar.account_move_line_deloitte"

     _columns = {
       'company_id'         : fields.many2one('res.company', 'Company'),
       'account'            : fields.char    ('Account', size=8, required=True),
       'amount'             : fields.float   ('Amount', required=True, digits=(16,2)),
       'analytic_account'   : fields.char    ('Analytic Account', size=8),
       'ba'                 : fields.char    ('BA', size=8),
       'bc'                 : fields.char    ('BC', size=8),
       'counter_account'    : fields.char    ('Counter Account', size=8),
       'date'               : fields.char    ('Date', size=16, required=True),
       'description'        : fields.char    ('text', size=128),
       'fix'                : fields.char    ('Fix', size=8),
       'fnr'                : fields.char    ('FNR', size=8),
       'lc'                 : fields.char    ('LC', size=8),
       'name'               : fields.char    ('Voucher', size=16, required=True),
       'symbol'             : fields.char    ('Symbol', size=8),
       'tax_code'           : fields.char    ('Tax Code', size=8),
}
     _defaults = {
       'company_id': lambda self,cr,uid,c: self.pool.get('res.users').browse(cr, uid, uid, c).company_id.id,
}
     _order = "name"
chricar_account_move_line_deloitte()
