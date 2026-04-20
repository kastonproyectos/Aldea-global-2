import re
import os

HTML_PATH = "index.html"
CSS_PATH = "styles.css"
JS_PATH = "script.js"

# ----------------- HTML -----------------
with open(HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# Replace DOFA Grid inner block 
dofa_new_html = """                <div class="dofa-grid-dense">
                    <!-- D -->
                    <div class="dofa-card card-shadow dofa-card-d text-white">
                        <div class="dofa-head text-white">
                            <h3 data-i18n="dofa_weak_title">D - Debilidades</h3>
                        </div>
                        <p class="text-justify text-white" data-i18n="dofa_weak_desc">En cuanto a las debilidades...</p>
                    </div>
                    <!-- O -->
                    <div class="dofa-card card-shadow dofa-card-o text-black">
                        <div class="dofa-head text-black">
                            <h3 data-i18n="dofa_opp_title">O - Oportunidades</h3>
                        </div>
                        <p class="text-justify text-black" data-i18n="dofa_opp_desc">En el contexto internacional...</p>
                    </div>
                    <!-- F -->
                    <div class="dofa-card card-shadow dofa-card-f text-white">
                        <div class="dofa-head text-white">
                            <h3 data-i18n="dofa_str_title">F - Fortalezas</h3>
                        </div>
                        <p class="text-justify text-white" data-i18n="dofa_str_desc">Las fortalezas presentadas...</p>
                    </div>
                    <!-- A -->
                    <div class="dofa-card card-shadow dofa-card-a text-white">
                        <div class="dofa-head text-white" style="color:white !important;">
                            <h3 data-i18n="dofa_thr_title">A - Amenazas</h3>
                        </div>
                        <p class="text-justify text-white" data-i18n="dofa_thr_desc">En cuanto a las amenazas...</p>
                    </div>
                </div>"""

# Find DOFA Block
dofa_grid_pattern = re.compile(r'<div class=\"dofa-grid-dense\">.*?</div>\s*</div>\s*</section>', re.DOTALL)
html = dofa_grid_pattern.sub(dofa_new_html + '\n            </div>\n        </section>', html)

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html)

# ----------------- CSS -----------------
with open(CSS_PATH, "r", encoding="utf-8") as f:
    css = f.read()

css_override = """
/* --- MASTER DOFA V12 --- */
.dofa-grid-dense {
    display: grid !important;
    grid-template-columns: repeat(2, 1fr) !important;
    grid-template-rows: 1fr 1fr;
    gap: 20px !important;
}
@media (max-width: 768px) {
    .dofa-grid-dense { grid-template-columns: 1fr !important; }
}
.dofa-card {
    padding: 25px !important;
    border-radius: 6px !important;
    box-shadow: 0 6px 20px rgba(0,0,0,0.12) !important;
    height: 100%;
}
.dofa-card-f { background-color: #3B65B9 !important; border: none !important; } /* Azul */
.dofa-card-d { background-color: #FF8201 !important; border: none !important; } /* Naranja */
.dofa-card-o { background-color: #F4F4F5 !important; border: 1px solid #ddd !important; } /* Gris Claro */
.dofa-card-a { background-color: #E26D6D !important; border: none !important; } /* Rojo Suave */

.dofa-list li {
    line-height: 1.5 !important;
    margin-bottom: 0.8rem;
    text-align: left;
}

/* --- MASTER BMC 3 COLUMNS 90% V12 --- */
.bmc-grid-complex {
    display: grid !important;
    grid-template-columns: repeat(3, 1fr) !important;
    grid-template-areas: none !important;
    gap: 1.5rem !important;
    width: 90% !important;
    margin: 0 auto !important;
}
.bmc-col {
    display: block;
}
@media (max-width: 900px) {
    .bmc-grid-complex { grid-template-columns: 1fr !important; grid-template-areas: none !important; }
}
.bmc-card {
    padding: 25px !important;
    border-radius: 6px !important;
    background: var(--white);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08) !important;
}
.bmc-vp-solid {
    background: var(--orange) !important;
    border: 3px solid var(--black) !important;
    box-shadow: 0 8px 30px rgba(255, 130, 1, 0.5) !important;
}
.bmc-list li {
    line-height: 1.4 !important;
    margin-bottom: 0.4rem !important; /* Returning to less stretchy */
    font-size: 0.9rem !important;
}
"""
css += css_override
with open(CSS_PATH, "w", encoding="utf-8") as f:
    f.write(css)

# ----------------- JS -----------------
with open(JS_PATH, "r", encoding="utf-8") as f:
    js = f.read()

es_dofa_str = "dofa_str_desc: \"Fortalezas (F): Trayectoria de 57 años corporativa estructurada, tecnología de inyección de poliuretano propia, robusto respaldo demostrable como proveedor OEM para Harley Davidson/Yamaha y flexibilidad productiva industrial para adaptaciones de diseño exactas al estándar del mercado estadounidense.\","
new_es_dofa = """        dofa_str_title: "Fortalezas (F)",
        dofa_str_desc: "<ul class='bmc-list dofa-list'><li>Trayectoria de 57 años.</li><li>Tecnología propia de inyección de poliuretano.</li><li>Respaldo como proveedor OEM (Original Equipment Manufacturer) de marcas élite como Harley Davidson y Yamaha.</li><li>Alta flexibilidad para diseños personalizados.</li></ul>",
        dofa_weak_title: "Debilidades (D)",
        dofa_weak_desc: "<ul class='bmc-list dofa-list'><li>Brecha de bilingüismo en el personal operativo.</li><li>Falta de plan de incentivos para actividades en el exterior (Diagnóstico P-I, 2026).</li></ul>",
        dofa_opp_title: "Oportunidades (O)",
        dofa_opp_desc: "<ul class='bmc-list dofa-list'><li>Auge de tecnologías eléctricas en podadoras.</li><li>Alta demanda en Missouri/Oklahoma (Emergen Research, 2025; USDA, 2025).</li></ul>",
        dofa_thr_title: "Amenazas (A)",
        dofa_thr_desc: "<ul class='bmc-list dofa-list'><li>Normativas de seguridad SAE.</li><li>Competencia de fabricantes OEM originales (Data Bridge Market Research, 2024).</li></ul>","""

js = re.sub(r'dofa_str_title:\s*"Fortalezas",.*?dofa_thr_desc:\s*".*?",', new_es_dofa, js, flags=re.DOTALL)

# Same for EN Dictionary (which might not be fully formed yet so we just locate 'en: {')
en_keys = """
        tooltip_about: "Strategic extraction from corporate executive interviews defining OEM capabilities.",
        intro_about: "Technical introduction to base industrial capacity, detailing export infrastructure and assembly origins.",
        intro_bmc: "Full Canvas breakdown optimized for direct B2B distributorship strategies.",
        tooltip_bmc: "Strategic layout built from original corporative BMC models targeting the North American agrarian sector.",
        intro_dpi: "DPI (Diagnostic of Potential Internationalization) is a mathematical framework indexing local readiness against foreign barriers.",
        tooltip_dpi: "Modeled from the Results spreadsheet, contrasting real metrics vs maximum thresholds.",
        intro_dofa: "Transversal strategic breakdown of UMOs internal virtues and external frictions mapped to the US base.",
        tooltip_dofa: "Designed cross-matching directive feedback with foreign automotive requirements.",
        intro_sust: "Sustainability integration matching strict ESG norms mandated by US regulations.",
        tooltip_sust: "Assembled strictly following platform guidelines regarding the Sustainability Podcast module.",
        intro_viab: "Identifying the safest landing spot inside the worlds largest economy requires rigorous NASS operations data.",
        tooltip_viab: "Mined from state tax profiling, NASS operations maps, and ITC trade balance logs.",
        intro_smart: "Definitive milestone conjugated mathematically matching the 0.457 DPI ceiling with raw geo-agricultural volume targets.",
        tooltip_smart: "Why this objective? Feasibility: Missouri and Oklahoma selected due to potent neutral structure natively. Capacity: 1,000 unit throughput handles UMOs OEM output.",
        
        // Replicating BMC bullet points for EN
        bmc_kp_desc: "<ul class='bmc-list'><li>Raw material suppliers.</li><li>Logistics operators.</li><li>Customs agencies.</li><li>Agricultural machinery distributors in the US.</li><li>Spare parts marketers.</li><li>Commercial allies.</li></ul>",
        bmc_ka_desc: "<ul class='bmc-list'><li>Saddle manufacturing.</li><li>Quality control.</li><li>Purchasing management.</li><li>Product development and adjustment.</li><li>Market research.</li></ul>",
        bmc_vp_desc: "<ul class='bmc-list'><li>Premium B2B value proposition.</li><li>Injected polyurethane saddles adapted for US lawnmowers.</li><li>Reliable alternative to unavailable OEM parts.</li><li>Demonstrable OEM track record with Harley Davidson and Yamaha.</li></ul>",
        bmc_cr_desc: "<ul class='bmc-list'><li>Direct B2B relationship with distributors.</li><li>Customized customer attention.</li><li>Follow-up via WhatsApp, email, and calls.</li></ul>",
        bmc_cs_desc: "<ul class='bmc-list'><li>Agricultural machinery distributors in MO/OK.</li><li>Dealerships selling farming equipment.</li><li>Mechanical repair centers.</li></ul>",
        bmc_kr_desc: "<ul class='bmc-list'><li>Manufacturing machinery and equipment.</li><li>Raw materials.</li><li>Technical product knowledge.</li><li>Production and commercial teams.</li></ul>",
        bmc_ch_desc: "<ul class='bmc-list'><li>Direct B2B sales.</li><li>Business contacts.</li><li>Website and LinkedIn.</li></ul>",
        bmc_cost_desc: "<ul class='bmc-list'><li>Raw materials cost.</li><li>Production chain costs.</li><li>Shipping and export tariffs.</li><li>Administrative and marketing tools.</li></ul>",
        bmc_rev_desc: "<ul class='bmc-list'><li>Wholesale revenue via direct B2B.</li><li>Scalability income from recurrent OEM requests.</li></ul>",

        // DOFA Translated
        dofa_str_title: "Strengths (S)",
        dofa_str_desc: "<ul class='bmc-list dofa-list'><li>57 years of trajectory.</li><li>In-house polyurethane injection technology.</li><li>Backed as an OEM supplier for elite brands like Harley Davidson and Yamaha.</li><li>High flexibility for custom designs.</li></ul>",
        dofa_weak_title: "Weaknesses (W)",
        dofa_weak_desc: "<ul class='bmc-list dofa-list'><li>Bilingualism gap among operative personnel.</li><li>Lack of an incentive plan for activities abroad (Diagnostic P-I, 2026).</li></ul>",
        dofa_opp_title: "Opportunities (O)",
        dofa_opp_desc: "<ul class='bmc-list dofa-list'><li>Rise of electric technologies in lawmowers.</li><li>High demand in Missouri/Oklahoma (Emergen Research, 2025; USDA, 2025).</li></ul>",
        dofa_thr_title: "Threats (T)",
        dofa_thr_desc: "<ul class='bmc-list dofa-list'><li>SAE safety regulations.</li><li>Competition from original OEM manufacturers (Data Bridge Market Research, 2024).</li></ul>",
"""

en_start = js.find("en: {")
if en_start != -1:
    insertion_point = js.find("{", en_start) + 2
    js = js[:insertion_point] + "\n" + en_keys + js[insertion_point:]
else:
    print("EN Dictionary Not Found!")

with open(JS_PATH, "w", encoding="utf-8") as f:
    f.write(js)
