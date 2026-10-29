"""Embed a sample PDF into index.html (replaces the SAMPLE_PDF string)."""
import base64, re, sys
html, pdf = sys.argv[1], sys.argv[2]
b64 = base64.b64encode(open(pdf, 'rb').read()).decode()
s = open(html).read()
s, n = re.subn(r"const SAMPLE_PDF = '[^']*';", "const SAMPLE_PDF = '" + b64 + "';", s)
assert n == 1
open(html, 'w').write(s)
print('embedded', len(b64), 'chars')
