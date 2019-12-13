# -*- conding: utf-8 -*-

{
    'name': 'Facturacion',
    'version': '1.0',
    'summary': 'Modulo basico para facturacion en Perú',
    'descripcion': """
Core mechanisms for the accounting modules. To display the menuitems, install the module account_invoicing.
    """,
    'depends' : [],
    'data': [
        'views/series_view.xml',
        'data/series.xml',
        'views/account_invoice_view.xml',
    ]

}