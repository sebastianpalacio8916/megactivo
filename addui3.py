with open("megactivo-main/src/App.jsx","r",encoding="utf-8") as fh:
    c = fh.read()

old = """            {resultado.react_data && (
              <div className="code-box">
                <span>Estructura del contenido</span>
                <pre>{JSON.stringify(resultado.react_data, null, 2)}</pre>
              </div>
            )}"""

new = """            {resultado.react_data && (
              <div className="rd-wrapper">
                <ReactDataRenderer data={resultado.react_data} formato={formatoResultado}></ReactDataRenderer>
              </div>
            )}"""

assert old in c, "anchor not found"
c = c.replace(old, new, 1)
with open("megactivo-main/src/App.jsx","w",encoding="utf-8") as fh:
    fh.write(c)
print("OK react_data replaced, lines:", len(c.splitlines()))
