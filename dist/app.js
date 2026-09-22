(()=>{'use strict';
const btn=document.querySelector('.menubtn'),nav=document.querySelector('#nav');
btn?.addEventListener('click',()=>{const open=btn.getAttribute('aria-expanded')!=='true';btn.setAttribute('aria-expanded',String(open));nav.classList.toggle('open',open)});
document.addEventListener('keydown',ev=>{if(ev.key==='Escape'){document.querySelectorAll('header details[open]').forEach(d=>d.open=false);nav?.classList.remove('open');btn?.setAttribute('aria-expanded','false')}});
document.querySelectorAll('#nav > details').forEach(menu=>menu.addEventListener('toggle',()=>{if(menu.open)document.querySelectorAll('#nav > details').forEach(other=>{if(other!==menu)other.open=false})}));
document.addEventListener('click',ev=>{if(!ev.target.closest('header'))document.querySelectorAll('header details[open]').forEach(d=>d.open=false)});
const params=new URLSearchParams(location.search),sector=document.getElementById('sector');
if(sector){
 const allowed=new Map([...sector.options].map(o=>[o.value,o.textContent]));
 const requested=params.get('secteur')||'';
 const parts=location.pathname.split('/').filter(Boolean);
 sector.value=allowed.has(requested)?requested:'';
 const destination=value=>'/zones/'+parts[1]+'/'+value+'/'+(parts[2]?parts[2]+'/':'');
 if(sector.value&&parts[0]==='zones'&&parts.length<=3){location.replace(destination(sector.value));}
 sector.addEventListener('change',()=>{
  if(sector.value&&allowed.has(sector.value)&&parts[0]==='zones'&&parts.length<=3){location.assign(destination(sector.value));}
 });
}
const context=document.getElementById('contact-context');if(context){const parts=['service','ville','secteur'].map(k=>params.get(k)).filter(Boolean).map(v=>v.replace(/-/g,' ').slice(0,100));if(parts.length)context.textContent='Votre sélection : '+parts.join(' · ');}
document.querySelectorAll('.brand img').forEach(img=>img.addEventListener('error',()=>{img.style.display='none';img.nextElementSibling.style.display='inline'}));
})();

(()=>{
const form=document.getElementById('service-finder');
if(!form)return;
const service=document.getElementById('finder-service');
const city=document.getElementById('finder-city');
const zone=document.getElementById('finder-zone');
const status=document.getElementById('finder-status');
const zones=JSON.parse(document.getElementById('finder-data').textContent);
function updateZones(){
 const entries=Object.hasOwn(zones,city.value)?zones[city.value]:[];
 zone.replaceChildren(new Option(entries.length?'Choisir une zone':'Choisissez d’abord une ville',''));
 entries.forEach(item=>zone.add(new Option(item.label,item.value)));
 zone.disabled=!entries.length;
 status.textContent=entries.length?entries.length+' zones disponibles. Choisissez votre quartier.':'Sélectionnez une ville pour afficher ses zones.';
}
city.addEventListener('change',updateZones);
zone.addEventListener('change',()=>{if(zone.value)status.textContent='Votre zone : '+zone.selectedOptions[0].textContent+'.';});
form.addEventListener('submit',event=>{
 event.preventDefault();
 if(!form.reportValidity())return;
 if(![...service.options].some(o=>o.value===service.value&&o.value)||!Object.hasOwn(zones,city.value)||!zones[city.value].some(z=>z.value===zone.value))return;
 window.location.assign('/zones/'+city.value+'/'+zone.value+'/'+service.value+'/');
});
updateZones();
})();

(()=>{
const form=document.getElementById('contact-form');if(!form)return;
const params=new URLSearchParams(location.search), service=document.getElementById('contact-service');
if([...service.options].some(o=>o.value===params.get('service')))service.value=params.get('service');
document.getElementById('contact-area').value=['ville','secteur'].map(k=>params.get(k)||'').filter(Boolean).join(' — ').replace(/-/g,' ').slice(0,160);
form.addEventListener('submit',event=>{event.preventDefault();if(!form.reportValidity())return;
const data=new FormData(form);if(data.get('website'))return;
const message=['Bonjour REPAREO, je souhaite préparer un projet.', 'Nom : '+data.get('name'),'Téléphone : '+data.get('phone'),'Service : '+service.selectedOptions[0].textContent,'Localisation : '+data.get('area'),'Demande : '+data.get('message')].join('\n');
location.assign('https://wa.me/212707072297?text='+encodeURIComponent(message));
});})();

(()=>{const form=document.getElementById('national-finder');if(!form)return;form.addEventListener('submit',event=>{event.preventDefault();if(!form.reportValidity())return;const city=document.getElementById('n-city'),service=document.getElementById('n-service');if(!city.value||!service.value)return;location.assign('/zones/'+city.value+'/'+service.value+'/');});})();
