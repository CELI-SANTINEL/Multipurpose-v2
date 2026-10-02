# Protected
import base64, marshal, zlib, os, sys
_EXP = "__init__.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("3c296abf78047a7411c91692a8f1e5184ece27f7e45aabaacb51f6839fc2fe0e")
_K2 = bytes.fromhex("c24810c1e74a405fc79823a5cf78cb4057ce4ed13012fc81e759d056b5241531")
_K3 = bytes.fromhex("f8b10f13bdfa41eb147bef4b90796ca11f26ba291f319640d2c3113080cdff09")
_S = """ehLnuqOfCOHcjkYCNNSxrs{LXBhFLGcES_wIFiv?RlEY`;gU@MXCD2jS$J1dtv(m`548!SrVl%Tt
1Aam3$y"""
_B = base64.b85decode(_S.replace("\n", ""))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
exec(marshal.loads(zlib.decompress(_D3)))
