import json
import uuid

path = r'd:\Artículos, Cursos y otros\Curso IA - EAFIT-ANDI\Hackathon_Andi-EAFIT\megactivo-main\megactivo-main\flujo_n8n_MERGED_v4.json'

def expr(field):
    return '={{ $json.body.' + field + ' }}'

with open(path, encoding='utf-8') as f:
    data = json.load(f)

for n in data['nodes']:
    if n['name'] == 'SET - Datos aprobación':
        n['parameters'] = {
            'mode': 'manual',
            'duplicateItem': False,
            'assignments': {
                'assignments': [
                    {'id': str(uuid.uuid4()), 'name': 'accion',             'value': expr('accion'),             'type': 'string'},
                    {'id': str(uuid.uuid4()), 'name': 'content_id',         'value': expr('content_id'),         'type': 'string'},
                    {'id': str(uuid.uuid4()), 'name': 'calendar_event_id',  'value': expr('calendar_event_id'),  'type': 'string'},
                    {'id': str(uuid.uuid4()), 'name': 'calendar_provider',  'value': expr('calendar_provider'),  'type': 'string'},
                    {'id': str(uuid.uuid4()), 'name': 'comentarios',        'value': expr('comentarios'),        'type': 'string'},
                ]
            },
            'includeOtherFields': False,
            'options': {}
        }
        print('SET - Datos aprobación: asignaciones agregadas OK')

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print('Archivo guardado')
