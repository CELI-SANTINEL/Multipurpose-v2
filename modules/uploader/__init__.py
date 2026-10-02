# Protected
import base64, marshal, zlib, os, sys
_EXP = "__init__.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("19522378383863f105e25610e0b715c32f9d7e264eb91232bbdeb02a320479f9")
_K2 = bytes.fromhex("82d0cff4d2d05d38b66e0b756fc8c3ff9f30224b15409d9f41e6fd22af97dec1")
_K3 = bytes.fromhex("94491b7001b360df5e8af1d58b6f1b6a584e46ed11423422b103d8ff92c85e59")
_S = """cM*&*YhOmU8DW}`)zICNNH4lcq6{f6!!oh|o#H$VT&I9{D1B)uNHU9Ms+idPL;K!%j(2lM6aSf$4
qNI40<Q"""
_B = base64.b85decode(_S.replace("\n", ""))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
exec(marshal.loads(zlib.decompress(_D3)))
