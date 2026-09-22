# REPAREO — site national

Site statique responsive : 9 métiers, 13 villes et la périphérie de Casablanca. Identité bleu nuit / orange, sélection ville-service, contact par appel, e-mail et message WhatsApp préparé par formulaire. Les images existantes sont des illustrations de présentation, pas des réalisations clients.

## Générer et vérifier

Python 3, sans dépendance externe :

```sh
python generate.py
python audit_seo.py
python audit_security.py
python apercu.py
```

La génération produit **1 000 pages de contenu**, plus une page 404. Elle préserve les anciennes adresses, ajoute 100 pages pour dix nouvelles villes et 31 pages de prestations. Les 71 répertoires de conseils par quartier restent en `noindex` : **929 URL dans le sitemap**. Ce nombre n'est pas une garantie d'indexation ni de classement. Les pages locales reprennent des contenus communs ; enrichir avec des informations et réalisations locales vérifiables avant une campagne SEO nationale.

## Modifier

- `home.py` : accueil.
- `dist/modern.css` : design responsive.
- `dist/app.js` : navigation et formulaire WhatsApp (pas de serveur d'envoi).
- `generate.py` : pages, coordonnées, navigation et villes historiques.
- `national.py` : dix villes supplémentaires et 31 prestations détaillées.
- `prestations.json` : catalogue des métiers.
- `site_config.json` : origine canonique. Définir le domaine final avant la génération destinée au site public.
- `dist/assets/` : logo et illustrations WebP.

## Hostinger

Après génération, transférer le contenu de `dist/` dans la racine web du domaine. Ce sont des fichiers HTML/CSS/JS, pas un thème WordPress ni un modèle Hostinger Website Builder. La configuration des erreurs 404 et des en-têtes dépend de l'hébergement. `_headers` et `_redirects` servent à Sites/Cloudflare, pas à Apache.

## Avant ouverture au public

Confirmer les disponibilités des services dans chaque ville, les mentions légales et la politique de confidentialité applicables à l'entreprise ; ajouter des preuves locales réelles et valider le domaine canonique. Aucune adresse d'agence, note client, prix ou délai garanti n'a été ajouté. L'aperçu Sites conserve son accès privé.
