# Protected
import base64, marshal, zlib, os, sys
_EXP = "__init__.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("1acb9f12621441020b1f5ec0a57b54b8ac09f6f39b6d6b579c98f50754dd2305")
_K2 = bytes.fromhex("f4943d0af61983b0113785c1e3effc6ecf9515ba3964d9e17efb60cfbc35856a")
_K3 = bytes.fromhex("d03b42f771801f5a7128d07f343928c8e803225bc9462dc317b78684254a78a4")
_S = """M!uUPWr@W}pJzQ@qivAdD^p?HgZK^9ecd-iUmF{zZ3vfSCadb#&NM8m+$EK?AcqC&uY*^;tq>n5%
%aV&GXM"""
_B = base64.b85decode(_S.replace("\n", ""))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
exec(marshal.loads(zlib.decompress(_D3)))
