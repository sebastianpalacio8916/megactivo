import json
import uuid

path = r'd:\Artículos, Cursos y otros\Curso IA - EAFIT-ANDI\Hackathon_Andi-EAFIT\megactivo-main\megactivo-main\flujo_n8n_MERGED_v4.json'

with open(path, encoding='utf-8') as f:
    data = json.load(f)

nodes_by_name = {n['name']: n for n in data['nodes']}
conns = data['connections']

# 1) Ya no crear el evento en la generacion: Guardar contenido -> CODE - Resultado Google Calendar (sin pasar por Calendar)
conns['Google Sheets - Guardar contenido'] = {
    'main': [[{'node': 'CODE - Resultado Google Calendar', 'type': 'main', 'index': 0}]]
}
print('Conexion Guardar contenido -> CODE - Resultado Google Calendar: OK (se omite creacion de evento en generacion)')

# 2) CODE - Resultado Google Calendar ya no depende de un evento creado en este punto
nodo_resultado_calendar = nodes_by_name['CODE - Resultado Google Calendar']
nodo_resultado_calendar['parameters']['jsCode'] = (
    "const gen = $items('CODE - Parsear respuesta + React mapping')[0].json;\n"
    "return [{ json: { ...gen, calendar_event: null, calendar_provider_final: gen.calendar_provider || 'google' } }];"
)
print('CODE - Resultado Google Calendar: jsCode actualizado (sin evento en generacion) OK')

# 3) SET - Datos aprobacion: agregar campos necesarios para crear el evento al aprobar
nodo_set_aprobacion = nodes_by_name['SET - Datos aprobación']
campos_extra = [
    'cliente', 'plataforma', 'formato_contenido', 'pilar_contenido',
    'caption_instagram', 'caption_linkedin', 'hashtags',
    'fecha_publicacion_sugerida', 'hora_publicacion', 'observaciones',
]
valores = nodo_set_aprobacion['parameters']['fields']['values']
nombres_existentes = {v['name'] for v in valores}
for campo in campos_extra:
    if campo not in nombres_existentes:
        valores.append({'name': campo, 'stringValue': '={{ $json.body.' + campo + ' }}'})
print('SET - Datos aprobación: campos de contenido agregados OK')

# 4) Code - process results: propagar los campos de contenido hacia el resto de la rama "aprobado"
nodo_process_results = nodes_by_name['Code - process results']
nodo_process_results['parameters']['jsCode'] = (
    "const aprobacionData = $items('SET - Datos aprobación')[0].json;\n"
    "const driveResults = $input.all();\n"
    "\n"
    "let imagen_url = '';\n"
    "\n"
    "if (driveResults && driveResults.length > 0 && driveResults[0].json && driveResults[0].json.id) {\n"
    "  const fileId = driveResults[0].json.id;\n"
    "  imagen_url = `https://drive.google.com/thumbnail?id=${fileId}&sz=w1000`;\n"
    "}\n"
    "\n"
    "return [{\n"
    "  json: {\n"
    "    accion: aprobacionData.accion,\n"
    "    content_id: aprobacionData.content_id,\n"
    "    calendar_event_id: aprobacionData.calendar_event_id,\n"
    "    calendar_provider: aprobacionData.calendar_provider,\n"
    "    comentarios: aprobacionData.comentarios,\n"
    "    cliente: aprobacionData.cliente,\n"
    "    plataforma: aprobacionData.plataforma,\n"
    "    formato_contenido: aprobacionData.formato_contenido,\n"
    "    pilar_contenido: aprobacionData.pilar_contenido,\n"
    "    caption_instagram: aprobacionData.caption_instagram,\n"
    "    caption_linkedin: aprobacionData.caption_linkedin,\n"
    "    hashtags: aprobacionData.hashtags,\n"
    "    fecha_publicacion_sugerida: aprobacionData.fecha_publicacion_sugerida,\n"
    "    hora_publicacion: aprobacionData.hora_publicacion,\n"
    "    observaciones: aprobacionData.observaciones,\n"
    "    imagen_url\n"
    "  }\n"
    "}];"
)
print('Code - process results: ahora propaga campos de contenido OK')

# 5) Nuevo nodo: Google Calendar - Crear evento (aprobado)
calendar_aprobado_id = str(uuid.uuid4())
nodo_calendar_aprobado = {
    'parameters': {
        'calendar': {'__rl': True, 'mode': 'list', 'value': 'primary'},
        'start': "={{ DateTime.fromISO(($json.fecha_publicacion_sugerida || DateTime.now().toISODate()) + 'T' + ($json.hora_publicacion || '09:00') + ':00').toISO() }}",
        'end': "={{ DateTime.fromISO(($json.fecha_publicacion_sugerida || DateTime.now().toISODate()) + 'T' + ($json.hora_publicacion || '09:00') + ':00').plus({hours:1}).toISO() }}",
        'additionalFields': {
            'description': "={{ 'ID: ' + $json.content_id + '\\nCliente: ' + $json.cliente + '\\nPlataforma: ' + $json.plataforma + '\\nFormato: ' + $json.formato_contenido + '\\nPilar: ' + $json.pilar_contenido + '\\n\\nCaption IG:\\n' + $json.caption_instagram + '\\n\\nCaption LI:\\n' + $json.caption_linkedin + '\\n\\nHashtags: ' + $json.hashtags + '\\n\\nEstado: aprobado' + ($json.observaciones ? '\\nObservaciones: ' + $json.observaciones : '') }}",
            'summary': "={{ '[EMILIANO] ' + $json.plataforma + ' — ' + $json.formato_contenido + ' — ' + $json.pilar_contenido }}"
        }
    },
    'id': calendar_aprobado_id,
    'name': 'Google Calendar - Crear evento (aprobado)',
    'type': 'n8n-nodes-base.googleCalendar',
    'typeVersion': 1.3,
    'position': [3200, 1240],
    'credentials': {
        'googleCalendarOAuth2Api': {
            'id': 'tXrQHIMlqum9ftYB',
            'name': 'Google Calendar OAuth2 API'
        }
    }
}

# 6) Nuevo nodo: CODE - Nota evento creado (agrega "Evento creado con exito" a comentarios)
nota_evento_id = str(uuid.uuid4())
nodo_nota_evento = {
    'parameters': {
        'jsCode': (
            "const datos = $items('Code - process results')[0].json;\n"
            "const evento = $json || {};\n"
            "const eventId = evento.id || evento.Id || '';\n"
            "const nota = eventId ? 'Evento creado con éxito' : 'No se pudo crear el evento de calendario';\n"
            "const comentariosFinal = [datos.comentarios, nota].filter(Boolean).join(' | ');\n"
            "\n"
            "return [{\n"
            "  json: {\n"
            "    ...datos,\n"
            "    calendar_event_id: eventId || datos.calendar_event_id,\n"
            "    comentarios: comentariosFinal\n"
            "  }\n"
            "}];"
        )
    },
    'id': nota_evento_id,
    'name': 'CODE - Nota evento creado',
    'type': 'n8n-nodes-base.code',
    'typeVersion': 2,
    'position': [3424, 1240],
}

data['nodes'].append(nodo_calendar_aprobado)
data['nodes'].append(nodo_nota_evento)
print('Nodos "Google Calendar - Crear evento (aprobado)" y "CODE - Nota evento creado" agregados OK')

# 7) Reconectar la rama "aprobado":
# Code - process results -> Google Calendar - Crear evento (aprobado) -> CODE - Nota evento creado -> Google Sheets - Actualizar estado
conns['Code - process results'] = {
    'main': [[{'node': 'Google Calendar - Crear evento (aprobado)', 'type': 'main', 'index': 0}]]
}
conns['Google Calendar - Crear evento (aprobado)'] = {
    'main': [[{'node': 'CODE - Nota evento creado', 'type': 'main', 'index': 0}]]
}
conns['CODE - Nota evento creado'] = {
    'main': [[{'node': 'Google Sheets - Actualizar estado', 'type': 'main', 'index': 0}]]
}
print('Reconexion de la rama "aprobado" OK')

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print('Archivo guardado')
