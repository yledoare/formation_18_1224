url = "http://localhost:8069/"
db = "formation_18"
username = 'admin'
password = "d9d2a76e05881aa4fd7f1bb5d160fb46cd759571"


import xmlrpc.client

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

import pdb; pdb.set_trace()
ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]])

models.execute_kw(db, uid, password, 'res.partner', 'read', [ids], {'fields': ['name', 'country_id', 'comment']})


id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': "New Partner"}])

