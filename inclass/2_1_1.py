from urllib.parse import urlparse
import os 
import mimetypes

urls = ["https://example.com/", "https://example.com/foo.jpeg", "https://example.com/bar.txt", "https://example.com/baz/foo/bar.git"]
paths = []
exts = []
mimets = []

for url in urls:
    parsed = urlparse(url)
    paths.append(parsed.path)
    
for path in paths:
    root, ext = os.path.splitext(path)
    exts.append(ext)

for path in paths:
    mimets.append(mimetypes.guess_type(path))

print(paths)    
print(exts)
print(mimets)
