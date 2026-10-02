# Protected
import base64, marshal, zlib, os, sys
_EXP = "soundcloud.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("cdcf0532ad0c3ee94bb93c7e46bf7d7f373b3ca522d80a33285345e69f8ca5b6")
_K2 = bytes.fromhex("64825543ad6c670875148ae6bf3ed35d7824483b8577ab01b1d2cb09a7e848d7")
_K3 = bytes.fromhex("afd409dd859a81548dbbc5bc3820f4d9f836dd9c747e801d282f8cf79ca64945")
_S = """enXV?-nPW-$+(${e}3c6An(0myXL1sakkFg+!>-jz!`uJ2p6eV#m6ou#B@!p;wE{Uf(ac9X|)T`N
(z9MvZMne12Y>xCItR_WBCwYLShZTUIHANJ?aosH@nC3i0^CtA!dun5-0u{PGAZgV^$aOOfKEXj!
AxJUHvqe8T|jyaN#KJ_4rdD`z@*xrOf!NM<5f1C0%f_V7jQVwD_Dn7p)Ev0z54ti&*M`|LVdf%IA
$TV_&!ez=-#+a{b>;aDG~Xqg*jzX{c9Pl3j;8y!F+2HJKA0RQ9)G_AM2;lw7NVqB7HA(Yk1!j`{f
km3p?(tw?RT#118{jN*u#%6n2@;V!qK*!d54BnTsmMjq2sHAQowCX9+W3!J6kz2K-%aM$b7`{wJ`
Sulgf6cd8Zsbey{Pi_}6IjkEiCvjyBhyoMmwV^eTTI>cmqoxJz;hC!O5B5tQeLs@bBkAYB#@;|46
D?^Ei>&seFCsuF&&QM%qwDj3eKHDG0(D*z+K{mW39b@tdELF2y>7mxK_3Yu5egqd|GA3bhX-sbSN
{X-bg6$_p!PikN)KAd>NDTf>1=|HaJN6^u8_f$@FgNvM=OsgHor)Nwd=92;}4Ycx2u$lO$>LFAMM
($ONFpB$?1EmGEv&EK$&KV|Blb9C+xLQ6eNl}sw-QNB67JW*nnx<THDhG)LM5UGYuT^F_ni9>{+o
>f%#J1JU$#r&M7kR?+1_{G0YQwr%FZ*<2z@C23{CZ2tx2$Q0zAM#=vZ|MVIN8Mor+gp|%(hW;g6Y
=~8Lwbd-r)Y2sYS+CLSioP+&S7T3^bdh|~ODH)Rscu(bJj8DI@;E~hHIo}0+oulkg0^Yqf#ZfV1w
=feHk!8vADU)Z_90*#)!G9TuLgOa*o8Ct>@Dp0D!JaKR|1cbi)K%h6#j*Faw8U<{)4CgTJ^(*hFE
d#fzhkEA(DIR0)1<(---Z^+Smawh&po=6s2mtHI;7iB#8F+mlsds8DK7w#)!Dm3HO_)lkC|;*MFM
wmVTIaY@k1SlUzC8JCt{2_7?@ElWU8|>b4qA*2I~9zUdGj=2cO^c7|0_B_A7ZoE#8U<65sYj!!B2
F@xb(p!xFTZL-7GUAKi9Ss(AFZ9{P@$(3FHhRBxrqGFf)6^eOV+|5{>GM9rA>ZVA2^e#P2ZW^du^
;&~3^&QBK=zG&8Azp&P~69A1h_5}HPih@lmq?k;ekMB32Z|FPRSH^zNxSyn3idVak7+mBi6$#S!C
GgiEyupP#wSDtL<y)Yi(L)cAiYXVijtpv}TXQ(mTa`~2=GT97`E9SPS%%uDR*cH(zry}TomMrq_(
E)__%Pj4jxYN0g-Xy&%X{SX5BZ{XncBrzZ3(QdVXRJ~VnXBb@KW?tK$^0GWR8KV4`OfxAqfz<rMT
6K=UO8GDn6g$#SbF|yR9RAEaj5&V0MaXY$7Q`xk88F00L@+nbDI8!?~kHDoI1<Qn$r>O8jc;)QCq
5h8;7>4X3id-+tO4RNqkOqpt{UECI=XhOzh@QcfmjT#gxJR9pnePBd0)i=bL|Q%xorLHaTx>qOvT
f|MSV)alt#*Gk!bDY2I*lNxA+io2r-$mCWVw#2|NA+sPlaW$)iSaX`12BKZThz+nf^Rsacn=DqCf
`^%8fuSap#eKdF@S(&eJv`f2F)k)JGh#&RGV*jfZ2xZ@Tv?XnTT_c2j$vRm^XV4I5OKPSwWTn2=X
xSf{}GQSe^&sN;lp}|eor?Mv7ki_FfjN9x#A7#z*>dOeAOh;%E_g>1rOlv_JX|B+_wZG6_2J8fV&
XwM<pf8uPSfHspJ)O%E*KYfRSmSm8ll=PCsQ<drjWEIQ6`|+KHJxe51rfnY6Au-C_M2TIwz(rH@a
v=r&*aN11P@!aQGboM*-F`dQ^NJ?jkD;i?tAp*J9)uSdY?>9V}rPw#tkDy4*V!wO)@Yafl1_`o1Q
#1l#e#Xn@8nY^EV%&am-d)U*9Aj%sTlTl+avTz!2raXy8%3Gv^`udPG>#@X5C%GM}tgF#1no;<o&
I49x6o3l=HP^j|BBY%Mh~ul00@`=oC+p5;lgz+IaW{6}9jQZy<LVB@gS%af!G@h!9=lDXt$fxH)=
d3F=#x?qIeYkj0_+gS3gC{YG+8Z9kRwhBy=1$TItC_ZLQmVe)oXoovle8In6F68sO)CQ2ZPgX$-Y
dqu!5Rg(ll8ti^n(<!cv+t{fbT=oT7j~h~FK7NGtgjn)1}-PX(tt&5=qwg5OO&0KV3}pyi?=bg_|
mn4CZn;`(9#%nTd)v5%2r%tD<|Cj){r{Oo-#aNf;LysP!7w<yEMbVvY!Xky$Hp_FhmJu>sX`QpxH
e*LmGS-5Hv(pKw%k(j1vX-z*N=vtgARf%J_8&T!*`AZ2FcO(L7P{a$+78l~GXOllIK6~thOR4y+E
d^4E@PsT&H-VQBO`ZH(H&EP%@O&I;XTKHeU||o3zVupfF7A9FD0pJP{IM*_eSYJ|2ZElg-R?O#dv
Fz`)3pL8&v2kYYy(^?>Ijcwrl-e##ZGJL!3B@Fi+yO<CtQ)v=VhbNISkJfH@FgA;l%1!X_eM-zPF
-csYH;TVz1{%`quA)qxOaT@cG4smPz5=OI?d&BlRp82BS5d|GXu>Pk}!_gPa3(yVu*4aW!f`AqE!
KMt@x2nLgIdn-y_y1ulFbXn11Ce10vOQ)5BIU{(YD4{3~<90nt9O0(H^(P0I9eQ##bWJ1FAHJQrK
Dp$ui-VfH}B%zP<Vo$5bYFmXECweuwJYC^}2S$8zXqs~z{d^AU95r_l&xv;au=F%{_r%?rFg=O+6
Dv1^*9?Q@RxzAwm=&On;Jl0`&`QvLJnuE@`qQw*G{C#RjIqT_1Y0MeP}c5IK3F=xoXfm9t~v4Mdi
<f;WGv`|=Ih;X)>5gwJ|CvBMSBeeQ^n(+HC^r)srhJkJ45dfxJCrs35jXDYdxn{1r{A$AUt;UCgt
8@Fz3=>nCj@4^8vEk`6!dq21`wXwy!5m$0|FlexKm`&R7g?t~kV@rKCO(w$dgwj&LRm0dE~sr(f*
J%x*@E-QJ;*X+^^kGyFWzhzIWxUGVM3ROc>#RAZ|l8=j2<<HOE<SdZ-^(@a)$wl1<q6WnsA{Fw^b
B|D5nJCT{+?(JlCh5qKpK_j=bEiJNmBI9Ot{N!cpGZd1hpqZgq>$mWDJCk|lXsyK-_BAH!bu~$0W
B21<eC%Mcom-H~w*0Xwk{=ntyR5sj|D*j|&D<6l%{v^y{_nf^^3=tbsr_;uhGxd8<==mM!wVfmI&
hReb0mRL<{P5xfq*Ai3FF|@!Xo>|Xo7#C%*w$CDKgK_yQ3G?Mn<ta0W*UnV4rPR0fCklMWJO`rU7
SnD}@a`Kyb+3f8cjN`HTb|v@7@m@B?DxyiJVni=zKEbKxFbjRG;5hbr%93K|l$9rS*9<S`FMmYS$
rCcs>Ul2l9>_z%Av`cx<bx0BLG(DiG~l(FwAJ^UQW*cMXy3XIr><1TfN-I3dm+aVdUX_k13ujQ*)
Kz|fP((WQIdf*TheGTs;WzE_o3extS^-!S!Oml<u#HTTDN84oHnc)P{80MzyHk%xXNh?zqaoO`zk
WW3sp+_5<w(IRHLC2JaJtx`s3L*H<c!zJ0Qq*6>#F-I>zq_Ys*-n{R%);WzY<Ev5{$2SuJ<eQe#R
Id^N?X>={>M3q*<XGwRRsq|e>hDP4GTdtp>UdH3~9mf6E3Cir6pAsGuUwR55~nA4M=Lo_01`^_1v
Gj%}pT^)QaJT!~?2a^ESywAp-&;_xU%{)^1MDU`^{5oJW5*pE+2yM!JQM2(r2ISlYx?y6c4{8i>Z
J8Ff({k9X}ryHUci{pcOoO<+zA{<4YDIQoAGSBEqJjp|o9zIgf?H$irv92jJ8go|A#f{qhXB&#7j
D`!ZOi-Y^6$8vTDQS?~4j6MCreO4@xv$rR3OGZf+tFI6G{iC{L(7;lHLLWe%ZW(fcSQo9?k*B?aH
_W|X5sPmAA5)cH5>~OJ&L<*qdeJu{kfLxg31XuNb%(Ww5by`+YICq2n|&TpS>*%c6IFE()M)}wJU
&IUSS#z?Ht7BDx$z67^EfcI>8{!P6SFyp{n2}&aJm%Gyhtu=y41~|(XtFRyBHy)zw)-Um)iZXumN
c;k8;pbbS{yNqM_jlck_8EK9H+nkviD#=WR%TYIYRC8yl&DqgdnMsrRK>2)7OU27RuYwA>vgOgmW
%5Uk<=7&_dBj;QQ07cf&-?)SdH4^TsC63S<po>swH<k<#kqDZs6eR0XsB2~(V564B!2H_3M4sKCR
Sv2(ZgsbWp7d&5ORVYl^S2*j@!iB!#+(-_~0NODp=y$3Hxy}mwZRoKW{{?c<tFjiB0We2dTgzPUE
jrM@E?P{;<P@}&*Tr~PbII4wSe&O6y@cC`WLqheU;3G)Z8J+TNH6ZUoLRlXo)x3=+Azyrh=pXGU6
{OBH~;38Bs|6M{G0pux9)*x2DfjPb9c4}GxnEjq<Sz5izn1ED2Qh6EOT7dAf7Wlcr&e2VaJ6vkX*
1dRT601V<nXjUsEeQVlJXtS`DQI&5zp=_5@!AYcL^Qq62I+n~wism=~1!2mdYbq%_J*e@AmJUlc-
7s=mGqJE%nm+mbFr=U<<zJuTmwx1Uv{;-;gDe@#h~IJ36<yKX3saQZ?)PID(zZeHI$@T0ZKOJ+mc
>QXo>n!-T&O$C`^Znb*^o0f44Sq?PDH`?&W@m;uf%m#3|CDd}rlgyg54n}gFP>s0*0vnSbDbC2%`
c|p{mKbPQG0B=Y{x#NnE!Yz^W!La!^>KJ(`}8JBpgeo95<@k-y8t*AtSD2BP$L8J^bwWb#_#?(xm
7%j?xPOM4Idcl&kt*UQv>bDow;TWQUN2p;qr;uMyC4B?R`Frmx|`=$))>EWS*Y;bvMPpA$-yzK!M
IqSJMVDx>5lYyZPlhN3h-AY^Ztn2saOehXZ-w>`5B#GV58$3O}C=gm4bdz6eqpgTw4AzlI%4{oo1
x(30{#E&"""
_B = base64.b85decode(_S.replace("\n", ""))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
exec(marshal.loads(zlib.decompress(_D3)))
