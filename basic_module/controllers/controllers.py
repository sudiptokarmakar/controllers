from odoo import http
from odoo.http import request
from werkzeug.utils import redirect


class BasicModule(http.Controller):
    @http.route('/hello', type='http', auth='public', website=True)
    def hello(self):
        print("done")
        return request.render('basic_module.hello_template')

        

        # return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        # name=kw.get('name')

        # rec=request.env['res.partner'].search([])
        # print(rec[0].name)
        # # request.render('module.listing', values)
        # name=(request.params.get('name'))
        # hi=(request.params.get('hi'))
        # print(name)
        # print(request.httprequest.user_agent)
        # return f"Hello, {name} {hi}!"

#     @http.route('/basic_module/basic_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('basic_module.listing', {
#             'root': '/basic_module/basic_module',
#             'objects': http.request.env['basic_module.basic_module'].search([]),
#         })

#     @http.route('/basic_module/basic_module/objects/<model("basic_module.basic_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('basic_module.object', {
#             'object': obj
#         })
