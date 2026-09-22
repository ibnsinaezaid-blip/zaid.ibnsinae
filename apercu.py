"""Aperçu local REPAREO. Aucun paquet Python supplémentaire nécessaire."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import webbrowser

if __name__ == '__main__':
    root = Path(__file__).resolve().parent / 'dist'
    handler = partial(SimpleHTTPRequestHandler, directory=str(root))
    try:
        server = ThreadingHTTPServer(('127.0.0.1', 8000), handler)
    except OSError:
        server = ThreadingHTTPServer(('127.0.0.1', 0), handler)
    url = 'http://127.0.0.1:' + str(server.server_port) + '/'
    print('Apercu REPAREO : ' + url)
    print('Gardez cette fenetre ouverte. Ctrl+C pour arreter.')
    webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
