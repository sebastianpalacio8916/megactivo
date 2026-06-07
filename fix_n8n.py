import json

path = r'd:\Artículos, Cursos y otros\Curso IA - EAFIT-ANDI\Hackathon_Andi-EAFIT\megactivo-main\megactivo-main\flujo_n8n_MERGED_v4.json'

def expr(field):
    return '={{ $json.' + field + ' }}'

def expr_raw(expression):
    return '={{ ' + expression + ' }}'

with open(path, encoding='utf-8') as f:
    data = json.load(f)

for n in data['nodes']:

    if n['name'] == 'Google Sheets - Guardar contenido':
        n['parameters']['operation'] = 'append'
        n['parameters']['columns'] = {
            'mappingMode': 'defineBelow',
            'value': {
                'content_id':                 expr('content_id'),
                'cliente':                    expr('cliente'),
                'plataforma':                 expr('plataforma'),
                'formato_contenido':          expr('formato_contenido'),
                'formato_solicitado':         expr('formato_solicitado'),
                'pilar_contenido':            expr('pilar_contenido'),
                'react_data_json':            expr_raw('JSON.stringify($json.react_data)'),
                'caption_instagram':          expr('caption_instagram'),
                'caption_linkedin':           expr('caption_linkedin'),
                'necesita_foto':              expr('necesita_foto'),
                'prompt_imagen':              expr('prompt_imagen'),
                'hashtags':                   expr_raw('($json.hashtags || []).join(" ")'),
                'observaciones':              expr('observaciones'),
                'fecha_publicacion_sugerida': expr('fecha_publicacion_sugerida'),
                'hora_publicacion':           expr('hora_publicacion'),
                'imagen_url':                 expr('imagen_url'),
                'estado':                     expr('estado'),
            },
            'matchingColumns': [],
            'schema': []
        }
        print('Guardar contenido: OK')

    if n['name'] == 'Google Sheets - Actualizar estado':
        n['parameters']['operation'] = 'appendOrUpdate'
        n['parameters']['columns'] = {
            'mappingMode': 'defineBelow',
            'value': {
                'content_id': expr_raw('String($json.content_id)'),
                'estado':     expr_raw("$json.accion === 'aprobar' ? 'aprobado' : 'rechazado'"),
                'comentarios':expr('comentarios'),
            },
            'matchingColumns': ['content_id'],
            'schema': []
        }
        print('Actualizar estado: OK')

    if n['name'] == 'Google Sheets - Actualizar rechazo':
        n['parameters']['operation'] = 'appendOrUpdate'
        n['parameters']['columns'] = {
            'mappingMode': 'defineBelow',
            'value': {
                'content_id': expr_raw('String($json.content_id)'),
                'estado':     'rechazado',
                'comentarios':expr('comentarios'),
            },
            'matchingColumns': ['content_id'],
            'schema': []
        }
        print('Actualizar rechazo: OK')

    if 'aprobaci' in n.get('name', '').lower() and 'set' in n.get('name', '').lower():
        n['parameters']['keepOnlySet'] = True
        print('SET aprobacion keepOnlySet=True: OK')

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print('Archivo guardado')
