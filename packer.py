import base64, zlib

source_file = "Blouch62.py"
target_file = "blouch.py"

with open(source_file, "r", encoding="utf-8") as f:
    code_content = f.read()

compressed = zlib.compress(code_content.encode("utf-8"))
encoded = base64.b64encode(compressed).decode("utf-8")

encrypted_template = f"""import base64, zlib
# AHB Protected Script v12.4
exec(zlib.decompress(base64.b64decode("{encoded}")))
"""

with open(target_file, "w", encoding="utf-8") as f:
    f.write(encrypted_template)

print("[✓] Successfully encrypted Blouch62.py into blouch.py!")
