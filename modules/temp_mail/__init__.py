# Protected
import base64, marshal, zlib, os, sys
_EXP = "__init__.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("56e7524c8ef48ecae1be8a15726381c07a1a1ad267bb4fec14d1102d5dcace79")
_K2 = bytes.fromhex("edc8f98d44d28acbf1686e3be85d5abfb83f7e58572045a05fba6aaa82f6418a")
_K3 = bytes.fromhex("59ff98d9a61d28ad3ac6ab8bae19995cc1699ea6570f80dc2fd6b5e5401d209c")
_S = """nhHqN>_0RO-gkM0<>yl8qkvlFk0Tf{?6m7@4VY>JvAjf+uN@nck0fYtny*)hs8l}GqgX;%JbA+go
*}#o@3a"""
_B = base64.b85decode(_S.replace("\n", ""))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
exec(marshal.loads(zlib.decompress(_D3)))
