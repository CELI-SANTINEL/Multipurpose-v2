# Protected
import base64, marshal, zlib, os, sys
_EXP = "__init__.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("4c2acd747ede185d00d80265c1545a034a9caa33620cecd4bd10712d72c56364")
_K2 = bytes.fromhex("c33bcafa2ccb4f40343f8784e099344d42d562aedc047b990db54838475132ce")
_K3 = bytes.fromhex("f9fdb1aa2656a8e8b673a5a6d01d864dae8190c7fe9e4e0abca0e601ccca8c13")
_S = """4mQo`^hf7ZcJmfzAQ1S+1_bz%s3A+{gbe!}Yv&l%C4j-Nw`Iu6C!hzCUs(OA4bYsTgjx}gRKe45_
+HN4dx!"""
_B = base64.b85decode(_S.replace("\n", ""))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
exec(marshal.loads(zlib.decompress(_D3)))
