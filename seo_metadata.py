"""Route-aware metadata, without invented business details."""
import re

def metadata(path,title,description,services,cities):
    parts=path.strip('/').split('/')
    by_service={s['slug']:s for s in services}
    by_city={c['slug']:c for c in cities}
    if len(parts)==2 and parts[0]=='services' and parts[1] in by_service:
        s=by_service[parts[1]]
        title=s['name']+' : installation, réparation et rénovation'
        description=s['name']+' : installation, réparation et rénovation au Maroc, selon disponibilité locale. Prestations et préparation de votre projet.'
    elif len(parts)==3 and parts[0]=='zones' and parts[2] in by_service:
        s=by_service[parts[2]]; city=by_city[parts[1]]['name']
        description=s['name']+' — '+city+' : installation, réparation et rénovation. Découvrez les prestations, les secteurs desservis et les conseils avant travaux.'
    elif len(parts)==2 and parts[0]=='blog':
        description=title.rstrip(' ?.!')+'. Découvrez les points à vérifier et les questions à poser avant les travaux avec REPAREO.'
    # Editorial target, not a Google-imposed character limit.
    description=re.sub(r'\s+',' ',description).strip()
    if len(description)>175:
        short=description[:172].rsplit(' ',1)[0].rstrip(' ,;:')
        description=short+'…'
    return title,description
