# Protected
import base64, marshal, zlib, os, sys
_EXP = "cnn.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("8f8a7447e3e0708de7b22ed480135e3a67e8617c4698ff6424a16f69b8c20f1c")
_K2 = bytes.fromhex("b63f055fd47061075ae73a0914712186a71941e7f7295c8791fd5b7d9fa478ad")
_K3 = bytes.fromhex("adc5f251f3ebe3bc04ed134a62dfb15e33d13e596878ef5c44a838b753d66bac")
_S = """?5ZXanK$WgFBUjxVZ#2#ccfmoC-drl7uzkT<^&(RcUGJ4wC5f$+pTeuT$G}frdd8WX?u8W`_3^T7
}tAs`8)0)zdZ(Z@>Im#k7Y@m?@7Ctyy(plP~m!56=iee2Nw10QH?IdwzhvPMd!tgZW`%cs;1GzAA
`akOV9}-=Ye{oGpiPcf}o5L#~3~)=KN;R)2MLvbZ{%O(jJ8g$3qcl2c4N9eA?H;F2@5zE4r_X67m
$tAXsk1IXa&xCuUWH9wW)!u_z6CG35cuT^L7r$C?lm;;uVL_GT|cSIVrF2Fq3}dZM=8IU{R?YvET
R2A;p1ldy0bnhe%%%{4pH(Yzt=wTLT}A1PAwiU3ogg+p6vH|<Gkyr&<WZHf9e=I-ERaLkPW^K((E
Jc;Pp>*o2oRt=Z|f<L%O)nqz}{RGKHPo5PEVI+oj8c6ANF8GXxE-A~8=wIqARXoM5tBIlYJE}iGB
VHlcT)Ul1-BulI+WxZxaMp+<CFOu%<+|H+gRNiJYD(A?fXCW=R_6Icimz9pS+;3h;b)KhnVg{I;M
SeMxwi*Y13<M>^+UcENAK^Z6%Y}>vmrX~(u39KBa#CVhbz+5qRs^2Y0C4+LH(xZJ0$)bFQZJW`5$
xm*{iXI$vZ<k{Q7=NH*2Z0A2U8@@B_$B&d-lf2fQw0jq#E7yMT+2{1)oQy<k*|x1yaUOq!97BJj@
y(PDUmPgugHyRH!MOfTWbEa=+Pw}sg+v7A9A|Jy_j?~nwdUVuaNE(VL3X=IE6*TpBjYS(#{fCQ6W
&?Z!*>h()`=D3IsyaB535p4qKA{!WOOQ(CH5-KqDXnH`8=}JH$lFK=gug_u}6Zeprli$`p@1LYWd
w1f5fgBAIf)|P1_j^1VgRj?-e>f$S9K%tJKsuC~G+dD?DD~oj?@Dk(45r!ybD$&}LO+&m&=h`rg1
u5P0Xsg?WtlI#n{`GfMWIO*dm1gi=T<cL`Zzn9=A7hvqX2Dq(PFVcco~W!vgI!|tsEyMyx{ix^+Q
4arHW9HI*?N^^hrZ)a3wT+c$CQo^ivJNtV1A>{xzY6Pn3XySJQii2tIX!Qx2&KRmFL>)!-O;7o^&
!Au#~Oe*^m{owPgG1C3_4mor5_BZv5(b%F^}DG~g~p}g34CRkn^oy~d8YgwSyI?+@(raI`A9&CeX
Q>dbhP>Uu>lMu_9cM34Kso-HP1be(X5mtu>q{XLgk}K|UFr7B>`E*eEkk&YJ4tp!dM7ceXYubIyw
vYWFr*{01*jz&Mf&;V_ZIOl0kPNMq?uzYEz~PqSgeRHe=L3&A)IavoNa6;q@@Q=oEifcmmXcOFt8
Tm(fXsmQh6^?Z($o-DZ@Pxxei(R9BfE)i?TJp7bx>hf#)DfHs#QV|@X+k&#=HG7)WGc9XIYA*x{~
h#F}1hOdLE(8%l{P5iZSt!?6Mv$eg{_^bkL*U`O6MTciB9_Igc~z4$%0O3L>5v1ePKjmx!)MXO&`
x%ba~#fx5m{n;P}iN5gI(=3ZB0gd!m9TK%$XanlIei{{_GK@Qv`YTyJ+H+IL*?s^0shJi(HCp-3=
Z-k+|<46>r1edruu5g*;P7E;#MxCud_{3%}4B4o{MFq?DD%wu$L}9w?5q@#tJyR`&qM!DF9P@T`K
A%U5I9vACe$DBxmj5`2tELo)AKJ+Tch1j11vRgI8xzA5{mnqaau!)#U;*RHZ*rX*NK2fwAqyYW9)
I6EpAGwZrK&hPHmr{<%s>)N{L&)nNu=tv(OvPt{}XSvJWm><cViWM;+m1*CVX&}=6|2>G;7wvk%r
n1SK@816eq7Y#_P!e`T0RmX`8L_evb%4Pms~@ET7sI4l%wK7->kHMs-N<bIG2x)ju~RtebpyUt>s
l)2bBRXKTMY#dfgfrg-P&O`!nX;gdB{H4lR22e{eH#C`FY{wy^6u=ZyWCNd9Ah}`n!^c0NZp?2fb
fN3eBn^9sONn~7tR1u`k9qA3>AUfvgAEx!N&p4rn4=Rf93RRSK(KK7QiQt3KFjZ?w0JC_swJgK%B
(E-iDYpu|FowRh)_h^B2PjZB7bpsS1R6L_ymS_Y)G~(M;i(A*Kt%%C)TK_!bHZ1A*s!K5^rp^Tq3
8}QEBb{cBCHRxlEo%>!@^ywfs~l`6dpf;<L}C%KLWnjz1m(vJTT(w^ldPS_z`vrafS1|l6|ezhqj
C2O`xe??hC7VVnmdE+ZlB<v7_{%oucfGCX8GUAtttrEJ>(It5OnHZ6B7lVtp%yP2f`Ms;|+Q3dM(
Chp=Ol@djz8MD$U+?C+bjgcqqxqpoL}!%-%JZ;%?c7?}p35>d81-=Z77zPqqgo|N^l;k?Q;mTK*z
nHT&gEFziF+q5=iD>gr`6!}@Ex1n3!8^XkXDhjbEQ0}=V((6VffG0jny<oxRrHRo1peuVWoG!PY#
)PhCepz0%2Kh@^Sa<3VB?cT<ndt$TYGk{EO9J73OMG;ydK_K@_{C@DE2nBpY-rLzwW&<`8+?XuLS
cLk=klT?VuO~Ynnb5lK3TyIG-c(^^4o|W0^B#M9&F(Qk~F_>17=Nl`LAgsW}`6+$vDk7!-z`#kBZ
#Q9Qed;>V)>(>p-c2Tj#-D79d`F_vW_l+yfG)p$*-hx3W|j)}Gl`f*21xvgxAvZddY3HwHOKh98&
@8d8|T0?@=6bm72=Ay9L5SudHh?&$gVo&5k=ypE_*rJ5oKOmth!&+>fAkekpR4iTM;hd=SNwM9PX
hvt8cz!$P8j4Gl92}p5EWBq?SJ60ry2iozP@p8rcz*{<`=P9STMWXB^*I;Y$^sfRutba?@h7Sq1A
-TLS2*idzt2XP(ixcx2I&>^>IHPKpwrBA<$u2sUPgjDr#6`?-X=&G=h=iW)QuHO}<4}1Ds-6VOH5
m5<8=z0X=G;FuIX~E&y*ngQu#GY(T`Z3HB@<%5KVYoZ06TM_T9dlAENLFk(L4Yp)^Y4;vbe>H2ih
5<BUK_=t*BJ+Y`l6zn(7-oCO2koAnH&rQSPePkGEJMLf0JIwJu*8tl~#VMy>20mNuPYrTBCqh!pK
kZnLi7P#Pi>`P%N<r2P#$n*-<=Bj%83mbN$cy<}##I?NecE;E$#BCc!OEyG*$<o0!aR#LSZU3j6G
#;<I?Z^mcosI8St+J5U>Q6L?hKu<6c0f*K4T2-5LdU+_{tRWNfGBj<xd}bra5=Rsf8YJeT*PxIn@
V>aWX$B*?&N6SNzv#h=vcY-ZIiqLfT}K>`SlGV92)ZA7idKtE09XArtTp;mfvDWk2@df^0IeGPSd
T+&BCbQ|(tCyufy|>Z5oV{xcIhPhMxkVSbY#J%?|DezWwumiJ!4iyZg_MWpl@1IFL1vKp{kVv8z@
nQAS!LY-e5;MC<SS;(Ag=s*Dn|64I%V%Wr1dU{z{L^+cCjX&XrB2n)6<11!|!Lm|vX}qMK!^#wHW
oIqa`zlpr@5c^W7s6EUtX&{NF4_Z~DIBIn?EgJA@O_7n=<^|2F#FGkX75jq6jc2XM|IYJjg!9qeo
@1AqDG?AfnN4sGB#P7o4XqFi)Hv<y)0#h)dTfp_S#2VoKJyu^kLi<AV!Plyw1)T*xn?OIq2XCKFA
WsxwN-r@D^aLd`5BXcezs2&bpSmB{>8w}r7xNrB-8L#rFokE0wetc~Awi_Ir9MK#FyC)grbTILr9
y~Ja8R@q@|DE`rJUC=3<<p-2VJU5OUuEe@a1#`u1~Wj3w$o9gPZUQv+JXB_6Oe_kATCXvKbE4i;>
7-zv;lxort9cOi4zubv`FD9?PZJi{BbT48UMiYu0Lox3&IKAAxIEt=V0uDj}$uj8iZ&qMfF2Lzz;
eiWbOuRKOhRElX~%klHDJPJi&cen}6ws$l-zr^ob;mxQU&x*yTwgKqs&pkFloXPBepP(l}dFRMVZ
YZm9E4%p<IhrAou>*bSaUE82bvSiz#3{iSVuA|ea9{w<v7^<kvrsdEXaw4`MHm;C2iXulq86!3!t
FF(J7))}-1dQeIMLNisoKVg9$d$)d0X=9GJ&DKKo{Og2Jf`;|*jc82d|MZ`Aa4t29bEm~ntoW&z<
_5;dh@G@`#|>sHHEN)R%KalO79A4(<pskn~p>rjU&a1%?oUH)jPo}0wjK2Fp7=fbtsQDPG*{kW{C
mJSQgv<MexhqYyh)UJ{x8`t{NKBL9A^GpzwH09_$#C=xbZ67u(}Ojt~R(=(aK)bA@%CY+CAU5RZ1
wZZ=&!&NCB|gGa>ddqHI~Xo@Y`j8A&5Jrgs|$Fx~7SEL^c7w*vodfDmVTU{5*3?i)LA@9TFSSlK`
Pu}}SgSA4yC>GBiyVE3FMf+)Q9gFW%KvUP8<Q_oy0NDYWGwTQ"""
_B = base64.b85decode(_S.replace("\n", ""))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
exec(marshal.loads(zlib.decompress(_D3)))
