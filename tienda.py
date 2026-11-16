from flask import Flask, render_template_string

app = Flask(__name__)
ENLACE_WA = "https:" + "//wa.me/524422321087?text=Hola%20ENRIQUEZCO,%20quiero%20cotizar%20serigrafia%20textil"

HTML_TIENDA = """<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ENRIQUEZCO™ | Serigrafía Textil</title><style>
body{font-family:system-ui,sans-serif;background:#0d0f14;color:#f5f5f5;margin:0;line-height:1.6}
nav{background:#090a0e;padding:18px 5%;display:flex;justify-content:center;border-bottom:2px solid #00d2ff}
.logo{font-size:28px;font-weight:900;letter-spacing:3px;color:#fff;text-decoration:none}.logo span{color:#00d2ff}
.hero{text-align:center;padding:70px 20px;background:#131620;border-bottom:1px solid #222634}
.hero h1{font-size:36px;margin-bottom:15px}
.hero p{max-width:600px;margin:0 auto;color:#b0b8d1;font-size:17px}
.btn-cta{display:inline-block;background:#25D366;color:#000;padding:14px 32px;border-radius:8px;font-weight:800;text-decoration:none;margin-top:25px;text-transform:uppercase}
.seccion{max-width:1050px;margin:50px auto;padding:0 20px}
.seccion h2{text-align:center;margin-bottom:30px;font-size:26px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px}
.card{background:#161922;padding:25px;border-radius:12px;border-top:3px solid #f11e9c}
.card h3{color:#fce514;margin-top:0}
.btn-flotante{position:fixed;bottom:25px;right:25px;background:#25D366;color:#000;width:62px;height:62px;border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 15px rgba(0,0,0,0.5);z-index:999;text-decoration:none;font-weight:900;font-size:14px}
footer{text-align:center;padding:30px;margin-top:50px;border-top:1px solid #222634;color:#777;font-size:14px}
</style></head><body>
<nav><a href="/" class="logo">ENRIQUEZ<span>CO</span></a></nav>
<section class="hero"><h1>Serigrafía Textil de Alta Durabilidad</h1>
<p>Estampado profesional sobre playeras, sudaderas, mandiles y bolsas textiles en Querétaro.</p>
<a href="{{ wa }}" class="btn-cta" style="display:inline-flex;align-items:center;gap:8px"><svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.274.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.1.824z"/></svg> Cotizar por WhatsApp</a></section>
<section class="seccion"><h2>Especialidades en Serigrafía Textil</h2><div class="grid">
<div class="card"><h3>Estampado por Volumen</h3><p>Playeras promocionales y uniformes con tintas plastisol y base agua.</p></div>
<div class="card"><h3>Separación de Color</h3><p>Impresión a múltiples tintas sobre prendas claras y oscuras con registro exacto.</p></div>
<div class="card"><h3>Textiles Especiales</h3><p>Sudaderas, mandiles de trabajo y bolsas ecológicas de algodón o poliéster.</p></div></div></section>
<a href="{{ wa }}" class="btn-flotante" style="color:#fff"><svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.274.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.1.824z"/></svg></a>
<footer>&copy; 2026 ENRIQUEZCO&trade; - Soluciones Creativas &amp; Digitales. Marca en uso comercial.</footer>
</body></html>"""

@app.route("/")
def index():
    return render_template_string(HTML_TIENDA, wa=ENLACE_WA)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
