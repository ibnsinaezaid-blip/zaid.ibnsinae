"""Pages des 71 zones, avec neuf services par zone et liens permanents."""
from html import escape as e
from seo_content import LOCAL, answered_questions, related

def publish_all(page, heading, pic, services, cities, slug, origin, prestations):
    for city in cities:
        for zone in city['zones']:
            base='/zones/'+city['slug']+'/'+slug(zone)+'/'
            label=zone+' — '+city['name']
            crumbs=[('Zones','/zones/'),(city['name'],'/zones/'+city['slug']+'/'),(zone,base)]
            cards=''.join('<a class="servicecard" href="'+base+s['slug']+'/"><div class="cardphoto">'+pic(s)+'</div><div class="cardtext"><h2>'+e(s['name'])+'</h2><p>'+e(s['short'])+'</p><span class="cardlink">Voir les prestations ↗</span></div></a>' for s in services)
            page(base,'Installation, réparation et rénovation — '+label,'Découvrez les neuf services REPAREO pour '+label+' : prestations, préparation du projet et informations pour organiser une intervention.',heading('VOTRE ZONE',label,'Sélectionnez le métier adapté à votre besoin. L’adresse exacte, la disponibilité et les modalités du déplacement sont à confirmer avant intervention.')+'<section class="wrap section compact"><div class="servicegrid">'+cards+'</div></section>',crumbs)
            for service in services:
                key=service['slug'];path=base+key+'/'
                title=service['trade']+' — '+label
                desc=service['name']+' dans le secteur '+zone+' ('+city['name']+') : installation, réparation et rénovation. Prestations, éléments du devis et réponses à vos questions.'
                sections=LOCAL[key]['sections']
                editorial=''.join('<section><h2>'+e(h.replace('Casablanca',zone))+'</h2><p>'+e(t.replace('À Casablanca,','Dans ce secteur,').replace('à Casablanca','dans ce secteur'))+'</p></section>' for h,t in sections)
                if key=='climatisation' and zone=='Dar Bouazza':
                    editorial+='<section><h2>Installation de climatiseur à Dar Bouazza</h2><p>Précisez la résidence ou un point de repère, le type de logement et les conditions d’accès aux emplacements envisagés. En copropriété, faites examiner les modalités de pose de l’unité extérieure avant l’achat. Si le logement est exposé aux embruns, signalez-le pour que le professionnel vérifie les préconisations du fabricant. Le choix définitif et le calendrier doivent être confirmés après évaluation.</p></section>'
                location='<section class="wrap prep"><h2>Organiser votre projet — '+e(zone)+'</h2><p>Cette page concerne le secteur '+e(zone)+', rattaché à '+e(city['name'])+'. Indiquez une adresse complète, un point de repère, l’étage et les modalités d’accès. La disponibilité et les frais éventuels de déplacement seront à confirmer.</p><h3>Informations à préparer</h3><p>'+e(service['prepare'])+'</p><a class="button" href="/contact/?service='+key+'&amp;ville='+city['slug']+'&amp;secteur='+slug(zone)+'">Préparer mon projet ↗</a><p>Contactez REPAREO par téléphone, WhatsApp ou via notre formulaire pour préciser votre demande.</p></section>'
                faq=answered_questions(service,zone)
                faq=faq.replace('</section>','<details><summary>Le devis inclut-il les travaux de finition ?</summary><p>Les reprises de support, les fournitures et les finitions doivent être indiquées dans la proposition. Faites préciser ce qui est inclus et ce qui relève d’un autre métier avant de valider.</p></details><details><summary>Quel délai prévoir pour ce secteur ?</summary><p>Le délai dépend de l’évaluation, du matériel, des pièces disponibles et des conditions d’accès. Un créneau ne peut pas être garanti sans confirmation préalable.</p></details></section>')
                links='<section class="wrap prep"><h2>Autres services — '+e(zone)+'</h2><div class="chips">'+''.join('<a href="'+base+s['slug']+'/">'+e(s['name'])+'</a>' for s in services if s['slug']!=key)+'</div><p><a href="/zones/'+city['slug']+'/'+key+'/">Voir ce métier dans tout le secteur '+e(city['name'])+' →</a></p></section>'
                body=heading('INSTALLATION · RÉPARATION · RÉNOVATION',title,service['intro'])+'<section class="wrap detailsgrid"><div class="detailimage">'+pic(service,True)+'</div><div><h2>'+e(service['install'])+'</h2><p>'+e(service['install_text'])+'</p><h2>'+e(service['repair'])+'</h2><p>'+e(service['repair_text'])+'</p></div></section>'+prestations(service)+'<article class="wrap article">'+editorial+'</article>'+location+faq+related(key)+links
                page(path,title,desc,body,crumbs+[(service['name'],path)],{'@type':'Service','name':title,'serviceType':service['name'],'provider':{'@id':origin+'/#organisation'},'areaServed':{'@type':'Place','name':label}})
