"""Shared REPAREO contact details and form."""
from html import escape
NUMBERS=[('07 07 07 22 97','+212707072297'),('07 12 12 31 12','+212712123112')]
EMAIL='info@repareo.ma'
def contact_links():
    return '<div class="contact-links">'+''.join('<div class="contact-line"><strong>'+label+'</strong><a href="tel:'+num+'" aria-label="Appeler le '+label+'">Appeler</a><a class="wa" href="https://wa.me/'+num[1:]+'" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp au '+label+'">WhatsApp</a></div>' for label,num in NUMBERS)+'<a class="contact-email" href="mailto:'+EMAIL+'">'+EMAIL+'</a></div>'
def contact_bar():
    return '<aside class="contact-dock" aria-label="Contacter REPAREO">'+contact_links()+'</aside>'
def contact_body(services):
    opts=''.join('<option value="'+s['slug']+'">'+escape(s['name'])+'</option>' for s in services)
    return '''<section class="wrap contactgrid"><div><h2>Parlons de votre projet</h2><p>Installation, réparation ou rénovation : contactez REPAREO par téléphone, WhatsApp ou e-mail.</p>'''+contact_links()+'''<p>Précisez votre service, votre quartier et les conditions d’accès. Le devis et le créneau sont à confirmer.</p></div><div><h2>Demander un devis</h2><p id="contact-context"></p><form id="contact-form" action="/contact/" method="post" class="contact-form">
<input type="hidden" name="token" id="contact-token" value="">
<label for="contact-name">Votre nom *</label><input id="contact-name" name="name" autocomplete="name" maxlength="100" required>
<label for="contact-phone">Téléphone *</label><input id="contact-phone" name="phone" type="tel" autocomplete="tel" maxlength="30" required>
<label for="contact-email">E-mail (facultatif)</label><input id="contact-email" name="email" type="email" autocomplete="email" maxlength="200">
<label for="contact-service">Service *</label><select id="contact-service" name="service" required><option value="">Choisir un service</option>'''+opts+'''</select>
<label for="contact-area">Ville et quartier *</label><input id="contact-area" name="area" maxlength="160" required>
<label for="contact-message">Votre demande *</label><textarea id="contact-message" name="message" rows="5" minlength="10" maxlength="4000" required></textarea>
<div class="contact-hp" aria-hidden="true"><label for="contact-website">Laisser ce champ vide</label><input id="contact-website" name="website" tabindex="-1" autocomplete="off"></div>
<label class="consent"><input name="consent" value="yes" type="checkbox" required>J’accepte que REPAREO utilise ces informations pour répondre à ma demande.</label>
<p class="form-privacy">Le bouton prépare un message WhatsApp. Vous pourrez le relire puis l’envoyer vous-même. Pour toute question sur vos données, écrivez à cette même adresse. N’envoyez pas de documents sensibles.</p>
<button class="button" type="submit" id="contact-submit">Préparer mon message WhatsApp</button><p id="contact-status" role="status" aria-live="polite">Aucune demande n’est envoyée automatiquement.</p><noscript>Activez JavaScript pour préparer votre message, ou contactez-nous par téléphone ou e-mail.</noscript>
</form></div></section>'''
