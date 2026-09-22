"""Lightweight service navigation pictograms."""
ICONS = {
 'plomberie': '<path d="M4 10h12a4 4 0 0 1 4 4v2h-5v-2H4zM7 10V6m-3 0h6m-3-2v2M3 9v6"/><path d="M18 19v1"/>',
 'electricite': '<path d="m13 2-9 12h7l-1 8 10-13h-7z"/>',
 'climatisation': '<path d="M12 2v20M3.3 7l17.4 10M3.3 17 20.7 7M9 4l3 3 3-3M9 20l3-3 3 3M4 10l4-1-1-4M17 19l-1-4 4-1M4 14l4 1-1 4M17 5l-1 4 4 1"/>',
 'vitrerie': '<rect x="4" y="3" width="16" height="18" rx="1"/><path d="M12 3v18M4 12h16M7 8l2-2m6 12 2-2"/>',
 'serrurerie': '<circle cx="8" cy="8" r="5"/><path d="m11.5 11.5 9 9m-3-3 3-3m-6 0 3-3"/><circle cx="7" cy="7" r=".7"/>',
 'volets-roulants': '<path d="M3 21V3h18v18M3 7h18M3 11h18M3 15h18M3 19h18M10 21h4"/>',
 'aluminium': '<rect x="3" y="3" width="18" height="18" rx="1"/><path d="M10 3v18M14 3v18M7 10v4m10-4v4"/>',
 'chauffage': '<rect x="4" y="9" width="16" height="11" rx="2"/><path d="M8 9v11m4-11v11m4-11v11M6 20v2m12-2v2M7 2c-3 3 3 3 0 5m5-5c-3 3 3 3 0 5m5-5c-3 3 3 3 0 5"/>',
 'marbre': '<path d="m12 3 10 6-10 6L2 9zM2 13l10 6 10-6M2 17l10 6 10-6M8 6l2 3-2 3m8-6-2 3 2 3"/>'
}
def service_icon(key):
 return '<span class="service-icon" aria-hidden="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round" focusable="false">'+ICONS[key]+'</svg></span>'
