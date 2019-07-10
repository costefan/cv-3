from collections import OrderedDict


images_params = OrderedDict([(
    'human4', {
        'path': "./task1/resources/tracking/Human4/img/%04d.jpg",
        'range_from': (0., 60., 32.),
        'range_to': (180., 255., 255.),
    }),
    ('bird2', {
        'path': "./task1/resources/tracking/Bird2/img/%04d.jpg",
        'range_from': (0., 60., 32.),
        'range_to': (180., 255., 255.),
    })]
)
