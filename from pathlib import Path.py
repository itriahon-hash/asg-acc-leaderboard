from pathlib import Path
import re

INDEX_FILE = Path("index.html")
CSS_FILE = Path("styles.css")
JS_FILE = Path("app.js")

html = INDEX_FILE.read_text(encoding="utf-8")

style_match = re.search(r"<style>([\s\S]*?)</style>", html, re.IGNORECASE)
script_match = re.search(r"<script>([\s\S]*?)</script>\s*</body>", html, re.IGNORECASE)

if not style_match:
    raise ValueError("Не найден блок <style>...</style> в index.html")

if not script_match:
    raise ValueError("Не найден блок <script>...</script> перед </body> в index.html")

css = style_match.group(1).strip("\n") + "\n"
js = script_match.group(1).strip("\n") + "\n"

new_html = html
new_html = new_html.replace(
    style_match.group(0),
    '  <link rel="stylesheet" href="./styles.css" />'
)
new_html = new_html.replace(
    script_match.group(0),
    '  <script src="./app.js"></script>\n</body>'
)

CSS_FILE.write_text(css, encoding="utf-8")
JS_FILE.write_text(js, encoding="utf-8")
INDEX_FILE.write_text(new_html, encoding="utf-8")

print("Готово.")
print("Созданы файлы:")
print(f" - {CSS_FILE.resolve()}")
print(f" - {JS_FILE.resolve()}")
print(f" - {INDEX_FILE.resolve()} обновлён")