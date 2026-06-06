with open("megactivo-main/src/App.jsx","r",encoding="utf-8") as fh:
    c = fh.read()
c = c.replace(
    'const N8N_WEBHOOK_URL = "/n8n/webhook-test/generar-contenido";',
    'const N8N_WEBHOOK_URL = "/n8n/webhook/generar-contenido";'
)
c = c.replace(
    'const N8N_APPROVAL_URL = "/n8n/webhook-test/aprobar-contenido";',
    'const N8N_APPROVAL_URL = "/n8n/webhook/aprobar-contenido";'
)
with open("megactivo-main/src/App.jsx","w",encoding="utf-8") as fh:
    fh.write(c)
print("OK URLs actualizadas")
