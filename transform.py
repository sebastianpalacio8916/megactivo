import re

with open("megactivo-main/MegactivoTemplates_visualizacion_react_SIN_SLOGAN.html","r",encoding="utf-8") as fh:
    html = fh.read()

sc_start = html.find("<script")
raw_start = html.find(">", sc_start) + 1
raw_end = html.rfind("<" + chr(47) + "script>")
raw = html[raw_start:raw_end]

BS = chr(92)
out = []
i = 0
while i < len(raw):
    c = raw[i]
    if c == BS and i+1 < len(raw):
        n = raw[i+1]
        if n == 'n':
            out.append(chr(10)); i += 2; continue
        if n == '"':
            out.append('"'); i += 2; continue
        if n == "'" :
            out.append("'"); i += 2; continue
        if n == 'u' and i+5 < len(raw):
            hx = raw[i+2:i+6]
            try:
                out.append(chr(int(hx,16))); i += 6; continue
            except ValueError:
                pass
    out.append(c)
    i += 1
js = "".join(out)

start = js.find("const LOGOS")
end   = js.find("function MegactivoTemplates")
chunk = js[start:end].strip()

chunk = chunk.replace("function PostEstatico(", "function PostEstaticoView(")
chunk = chunk.replace("function Carrusel(",     "function CarruselView(")
chunk = chunk.replace("function Story(",        "function StoryView(")
chunk = chunk.replace("function GuionReel(",    "function GuionReelView(")

with open("megactivo-main/src/App.jsx","r",encoding="utf-8") as fh:
    lines = fh.readlines()

rd_idx = None
for i, ln in enumerate(lines):
    if "function ReactDataRenderer" in ln:
        rd_idx = i
        break

if rd_idx is None:
    print("ReactDataRenderer not found"); exit(1)

NL = chr(10)
new_block = chunk + NL + NL
lines = lines[:7] + [new_block] + lines[rd_idx:]

with open("megactivo-main/src/App.jsx","w",encoding="utf-8") as fh:
    fh.writelines(lines)

with open("megactivo-main/src/App.jsx","r",encoding="utf-8") as fh:
    total = len(fh.readlines())
print("OK lines:", total)
