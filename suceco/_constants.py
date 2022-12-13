STAGES = (('Pioneira', 'Pioneira'),
          ('Secundária Inicial', 'Secundária Inicial'),
          ('Secundária Tardia', 'Secundária Tardia'),
          ('Umbrófila', 'Umbrófila'),
          ('Secundária', 'Secundária'),
          ('Climácica', 'Climácica'))

STATUS = (
    (1, 'Active'),
    (0, 'Inactive')
)

DOMAINS = (
    ('Amazonia', 'Amazonia'),
    ('Mata Atlantica', 'Mata Atlantica'),
    ('Caatinga', 'Caatinga'),
    ('Cerrado', 'Cerrado'),
    ('Pantanal', 'Pantanal'),
    ('Pradarias', 'Pradarias'),
    ('', '')
)

CLASS_TRANSLATOR = {'Pioneira': 'Pioneira',
                     'Secundária Inicial': 'Secundária Inicial',
                     'Secundária Tardia': 'Secundária Tardia',
                     'Umbrófila': 'Umbrófila',
                     'Climácica': 'Climácica',
                     'Secundária': 'Secundária',
                     'P': 'Pioneira',
                     'SI': 'Secundária Inicial',
                     'ST': 'Secundária Tardia',
                     'U': 'Umbrófila',
                     'S': 'Secundária',
                     'C': 'Climácica'}

CLASS_COLOR = {'Pioneira': '#E1E1E1',
               'Secundária Inicial': '#B1B1B1',
               'Secundária Tardia': '#7E7E7E',
               'Umbrófila': '#626262',
               'Climácica': '#515151',
               'Secundária': '#222222'}

STATES = ( ('AC', 'AC'),
           ('AL', 'AL'),
           ('AP', 'AP'),
           ('AM', 'AM'),
           ('BA', 'BA'),
           ('CE', 'CE'),
           ('DF', 'DF'),
           ('ES', 'ES'),
           ('GO', 'GO'),
           ('MA', 'MA'),
           ('MG', 'MG'),
           ('MT', 'MT'),
           ('MS', 'MS'),
           ('PA', 'PA'),
           ('PE', 'PE'),
           ('PB', 'PB'),
           ('PI', 'PI'),
           ('PR', 'PR'),
           ('RJ', 'RJ'),
           ('RN', 'RN'),
           ('RR', 'RR'),
           ('RS', 'RS'),
           ('RO', 'RO'),
           ('SC', 'SC'),
           ('SE', 'SE'),
           ('SP', 'SP'),
           ('TO', 'TO'))