with open("megactivo-main/src/App.jsx","r",encoding="utf-8") as a:
    c = a.read()

renderer = """const N8N_APPROVAL_URL = "/n8n/webhook-test/aprobar-contenido";

function PostEstaticoView({ data }) {
  return (
    <div className="rd-post">
      {data.hook && (
        <div className="rd-section rd-hook">
          <span>Hook</span>
          <p>{data.hook}</p>
        </div>
      )}
      {data.cuerpo && (
        <div className="rd-section">
          <span>Cuerpo</span>
          <p>{data.cuerpo}</p>
        </div>
      )}
      {data.cierre && (
        <div className="rd-section">
          <span>Cierre</span>
          <p>{data.cierre}</p>
        </div>
      )}
      {data.cta && (
        <div className="rd-section rd-cta">
          <span>CTA</span>
          <p>{data.cta}</p>
        </div>
      )}
    </div>
  );
}

function CarruselView({ data }) {
  const slides = data.slides || [];
  return (
    <div className="rd-carrusel">
      {slides.map((slide, i) => (
        <div key={i} className="rd-slide">
          <div className="rd-slide-header">
            <span className="rd-slide-num">{i + 1}</span>
            <span className={"rd-badge rd-badge-" + slide.tipo}>{slide.tipo}</span>
          </div>
          {slide.texto && <p className="rd-slide-texto">{slide.texto}</p>}
          {slide.titulo && <strong className="rd-slide-titulo">{slide.titulo}</strong>}
          {slide.cuerpo && <p className="rd-slide-cuerpo">{slide.cuerpo}</p>}
          {slide.marca && <span className="rd-slide-marca">{slide.marca}</span>}
        </div>
      ))}
    </div>
  );
}

function StoryView({ data }) {
  const frames = data.frames || [];
  return (
    <div className="rd-story">
      {frames.map((frame, i) => (
        <div key={i} className="rd-frame">
          <span className={"rd-badge rd-badge-" + frame.tipo}>{frame.tipo}</span>
          {frame.texto && <p>{frame.texto}</p>}
          {frame.detalle && <small>{frame.detalle}</small>}
          {frame.poll && (
            <div className="rd-poll">
              {frame.poll.map((opt, j) => (
                <span key={j} className="rd-poll-opt">{opt}</span>
              ))}
            </div>
          )}
          {frame.link && <span className="rd-frame-link">{frame.link}</span>}
        </div>
      ))}
    </div>
  );
}

function GuionReelView({ data }) {
  return (
    <div className="rd-reel">
      {data.gancho && (
        <div className="rd-reel-step rd-gancho">
          <span className="rd-step-label">Gancho · 0-3s</span>
          <p>{data.gancho}</p>
        </div>
      )}
      {data.problema && (
        <div className="rd-reel-step rd-problema">
          <span className="rd-step-label">Problema · 3-8s</span>
          <p>{data.problema}</p>
        </div>
      )}
      {(data.puntos || []).map((punto, i) => (
        <div key={i} className="rd-reel-step rd-punto">
          <span className="rd-step-label">{"Punto " + (i + 1) + " — " + punto.titulo}</span>
          {punto.overlay && <code className="rd-overlay">{punto.overlay}</code>}
          <p>{punto.cuerpo}</p>
        </div>
      ))}
      {data.cierre && (
        <div className="rd-reel-step rd-cierre">
          <span className="rd-step-label">Cierre</span>
          <p>{data.cierre}</p>
        </div>
      )}
      {data.cta && (
        <div className="rd-reel-step rd-cta-step">
          <span className="rd-step-label">CTA final</span>
          <p>{data.cta}</p>
        </div>
      )}
      {data.duracion && (
        <div className="rd-duracion">
          {"Duración estimada: "}<strong>{data.duracion}</strong>
        </div>
      )}
    </div>
  );
}

function ReactDataRenderer({ data, formato }) {
  if (!data) return null;
  switch (formato) {
    case "post_estatico": return <PostEstaticoView data={data}></PostEstaticoView>;
    case "carrusel":      return <CarruselView data={data}></CarruselView>;
    case "story":         return <StoryView data={data}></StoryView>;
    case "guion_reel":    return <GuionReelView data={data}></GuionReelView>;
    default:
      return <pre className="rd-raw">{JSON.stringify(data, null, 2)}</pre>;
  }
}

"""
c = c.replace("function App() {\n", renderer + "function App() {\n", 1)

# 2. New state vars after error state
c = c.replace(
    "  const [error, setError] = useState(\"\");\n",
    "  const [error, setError] = useState(\"\");\n\n"
    "  const [aprobando, setAprobando] = useState(false);\n"
    "  const [aprobacionResultado, setAprobacionResultado] = useState(null);\n"
    "  const [aprobacionError, setAprobacionError] = useState(\"\");\n"
    "  const [comentariosAprobacion, setComentariosAprobacion] = useState(\"\");\n"
)

# 3. Reset approval state in handleSubmit
c = c.replace(
    "    setError(\"\");\n    setResultado(null);\n\n    const validationError",
    "    setError(\"\");\n    setResultado(null);\n    setAprobacionResultado(null);\n"
    "    setAprobacionError(\"\");\n    setComentariosAprobacion(\"\");\n\n    const validationError"
)

# 4. Add handleAprobacion + formatoResultado before return
approval_fn = """
  const handleAprobacion = async (accion) => {
    setAprobando(accion);
    setAprobacionError("");
    try {
      const payload = {
        accion,
        content_id: resultado.content_id || "",
        calendar_event_id: resultado.calendar_event?.id || "",
        calendar_provider: resultado.calendar_provider || formData.calendar_provider,
        comentarios: comentariosAprobacion,
      };
      const response = await fetch(N8N_APPROVAL_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      if (!response.ok) throw new Error("Error HTTP: " + response.status);
      const raw = await response.text();
      let data;
      try { data = JSON.parse(raw); } catch { data = raw; }
      setAprobacionResultado({ ...data, accion });
    } catch (err) {
      console.error("Error en aprobación:", err);
      setAprobacionError("No se pudo procesar la acción. Revisa que el workflow de aprobación esté activo.");
    } finally {
      setAprobando(false);
    }
  };

  const formatoResultado = resultado?.formato_contenido || formData.formato_contenido;

"""
c = c.replace("  return (\n    <main className=\"app-shell\">", approval_fn + "  return (\n    <main className=\"app-shell\">", 1)

with open("megactivo-main/src/App.jsx","w",encoding="utf-8") as a:
    a.write(c)
print("Part 1 done, lines:", len(c.splitlines()))

