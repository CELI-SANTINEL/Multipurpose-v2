# Protected
import base64, marshal, zlib, os, sys
_EXP = "__init__.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("31dc4907319b990ec8a975bcda6199410b656a448947d60568e01e146c2e2c83")
_K2 = bytes.fromhex("0d7616e78c283e6f473aee12cd4170768cce2a7f01535af2b224fddd07ca0744")
_K3 = bytes.fromhex("6e608c6314742901a72d738d94e49d825c46efccbb61cdbdb8405290a0b86f7f")
_S = """DiEkoDZ`e*+}Yj(QUqjidm#@#+rrc9>W!6AS>=J$0j8t~YT>zGjf&6qElgn_aP?~s_qmCJIzYWW%
3N36U#<"""
_B = base64.b85decode(_S.replace("\n", ""))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
exec(marshal.loads(zlib.decompress(_D3)))
