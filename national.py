"""National expansion. Availability must be confirmed; no invented local offices."""
from html import escape as e

NEW_CITIES = ['Rabat','Salé','Tanger','Marrakech','Fès','Meknès','Agadir','Kénitra','Tétouan','Oujda']

def extend_cities(cities, slug):
    return cities + [dict(name=n,slug=slug(n),zones=[],intro='Vous préparez des travaux à '+n+' ? Consultez les prestations puis contactez REPAREO pour vérifier la disponibilité à votre adresse. Le déplacement, le devis et le créneau restent à confirmer.') for n in NEW_CITIES]

def task_catalog(services, prestations, slug):
    # 31 distinct project pages, linked from their parent service.
    result=[]
    for i,s in enumerate(services):
        for title,description in prestations[s['slug']]['items'][:4 if i<4 else 3]:
            result.append(dict(service=s,title=title,description=description,path='/services/'+s['slug']+'/'+slug(title)+'/'))
    return result

def task_links(service, services, prestations, slug):
    tasks=[t for t in task_catalog(services,prestations,slug) if t['service']['slug']==service['slug']]
    return '<section class="wrap prep"><div class="eyebrow">VOTRE BESOIN EN DÉTAIL</div><h2>Choisir une prestation</h2><div class="task-grid">'+''.join('<a class="task-card" href="'+t['path']+'"><h3>'+e(t['title'])+'</h3><p>'+e(t['description'])+'</p><span>Préparer ce projet →</span></a>' for t in tasks)+'</div></section>'

def publish_tasks(page,heading,pic,services,cities,prestations,slug):
    for t in task_catalog(services,prestations,slug):
        s=t['service'];path=t['path']
        body=heading('PRESTATION · '+s['name'].upper(),t['title'],t['description'])
        body+='<section class="wrap detailsgrid"><div class="detailimage">'+pic(s,True)+'</div><div><h2>Un projet défini avant le devis</h2><p>'+e(t['description'])+'</p><h3>Les informations utiles</h3><p>'+e(s['prepare'])+'</p><p>Précisez ce que vous souhaitez conserver et le résultat attendu. Le professionnel vérifie la compatibilité des éléments avant de proposer une solution.</p><a class="button" href="/contact/?service='+s['slug']+'">Décrire mon besoin ↗</a></div></section>'
        body+='<section class="wrap prep"><h2>Que faire préciser dans la proposition ?</h2><div class="task-grid"><article class="task-card"><h3>Le périmètre</h3><p>Pour « '+e(t['title'].lower())+' », demandez la liste des opérations incluses, des fournitures et des travaux complémentaires éventuels.</p></article><article class="task-card"><h3>Le matériel</h3><p>Les références, dimensions et finitions doivent être validées. Une estimation à distance ne remplace pas les vérifications nécessaires sur place.</p></article><article class="task-card"><h3>L’organisation</h3><p>Confirmez les accès, la durée estimée, la protection des espaces et les conditions de réception. Le prix et la disponibilité sont à confirmer avant engagement.</p></article></div></section>'
        body+='<section class="wrap prep"><h2>Dans quelle ville se trouve votre projet ?</h2><div class="chips">'+''.join('<a href="/zones/'+c['slug']+'/'+s['slug']+'/">'+e(c['name'])+'</a>' for c in cities)+'</div><p>La présence d’une ville dans cet annuaire ne garantit pas un créneau : contactez-nous pour confirmer la prise en charge.</p></section>'
        page(path,t['title']+' : projet et devis',t['description']+' Préparez votre demande auprès de REPAREO.',body,[('Services','/services/'),(s['name'],'/services/'+s['slug']+'/'),(t['title'],path)])
