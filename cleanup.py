import sys

try:
    with open('index.html', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    out = []
    skip = False
    for line in lines:
        if '<!-- Card 1: GDP -->' in line:
            # If it's the duplicate card, skipping starts
            if 'style="font-size:1.6rem; font-weight:800;"' not in line and 'font-size:1.55rem' not in line:
                skip = True
                
        if '<section id="smart"' in line:
            skip = False
            
        if not skip:
            out.append(line)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(out)
        
    print("Cleanup successful")
except Exception as e:
    print(e)
