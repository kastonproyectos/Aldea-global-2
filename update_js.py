import re

js_file = 'script.js'
with open(js_file, 'r', encoding='utf-8') as f:
    js = f.read()

# Defining the new keys
es_keys = """
        eco_comp_table: "Tabla de comparación:",
        eco_strat_title: "Strategic Analysis",
        eco_sources_title: "Sources (APA 7):",
        eco_mvs_title: "Market Viability Score",
        eco_mo: "Missouri",
        eco_ok: "Oklahoma",
        state_mo: "Missouri",
        state_ok: "Oklahoma",
        eco_intro_header: "Análisis del\\n                        Entorno Macroeconómico",
        eco_gdp_head: "GDP: Agriculture, Forestry, Fishing and Hunting",
        eco_income_head: "Per Capita Personal Income",
        eco_rpp_head: "RPP (Regional Price Parities)",
        eco_land_head: "Land in Farms",
        eco_tax_head: "State Tax Competitiveness Index",
        diag_completo: "Diagnóstico\\n                            Completo",
        eco_intro_p1: "Para evaluar la viabilidad de internacionalización de UMO en Estados Unidos, se desarrolló un\\n                        análisis comparativo entre los estados de Missouri y Oklahoma, enfocado en variables\\n                        macroeconómicas clave que permiten entender no solo el tamaño del mercado, sino también su\\n                        estabilidad, capacidad de consumo y condiciones operativas.",
        eco_intro_p2: "La selección de los cinco indicadores se realizó con un criterio estratégico: cada uno refleja\\n                        un componente esencial del entorno económico que impacta directamente la demanda y el uso de\\n                        maquinaria, y por ende, la necesidad de repuestos como los sillines para podadoras. En conjunto,\\n                        los indicadores permiten analizar el mercado desde diferentes ángulos: actividad económica del\\n                        sector (PIB agrícola), capacidad de compra (ingreso per cápita), costos del entorno (RPP),\\n                        escala productiva (land in farms) y competitividad fiscal (State Tax Competitiveness Index).",
        eco_intro_p3: "Más allá de observar datos aislados, este análisis busca identificar patrones de comportamiento\\n                        económico en los últimos cinco años, permitiendo comparar la evolución y consistencia de cada\\n                        estado. Esto es clave, ya que un mercado atractivo no solo debe ser grande, sino también estable\\n                        y predecible en el tiempo.",
        eco_intro_p4: "Como herramienta de síntesis, se construyó el Market Viability Score, una calificación de 1 a 5\\n                        asignada a cada indicador según su impacto en la viabilidad del mercado. Esta puntuación\\n                        facilita la comparación directa entre estados y permite traducir datos complejos en una lectura\\n                        clara para la toma de decisiones.",
        eco_intro_p5: "En este\\n                        contexto, el objetivo no es únicamente identificar cuál estado presenta mejores cifras, sino\\n                        determinar cuál ofrece mejores condiciones reales para la entrada, crecimiento y sostenibilidad\\n                        del producto en el mercado. Este enfoque permite concluir, con base en evidencia, cuál\\n                        territorio representa una oportunidad más sólida para la estrategia de internacionalización de\\n                        UMO.",
"""

en_keys = """
        eco_comp_table: "Comparison Table:",
        eco_strat_title: "Strategic Analysis",
        eco_sources_title: "Sources (APA 7):",
        eco_mvs_title: "Market Viability Score",
        eco_mo: "Missouri",
        eco_ok: "Oklahoma",
        state_mo: "Missouri",
        state_ok: "Oklahoma",
        eco_intro_header: "Macroeconomic Environment\\n                        Analysis",
        eco_gdp_head: "GDP: Agriculture, Forestry, Fishing and Hunting",
        eco_income_head: "Per Capita Personal Income",
        eco_rpp_head: "RPP (Regional Price Parities)",
        eco_land_head: "Land in Farms",
        eco_tax_head: "State Tax Competitiveness Index",
        diag_completo: "Complete\\n                            Diagnostic",
        eco_intro_p1: "To assess UMO's internationalization viability in the United States, a comparative\\n                        analysis was developed between the states of Missouri and Oklahoma, focusing on key\\n                        macroeconomic variables that help to understand not only market size, but also its\\n                        stability, consumer capacity, and operational conditions.",
        eco_intro_p2: "The selection of the five indicators was made under a strategic criterion: each reflects\\n                        an essential component of the economic environment directly impacting demand and machinery\\n                        usage, hence the need for parts such as mower saddles. Collectively,\\n                        the indicators allow analyzing the market from different angles: economic activity of the\\n                        sector (agricultural GDP), purchasing power (per capita income), cost environment (RPP),\\n                        productive scale (land in farms) and tax competitiveness (State Tax Competitiveness Index).",
        eco_intro_p3: "Beyond observing isolated data, this analysis seeks to identify patterns of economic\\n                        behavior over the last five years, allowing a comparison of each state's consistency and evolution.\\n                        This is crucial, as an attractive market must not only be large, but also stable\\n                        and predictable over time.",
        eco_intro_p4: "As a synthesis tool, the Market Viability Score was constructed—a rating from 1 to 5\\n                        assigned to each indicator based on its impact on market viability. This score\\n                        facilitates direct comparison between states and translates complex data into a clear\\n                        reading for decision-making.",
        eco_intro_p5: "In this\\n                        context, the objective is not simply to identify which state shows better figures, but rather\\n                        to determine which offers better real conditions for market entry, growth, and product\\n                        sustainability. This approach allows a conclusion, grounded in evidence, regarding which\\n                        territory represents a stronger opportunity for UMO's internationalization strategy.",
"""

# Insert es_keys into es dictionary (finding `es: {` block somewhere near the top of the file)
js = js.replace('es: {\n', 'es: {\n' + es_keys)

# Insert en_keys into en dictionary
js = js.replace('en: {\n', 'en: {\n' + en_keys)

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated script.js with missing dictionary keys.")
