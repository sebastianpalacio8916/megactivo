import json

path = r'd:\Artículos, Cursos y otros\Curso IA - EAFIT-ANDI\Hackathon_Andi-EAFIT\megactivo-main\megactivo-main\flujo_n8n_MERGED_v3.json'

NL = '\\n'  # literal backslash-n, matches the escaped newlines inside the prompt string

addition = (
    NL + NL + "INSTRUCCIONES PARA prompt_imagen:" + NL
    + "- Describe una escena visual concreta y especifica relacionada con el contenido del post (evita cliches genericos como 'gente sonriendo en una oficina')." + NL
    + "- Indica un estilo visual claro (fotografia profesional realista, ilustracion plana moderna, etc.), el que mejor se adapte al pilar_contenido y al sector (pymes, contabilidad, finanzas, productividad)." + NL
    + "- Si el Brand JSON incluye colores de marca, menciona esos colores para mantener coherencia visual." + NL
    + "- NUNCA pidas texto, palabras, letras, numeros, logotipos ni tipografia dentro de la imagen: el copy va aparte en el caption." + NL
    + "- Manten un tono profesional y aspiracional. Se conciso pero descriptivo: 2 a 4 frases con detalles de composicion, iluminacion y ambiente."
)

old_anchor = "react_data." + NL + NL + "El campo react_data debe tener la estructura EXACTA segun formato_contenido:"
new_anchor = "react_data." + addition + NL + NL + "El campo react_data debe tener la estructura EXACTA segun formato_contenido:"

with open(path, encoding='utf-8') as f:
    data = json.load(f)

for n in data['nodes']:
    if n['name'] == 'HTTP - Groq Llama 3.3 70B':
        body = n['parameters']['jsonBody']
        count = body.count(old_anchor)
        if count == 1:
            n['parameters']['jsonBody'] = body.replace(old_anchor, new_anchor)
            print('System prompt actualizado OK')
        else:
            print('Coincidencias encontradas: ' + str(count) + ' (se esperaba 1) - revisar manualmente')

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print('Archivo guardado')
