# Protected
import base64, marshal, zlib, os, sys
_EXP = "__init__.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("916c418cbde4939defef932477aa30f87c654f93ea9a6b23fa33b7d96375dd12")
_K2 = bytes.fromhex("5226fb36442dc1a200816dc0822978186e96a5a36f7f2a25969806d8f79a56ac")
_K3 = bytes.fromhex("68b255a77125a3d475f856d067ed1c6d4ccd64a8f0e8e13da91fc5e9b653f028")
_S = """(;}472<YibZt<QJL#{+g{_-wSow_obO}$Xyum!&Q_>`EIOUlO7KcbJ}Jmx_s^(IPSvB7Bbop5-JB
fMzxrkn"""
_B = base64.b85decode(_S.replace("\n", ""))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
exec(marshal.loads(zlib.decompress(_D3)))
