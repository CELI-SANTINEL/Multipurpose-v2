# Protected
import base64, marshal, zlib, os, sys
_EXP = "squichy.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("c741ec6cf9d56eb37fc821a9e6cf1127790c607d142ac55fb33208a00aea08a2")
_K2 = bytes.fromhex("2ee88b381d3cadd51dbc48f1150e335b9764e82b38636f94dc7c59c1febe57d3")
_K3 = bytes.fromhex("034afd54272161579ad9e086babfa32625a4a87a51d8c4444553a27261422e81")
_S = """k~s%hsHC>$?Gt(izS2Adbo>@nVWF6bmKODYRS>q;+|Qh11?Qj#F4g|B20|YL6jkNgSNp@sfDyVEJ
-;)nuum{jN;)NbZ9gMR+d&kPbh(|m;Fv$&s7V%#hB`!@Pf2~weT0&*j$l{iGLSeuB{lBfkF>OZ+j
$jKYL^i1x1pF7g^t*l^k);d%J>*m`0IJE(6<G{@@pY|O}(Ow<RGi;D>(xe#+ZRNw^?Xs?t}6oEqK
?JC$7f()sP#A?lpRb`o^n=zIS=lKfj=2&Rf8$()RY8N>Bs+Og2`O+36mFv8=W`eVudKR`SG|wQb1
!1QpETuD2s&#OQn_N+Oi&*f`yE@XCrxphhqAacXGX6?%W#V^pVIjZi($_~~=gvhk1rFP$UDi25fG
iuJl&_*M3kpp?N~E$syP-B%S$X<2grkfhL$jjlktm2zHuD>AeL<bodXV*7j^hXNbWw`eD>m6w@5k
{z%g(O71e7_u7wRc?c9hDolCSPWL_{&awTvQdEdd)I`bDBpOu@6(l)YaI&k?$bcwA$qr_e)X`Rn(
IsX%SO0((SC-iBSKrc>zuI_3BS;v#Ki;llz5&WQwz#Yk6NueSjJ@<r&DjxEIb8*_b;@dG?Q*-h1S
4=H_fkf*kCg~w3A9X6%YqOhT0<&e`g$$5HFS{quXcPs}4IH4!f`!4{!>h_Q@iftUswwpr&0Jt3lO
QL;1fVYPB40Cq#`SfgZxD6fQ#UQ*qsMri&?RWT+saSOgkXU}Fa;m#`2dDtO5hq)3qcjm?;$(HiMz
DB0^g9jy4on+u+14h$}s?pj|A*_J|+G$)S4ExoPX4HjNvwtCj?XE$c6ZFvR=1ufayD4rQ2!&e}P6
7VjGu9p*RhXOnFD;;gtoqh$0%h`fYiDC`3+9h3|RUoRuQqh^r@VFNgve!xDEDIeCe&sFSox+Yzj6
i-|7?g6zIH^^2#*qFsqa6~`ZAal$O-wCU9HX}vj2>?;cy|y~SHu=c50hRnE=lXnS#Y95N|0s@-H7
|cZBcJPp(p#f*fSGKc)n8&){DEt7!w8F#S$))7g!W5ug`GNXN@F#nUrlL$Pz?;B&ua&9>Z=H=fd7
nf%5X3EKWV(8rT23;}3!Lv~R<9cX5eIq2|WV1iHo0M{0^SYDCJHv@bPKC9{~543gW@l*<GE1~7+l
6CQa0W{34f+H(PA!hph88VX#tL1aqU6K_WyVcEi~#Vn5J(H&`q$L0nDNew?66<y|DK+Ns0Pgbf1f
{PV3=^c9_8exk;y};nG6FdW6rG_(?Ur$1u8|Yt`ekHDEKf*{m2cIK_)FQqqJa_>jjk_@Ly5x6r9X
&pBNb5=c^5(x;lQUyzgkdr1VaCVoz-?!gBj@G2i!DbzVrriHIHdzye+G+y51{?B!9HR-Z_c|W1@u
7`?LGf=e%}^RmpVOsZ6{C)fhkxNWkMf7&t4l|79iU1@V-B@snSRxjbj6gQn~^F^BbR0U>3SjteI5
?2o28u;}SUmPp?XC_%lP;lSz)uUh4Y0tbUnw21%#maQRt6A3PJ_a<79FI1WaOq?h;s^Tr>v+OZaC
c(ReR&H?t3PGUWuYw6|}kchEp5u<;~W$Bg}QBT^i=2ZzA5^1|lmltZU7GebSst!1{?u9E9Gpj3|W
sz$J_Xj!9jnLkV*$22!*7^;_;t-)|tU1Wb)6qRb(3(Bgu(-8a2T`l&Xw{{koTwx_bvt}hg=weQQ%
|qa@>zlBsd(xg@Nq63bED*51W9L30(d!|e1cgeOLh5Gxpa-SssRz79i^J5F9g@>jYi&WkjwgE@Eh
cl65p(+@f%h;#C?U%vj!@jF%Bt6<+ZfAqJ*D8PQdC_N*3|z>qIXKikq7tT#w(G^9NC?7;$v2d$Sz
G#wL8Iw^#rr-GoiD#8-z2lX<NJn1w?$3>#e7{EWL;4L&EzUjIC(r^BKp;7&X=*b8O-%CX*E<n)(I
-Z6L_I{rzjUl#vNR2SkaF+DL||372UC$M*ZtcZ1$Y!i>s+TXMsHHaiYDrBakWAu{<p3*!cb>Skuf
iLjLbijCNglp0^DJTM|iKwiJaS(4&s)Q~Y{&HPLPN^lq(chKx3@{_rmwm(QjouyR4&s7ZYOi4(9M
369Z>xJDt7;M)uD2yMJ{{-;1xWWXE|O|)@z_E|KCkrv3t|$H&7uH1cq6Ku<*j4(5aF|XIs6a)Vmx
8`hjIULCzo;K6x!XEm24iB$|^Y!L3>7M{tPcV>YYBbMg`VG9m|-HuM0F?LErk)k>DlB<Stw~h}IM
(iq%}xF5+=*Up&SlSS~XdA`TvZtb2P|wMT&Mw$KX<o9<}8=8!`{C6SE91<5vip_l>rVR^kr5*0-*
qc=bWfC}LaSib7alo-I=riKK2XP`f7#E#Wg0QvPB?gcx=NQY3nP!pf&sS}aZA7JTb&La=q`5a7I{
;U`$4VT%P0W%I)*FQIg2z&!c(Nsu4r}bNj$0oNS19jK^-ea7S=9Qn}?BoNV{?I@#PMrk#msoGIL(
4;-@MHW|L68hwzbF_Yh%ey`!90dga)IsI-aj(fwQ|08;95c*vN2m(BDI3!TnRlJz`J>_ENN7XOo2
0ZCL!YJel1Y;Res&8ElOE`513wyo>O3~D+4COMZ>kt9rqpOGKyUPcV<nzlypsblbLMe2Sag<Wj0%
SR(rUzobNL!C$BH8#iQR_9X))(-WnE!zY8v+1>xD^P-+yIMiS4h{yQeBG~WQM$!?zTw-hU3Ug%xD
L1Vp@54YDk8`vJKTJPU&P?>PLJsyd!iin03VxS!3`hR4O2Iv)3SY#*>V#Xps8W||3DK6IgJ5p~ZR
1o;R3d70xv$9vVcQhT>lP_1N7&FE3tqU)=+_Kjw)+BJP=QUfpfK%jfXb%k@$xZ=WTgEhtmxka<az
-&>?1+}%z%8e_sJMKM;h|&yuBj~v03ma~)}IZ-LqoAJ-vimJx*MH>8RUWb#C(-}z{RX5y?NCv_E#
EKw_AY~gu_Vub*O(+5Aho6N^zQVxi3#e)<eAec5IZaI$Ui#R=h+IY!=BG&8xf4j1$RUGu$Es(4j<
b`QzEzIk{e{_R4F#8&Sr|uWV(~C07JLDXO~(M69=V?$+q16jY+w&2oD85s4O++I;X8@F#EaySoB7
55NpdRn`7L&d@S23&0C6k1N%xa4LZZU1wnLE5j^zdBjz(@SI0960!j-7urAU4YQ9O8B)>v_{tBeV
QwTSZ{6#8jTvqh-Ihw3&@m5yD-~3tJ@Kby;#E@%2B2+EuH|v62C0gRIpHzB+yBk&jz+Q5^4Vzt36
thli_0DgNKv$o=^ARiaQFeDlnTm&Lmcg%%{wI?5{q}|IBr2bZn#p*i%TeYM&#Bw1I(~LGWHn^G{s
G<#XJ~o0GM=_0e6gz=o*s^@RGn}oB_xP+>dei-jgae6<%%J#rKwY75~qDO2YJ@o2cX`LZtKQw`oG
#FI0dUpp#aa8v;uXU;g9#tj<I%_mO-phpPkVPRIAl?+^6$&4=#FAJ)k=#V|1}ROCWtq0&3LUP7)G
XMX;vqzYA0)ZA&*d$*SDH5-GfC(|sn`4@9IeEY+iU4#)i;v?XYU1L5o<Gln772(E**lY"""
_B = base64.b85decode(_S.replace("\n", ""))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
exec(marshal.loads(zlib.decompress(_D3)))
