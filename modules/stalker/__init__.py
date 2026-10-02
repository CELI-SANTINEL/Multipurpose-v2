# Protected
import base64, marshal, zlib, os, sys
_EXP = "__init__.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("7d77a537a4ff2f07e66531714bc6dee48ec7eb12c15e5914fc081618e019cfd1")
_K2 = bytes.fromhex("1e7538fcccd2fb36b93095c3a8fc13a66054a75998e2ed5e20d9ccbf0037be10")
_K3 = bytes.fromhex("f6041d84f5516f6aa86e24e8b1881b4d281f97f7b17dfa0352a1d3a755817355")
_S = """?cDo=9eAVq16;OxgL1~pW<Yy&0CwEy26-(ACl<%}#%lM(URsP~QV*w({5r#>ZImBGEDeT%*0cp=w
678Hm|_"""
_B = base64.b85decode(_S.replace("\n", ""))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
exec(marshal.loads(zlib.decompress(_D3)))
