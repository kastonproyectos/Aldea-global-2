import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Exact Elements where possible
# Headers
html = html.replace('Tabla de comparación:', '<span data-i18n="eco_comp_table">Tabla de comparación:</span>')
html = html.replace('>Strategic Analysis<', ' data-i18n="eco_strat_title">Strategic Analysis<')
html = html.replace('>Sources (APA 7):<', ' data-i18n="eco_sources_title">Sources (APA 7):<')
html = html.replace('>Market Viability Score<', ' data-i18n="eco_mvs_title">Market Viability Score<')

# State names and formats
html = html.replace('Missouri: 5', '<span data-i18n="eco_mo">Missouri</span>: 5')
html = html.replace('Oklahoma: 2.62', '<span data-i18n="eco_ok">Oklahoma</span>: 2.62')
html = html.replace('Oklahoma: 4.83', '<span data-i18n="eco_ok">Oklahoma</span>: 4.83')
html = html.replace('Oklahoma: 4.05', '<span data-i18n="eco_ok">Oklahoma</span>: 4.05')
html = html.replace('Oklahoma: 3.82', '<span data-i18n="eco_ok">Oklahoma</span>: 3.82')

# Table Headers
html = html.replace('>Missouri<', ' data-i18n="state_mo">Missouri<')
html = html.replace('>Oklahoma<', ' data-i18n="state_ok">Oklahoma<')

# The 5 paragraphs of intro
p1 = "Para evaluar la viabilidad de internacionalización de UMO en Estados Unidos, se desarrolló un\n                        análisis comparativo entre los estados de Missouri y Oklahoma, enfocado en variables\n                        macroeconómicas clave que permiten entender no solo el tamaño del mercado, sino también su\n                        estabilidad, capacidad de consumo y condiciones operativas."
html = html.replace(p1, '<span data-i18n="eco_intro_p1">' + p1 + '</span>')

p2 = "La selección de los cinco indicadores se realizó con un criterio estratégico: cada uno refleja\n                        un componente esencial del entorno económico que impacta directamente la demanda y el uso de\n                        maquinaria, y por ende, la necesidad de repuestos como los sillines para podadoras. En conjunto,\n                        los indicadores permiten analizar el mercado desde diferentes ángulos: actividad económica del\n                        sector (PIB agrícola), capacidad de compra (ingreso per cápita), costos del entorno (RPP),\n                        escala productiva (land in farms) y competitividad fiscal (State Tax Competitiveness Index)."
html = html.replace(p2, '<span data-i18n="eco_intro_p2">' + p2 + '</span>')

p3 = "Más allá de observar datos aislados, este análisis busca identificar patrones de comportamiento\n                        económico en los últimos cinco años, permitiendo comparar la evolución y consistencia de cada\n                        estado. Esto es clave, ya que un mercado atractivo no solo debe ser grande, sino también estable\n                        y predecible en el tiempo."
html = html.replace(p3, '<span data-i18n="eco_intro_p3">' + p3 + '</span>')

p4 = "Como herramienta de síntesis, se construyó el Market Viability Score, una calificación de 1 a 5\n                        asignada a cada indicador según su impacto en la viabilidad del mercado. Esta puntuación\n                        facilita la comparación directa entre estados y permite traducir datos complejos en una lectura\n                        clara para la toma de decisiones."
html = html.replace(p4, '<span data-i18n="eco_intro_p4">' + p4 + '</span>')

p5 = "En este\n                        contexto, el objetivo no es únicamente identificar cuál estado presenta mejores cifras, sino\n                        determinar cuál ofrece mejores condiciones reales para la entrada, crecimiento y sostenibilidad\n                        del producto en el mercado. Este enfoque permite concluir, con base en evidencia, cuál\n                        territorio representa una oportunidad más sólida para la estrategia de internacionalización de\n                        UMO."
html = html.replace(p5, '<span data-i18n="eco_intro_p5">' + p5 + '</span>')

# Final specific intro header
intro_header = "Análisis del\n                        Entorno Macroeconómico"
html = html.replace(intro_header, '<span data-i18n="eco_intro_header">' + intro_header + '</span>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Structural replacements done.")
