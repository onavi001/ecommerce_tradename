# Copyright 2021, Qualmex
{
    'name': "tradename",
    'summary': """
        tradename for products to appear in e-commerce
    """,
    'description': """
        Add a new field in product_template table (tradename)
        replace product name for tradename in all Qweb views on ecommerce
    """,
    'author': "Qualmex",
    'website': "https://qualmex.com/",
    'category': 'product',
    'version': '14.0.0.1',
    'depends': ['website','website_sale'],
    'data': [
        'views/product_template_tradename_views.xml',
    ],
    'demo': [
    ],
}