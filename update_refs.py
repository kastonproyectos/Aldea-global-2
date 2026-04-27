import re
from uuid import uuid4

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Specifically target the references section which starts at <section id="references">
# and look for the <p style="font-size:0.95rem; line-height:1.8; margin-bottom:1rem;"> tags
refs_start = html.find('<section id="references"')
refs_end = html.find('</section>', refs_start)

refs_html = html[refs_start:refs_end]

# Extract all paragraphs without data-i18n
pattern = re.compile(r'<p style="font-size:0.95rem; line-height:1.8; margin-bottom:1rem;">(.*?)</p>', re.DOTALL)
matches = pattern.findall(refs_html)

es_dict_refs = ""
en_dict_refs = ""
new_refs_html = refs_html

for i, m in enumerate(matches):
    key = f"ref_auto_{i}"
    # Replace the exact <p> wrap in HTML
    new_refs_html = new_refs_html.replace(
        f'<p style="font-size:0.95rem; line-height:1.8; margin-bottom:1rem;">{m}</p>',
        f'<p style="font-size:0.95rem; line-height:1.8; margin-bottom:1rem;" data-i18n="{key}">{m}</p>'
    )
    
    # Store original as ES
    # clean newlines and excessive spaces for string safety
    clean_m = re.sub(r'\s+', ' ', m).replace('"', '\\"')
    es_dict_refs += f'\n        {key}: "{clean_m}",'
    
    # Simple EN translation logic
    en_m = clean_m.replace('Asociación Nacional de Empresarios de Colombia', 'National Business Association of Colombia')
    en_m = en_m.replace('Informe del sector automotor en Colombia', 'Report of the automotive sector in Colombia')
    en_m = en_m.replace('Comisión Económica para América Latina y el Caribe', 'Economic Commission for Latin America and the Caribbean')
    en_m = en_m.replace('Desarrollo productivo y empleo', 'Productive development and employment')
    en_m = en_m.replace('Sistemas de gestión ambiental', 'Environmental management systems')
    en_m = en_m.replace('Gestión ambiental empresarial en Colombia', 'Corporate environmental management in Colombia')
    en_m = en_m.replace('Ministerio de Ambiente y Desarrollo Sostenible', 'Ministry of Environment and Sustainable Development')
    en_m = en_m.replace('Organización Internacional del Trabajo', 'International Labour Organization')
    en_m = en_m.replace('Empleo y desarrollo industrial', 'Employment and industrial development')
    en_m = en_m.replace('Industria automotriz en Colombia', 'Automotive industry in Colombia')
    en_m = en_m.replace('Quiénes somos', 'Who we are')
    en_m = en_m.replace('para el 2024 usamos el site de Bureou y para el resto de los años el de fred', 'for 2024 we use the Bureau site and for other years fred')
    
    en_dict_refs += f'\n        {key}: "{en_m}",'

html = html[:refs_start] + new_refs_html + html[refs_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Inject into script.js
js = js.replace('es: {\n', 'es: {' + es_dict_refs)
js = js.replace('en: {\n', 'en: {' + en_dict_refs)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Translated APA references and injected logic successfully!")
