# -*- coding: utf-8 -*-
from odoo import http
from odoo import fields, http, tools, _
from odoo.http import request
from odoo.addons.sale_product_configurator.controllers.main import ProductConfiguratorController


class WebsiteSaleExtra(http.Controller):
    @http.route(['/shop/cart/status'], type='json', auth="public", methods=['POST'], website=True)
    def cart_status(self, product_id, line_id=None, add_qty=None, set_qty=None, display=True):
        """This route is called when changing quantity from the cart or adding
        a product from the product list."""
        order = request.website.sale_get_order()
        # value['cart_quantity'] = order.cart_quantity
        from_currency = order.company_id.currency_id
        to_currency = order.pricelist_id.currency_id

        value = order._cart_update(product_id=product_id, line_id=line_id, add_qty=add_qty, set_qty=set_qty)

        value['cart_quantity'] = order.cart_quantity
        value['website_sale'] = {}

        # value = {
        #     'cart_quantity': order.cart_quantity,
        #     'website_sale': {}
        # }

        value['website_sale.cart_lines'] = request.env['ir.ui.view']._render_template("website_sale.cart_lines", {
            'website_sale_order': order,
            # compute_currency deprecated (not used in view)
            # 'compute_currency': lambda price: from_currency._convert(
            #     price, to_currency, order.company_id, fields.Date.today()),
            'date': fields.Date.today(),
            'suggested_products': order._cart_accessories()
        })
        value['website_sale.short_cart_summary'] = request.env['ir.ui.view']._render_template(
            "website_sale.short_cart_summary", {
                'website_sale_order': order,
                # 'compute_currency': lambda price: from_currency._convert(
                #     price, to_currency, order.company_id, fields.Date.today()),
            })
        return value

    @http.route(['/shop/cart/update/product'], type='http', auth="public", methods=['POST'], website=True)
    def cart_update_product(self, product_id, add_qty=1, set_qty=0, **kw):
        try:
            add_qty = float(add_qty)
        except ValueError:
            return None
        if add_qty <= 0.0:
            return None
        request.website.sale_get_order(force_create=1)._cart_update(product_id=int(product_id), add_qty=add_qty,
                                                                    set_qty=float(set_qty))

    @http.route(['/shop/cart/update/client_order_ref/'], type='json', auth="public", methods=['POST'], website=True)
    def cart_update_origin(self, client_order_ref):
        order = request.website.sale_get_order()
        order.write({'client_order_ref': client_order_ref})
