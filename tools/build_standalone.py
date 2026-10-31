"""Wrap the artifact page (no <html>/<head>) into a standalone index.html for GitHub Pages."""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src).read()
i = s.index('</style>') + len('</style>')
head, rest = s[:i], s[i:]
head = head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
out = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       + head + '\n</head>\n<body>' + rest.rstrip() + '\n</body>\n</html>\n')
open(dst, 'w').write(out)
