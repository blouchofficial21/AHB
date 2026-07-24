import base64
import zlib

input_file = "/storage/emulated/0/Blouch55.py"
output_file = "/storage/emulated/0/blouch.py"

with open(input_file, "rb") as f:
    data = f.read()

encoded = base64.b64encode(zlib.compress(data)).decode()

stub = f'''import base64,zlib
exec(zlib.decompress(base64.b64decode("{encoded}")).decode("utf-8"))
'''

with open(output_file, "w", encoding="utf-8") as f:
    f.write(stub)

print("[+] Done!")
print("[+] Output:", output_file)
