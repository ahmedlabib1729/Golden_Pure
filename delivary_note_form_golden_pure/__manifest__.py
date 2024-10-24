
{
'name' : "Golden Pure Invoice Form" ,
'author' : "Ahmed Labib",

'depends' : ['base', 'stock' ],
'data' : [

        'report/ir_actions_report.xml',
        'report/tax_invoice.xml',
        'report/layout.xml'

        ],

'assets': {
        'web.report_assets_common': [
            'delivery_form/static/src/fonts/Amiri-Regular.ttf',

            # Other assets
        ],
    },

}
