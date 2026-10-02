# Protected
import base64, marshal, zlib, os, sys
_EXP = "kompas.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("23ce3e61bdc5e2b103bc7f63ca161e16b6fdff7e1f8f01b5ec8441c9b04d19f9")
_K2 = bytes.fromhex("6bb261f932ca19a1209971c461ab7e5e69a94125422c7d63f5e9ac9d4e5c4fd3")
_K3 = bytes.fromhex("19576a2973ccbeb29a2febf4b19d5d58e885389c402221185df257320177513a")
_S = """De<7@qmN!|pp_8)r~ZhYx}Y`+j4|15fF21o0peTm*$WMm-Hq8NA(rP0k)8d9!mBlW6Gazo?2xZ7t
3$K7Azz(9H<l5Y5OZ0SFin}dcpt~b#G+>!?+avomL5M%4iSz|yGStA448b1b)Etv#2k9L0^Z*9dn
;<$1VL+l(qeUzn?l!3s1GzKnL_PrW02>lB??g2QT#c;eE2dQupyg1O>m=w`z!yUtb~7Fr!d@i@>W
%Dm@MUZQN1Yp71>C#WCLE~-b+sh%Vzjqthu^JHIIjk-$FVeYYd%WQtk}kzffWfxf;S!vL`Oyg^Y!
pN)n?HBVzn@qn0MRJgZRS_Vn05{+P@{5YX;fcAs?X0h^vegl$v2rXv>h!m9O60Dn4+AR7FN1#26^
)3hH_BWc2~LAqyswZJ}(HYsRNpBL1V_kzN-f6D(j!UE+ve!NNASa4Ry>F99k`Bh|9CGs=KAz9}R2
mQmI)ZpR>gK#07^ymdumv4R_-MqSatSWtF2<V-UPCRht<=N{mGfmY7e9k8C-v@QCMlsl(1l35~nW
zTkNGdn2zm$rmW`q`E+`GMA3}o#Ia_vRL`Tl0lQzVVqDpemI!n>?5gbJgIH(O>jZ=h_XHEsFONI^
jJ3(BU3%F8nNbDg7Tb4<22#Z6=Wbv%^xSPV6SMD=>KMp`x&uhEShf*}+-eEbNuoWh$#rjk;`&zjv
}wi@@~@*$06+BK*w`86dw16u~{ycplF;0Iegz4j^=KqW)6_{j<eLa7LHmAsexeW^CUE1&x2ytakb
aw|0ae8Hwy`~mjc!IYIU*4D2CT!HS3*u5ZZ!r^zYRu(;pIF!(wi5PZEi-lWB5g+x%RwPO2g#$~+)
yR%W7=1)Ew{wg(8<0!j2p2#zT1eB?q24*_yyIvGz(p=h-AtC?d5}F6H2A{7sB*(XZ@385r8E83?z
590e}uk4yvqMOI7(9XJzG=?lfAn=OB3&P;rR${Dl-^Qc9Gsi;_qwvO>t)lQ3g)?{Gr2vS0%K%Lqy
t4xg7f(yR<2V+XC4$USW6kh{MU8+<+IvxI5$wDgCIQ{IW7()vUCV8{t3gX8($d3Lr0+`HHjwa)%C
VS@C=b&Xp~4gTig}=r58PbY~}!Jt}Z}ba1;8A#1mHq1E_FlW86N3`eD$+na|+YP<)x#vng<?TIr<
_?R*yTDxC+@C2LP?`u?M;b?PKY8EhEMb{R1gztwhC@Iygz?%n(@^erBwCN<DbMm}|hXiL7RG_$bt
jzOk9_jEAGd6R3qLDL6VzChyXLf*kKZu5VL5T!rP0L?k@YUK`*gz0@GiGeGQVMI`EMG)f*LXg0WV
)Fk^G3_ut!nem#s`iW(=pw^fEDZ!r;YOhj`=QLUDi(^|H4=LgiblNWnYD*b{sWH!Q8)UH;9W;cR9
-s1Ic{p_CU*M`K*#%#p<)>U38F;Ew!=vAqK7{Fj_{fRFUhvoTEqnmt(7JK+ebUGkTz%p<GF=JSqU
APOwp$1(QD?Y3_6N`voza3s!TE$Wiwl3dxUezKcakVINNIULEGr+YZg7iqJ5)Ygad8i!l#*p4R%C
n1q1rYGY8}znaC}Bx5aoyUOR>#(KX-W*gO;r*0_UGCnJTUNGFOy}rcPT96Yh)8k@5lzhuA(yjIl|
0?99=wm;mfgAg+gCQg=lRkYEV^e!2A#8I^Y{Fq;FhW%lmy=+&I?-I_^I`6CiG;-yO#Owb-k){RX=
bYTuEGPqDC^44gH`t(DN4SSQNRP5Bep6>t2F*>B}3u(WFn0OTcYK@JpZ{cgEfoMpmm-ITE1PB!ok
FCS@dBQCB$aL5qx%x8$7Ld4XGObEnE>F>h7>K%`QwRnMya9U>`U@hbI?ujl*o9Z+z8E9pS{UBH2b
%>jwqz(b&ffr{PdKUKFR>=umeR84$#0DYCcLPw3l_y$by78IvuoR*bGRPK=Y4lBE+X_xq_oH2v;t
V#Y`aZ;KX(XuGQaV#a|#*XhWTC<`nYh898kv7t9wN_#UWR~8<O#yiU8n3Yd@%wc~aU}67?%m{C-<
og;A!+>Fx6d%On_eLvT#H*udRJ}yps0atCjLpOK0=~|TlYeZvI#aTdX<GxQ4H|WBQ?>HFZ(FBYD;
-*lg;uj-Mz;v1|IHLqg4ii+Jo%%-$GN$cFU5K{<|(K3Q>fIH4?}Q2&t-^?x(uEh`ES`GaV`PK!TO
JEhzRgUI(=_Bc9=_+A)=w;;a^&DAApt>L`WiqW_qI$5R5@z6U@83huD+Ug@yJk_2X}CY(RFBb25O
W<oX2ekQhwd`~F>CX1vs74#?&-Zk{RmpF;r-;d&1hb=dG^9Hn{yi+N;YlcE)4Aj3#o79GxPahx+M
JO13+XK$a7D*bHe-YURo+W=neqyKGwkZoR+Mc?2LH_%9G;TQ(gYH)#o!<^Ktk2vcdII-%XQ~!Rqq
D`;neek2*MSv1?r4@>6xbGmr0@gLJ!8c_fvqMwg2sf$D?nT57PL-;{k?R||YU}>PE;2>5wsk+gla
sRH8CX!u>P5@hH#R#|3rvHT0h?OeZKAoeIu-Uk`!BrE@Up0!HI}OV8Y!Oi`m=w)k)vjg@qOts&&m
?6P2@Tz(X2Cdxd*4*1y_lF<!34?<_{t6FiEhsDf)C(zH9K1BTSg%rI$rT0NFmtz0`(drtO#&Zn#L
Lq&E(+QAtriDa(|VY|LK@$`67aWMiRQEkx$4_CDgDjsyCbct^JQMGCiVho>;=trl4?pAxIvTwV1i
ZDacBw9;at-2LL!Ka@;jx%6hkn|;+2^Hzz4Md*aI22;!}KhUN{V*tl`X&^f%go+PSU=ImnLtuNt9
&V+9VneGDGBXFY5)WfOwFK^LSRSM1Zh7!287IAgnjJ!SgB9&;$S(o<zL-iVeDV9$VcZiV4cCfP@E
ry8oE(o5ESX8q?=M&Gpa{B{Od1aS{_6B*e7Q(S1`M#s8vi|x7*U}l!*T2IvnkXb`1pJmhw9u0+M_
glO4lRgH*JdD>`A2{5pMm+&wh;9v^0<74oszTv^0ydyE+arU_HpL^&#28!XsT}*WHSifM)wJ0yh"""
_B = base64.b85decode(_S.replace("\n", ""))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
exec(marshal.loads(zlib.decompress(_D3)))
