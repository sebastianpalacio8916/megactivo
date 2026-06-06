with open("megactivo-main/src/App.jsx","r",encoding="utf-8") as fh:
    c = fh.read()
c = c.replace(
    'throw new Error(`Error HTTP: ${response.status}`);',
    'throw new Error("HTTP " + response.status + ": " + await response.text().catch(() => ""));'
)
c = c.replace(
    '"No se pudo conectar con N8N. Revisa que el workflow esté activo, que la URL del webhook sea correcta y que N8N permita solicitudes desde React."',
    '"No se pudo conectar con N8N (" + err.message + "). Revisa que el workflow esté publicado en N8N."'
)
with open("megactivo-main/src/App.jsx","w",encoding="utf-8") as fh:
    fh.write(c)
print("OK error detail mejorado")
