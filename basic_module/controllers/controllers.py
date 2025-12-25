from odoo import http


class BasicModule(http.Controller):
    @http.route('/hi', auth='public')
    def index(self, **kw):
        return "Hello, world"

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

