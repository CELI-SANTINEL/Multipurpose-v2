# Protected
import base64, marshal, zlib, os, sys
_EXP = "loading.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("31cccf8dfd59b99b3f2ec745f38573a4b22c5bd46754a16a8d2655168bc15825")
_K2 = bytes.fromhex("18c406cbf05e96fcfe163f5ab880b5b1bf80d764535335bc350a80f7499115ff")
_K3 = bytes.fromhex("9de71dc9e6a4f312da0c78145fb1c3fbb35edc80f574cda125532cc981ee85c9")
_S = """%r&n=Yo|oj?^A^<#dH-Zt~R*&k#YEL)@ORKz$Od|#`m8WX}d{mFKyn5z)m3DpKFjg1;2S@KWDfOt
B=g0PTa!3Zju=M^Ms<G0ffTdd@3>g=OgcT9whR3&701B*6-hp?en;OeBxnE<ki0mr;v!yJ4<PTm=
BtwMvqP+M&HoB@{(KL-^4;z(6BbWIsfryhI!EX@p;M`%+?>{*JVw=D_5q%nzqt~HS!g`ka|@pHy;
MV9OIF}EB&KbXET#r{p*`<8=VESMA(r2kyTQBd}R>=F+J>~-5^#`p~PG$3j`G)A3kkaAU6zlqj?n
#|6XCEeye+Pe#qr(VT=XMqn>7CIp8B>HTpQLwIjNbn-OeI^3LxKr5kU}*2Wz}rXCqDho>4*WIw!C
3<^eTusRb7^tROgu^a?}V6+&vLfUIB$VSS5C)%|5s+YE<slkU8)>hPFZ*a`{`Xc%<E;>Zwg0I+_j
k{5{EUm(*viNAkh3km@m#W+c+TIVFFn&I}(tFIp*#C;5^xk?Rz`59y78E#bg_-Vs^;yzD<gw7n*(
U;Vsjpc9PWT-FEcmb&A-p*IjB5=hb%TCV{;hdV2k3oQiRjYTn%p9Io#St+4b9j@#COeFGwedx>EQ
D5-D!@8t6m<FYs;~krLo+TLDXxJ6oxuOz_K?V5o;2)Ji!Hsl_9PpL&11UsX^p(h(J#8KAxt>(81Q
~Re_8vACL7eS0ycGll}trpy0yj&*f@D6q>>JHl4aY>oX*^*ZfHHj5Y4qy#;3`;5A3blYf9F({K"""
_B = base64.b85decode(_S.replace("\n", ""))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
exec(marshal.loads(zlib.decompress(_D3)))
