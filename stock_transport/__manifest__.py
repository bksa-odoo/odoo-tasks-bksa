{
    "name" : "Transport Management System",
    "version" : '1.0',
    "author" : "Bibhav Shah",
    "summary" : "A Module that implements TMS using batch picking",
    "depends" : ['fleet','stock_picking_batch','web_gantt'],
    "data" : [
        'security/ir.model.access.csv',
        'views/fleet_vehicle_model_category_views.xml',
        'views/stock_picking_batch_views.xml',
        'views/stock_picking_views.xml',
    ],
}