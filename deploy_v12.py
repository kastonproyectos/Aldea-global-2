import re

HTML_PATH = "index.html"
CSS_PATH = "styles.css"
JS_PATH = "script.js"

# ======================= HTML ======================= #
with open(HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. DOFA Grid Replacement (Exact D-O-F-A with Solid Colors)
dofa_new = """                <div class="dofa-grid-dense">
                    <!-- D -->
                    <div class="dofa-card card-shadow dofa-card-d text-white">
                        <div class="dofa-head text-white">
                            <h3 data-i18n="dofa_weak_title">Debilidades</h3>
                        </div>
                        <div class="text-white text-justify dofa-inject" data-i18n="dofa_weak_desc"></div>
                    </div>
                    <!-- O -->
                    <div class="dofa-card card-shadow dofa-card-o text-black">
                        <div class="dofa-head text-black">
                            <h3 data-i18n="dofa_opp_title">Oportunidades</h3>
                        </div>
                        <div class="text-black text-justify dofa-inject" data-i18n="dofa_opp_desc"></div>
                    </div>
                    <!-- F -->
                    <div class="dofa-card card-shadow dofa-card-f text-white">
                        <div class="dofa-head text-white">
                            <h3 data-i18n="dofa_str_title">Fortalezas</h3>
                        </div>
                        <div class="text-white text-justify dofa-inject" data-i18n="dofa_str_desc"></div>
                    </div>
                    <!-- A -->
                    <div class="dofa-card card-shadow dofa-card-a text-white">
                        <div class="dofa-head text-white">
                            <h3 data-i18n="dofa_thr_title">Amenazas</h3>
                        </div>
                        <div class="text-white text-justify dofa-inject" data-i18n="dofa_thr_desc"></div>
                    </div>
                </div>"""
html = re.sub(r'<div class="dofa-grid-dense">.*?</div>\s*</div>\s*</section>', dofa_new + '\n            </div>\n        </section>', html, flags=re.DOTALL)

# 2. BMC Grid Replacement (3x3 Centered, VP in Middle)
bmc_new = """                <div class="title-wrapper">
                    <h2 class="section-title text-center text-black" data-i18n="bmc_title">Business Model Canvas</h2>
                    <div class="tooltip-container">i<span class="tooltip-text" data-i18n="tooltip_bmc">Estructura estratégica del modelo de negocio de UMO, diseñada a partir del análisis de capacidades internas y necesidades del mercado estadounidense.</span></div>
                </div>
                <div class="bmc-grid-complex">
                    <!-- Top Row -->
                    <div class="bmc-card card-shadow border-solid-black">
                        <h4 data-i18n="bmc_key_partners" class="text-black">Socios Clave (Key Partners)</h4>
                        <div data-i18n="bmc_kp_desc" class="bmc-inject"></div>
                    </div>
                    <div class="bmc-card card-shadow border-solid-black">
                        <h4 data-i18n="bmc_key_activities" class="text-black">Actividades Clave (Key Activities)</h4>
                        <div data-i18n="bmc_ka_desc" class="bmc-inject"></div>
                    </div>
                    <div class="bmc-card card-shadow border-solid-black">
                        <h4 data-i18n="bmc_key_resources" class="text-black">Recursos Clave (Key Resources)</h4>
                        <div data-i18n="bmc_kr_desc" class="bmc-inject"></div>
                    </div>
                    
                    <!-- Mid Row -->
                    <div class="bmc-card card-shadow border-solid-black">
                        <h4 data-i18n="bmc_customer_relation" class="text-black">Relaciones con Clientes (Customer Relationships)</h4>
                        <div data-i18n="bmc_cr_desc" class="bmc-inject"></div>
                    </div>
                    <div class="bmc-card card-shadow bmc-vp-solid">
                        <h4 data-i18n="bmc_value_prop" class="text-white">Propuesta de Valor (Value Proposition)</h4>
                        <div data-i18n="bmc_vp_desc" class="text-white bmc-inject"></div>
                    </div>
                    <div class="bmc-card card-shadow border-solid-black">
                        <h4 data-i18n="bmc_channels" class="text-black">Canales (Channels)</h4>
                        <div data-i18n="bmc_ch_desc" class="bmc-inject"></div>
                    </div>

                    <!-- Bottom Row -->
                    <div class="bmc-card card-shadow border-solid-black">
                        <h4 data-i18n="bmc_customer_segments" class="text-black">Segmentos de Clientes (Customer Segments)</h4>
                        <div data-i18n="bmc_cs_desc" class="bmc-inject"></div>
                    </div>
                    <div class="bmc-card card-shadow border-solid-black">
                        <h4 data-i18n="bmc_cost_structure" class="text-black">Estructura de Costos (Cost Structure)</h4>
                        <div data-i18n="bmc_cost_desc" class="bmc-inject"></div>
                    </div>
                    <div class="bmc-card card-shadow border-solid-black">
                        <h4 data-i18n="bmc_revenue" class="text-black">Fuentes de Ingresos (Revenue Streams)</h4>
                        <div data-i18n="bmc_rev_desc" class="bmc-inject"></div>
                    </div>
                </div>"""
html = re.sub(r'<div class="title-wrapper">\s*<h2 class="section-title text-center text-black" data-i18n="bmc_title">Business Model Canvas</h2>.*?</div>\s*</div>\s*</section>\s*<!-- Literal Copy 3: DPI Radar -->', bmc_new + '\n            </div>\n        </section>\n\n        <!-- Literal Copy 3: DPI Radar -->', html, flags=re.DOTALL)

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html)


# ======================= CSS ======================= #
with open(CSS_PATH, "r", encoding="utf-8") as f:
    css = f.read()

# Sanitize any old bmc overrides
css = re.sub(r'/\* --- V11 OVERRIDE: BMC & DOFA GRIDS --- \*/.*', '', css, flags=re.DOTALL)

css_override = """
/* --- MASTER DOFA V12 --- */
.dofa-grid-dense {
    display: grid !important;
    grid-template-columns: repeat(2, 1fr) !important;
    grid-template-rows: auto auto;
    gap: 20px !important;
}
@media (max-width: 768px) {
    .dofa-grid-dense { grid-template-columns: 1fr !important; }
}
.dofa-card {
    padding: 25px !important;
    border-radius: 8px !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.12) !important;
    height: 100%;
}
.dofa-card-f { background-color: #3B65B9 !important; border: none !important; } /* Azul */
.dofa-card-d { background-color: #FF8201 !important; border: none !important; } /* Naranja */
.dofa-card-o { background-color: #F4F4F5 !important; border: 1px solid #ddd !important; } /* Gris Claro */
.dofa-card-a { background-color: #E26D6D !important; border: none !important; } /* Rojo Suave */

.dofa-list li {
    line-height: 1.5 !important;
    margin-bottom: 0.1rem;
    text-align: left;
}

/* --- MASTER BMC 3x3 COLUMNS 90% V12 --- */
.bmc-grid-complex {
    display: grid !important;
    grid-template-columns: repeat(3, 1fr) !important;
    grid-template-areas: none !important;
    gap: 20px !important;
    width: 90% !important;
    margin: 2rem auto !important;
}
@media (max-width: 900px) {
    .bmc-grid-complex { grid-template-columns: 1fr !important; width: 100% !important; }
}
.bmc-card {
    padding: 25px !important;
    border-radius: 8px !important;
    background: var(--white);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08) !important;
    border: 1px solid var(--black) !important;
}
.bmc-card h4 {
    margin-bottom: 1rem;
}
.bmc-vp-solid {
    background: var(--orange) !important;
    border: 3px solid var(--black) !important;
    box-shadow: 0 8px 30px rgba(255, 130, 1, 0.5) !important;
    transform: scale(1.05) !important;
    z-index: 10;
}
.bmc-list li {
    line-height: 1.5 !important;
    margin-bottom: 0.5rem !important;
    font-size: 0.95rem !important;
    text-align: left;
}
"""
css += css_override
with open(CSS_PATH, "w", encoding="utf-8") as f:
    f.write(css)


# ======================= JS ======================= #
with open(JS_PATH, "r", encoding="utf-8") as f:
    js = f.read()

# Exact Dictionary Injection using Regex
new_es_keys = """        // BMC EXACT REPLACEMENTS
        tooltip_bmc: "Estructura estratégica del modelo de negocio de UMO, diseñada a partir del análisis de capacidades internas y necesidades del mercado estadounidense.",
        bmc_kp_desc: "<ul class='bmc-list'><li>Proveedores de materias primas.</li><li>Operadores logísticos y transportadores.</li><li>Agentes de aduana y comercio exterior.</li><li>Distribuidores de maquinaria agrícola en Estados Unidos.</li><li>Comercializadores de repuestos.</li><li>Aliados comerciales en estados objetivo.</li><li>Ferias, gremios o redes del sector agrícola.</li></ul>",
        bmc_ka_desc: "<ul class='bmc-list'><li>Fabricación de sillines.</li><li>Control de calidad.</li><li>Gestión de compras de materias primas e insumos.</li><li>Desarrollo y ajuste del producto según necesidad del cliente.</li><li>Cotización, negociación y cierre de ventas.</li><li>Investigación de mercado en estados objetivo.</li></ul>",
        bmc_kr_desc: "<ul class='bmc-list'><li>Maquinaria y equipos de fabricación.</li><li>Materias primas e insumos.</li><li>Conocimiento técnico del producto.</li><li>Equipo de producción.</li><li>Equipo comercial.</li><li>Certificaciones y respaldo empresarial.</li><li>Infraestructura física de producción.</li><li>Base de contactos comerciales y posibles clientes.</li></ul>",
        bmc_vp_desc: "UMO ofrece sillines para podadoras agrícolas dirigidos al mercado de Estados Unidos, brindando a distribuidores y comercializadores una alternativa confiable cuando los repuestos 'gringos' no están disponibles o resultan poco convenientes en costo. Su propuesta de valor no se basa en competir directamente con las marcas líderes más grandes, sino en convertirse en una alternativa confiable cuando el repuesto original no sea posible de conseguir.",
        bmc_cr_desc: "<ul class='bmc-list'><li>Relación B2B directa con distribuidores y empresas comercializadoras.</li><li>Atención personalizada para clientes.</li><li>Seguimiento por WhatsApp, correo y llamadas.</li></ul>",
        bmc_ch_desc: "<ul class='bmc-list'><li>Venta directa a distribuidores de maquinaria agrícola.</li><li>Llamadas y número telefónico empresarial.</li><li>WhatsApp Business.</li><li>Página web.</li><li>Linkedin para contacto B2B.</li></ul>",
        bmc_cs_desc: "<ul class='bmc-list'><li>Empresas distribuidoras de maquinaria agrícola en Estados Unidos.</li><li>Tiendas o dealers que venden equipos para fincas y operación agrícola.</li></ul>",
        bmc_cost_desc: "<ul class='bmc-list'><li>Costos de materias primas.</li><li>Costos de producción y ensamble.</li><li>Mano de obra.</li><li>Costos de empaque.</li><li>Transporte y logística.</li><li>Costos de exportación.</li><li>Aranceles, trámites y documentación.</li><li>Marketing y presencia digital.</li><li>Costos administrativos.</li><li>Mantenimiento de maquinaria y operación.</li></ul>",
        bmc_rev_desc: "<ul class='bmc-list'><li>Venta de sillines para landmowers agrícolas a distribuidores.</li><li>Venta por volumen a comercializadores.</li><li>Ingresos por pedidos recurrentes.</li></ul>",

        // DOFA EXACT REPLACEMENTS
        dofa_str_title: "Fortalezas",
        dofa_str_desc: "<ul class='dofa-list'><li>Trayectoria de 57 años, tecnología propia de inyección de poliuretano, respaldo como proveedor OEM de Harley Davidson y Yamaha, y alta flexibilidad para diseños personalizados.</li></ul>",
        dofa_weak_title: "Debilidades",
        dofa_weak_desc: "<ul class='dofa-list'><li>Brecha de bilingüismo en el personal operativo y falta de plan de incentivos para actividades en el exterior (Diagnóstico P-I, 2026).</li></ul>",
        dofa_opp_title: "Oportunidades",
        dofa_opp_desc: "<ul class='dofa-list'><li>Auge de tecnologías eléctricas en podadoras y alta demanda en Missouri/Oklahoma (Emergen Research, 2025; USDA, 2025).</li></ul>",
        dofa_thr_title: "Amenazas",
        dofa_thr_desc: "<ul class='dofa-list'><li>Normativas de seguridad SAE y competencia de fabricantes OEM originales (Data Bridge Market Research, 2024).</li></ul>",
"""

new_en_keys = """        // BMC EXACT REPLACEMENTS (Translated)
        tooltip_bmc: "Strategic structure of UMOs business model, designed from the analysis of internal capabilities and the needs of the US market.",
        bmc_kp_desc: "<ul class='bmc-list'><li>Raw material suppliers.</li><li>Logistics and transport operators.</li><li>Customs and foreign trade agents.</li><li>Agricultural machinery distributors in the United States.</li><li>Spare parts marketers.</li><li>Commercial allies in target states.</li><li>Fairs, guilds, or networks in the agricultural sector.</li></ul>",
        bmc_ka_desc: "<ul class='bmc-list'><li>Saddle manufacturing.</li><li>Quality control.</li><li>Purchasing management of raw materials and supplies.</li><li>Product development and adjustment according to customer needs.</li><li>Quotation, negotiation, and closing of sales.</li><li>Market research in target states.</li></ul>",
        bmc_kr_desc: "<ul class='bmc-list'><li>Manufacturing machinery and equipment.</li><li>Raw materials and supplies.</li><li>Technical knowledge of the product.</li><li>Production team.</li><li>Commercial team.</li><li>Certifications and corporate backing.</li><li>Physical production infrastructure.</li><li>Database of commercial contacts and potential clients.</li></ul>",
        bmc_vp_desc: "UMO offers saddles for agricultural mowers targeting the US market, providing distributors and marketers with a reliable alternative when original parts are unavailable or cost-prohibitive. Its value proposition is not based on competing directly with major leading brands, but rather on becoming a reliable alternative when the original spare part cannot be obtained.",
        bmc_cr_desc: "<ul class='bmc-list'><li>Direct B2B relationship with distributors and trading companies.</li><li>Personalized customer service.</li><li>Follow-up via WhatsApp, email, and calls.</li></ul>",
        bmc_ch_desc: "<ul class='bmc-list'><li>Direct sales to agricultural machinery distributors.</li><li>Calls and corporate phone numbers.</li><li>WhatsApp Business.</li><li>Website.</li><li>LinkedIn for B2B contact.</li></ul>",
        bmc_cs_desc: "<ul class='bmc-list'><li>Agricultural machinery distribution companies in the United States.</li><li>Stores or dealers selling equipment for farms and agricultural operations.</li></ul>",
        bmc_cost_desc: "<ul class='bmc-list'><li>Cost of raw materials.</li><li>Production and assembly costs.</li><li>Labor.</li><li>Packaging costs.</li><li>Transport and logistics.</li><li>Export costs.</li><li>Tariffs, procedures, and documentation.</li><li>Marketing and digital presence.</li><li>Administrative costs.</li><li>Machinery maintenance and operation.</li></ul>",
        bmc_rev_desc: "<ul class='bmc-list'><li>Sale of agricultural lawnmower saddles to distributors.</li><li>Volume sales to marketers.</li><li>Income from recurring orders.</li></ul>",

        // DOFA EXACT REPLACEMENTS (Translated)
        dofa_str_title: "Strengths",
        dofa_str_desc: "<ul class='dofa-list'><li>57-year trajectory, proprietary polyurethane injection technology, backing as an OEM supplier for Harley Davidson and Yamaha, and high flexibility for custom designs.</li></ul>",
        dofa_weak_title: "Weaknesses",
        dofa_weak_desc: "<ul class='dofa-list'><li>Bilingualism gap within operating personnel and lack of incentive plan for activities abroad (Diagnostic P-I, 2026).</li></ul>",
        dofa_opp_title: "Opportunities",
        dofa_opp_desc: "<ul class='dofa-list'><li>Rise of electric technologies in lawmowers and high demand in Missouri/Oklahoma (Emergen Research, 2025; USDA, 2025).</li></ul>",
        dofa_thr_title: "Threats",
        dofa_thr_desc: "<ul class='dofa-list'><li>SAE safety regulations and competition from original OEM manufacturers (Data Bridge Market Research, 2024).</li></ul>",
"""

# Completely wipe existing bmc and dofa keys from es and en using dumb replacement 
js = re.sub(r'bmc_title:\s*"Business Model Canvas",.*?dpi_title:', 'bmc_title: "Business Model Canvas",\n' + new_es_keys + '\n        dpi_title:', js, flags=re.DOTALL)
js = re.sub(r'dofa_title:\s*"Análisis DOFA de la Empresa UMO",.*?(?:sust_title:|intro_viab:)', 'dofa_title: "Análisis DOFA de la Empresa UMO",\n' + new_es_keys[new_es_keys.find('dofa_str_title'):] + '\n        sust_title:', js, flags=re.DOTALL)

# For EN, we find the "en: {" marker, but JS might have it malformed.
# Actually we can just inject into en if we find it.
en_idx = js.find('en: {')
if en_idx != -1:
    js = js[:en_idx+5] + '\n' + new_en_keys + js[en_idx+5:]

with open(JS_PATH, "w", encoding="utf-8") as f:
    f.write(js)

print("SUCCESS: V12 Structural Deployment Completed Locally.")
