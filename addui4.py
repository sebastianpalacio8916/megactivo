with open("megactivo-main/src/App.jsx","r",encoding="utf-8") as fh:
    c = fh.read()

old = """              </div>
            )}
          </section>
        )}
      </section>"""

new = """              </div>
            )}

            <div className="approval-section">
              <label htmlFor="comentarios">Comentarios (opcional)</label>
              <textarea
                id="comentarios"
                value={comentariosAprobacion}
                onChange={(e) => setComentariosAprobacion(e.target.value)}
                placeholder="Escribe tus comentarios o ajustes..."
                rows={3}
              ></textarea>
              <div className="approval-actions">
                <button
                  className="btn-approve"
                  disabled={aprobando !== false}
                  onClick={() => handleAprobacion("aprobar")}
                  type="button"
                >
                  {aprobando === "aprobar" ? "Aprobando..." : "Aprobar"}
                </button>
                <button
                  className="btn-reject"
                  disabled={aprobando !== false}
                  onClick={() => handleAprobacion("rechazar")}
                  type="button"
                >
                  {aprobando === "rechazar" ? "Rechazando..." : "Rechazar"}
                </button>
              </div>
              {aprobacionError && (
                <p className="approval-err">{aprobacionError}</p>
              )}
              {aprobacionResultado && (
                <div className={aprobacionResultado.accion === "aprobar" ? "approval-ok" : "approval-rej"}>
                  <strong>
                    {aprobacionResultado.accion === "aprobar"
                      ? "Contenido aprobado"
                      : "Contenido rechazado o con ajustes"}
                  </strong>
                  <p>
                    {aprobacionResultado.mensaje ||
                      (aprobacionResultado.accion === "aprobar"
                        ? "El contenido fue marcado como aprobado."
                        : "El contenido fue rechazado.")}
                  </p>
                </div>
              )}
            </div>
          </section>
        )}
      </section>"""

cnt = c.count(old)
assert cnt == 1, "anchor matches " + str(cnt) + " times, expected 1"
c = c.replace(old, new, 1)
with open("megactivo-main/src/App.jsx","w",encoding="utf-8") as fh:
    fh.write(c)
print("OK approval section added, lines:", len(c.splitlines()))
