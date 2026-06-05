import { useEffect, useMemo, useState } from "react";
import "./App.css";

const N8N_WEBHOOK_URL = "/n8n/webhook-test/generar-contenido";

function App() {
  const [formData, setFormData] = useState({
    plataforma: "Instagram",
    formato_contenido: "post_estatico",
    objetivo_post: "",
    fecha_publicacion: "",
    hora_publicacion: "14:00",
    calendar_provider: "google",
  });

  const [loading, setLoading] = useState(false);
  const [resultado, setResultado] = useState(null);
  const [error, setError] = useState("");

  const hoy = useMemo(() => new Date().toISOString().split("T")[0], []);

  const formatosPorPlataforma = useMemo(
    () => ({
      Instagram: [
        {
          label: "Post estático",
          value: "post_estatico",
          description: "Pieza visual individual para feed.",
        },
        {
          label: "Carrusel",
          value: "carrusel",
          description: "Secuencia de slides para explicar una idea.",
        },
        {
          label: "Story",
          value: "story",
          description: "Formato vertical para historias de Instagram.",
        },
        {
          label: "Guión Reel",
          value: "guion_reel",
          description: "Guión corto para video tipo Reel.",
        },
      ],
      LinkedIn: [
        {
          label: "Post estático",
          value: "post_estatico",
          description: "Publicación profesional individual.",
        },
        {
          label: "Carrusel",
          value: "carrusel",
          description: "Secuencia tipo documento o presentación.",
        },
      ],
      Ambas: [
        {
          label: "Post estático",
          value: "post_estatico",
          description: "Formato compatible con Instagram y LinkedIn.",
        },
        {
          label: "Carrusel",
          value: "carrusel",
          description: "Formato adaptable para ambas plataformas.",
        },
      ],
    }),
    []
  );

  const formatosDisponibles = useMemo(
    () => formatosPorPlataforma[formData.plataforma] || formatosPorPlataforma.Instagram,
    [formData.plataforma, formatosPorPlataforma]
  );

  const formatoSeleccionado = formatosDisponibles.find(
    (formato) => formato.value === formData.formato_contenido
  );

  const opcionesHora = useMemo(
    () => [
      { label: "12:00 AM", value: "00:00" },
      { label: "12:30 AM", value: "00:30" },
      { label: "1:00 AM", value: "01:00" },
      { label: "1:30 AM", value: "01:30" },
      { label: "2:00 AM", value: "02:00" },
      { label: "2:30 AM", value: "02:30" },
      { label: "3:00 AM", value: "03:00" },
      { label: "3:30 AM", value: "03:30" },
      { label: "4:00 AM", value: "04:00" },
      { label: "4:30 AM", value: "04:30" },
      { label: "5:00 AM", value: "05:00" },
      { label: "5:30 AM", value: "05:30" },
      { label: "6:00 AM", value: "06:00" },
      { label: "6:30 AM", value: "06:30" },
      { label: "7:00 AM", value: "07:00" },
      { label: "7:30 AM", value: "07:30" },
      { label: "8:00 AM", value: "08:00" },
      { label: "8:30 AM", value: "08:30" },
      { label: "9:00 AM", value: "09:00" },
      { label: "9:30 AM", value: "09:30" },
      { label: "10:00 AM", value: "10:00" },
      { label: "10:30 AM", value: "10:30" },
      { label: "11:00 AM", value: "11:00" },
      { label: "11:30 AM", value: "11:30" },
      { label: "12:00 PM", value: "12:00" },
      { label: "12:30 PM", value: "12:30" },
      { label: "1:00 PM", value: "13:00" },
      { label: "1:30 PM", value: "13:30" },
      { label: "2:00 PM", value: "14:00" },
      { label: "2:30 PM", value: "14:30" },
      { label: "3:00 PM", value: "15:00" },
      { label: "3:30 PM", value: "15:30" },
      { label: "4:00 PM", value: "16:00" },
      { label: "4:30 PM", value: "16:30" },
      { label: "5:00 PM", value: "17:00" },
      { label: "5:30 PM", value: "17:30" },
      { label: "6:00 PM", value: "18:00" },
      { label: "6:30 PM", value: "18:30" },
      { label: "7:00 PM", value: "19:00" },
      { label: "7:30 PM", value: "19:30" },
      { label: "8:00 PM", value: "20:00" },
      { label: "8:30 PM", value: "20:30" },
      { label: "9:00 PM", value: "21:00" },
      { label: "9:30 PM", value: "21:30" },
      { label: "10:00 PM", value: "22:00" },
      { label: "10:30 PM", value: "22:30" },
      { label: "11:00 PM", value: "23:00" },
      { label: "11:30 PM", value: "23:30" },
    ],
    []
  );

  useEffect(() => {
    setFormData((prevData) => {
      const esValido = formatosDisponibles.some(
        (f) => f.value === prevData.formato_contenido
      );
      if (esValido) return prevData;
      return { ...prevData, formato_contenido: formatosDisponibles[0].value };
    });
  }, [formatosDisponibles]);

  const handleChange = (event) => {
    const { name, value } = event.target;

    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const validarFormulario = () => {
    if (!formData.formato_contenido) {
      return "Debes seleccionar un formato de contenido.";
    }

    if (!formData.objetivo_post.trim()) {
      return "Debes escribir el objetivo del contenido.";
    }

    if (!formData.fecha_publicacion) {
      return "Debes seleccionar una fecha sugerida de publicación.";
    }

    if (formData.fecha_publicacion < hoy) {
      return "La fecha sugerida no puede ser anterior al día de hoy.";
    }

    if (!formData.hora_publicacion) {
      return "Debes seleccionar una hora de publicación.";
    }

    return "";
  };

  /* const construirFechaISO = () => {
    const fechaHoraLocal = `${formData.fecha_publicacion}T${formData.hora_publicacion}:00`;
    return new Date(fechaHoraLocal).toISOString();
  }; */

  const handleSubmit = async (event) => {
    event.preventDefault();

    setError("");
    setResultado(null);

    const validationError = validarFormulario();

    if (validationError) {
      setError(validationError);
      return;
    }

    setLoading(true);

    try {
      const payload = {
        cliente: "Megactivo",
        plataforma: formData.plataforma,
        formato_contenido: formData.formato_contenido,
        objetivo_post: formData.objetivo_post,
        fecha_publicacion: formData.fecha_publicacion,
        hora_publicacion: formData.hora_publicacion,
        calendar_provider: formData.calendar_provider,
      };


      const response = await fetch(N8N_WEBHOOK_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        throw new Error(`Error HTTP: ${response.status}`);
      }
      const raw = await response.text(); // leer una sola vez
      let data;

      try {
        data = JSON.parse(raw); // intentar parsear como JSON
      } catch {
        data = raw; // si no es JSON, usar texto plano
      }

      setResultado(data);
    } catch (err) {
      console.error("Error al conectar con N8N:", err);

      setError(
        "No se pudo conectar con N8N. Revisa que el workflow esté activo, que la URL del webhook sea correcta y que N8N permita solicitudes desde React."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="app-shell">
      <section className="hero-panel">
        <div className="hero-content">
          <div className="logo-row">
            <img
              src="/megactivo-logo.png"
              alt="Megactivo"
              className="main-logo"
            />
          </div>

          <h1>Generador de contenido con IA</h1>

          <p>
            Crea piezas de contenido para Megactivo, agenda la publicación en el
            calendario del cliente y deja cada propuesta lista para aprobación.
          </p>
        </div>

        <div className="hero-mark">
          <img
            src="/megactivo-icon.png"
            alt="Ícono Megactivo"
            className="hero-icon"
          />
        </div>
      </section>

      <section className="form-card">
        <form className="content-form" onSubmit={handleSubmit}>
          <div className="form-row two-columns">
            <div className="form-group">
              <label htmlFor="plataforma">Plataforma</label>

              <select
                id="plataforma"
                name="plataforma"
                value={formData.plataforma}
                onChange={handleChange}
              >
                <option value="Instagram">Instagram</option>
                <option value="LinkedIn">LinkedIn</option>
                <option value="Ambas">Ambas</option>
              </select>
            </div>

            <div className="form-group">
              <label htmlFor="formato_contenido">Formato de contenido</label>

              <select
                id="formato_contenido"
                name="formato_contenido"
                value={formData.formato_contenido}
                onChange={handleChange}
              >
                {formatosDisponibles.map((formato) => (
                  <option key={formato.value} value={formato.value}>
                    {formato.label}
                  </option>
                ))}
              </select>
            </div>
          </div>

          {formatoSeleccionado && (
            <div className="format-helper">
              <span>Formato seleccionado</span>
              <strong>{formatoSeleccionado.label}</strong>
              <p>{formatoSeleccionado.description}</p>
            </div>
          )}

          <div className="compatibility-box">
            <span>Compatibilidad activa</span>
            <p>
              {formData.plataforma === "Instagram" &&
                "Instagram permite Post estático, Carrusel, Story y Guión Reel."}
              {formData.plataforma === "LinkedIn" &&
                "LinkedIn permite únicamente Post estático y Carrusel."}
              {formData.plataforma === "Ambas" &&
                "Para publicar en ambas plataformas, se permite Post estático o Carrusel."}
            </p>
          </div>

          <div className="form-group">
            <label htmlFor="objetivo_post">Objetivo del contenido</label>

            <textarea
              id="objetivo_post"
              name="objetivo_post"
              value={formData.objetivo_post}
              onChange={handleChange}
              rows="5"
              placeholder="Ejemplo: Crear un post educativo sobre los beneficios de automatizar procesos contables para empresarios."
            />
          </div>

          <div className="form-row three-columns">
            <div className="form-group">
              <label htmlFor="fecha_publicacion">Fecha sugerida</label>

              <input
                id="fecha_publicacion"
                name="fecha_publicacion"
                type="date"
                min={hoy}
                value={formData.fecha_publicacion}
                onChange={handleChange}
                className="calendar-input"
              />
            </div>

            <div className="form-group">
              <label htmlFor="hora_publicacion">Hora sugerida</label>

              <select
                id="hora_publicacion"
                name="hora_publicacion"
                value={formData.hora_publicacion}
                onChange={handleChange}
              >
                {opcionesHora.map((hora) => (
                  <option key={hora.value} value={hora.value}>
                    {hora.label}
                  </option>
                ))}
              </select>
            </div>

            <div className="form-group">
              <label htmlFor="calendar_provider">Calendario</label>

              <select
                id="calendar_provider"
                name="calendar_provider"
                value={formData.calendar_provider}
                onChange={handleChange}
              >
                <option value="google">Google Calendar</option>
                <option value="microsoft">Microsoft Outlook</option>
              </select>
            </div>
          </div>

          {error && <div className="alert-error">{error}</div>}

          <button type="submit" disabled={loading}>
            {loading ? "Generando contenido..." : "Generar contenido"}
          </button>
        </form>

        {resultado && (
          <section className="result-card">
            <div className="result-header">
              <span>Resultado generado</span>
              <strong>{resultado.estado || "Pendiente aprobación"}</strong>
            </div>

            <div className="result-grid">
              <div>
                <span>Cliente</span>
                <strong>{resultado.cliente || "Megactivo"}</strong>
              </div>

              <div>
                <span>Plataforma</span>
                <strong>{resultado.plataforma || formData.plataforma}</strong>
              </div>

              <div>
                <span>Formato</span>
                <strong>
                  {resultado.formato_contenido ||
                    resultado.formato ||
                    formData.formato_contenido}
                </strong>
              </div>

              <div>
                <span>Calendario</span>
                <strong>
                  {resultado.calendar_provider || formData.calendar_provider}
                </strong>
              </div>
            </div>

            {resultado.copy && (
              <div className="copy-box">
                <span>Copy generado</span>
                <p>{resultado.copy}</p>
              </div>
            )}

            {resultado.hashtags && resultado.hashtags.length > 0 && (
              <div className="hashtags">
                {resultado.hashtags.map((hashtag, index) => (
                  <span key={index}>{hashtag}</span>
                ))}
              </div>
            )}

            {resultado.design_spec && (
              <div className="code-box">
                <span>Design spec</span>
                <pre>{JSON.stringify(resultado.design_spec, null, 2)}</pre>
              </div>
            )}

            {resultado.calendar_event?.id && (
              <div className="calendar-box">
                <span>ID del evento en calendario</span>
                <code>{resultado.calendar_event.id}</code>
              </div>
            )}

            {resultado.preview_png_url && (
              <div className="calendar-box">
                <span>Preview PNG</span>
                <code>{resultado.preview_png_url}</code>
              </div>
            )}
          </section>
        )}
      </section>
    </main>
  );
}

export default App;