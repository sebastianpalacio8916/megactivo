import json
import uuid

path = r'd:\Artículos, Cursos y otros\Curso IA - EAFIT-ANDI\Hackathon_Andi-EAFIT\megactivo-main\megactivo-main\flujo_n8n_MERGED_v4.json'

def expr(field):
    return '={{ $json.body.' + field + ' }}'

with open(path, encoding='utf-8') as f:
    data = json.load(f)

for n in data['nodes']:

    if n['name'] == 'SET - Entrada + Brand JSON':
        n['parameters'] = {
            'mode': 'manual',
            'duplicateItem': False,
            'assignments': {
                'assignments': [
                    {'id': str(uuid.uuid4()), 'name': 'cliente',           'value': "={{ $json.body.cliente || 'Megactivo' }}", 'type': 'string'},
                    {'id': str(uuid.uuid4()), 'name': 'plataforma',        'value': expr('plataforma'),        'type': 'string'},
                    {'id': str(uuid.uuid4()), 'name': 'formato_contenido', 'value': expr('formato_contenido'), 'type': 'string'},
                    {'id': str(uuid.uuid4()), 'name': 'objetivo_post',     'value': expr('objetivo_post'),     'type': 'string'},
                    {'id': str(uuid.uuid4()), 'name': 'fecha_publicacion', 'value': expr('fecha_publicacion'), 'type': 'string'},
                    {'id': str(uuid.uuid4()), 'name': 'hora_publicacion',  'value': expr('hora_publicacion'),  'type': 'string'},
                    {'id': str(uuid.uuid4()), 'name': 'calendar_provider', 'value': expr('calendar_provider'), 'type': 'string'},
                    {'id': str(uuid.uuid4()), 'name': 'brand_json',        'value': "={{ $json.body.brand_json || {} }}", 'type': 'object'},
                ]
            },
            'includeOtherFields': False,
            'options': {}
        }
        print('SET - Entrada + Brand JSON: asignaciones agregadas OK')

    if n['name'] == 'CODE - Parsear respuesta + React mapping':
        code = n['parameters']['jsCode']
        old = 'fecha_publicacion_sugerida: ai.fecha_publicacion_sugerida || input.fecha_publicacion,'
        new = 'fecha_publicacion_sugerida: input.fecha_publicacion || ai.fecha_publicacion_sugerida,'
        if old in code:
            n['parameters']['jsCode'] = code.replace(old, new)
            print('CODE node: prioridad de fecha_publicacion_sugerida corregida OK')
        else:
            print('CODE node: patron no encontrado, revisar manualmente')
            print(repr(code[-700:]))

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print('Archivo guardado')
