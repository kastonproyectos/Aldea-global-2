import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# The ES Dictionary texts
es_viab_just_desc = "<ul style='list-style-type: disc; padding-left: 20px; line-height: 1.6;'><li class='mb-2'><strong>Integración en la cadena de valor:</strong> Aunque los sillines para podadoras no figuran de forma independiente en las bases de datos, hacen parte de la cadena de valor de la partida arancelaria 8433.11 (podadoras y equipos de césped), lo que vincula su demanda directamente al crecimiento de este mercado mayor (International Trade Centre [ITC], 2024).</li><li class='mb-2'><strong>Dependencia de la demanda global:</strong> El comportamiento del mercado de sillines depende del tamaño y expansión del sector de maquinaria agrícola y de jardín, donde estos funcionan tanto como piezas originales como repuestos (ITC, 2024).</li><li class='mb-2'><strong>Oportunidades de mantenimiento:</strong> El incremento en la importación de podadoras en distintos países genera una necesidad constante de mantenimiento y reemplazo de piezas, lo que abre oportunidades para empresas que ofrecen componentes compatibles (ITC, 2024).</li></ul>"

es_viab_sec_desc = "<ul style='list-style-type: disc; padding-left: 20px; line-height: 1.6;'><li class='mb-2'><strong>Especialización en entornos agroindustriales:</strong> El producto se inserta en el sector de lawn and garden equipment, caracterizado por altos niveles de mecanización en economías desarrolladas, donde la productividad depende del uso de maquinaria y del mantenimiento constante de estas (ITC, 2024).</li><li class='mb-2'><strong>Liderazgo importador de Estados Unidos:</strong> Estados Unidos se posiciona como el mercado con mayor participación en importaciones del producto analizado, lo que evidencia una alta demanda interna y una oportunidad clara para productos complementarios como los sillines (ITC, 2024).</li><li class='mb-2'><strong>Contexto de economías desarrolladas:</strong> Además del mercado estadounidense, países como Canadá, Australia y Bélgica presentan una participación relevante, lo que demuestra que el producto tiene viabilidad en economías con alto nivel de desarrollo e infraestructura (ITC, 2024).</li></ul>"

es_viab_size_desc = "<ul style='list-style-type: disc; padding-left: 20px; line-height: 1.6;'><li class='mb-2'><strong>Concentración estratégica en EE. UU.:</strong> En el análisis de concentración y distancia, Estados Unidos ocupa una posición dominante tanto por el tamaño de su mercado como por su nivel de concentración en importaciones (ITC, 2024).</li><li class='mb-2'><strong>Balanza comercial deficitaria:</strong> La balanza comercial negativa de Estados Unidos en este producto indica que importa más de lo que exporta, lo que evidencia una alta dependencia de proveedores externos y una fuerte demanda interna (ITC, 2024).</li></ul>"

es_viab_size_desc_p2 = "<ul style='list-style-type: disc; padding-left: 20px; line-height: 1.6;'><li class='mb-2'><strong>Potencial de diversificación:</strong> La participación de mercados como Alemania, Francia, Italia y Polonia demuestra que la demanda no está concentrada en un solo país, lo que permite plantear estrategias de expansión hacia mercados secundarios (ITC, 2024).</li><li class='mb-2'><strong>Dinámica de crecimiento positivo:</strong> El crecimiento de las importaciones en países como Estados Unidos y Bélgica representa una señal positiva, ya que indica que la demanda en estos mercados está aumentando (ITC, 2024).</li></ul>"

es_viab_size_desc_p3 = "<ul style='list-style-type: disc; padding-left: 20px; line-height: 1.6;'><li class='mb-2'><strong>Exploración de nichos específicos:</strong> Países europeos con menor tamaño de mercado pero crecimiento positivo representan oportunidades para estrategias de internacionalización gradual y exploración de nichos (ITC, 2024).</li></ul>"

es_viab_comp_desc = "<p style='margin-bottom: 1rem;'>Al analizar los actores del sector, se identifica que la competencia no se limita a los fabricantes de maquinaria, sino que también incluye empresas especializadas en componentes y distribuidores de repuestos.</p><ul style='list-style-type: disc; padding-left: 20px; line-height: 1.6;'><li class='mb-2'><strong>Fabricantes OEM:</strong> Empresas como John Deere ofrecen maquinaria completa (lawn mowers) (John Deere, s. f.-a) y repuestos como asientos dentro de su portafolio (John Deere, s. f.-b), lo que demuestra que el sillín forma parte del negocio de mantenimiento. De manera similar, Kubota comercializa maquinaria y repuestos diseñados específicamente para sus equipos (Kubota, s. f.).</li><li class='mb-2'><strong>Fabricantes especializados en asientos:</strong> Empresas como GRAMMER desarrollan soluciones de asientos para el sector agrícola (GRAMMER, s. f.-a, s. f.-b), mientras que Seats Inc. diseña productos específicos para maquinaria como podadoras y tractores (Seats Inc., s. f.-a, s. f.-b). Estas empresas compiten en aspectos como comodidad, calidad y durabilidad (Seats Inc., s. f.-c; GRAMMER, s. f.-b).</li><li class='mb-2'><strong>Mercado aftermarket:</strong> Distribuidores como TractorSeats.com ofrecen sillines de reemplazo para múltiples marcas, así como kits de asiento y suspensión (TractorSeats.com, s. f.-a, s. f.-b, s. f.-c), lo que evidencia una demanda activa por repuestos y un mercado donde el cliente compara alternativas según precio y compatibilidad.</li></ul>"

# The EN Dictionary texts 
en_viab_just_desc = "<ul style='list-style-type: disc; padding-left: 20px; line-height: 1.6;'><li class='mb-2'><strong>Value chain integration:</strong> Although mower saddles are not listed independently in databases, they are part of the value chain of tariff heading 8433.11 (mowers and lawn equipment), linking their demand directly to the growth of this larger market (International Trade Centre [ITC], 2024).</li><li class='mb-2'><strong>Global demand dependence:</strong> The behavior of the saddle market depends on the size and expansion of the agricultural and garden machinery sector, where these function as both original parts and replacements (ITC, 2024).</li><li class='mb-2'><strong>Maintenance opportunities:</strong> The increase in mower imports in different countries generates a constant need for component maintenance and replacement, opening opportunities for companies offering compatible components (ITC, 2024).</li></ul>"

en_viab_sec_desc = "<ul style='list-style-type: disc; padding-left: 20px; line-height: 1.6;'><li class='mb-2'><strong>Specialization in agro-industrial environments:</strong> The product fits into the lawn and garden equipment sector, characterized by high levels of mechanization in developed economies, where productivity depends on the use of machinery and their constant maintenance (ITC, 2024).</li><li class='mb-2'><strong>U.S. import leadership:</strong> The United States is positioned as the market with the highest share of imports of the analyzed product, evidencing high domestic demand and a clear opportunity for complementary products such as saddles (ITC, 2024).</li><li class='mb-2'><strong>Context of developed economies:</strong> Besides the U.S. market, countries like Canada, Australia, and Belgium present a relevant share, demonstrating that the product is viable in economies with a high level of development and infrastructure (ITC, 2024).</li></ul>"

en_viab_size_desc = "<ul style='list-style-type: disc; padding-left: 20px; line-height: 1.6;'><li class='mb-2'><strong>Strategic concentration in the US:</strong> In the concentration and distance analysis, the United States occupies a dominant position both due to its market size and its level of import concentration (ITC, 2024).</li><li class='mb-2'><strong>Trade balance deficit:</strong> The negative trade balance of the United States in this product indicates that it imports more than it exports, demonstrating a high dependence on external suppliers and strong domestic demand (ITC, 2024).</li></ul>"

en_viab_size_desc_p2 = "<ul style='list-style-type: disc; padding-left: 20px; line-height: 1.6;'><li class='mb-2'><strong>Diversification potential:</strong> The participation of markets such as Germany, France, Italy, and Poland demonstrates that demand is not concentrated in a single country, allowing for expansion strategies into secondary markets (ITC, 2024).</li><li class='mb-2'><strong>Positive growth dynamics:</strong> The growth of imports in countries like the United States and Belgium represents a positive signal, as it indicates that demand in these markets is increasing (ITC, 2024).</li></ul>"

en_viab_size_desc_p3 = "<ul style='list-style-type: disc; padding-left: 20px; line-height: 1.6;'><li class='mb-2'><strong>Exploration of specific niches:</strong> European countries with smaller market sizes but positive growth represent opportunities for gradual internationalization strategies and niche exploration (ITC, 2024).</li></ul>"

en_viab_comp_desc = "<p style='margin-bottom: 1rem;'>Analyzing the sector's players reveals that competition is not limited to machinery manufacturers but also includes companies specialized in components and parts distributors.</p><ul style='list-style-type: disc; padding-left: 20px; line-height: 1.6;'><li class='mb-2'><strong>OEM Manufacturers:</strong> Companies like John Deere offer complete machinery (lawn mowers) (John Deere, n.d.-a) and parts such as seats within their portfolio (John Deere, n.d.-b), proving that the saddle is part of the maintenance business. Similarly, Kubota sells machinery and parts specifically designed for its equipment (Kubota, n.d.).</li><li class='mb-2'><strong>Specialized seat manufacturers:</strong> Companies like GRAMMER develop seating solutions for the agricultural sector (GRAMMER, n.d.-a, n.d.-b), while Seats Inc. designs specific products for machinery like mowers and tractors (Seats Inc., n.d.-a, n.d.-b). These companies compete on aspects like comfort, quality, and durability (Seats Inc., n.d.-c; GRAMMER, n.d.-b).</li><li class='mb-2'><strong>Aftermarket:</strong> Distributors like TractorSeats.com offer replacement saddles for multiple brands, as well as seat and suspension kits (TractorSeats.com, n.d.-a, n.d.-b, n.d.-c), evidencing active demand for parts and a market where the customer compares alternatives based on price and compatibility.</li></ul>"

def replace_val(text, key, new_val):
    pattern = r'(' + re.escape(key) + r':\s*")[^"]*(")'
    return re.sub(pattern, r'\g<1>' + new_val.replace('"', '\\"') + r'\g<2>', text)

# For Spanish keys
js = replace_val(js, 'viab_just_desc', es_viab_just_desc)
js = replace_val(js, 'viab_sec_desc', es_viab_sec_desc)
js = replace_val(js, 'viab_size_desc', es_viab_size_desc)
js = replace_val(js, 'viab_size_desc_p2', es_viab_size_desc_p2)
js = replace_val(js, 'viab_size_desc_p3', es_viab_size_desc_p3)
js = replace_val(js, 'viab_comp_desc', es_viab_comp_desc)

# Because we have EN and ES blocks, the naive replace_val will replace BOTH occurrences (the ES one and EN one) with the ES text!
# Let's fix that by splitting the file into ES and EN sections, since 'en: {' splits it.
es_part, en_part = js.split('en: {', 1)

es_part = replace_val(es_part, 'viab_just_desc', es_viab_just_desc)
es_part = replace_val(es_part, 'viab_sec_desc', es_viab_sec_desc)
es_part = replace_val(es_part, 'viab_size_desc', es_viab_size_desc)
es_part = replace_val(es_part, 'viab_size_desc_p2', es_viab_size_desc_p2)
es_part = replace_val(es_part, 'viab_size_desc_p3', es_viab_size_desc_p3)
es_part = replace_val(es_part, 'viab_comp_desc', es_viab_comp_desc)

en_part = replace_val(en_part, 'viab_just_desc', en_viab_just_desc)
en_part = replace_val(en_part, 'viab_sec_desc', en_viab_sec_desc)
en_part = replace_val(en_part, 'viab_size_desc', en_viab_size_desc)
en_part = replace_val(en_part, 'viab_size_desc_p2', en_viab_size_desc_p2)
en_part = replace_val(en_part, 'viab_size_desc_p3', en_viab_size_desc_p3)
en_part = replace_val(en_part, 'viab_comp_desc', en_viab_comp_desc)

# Also ensure viab_fig1_cap and viab_fig2_cap maintain correct text in ES and EN if needed. The user hasn't asked them to change, but has said "Mantener figuras y lineas de Fuente:" which is:
es_fig_1 = "Figura 1. Concentración y distancia de los países importadores del producto 843311.<br>Fuente: International Trade Centre (2024)."
es_fig_2 = "Figura 2. Crecimiento de las importaciones por país del producto 843311.<br>Fuente: International Trade Centre (2024)."

en_fig_1 = "Figure 1. Concentration and distance of importing countries for product 843311.<br>Source: International Trade Centre (2024)."
en_fig_2 = "Figure 2. Import growth by country for product 843311.<br>Source: International Trade Centre (2024)."

es_part = replace_val(es_part, 'viab_fig1_cap', es_fig_1)
es_part = replace_val(es_part, 'viab_fig2_cap', es_fig_2)
en_part = replace_val(en_part, 'viab_fig1_cap', en_fig_1)
en_part = replace_val(en_part, 'viab_fig2_cap', en_fig_2)

js = es_part + 'en: {' + en_part

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated successfully")
