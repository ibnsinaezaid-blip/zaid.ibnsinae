"""Browser policy for the static REPAREO site."""
# No remote assets, executable inline scripts, API calls or uploads are needed.
CSP = "; ".join([
 "default-src 'self'", "script-src 'self'", "script-src-attr 'none'",
 "style-src 'self'", "img-src 'self'", "font-src 'self'",
 "connect-src 'self'", "object-src 'none'", "base-uri 'none'",
 "form-action 'self'", "frame-src 'none'", "worker-src 'none'",
 "upgrade-insecure-requests"
])
# Permit only this site and the known ChatGPT embedding surface.
HEADER_CSP = CSP + "; frame-ancestors 'self' https://chatgpt.com"
HEADERS = "/*\n" + "\n".join("  "+k+": "+v for k,v in {
 "Content-Security-Policy": HEADER_CSP,
 "X-Content-Type-Options": "nosniff",
 "Referrer-Policy": "strict-origin-when-cross-origin",
 "Permissions-Policy": "camera=(), microphone=(), geolocation=(), payment=(), usb=()",
 "Strict-Transport-Security": "max-age=31536000",
 "X-Permitted-Cross-Domain-Policies": "none"
}.items()) + "\n/assets/*\n  Cache-Control: public, max-age=604800\n"
