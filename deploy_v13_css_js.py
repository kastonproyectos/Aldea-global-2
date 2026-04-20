import os

CSS_PATH = "styles.css"
JS_PATH = "script.js"

# ----------------- CSS -----------------
with open(CSS_PATH, "r", encoding="utf-8") as f:
    css = f.read()

# Find /* --- MASTER DOFA V12 --- */ if it exists from previous run, wipe it out
purge_idx = css.find('/* --- MASTER DOFA')
if purge_idx != -1:
    css = css[:purge_idx]

css_override = """
/* --- MASTER DOFA V13 --- */
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
    box-shadow: 0 6px 20px rgba(0,0,0,0.12) !important;
    height: 100%;
}
.dofa-card-f { background-color: #3B65B9 !important; border: none !important; } /* Azul */
.dofa-card-d { background-color: #FF8201 !important; border: none !important; } /* Naranja */
.dofa-card-o { background-color: #F4F4F5 !important; border: 1px solid #ddd !important; } /* Gris Claro */
.dofa-card-a { background-color: #E26D6D !important; border: none !important; } /* Rojo Suave */

.dofa-inject ul {
    padding-left: 1.5rem;
    margin-top: 1rem;
}
.dofa-inject li {
    line-height: 1.5 !important;
    margin-bottom: 0.8rem;
    text-align: left;
}

/* --- MASTER BMC 3x3 COLUMNS 90% V13 --- */
.bmc-grid-complex {
    display: grid !important;
    grid-template-columns: repeat(3, 1fr) !important;
    grid-template-areas: none !important;
    gap: 20px !important;
    width: 90% !important;
    margin: 2rem auto !important;
    justify-content: center;
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
.bmc-inject ul {
    padding-left: 1.5rem;
    margin-top: 1rem;
}
.bmc-inject li {
    line-height: 1.5 !important;
    margin-bottom: 0.8rem !important;
    font-size: 0.95rem !important;
    text-align: left;
}
"""
css += css_override
with open(CSS_PATH, "w", encoding="utf-8") as f:
    f.write(css)


# ----------------- JS -----------------
with open(JS_PATH, "r", encoding="utf-8") as f:
    js = f.read()

# Replace Spanish dictionary entirely
es_start = js.find('es: {')
en_start = js.find('en: {')

if es_start != -1 and en_start != -1:
    # Slice the ES dictionary entirely
    es_dict = js[es_start:en_start]
    
    # We will slice out DOFA and BMC sections and repopulate them, OR wipe it all.
    # It's safer to just str.replace the blocks we know inside es_dict
    
    # Wipe out bmc_... and dofa_... lines in es_dict
    import re
    es_dict = re.sub(r'\s*bmc_key_partners:.*?(?=dpi_title)', '\n', es_dict, flags=re.DOTALL)
    es_dict = re.sub(r'\s*dofa_title:.*?(?=sust_title)', '\n', es_dict, flags=re.DOTALL)
    
    # Insert new lines at bottom of es_dict (just before en:)
    insert_idx = es_dict.rfind('},')
    if insert_idx == -1: insert_idx = len(es_dict) - 2
    
    # Exact Content mapped
    es_new_content = """        // BMC EXACT REPLACEMENTS (V13)
        tooltip_bmc: "Estructura estratégica del modelo de negocio de UMO, diseñada a partir del análisis de capacidades internas y necesidades del mercado estadounidense.",
        bmc_key_partners: "Socios Clave (Key Partners)",
        bmc_kp_desc: "<ul><li>Proveedores de materias primas.</li><li>Operadores logísticos y transportadores.</li><li>Agentes de aduana y comercio exterior.</li><li>Distribuidores de maquinaria agrícola en Estados Unidos.</li><li>Comercializadores de repuestos.</li><li>Aliados comerciales en estados objetivo.</li><li>Ferias, gremios o redes del sector agrícola.</li></ul>",
        bmc_key_activities: "Actividades Clave (Key Activities)",
        bmc_ka_desc: "<ul><li>Fabricación de sillines.</li><li>Control de calidad.</li><li>Gestión de compras de materias primas e insumos.</li><li>Desarrollo y ajuste del producto según necesidad del cliente.</li><li>Cotización, negociación y cierre de ventas.</li><li>Investigación de mercado en estados objetivo.</li></ul>",
        bmc_key_resources: "Recursos Clave (Key Resources)",
        bmc_kr_desc: "<ul><li>Maquinaria y equipos de fabricación.</li><li>Materias primas e insumos.</li><li>Conocimiento técnico del producto.</li><li>Equipo de producción.</li><li>Equipo comercial.</li><li>Certificaciones y respaldo empresarial.</li><li>Infraestructura física de producción.</li><li>Base de contactos comerciales y posibles clientes.</li></ul>",
        bmc_value_prop: "Propuesta de Valor (Value Proposition)",
        bmc_vp_desc: "UMO ofrece sillines para podadoras agrícolas dirigidos al mercado de Estados Unidos, brindando a distribuidores y comercializadores una alternativa confiable cuando los repuestos 'gringos' no están disponibles o resultan poco convenientes en costo. Su propuesta de valor no se basa en competir directamente con las marcas líderes más grandes, sino en convertirse en una alternativa confiable cuando el repuesto original no sea posible de conseguir.",
        bmc_customer_relation: "Relaciones con Clientes (Customer Relationships)",
        bmc_cr_desc: "<ul><li>Relación B2B directa con distribuidores y empresas comercializadoras.</li><li>Atención personalizada para clientes.</li><li>Seguimiento por WhatsApp, correo y llamadas.</li></ul>",
        bmc_channels: "Canales (Channels)",
        bmc_ch_desc: "<ul><li>Venta directa a distribuidores de maquinaria agrícola.</li><li>Llamadas y número telefónico empresarial.</li><li>WhatsApp Business.</li><li>Página web.</li><li>Linkedin para contacto B2B.</li></ul>",
        bmc_customer_segments: "Segmentos de Clientes (Customer Segments)",
        bmc_cs_desc: "<ul><li>Empresas distribuidoras de maquinaria agrícola en Estados Unidos.</li><li>Tiendas o dealers que venden equipos para fincas y operación agrícola.</li></ul>",
        bmc_cost_structure: "Estructura de Costos (Cost Structure)",
        bmc_cost_desc: "<ul><li>Costos de materias primas.</li><li>Costos de producción y ensamble.</li><li>Mano de obra.</li><li>Costos de empaque.</li><li>Transporte y logística.</li><li>Costos de exportación.</li><li>Aranceles, trámites y documentación.</li><li>Marketing y presencia digital.</li><li>Costos administrativos.</li><li>Mantenimiento de maquinaria y operación.</li></ul>",
        bmc_revenue: "Fuentes de Ingresos (Revenue Streams)",
        bmc_rev_desc: "<ul><li>Venta de sillines para landmowers agrícolas a distribuidores.</li><li>Venta por volumen a comercializadores.</li><li>Ingresos por pedidos recurrentes.</li></ul>",

        // DOFA EXACT REPLACEMENTS (V13)
        dofa_title: "Análisis DOFA de la Empresa UMO",
        dofa_str_title: "Fortalezas (F)",
        dofa_str_desc: "<ul><li>Trayectoria de 57 años, tecnología propia de inyección de poliuretano, respaldo como proveedor OEM de Harley Davidson y Yamaha, y alta flexibilidad para diseños personalizados.</li></ul>",
        dofa_weak_title: "Debilidades (D)",
        dofa_weak_desc: "<ul><li>Brecha de bilingüismo en el personal operativo y falta de plan de incentivos para actividades en el exterior (Diagnóstico P-I, 2026).</li></ul>",
        dofa_opp_title: "Oportunidades (O)",
        dofa_opp_desc: "<ul><li>Auge de tecnologías eléctricas en podadoras y alta demanda en Missouri/Oklahoma (Emergen Research, 2025; USDA, 2025).</li></ul>",
        dofa_thr_title: "Amenazas (A)",
        dofa_thr_desc: "<ul><li>Normativas de seguridad SAE y competencia de fabricantes OEM originales (Data Bridge Market Research, 2024).</li></ul>",
"""
    es_dict = es_dict[:insert_idx] + es_new_content + es_dict[insert_idx:]

    js = js[:es_start] + es_dict + js[en_start:]


# Exact same structure for EN
en_start = js.find('en: {')
if en_start != -1:
    en_dict = js[en_start:]
    en_dict = re.sub(r'\s*bmc_key_partners:.*?(?=dpi_title)', '\n', en_dict, flags=re.DOTALL)
    en_dict = re.sub(r'\s*dofa_title:.*?(?=sust_title)', '\n', en_dict, flags=re.DOTALL)
    
    insert_idx = en_dict.rfind('}')
    
    en_new_content = """        // BMC EXACT REPLACEMENTS (V13)
        tooltip_bmc: "Strategic structure of UMOs business model, designed from the analysis of internal capabilities and the needs of the US market.",
        bmc_key_partners: "Key Partners",
        bmc_kp_desc: "<ul><li>Raw material suppliers.</li><li>Logistics and transport operators.</li><li>Customs and foreign trade agents.</li><li>Agricultural machinery distributors in the United States.</li><li>Spare parts marketers.</li><li>Commercial allies in target states.</li><li>Fairs, guilds, or networks in the agricultural sector.</li></ul>",
        bmc_key_activities: "Key Activities",
        bmc_ka_desc: "<ul><li>Saddle manufacturing.</li><li>Quality control.</li><li>Purchasing management of raw materials and supplies.</li><li>Product development and adjustment according to customer needs.</li><li>Quotation, negotiation, and closing of sales.</li><li>Market research in target states.</li></ul>",
        bmc_key_resources: "Key Resources",
        bmc_kr_desc: "<ul><li>Manufacturing machinery and equipment.</li><li>Raw materials and supplies.</li><li>Technical knowledge of the product.</li><li>Production team.</li><li>Commercial team.</li><li>Certifications and corporate backing.</li><li>Physical production infrastructure.</li><li>Database of commercial contacts and potential clients.</li></ul>",
        bmc_value_prop: "Value Proposition",
        bmc_vp_desc: "UMO offers saddles for agricultural mowers targeting the US market, providing distributors and marketers with a reliable alternative when original parts are unavailable or cost-prohibitive. Its value proposition is not based on competing directly with major leading brands, but rather on becoming a reliable alternative when the original spare part cannot be obtained.",
        bmc_customer_relation: "Customer Relationships",
        bmc_cr_desc: "<ul><li>Direct B2B relationship with distributors and trading companies.</li><li>Personalized customer service.</li><li>Follow-up via WhatsApp, email, and calls.</li></ul>",
        bmc_channels: "Channels",
        bmc_ch_desc: "<ul><li>Direct sales to agricultural machinery distributors.</li><li>Calls and corporate phone numbers.</li><li>WhatsApp Business.</li><li>Website.</li><li>LinkedIn for B2B contact.</li></ul>",
        bmc_customer_segments: "Customer Segments",
        bmc_cs_desc: "<ul><li>Agricultural machinery distribution companies in the United States.</li><li>Stores or dealers selling equipment for farms and agricultural operations.</li></ul>",
        bmc_cost_structure: "Cost Structure",
        bmc_cost_desc: "<ul><li>Cost of raw materials.</li><li>Production and assembly costs.</li><li>Labor.</li><li>Packaging costs.</li><li>Transport and logistics.</li><li>Export costs.</li><li>Tariffs, procedures, and documentation.</li><li>Marketing and digital presence.</li><li>Administrative costs.</li><li>Machinery maintenance and operation.</li></ul>",
        bmc_revenue: "Revenue Streams",
        bmc_rev_desc: "<ul><li>Sale of agricultural lawnmower saddles to distributors.</li><li>Volume sales to marketers.</li><li>Income from recurring orders.</li></ul>",

        // DOFA EXACT REPLACEMENTS (V13)
        dofa_title: "UMO SWOT Analysis",
        dofa_str_title: "Strengths (S)",
        dofa_str_desc: "<ul><li>57-year trajectory, proprietary polyurethane injection technology, backing as an OEM supplier for Harley Davidson and Yamaha, and high flexibility for custom designs.</li></ul>",
        dofa_weak_title: "Weaknesses (W)",
        dofa_weak_desc: "<ul><li>Bilingualism gap within operating personnel and lack of incentive plan for activities abroad (Diagnostic P-I, 2026).</li></ul>",
        dofa_opp_title: "Opportunities (O)",
        dofa_opp_desc: "<ul><li>Rise of electric technologies in lawmowers and high demand in Missouri/Oklahoma (Emergen Research, 2025; USDA, 2025).</li></ul>",
        dofa_thr_title: "Threats (T)",
        dofa_thr_desc: "<ul><li>SAE safety regulations and competition from original OEM manufacturers (Data Bridge Market Research, 2024).</li></ul>",
"""
    en_dict = en_dict[:insert_idx] + en_new_content + en_dict[insert_idx:]
    js = js[:en_start] + en_dict


with open(JS_PATH, "w", encoding="utf-8") as f:
    f.write(js)

print("CSS/JS Restructured")
