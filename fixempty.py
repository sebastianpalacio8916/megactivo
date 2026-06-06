with open("megactivo-main/src/App.jsx","r",encoding="utf-8") as fh:
    lines = fh.readlines()

idx = None
for i, ln in enumerate(lines):
    if 'setResultado(data);' in ln:
        idx = i
        break

if idx is None:
    print("not found")
else:
    NL = chr(10)
    guard = [
        '      if (!data || (typeof data === "string" && !data.trim())) {' + NL,
        '        throw new Error("N8N respondio vacio: revisa los Executions en N8N.");' + NL,
        '      }' + NL,
    ]
    lines = lines[:idx] + guard + lines[idx:]
    with open("megactivo-main/src/App.jsx","w",encoding="utf-8") as fh:
        fh.writelines(lines)
    print("OK guard inserted before line", idx+1)
