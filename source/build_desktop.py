"""Wrap the artifact page in the same shell claude.ai adds, for the desktop (FLX4) version.
Usage: build_desktop.py <page.html> <out/index.html>"""
import pathlib
import sys

HEAD = (
    '<!doctype html><html lang="en"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
    '<link rel="apple-touch-icon" href="apple-touch-icon.png"><meta name="apple-mobile-web-app-title" content="JustGood Sets">'
    "<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}"
    "body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>"
    "</head><body>"
)

page = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
out = pathlib.Path(sys.argv[2])
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(HEAD + page + "</body></html>", encoding="utf-8")
print(out, out.stat().st_size, "bytes")
