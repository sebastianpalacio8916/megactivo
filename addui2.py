with open("megactivo-main/src/App.jsx","r",encoding="utf-8") as fh:
    c = fh.read()

old = """            {resultado.copy && (
              <div className="copy-box">
                <span>Caption Instagram</span>
                <p>{resultado.copy}</p>
              </div>
            )}"""

new = """            {resultado.copy && (
              <div className="copy-box">
                <span>Caption Instagram</span>
                <p>{resultado.copy}</p>
              </div>
            )}

            {resultado.caption_linkedin && (
              <div className="copy-box">
                <span>Caption LinkedIn</span>
                <p>{resultado.caption_linkedin}</p>
              </div>
            )}"""

assert old in c, "anchor not found: " + repr(old[:60])
c = c.replace(old, new, 1)
with open("megactivo-main/src/App.jsx","w",encoding="utf-8") as fh:
    fh.write(c)
print("OK linkedin block added, lines:", len(c.splitlines()))
