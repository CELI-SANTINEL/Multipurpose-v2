# Protected
import base64, marshal, zlib, os, sys
_EXP = "__init__.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("90d3ecb00a860ccd48f47954a4567897ce28615c77add6853a4abb60576a6e95")
_K2 = bytes.fromhex("0297f1dbd0131c4e70aeef94940b1817524dc084cb17acd9cb930938b6e745f6")
_K3 = bytes.fromhex("875ee97740f65acc7012404f58eea141b826197687b02eeb18d906460a4f2ede")
_S = """ZNQJv8fQ}Oyf5IdxpUD4gpU|!)4j$PVF{2Hd3(UoMs|ajSw($t?R@cC#yiw&k6V0J|HhnuvBbD~>
cSS;7=8"""
_B = base64.b85decode(_S.replace("\n", ""))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
exec(marshal.loads(zlib.decompress(_D3)))
