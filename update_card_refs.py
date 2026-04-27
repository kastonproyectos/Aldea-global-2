import re
from uuid import uuid4

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract all paragraphs that contain the card references
pattern = re.compile(r'<p style="font-size:0.82rem; color:var\(--gray\); line-height:1.8; margin:0;">(.*?)</p>', re.DOTALL)
matches = pattern.findall(html)

es_dict_refs = ""
en_dict_refs = ""
new_html = html

for i, m in enumerate(matches):
    key = f"ref_card_auto_{i}"
    # Replace the exact <p> wrap in HTML
    new_html = new_html.replace(
        f'<p style="font-size:0.82rem; color:var(--gray); line-height:1.8; margin:0;">{m}</p>',
        f'<p style="font-size:0.82rem; color:var(--gray); line-height:1.8; margin:0;" data-i18n="{key}">{m}</p>'
    )
    
    clean_m = re.sub(r'\s+', ' ', m).replace('"', '\\"')
    es_dict_refs += f'\n        {key}: "{clean_m}",'
    
    # Translate specific spans
    en_m = clean_m.replace('para el 2024 usamos el site de Bureou y para el resto de los años el de fred', 'for 2024 we use the Bureau site and for the other years, FRED')
    en_m = en_m.replace('Fuentes', 'Sources')
    
    en_dict_refs += f'\n        {key}: "{en_m}",'

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Inject into script.js
js = js.replace('es: {\n', 'es: {' + es_dict_refs)
js = js.replace('en: {\n', 'en: {' + en_dict_refs)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Translated Card references successfully!")
