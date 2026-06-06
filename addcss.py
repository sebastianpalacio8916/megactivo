css = """

/* ─── ReactDataRenderer ─────────────────────────────────────────────── */
.rd-wrapper {
  margin-top: 16px;
}

.rd-post {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.rd-section {
  background: #f8f9fb;
  border-radius: 10px;
  padding: 14px 16px;
  border-left: 3px solid #d1d5db;
}

.rd-section span {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #6b7280;
  display: block;
  margin-bottom: 6px;
}

.rd-section p {
  margin: 0;
  font-size: 0.92rem;
  color: #1f2937;
  line-height: 1.55;
}

.rd-hook  { border-left-color: #6366f1; }
.rd-cuerpo { border-left-color: #10b981; }
.rd-cierre { border-left-color: #f59e0b; }
.rd-cta   { border-left-color: #ef4444; }

/* Carrusel */
.rd-carrusel-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 12px;
}

.rd-slide {
  background: #f8f9fb;
  border-radius: 10px;
  padding: 14px;
  border: 1px solid #e5e7eb;
  position: relative;
}

.rd-slide-badge {
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #6366f1;
  background: #ede9fe;
  border-radius: 4px;
  padding: 2px 6px;
  display: inline-block;
  margin-bottom: 8px;
}

.rd-slide-titulo {
  font-weight: 600;
  font-size: 0.88rem;
  color: #1f2937;
  margin-bottom: 6px;
  display: block;
}

.rd-slide-cuerpo {
  font-size: 0.82rem;
  color: #4b5563;
  line-height: 1.5;
}

/* Story */
.rd-story-grid {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.rd-frame {
  width: 160px;
  min-height: 280px;
  background: #111827;
  border-radius: 18px;
  padding: 18px 14px;
  color: #f9fafb;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.rd-frame-num {
  font-size: 0.7rem;
  color: #9ca3af;
}

.rd-frame-texto {
  font-size: 0.84rem;
  line-height: 1.55;
  flex: 1;
}

.rd-frame-cta {
  font-size: 0.78rem;
  font-weight: 700;
  color: #818cf8;
}

/* Guion Reel */
.rd-reel-timeline {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.rd-escena {
  display: flex;
  gap: 12px;
  align-items: flex-start;
}

.rd-escena-num {
  font-size: 0.72rem;
  font-weight: 700;
  color: #ffffff;
  background: #6366f1;
  border-radius: 50%;
  width: 22px;
  height: 22px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  margin-top: 2px;
}

.rd-escena-body {
  flex: 1;
  background: #f8f9fb;
  border-radius: 8px;
  padding: 10px 12px;
  font-size: 0.86rem;
  color: #1f2937;
  line-height: 1.5;
}

.rd-escena-tipo {
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  color: #9ca3af;
  margin-bottom: 4px;
  display: block;
}

/* ─── Approval section ───────────────────────────────────────────────── */
.approval-section {
  margin-top: 20px;
  padding-top: 20px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.approval-section label {
  font-size: 0.82rem;
  font-weight: 600;
  color: #374151;
}

.approval-section textarea {
  width: 100%;
  border: 1px solid #d1d5db;
  border-radius: 10px;
  padding: 10px 12px;
  font-size: 0.9rem;
  color: #1f2937;
  resize: vertical;
  font-family: inherit;
  box-sizing: border-box;
}

.approval-section textarea:focus {
  outline: none;
  border-color: #6366f1;
}

.approval-actions {
  display: flex;
  gap: 12px;
}

.btn-approve,
.btn-reject {
  flex: 1;
  padding: 10px 16px;
  border: none;
  border-radius: 10px;
  font-weight: 700;
  font-size: 0.9rem;
  cursor: pointer;
  transition: opacity 0.2s;
}

.btn-approve:disabled,
.btn-reject:disabled {
  opacity: 0.55;
  cursor: not-allowed;
}

.btn-approve {
  background: #10b981;
  color: #ffffff;
}

.btn-approve:hover:not(:disabled) {
  background: #059669;
}

.btn-reject {
  background: #ef4444;
  color: #ffffff;
}

.btn-reject:hover:not(:disabled) {
  background: #dc2626;
}

.approval-err {
  font-size: 0.84rem;
  color: #dc2626;
  background: #fef2f2;
  border-radius: 8px;
  padding: 10px 12px;
  margin: 0;
}

.approval-ok {
  background: #ecfdf5;
  border: 1px solid #6ee7b7;
  border-radius: 10px;
  padding: 14px 16px;
  color: #065f46;
}

.approval-rej {
  background: #fef2f2;
  border: 1px solid #fca5a5;
  border-radius: 10px;
  padding: 14px 16px;
  color: #7f1d1d;
}

.approval-ok strong,
.approval-rej strong {
  display: block;
  font-size: 0.9rem;
  margin-bottom: 6px;
}

.approval-ok p,
.approval-rej p {
  margin: 0;
  font-size: 0.86rem;
  line-height: 1.5;
}
"""

with open("megactivo-main/src/App.css","r",encoding="utf-8") as fh:
    existing = fh.read()

with open("megactivo-main/src/App.css","w",encoding="utf-8") as fh:
    fh.write(existing + css)

print("OK CSS appended")
