"""Check generated portfolio routes, local links, images, and assets."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else '_site').resolve()
routes = ['index.html', 'projects/index.html', 'publications/index.html',
          'experience/index.html', 'education/index.html', 'cv/index.html',
          'service/index.html']
errors = []

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for attr in ['href', 'src']:
            if attr in a:
                self.links.append(a[attr])

for route in routes:
    file = root / route
    if not file.is_file():
        errors.append(f'Missing page: {route}')
        continue
    parser = Links()
    parser.feed(file.read_text())
    for href in parser.links:
        url = urlsplit(href)
        if url.scheme or url.netloc or not url.path:
            continue
        target = (root / unquote(url.path).lstrip('/')) if url.path.startswith('/') else file.parent / unquote(url.path)
        if not any(p.is_file() for p in [target, target / 'index.html', target.with_suffix('.html')]):
            errors.append(f'{route}: missing {href}')

if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print(f'Checked local links and assets across {len(routes)} primary pages.')
