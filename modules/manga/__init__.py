# Protected
import base64, marshal, zlib, os, sys
_EXP = "__init__.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("0f1c644826e855b72a73c48fef94c137b1ea75a60e9be230a168c52f90f60253")
_K2 = bytes.fromhex("a816c8bee0af3a0301589de3a85ef00836400695fb5c66c5c1c341c5d56865fe")
_K3 = bytes.fromhex("2b634aac107e4fecd8f3581aae4d5d6888e8f3a12af449a92f3e933e00e28f86")
_S = """^s}9oRy{cR2fsH~I7fVwuZ|#FH-umP$DA|V*TpSI-vyD;6(1L8R_rFDM-O@Zq*_F38~+8A7f~CqM
11>Cfei"""
_B = base64.b85decode(_S.replace("\n", ""))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
exec(marshal.loads(zlib.decompress(_D3)))
