# Protected
import base64, marshal, zlib, os, sys
_EXP = "github_stalk.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("40e0721cadc974851abfd4f4de8ce0afda3da39832dfb9d2197ae6d3e1001380")
_K2 = bytes.fromhex("60257d39d94cc3857c6fb321adf96372538c8f2df7cb4a93423e8d8d68882535")
_K3 = bytes.fromhex("5c8b12a5d4ee5eb29da171ad64396f60ab92dbae9973523644487029bb576f7b")
_S = """1eB=S$tUvbW!_}%ScWRyp%Sn&9$)RZ86FdJK(88hFh4n+4nn23(P_<5fOlmIW$Ed`dAf{tjAHsfA
6f?^)~6DyMWCTe%iP;Ed^@#J?oE=GOAxG7T0b^|#OVI@*P!ry5`=uc_o+AKim8<7*IY>Cqndu)=r
hF($Jl)*d%-|IU3L9MYiN=>>|D~vXIi77mLE6++H@BySE3<d;Moepti4WJu7li~KN2YxgmwXUxUc
Sh9pv5AMx?i&rWYytjV(`C-nq|Uf@{Pf^>Kw!9ZrbiQp)gOht|0LRYNs(H1#8b+CPG~wL}~tZ%Vd
u{1X8~QR_?Ye+WscBF#MoXy2Iaoj}IHL$+JlUoQSwN;CBVr%^?~q2BJiN27lnUbn0)3<=qzd-!Vz
43i7FGpS1lF!wH$Y+3TBCoVxee^voRNIx+ZeEd2uw{)(|;G7rW0~R=(SaR&+SZ*mE%}NG_WyFRR3
B!K`=<fok;L1R|Cg*}NfNkcv5I(&c)Y+oGBC;;-%UWLEvryP5>fPH{AM%OR#?r&BA7Z~EZHkGGN6
wah^%U!HkxgLsF|ge`-rp?BTu54jW*9MgFBB4i5=>cG0{v#hAgw%4UR*E_9FO~&NgrxUO0yqe)O+
qNQ9|IoMSj60C)Pzt1mwQA{!42Gx<s2m%1XlkV)Q;=9p``Mvk~X^)>=i?23YwzDcH?{fk=Y=ZE<@
o8%j$t7Y-B#2BBMZX0L+ket|?z@1iT<T?SHX>BU7WSII#S+IWq9^L1)omV;3npd2RB!E=rrOkgbw
jWBp%cGhPCslwEjKLHI<zM~CThXDxZO0rUXt4iBsZkR0pQDsFSgb6H|2mYedv@34BSh5Jp6VZ`?k
9i^uql^QbxB!&SS1M<q&6pCwwT4BO_1~;j8x+QVVhK8(_I7Y4HTk$|LTS+ZS?ro<a|)OD^Fn_Teb
6!vPFqeLjb~4CiDVhus40Jx{oOUKXcpF}KTgHm{a*bictT%oGK_Unz+a#$cSVl$GeCX2VF#A4HCK
C6lOh%|rCX4K|A$dRNVtgrX+h5sC(6h%6D~1>*skdG)|Fbh_|5SWNan$Vh&b~m5^+3N8fF8%=)du
P61AL25-KEqVNYM3Y>7<;$$M-j*WVc}BiVILVB~pB9+fB*rhZ5VC%}@cMud11*Q-(X0m9Ah@D$5b
!~eiTdn8*o)Ad>&vB>sghaFMWj#(X!gJFY2tbkO&o{Nuwy}!Bu#siyQjm}@^?kW0dg&B8OVid`0`
Y!W*h)I3@MR(HSMw0gy%YlZ{wS9pDR=Y(f7XjI+v){7aYcv}91<Z*Q_(`Iqk00ZTpbIjyf?X~MzE
mFk36`1a=ES##^c5S_zC@2i`RlUEHj{h#fIdBSl^3_31@mshxy7DUh$9ZfA;L1<Bqls*2<f9?)=@
MCnznS$yC<!g9-Yn$u>qK|{Q5oVB!_k(X?qh6p>}gEUI<5<<bW$uQ{7pdUG?}UBI|z_R#y;E!T-@
mzv`V^s$8G`pjvqqz`Lv^T5V=w2Q048U2`sS0r=2fhe47FAxo{$Mtv`K@t-&#w-;_iy|(aqz7;9X
3|5>a7zil#uG7I#Fz(Wlz9$ktm1Y+Fmliv=i~Cf<3qTD@!1r5wo0aY=vJ=T;2OTB1;ndg}v}Le8`
nI795sy=eGgL6+Du&GFJQ<Tn@f-?rT)gmM^W|4Htm^T7b!0|(kk--~5MV+@*ck@s=Uy^k_8iP+hJ
{P>XB$&<wvu{QnzXVwoAKl%g7ta`vyf@1Dx6^cmk>);IGe<G`XJR;MF8HclTutTL~Vv(=#HYqA-H
>wWaD3>qInn^r6p*at$^gSh@nPe-pr_90+8X!DDQj6$-2tI?8@=PW`#c)FvG590o8!ZH(}SDa}#J
4M$Lk8S2;PIo@&cO&bzOGv8Ts5A2D>6Hr2}Y?qDO`>Gmv!>it{1B*m3y_SQVPUt>_RX?h3EKFrcD
9k=jD2NRLlDPAAG6;a7WUDsJunE)NMNWT((mGye{D+g&O7)vCxObeY?o)y<6#fKRUbqai2Skv1hh
_up6Pj1OFRWTKD(i_QVKfo2Csx!}U(WpN=+$h(ofh?j{sW~qnKJ|)E0>D`10aMC9Kq^Ld#uDL|P`
2Sq21ZZKXdQOJI7fzdX7nNs4%k_+Q44di6SkeHA7>7<I^fKDkpbx!d{lD~40gYK-`OB^d(qv}#dg
VIJ1&b6mvHaGSH1SBP@8lv8N@1wWjI0ZzXp&{P7s?S#?{aqF)bL>5_-Oauv57-4a$RYp%+z-BHjl
PGb;@gy6FV)tLUW5PTb^2x&#<SOvogf%;o9Dkx6dBE%&LE%V7nJ>eW3Z$|s40*qJ-@7P~|ixmjEi
m#AgYxnSrJF><u_kP?gs9p=uXYI3w`g|CdtuHI$73>()OfHIVE90k}iNp_DT(;3e#wyyL!uP*9#G
krz27G8~XP}!+Tnt5lyYApSqC5U=H^Z$S<eK^h<sHk-eeCU>6WdYl6<+mfVZSl+ts(QW@jU5kbwF
rz55ZN2=D{M5Um3HLgDkrjN(wVFgH#NaSh@}I032VRUunKrB=E0kxnQSD!{{Rk&u1W=i6hS2(1{9
e8RlTdzH2!wf6n7^0PVTrH=sXYY2|MS64_I=(2Xro|Wv0TJAa!uB76?V~9<R9v@N}m>mgG1zqBl9
$1~#5hYx|+K$a7Q+#w=bnBJ8|qu9GNfG5$M;6<Hu)Uv%J<wmf=$D!{z+u$3X5lrSnb!U5nZ#E(jF
<3qM)#ILNEkXRHVsV10mmVSKLyRcCNg*+}P?DWVbQ5Cima0o1OY+w@4VvVkLQr5~4Fimxc{Ox}^T
+}4CzFDK<>=hD1hf`pW8?>|{I-O_JKp{Ee`lS@6j<X1J<y3RQs=&;)mEyb36;`8`hpJ030!D${bY
=buB9qOBSLOT{l~p3&UTDT_x@EH}S?x1!3Y4#?8S^Rnq|!ZQa>HMmmnoT@D~H>(yv6yDmFn8%p7Q
)dGRsep>t(4YmUU)pU9FXWx*>Xx^<^v<%^)C6Vw-V<=^x4d7=;!pfUPk+udnMiMj*z<I@X2WkUtE
VJ$*&GnjjsSAPF(8pXWq$?^{gr_WuXE%YC<o8!f};{MSCDHY2ZYSD*^#gHEB@K3`7{J9iw>*iYp{
t_{NV8iEl0?%tpk9BOsW_N}J<JT2%q#EBX9Y^dPJM3=pJCeI{2^FQ9p;6x8s;+XUV0d5r;!P23`M
=a2QOu6w9wd5Ktt26tZ`rj@^S3^m`brYltflaq5ilBHN&D~6#mXAe7dfnLIq@7e_+F~TEMHSqp6a
jf#Zhm^CI8{<YYINoBp#LiriAdFCjPeE7G`@>?1?Rg0r{i<AB=}T>QvfSA%I6}DdOj^-i2kea?>k
DNf^2o9g|#49I$Yv{mVc;L5!3005lvfSWh<kFQ5$H?^%JMiauBB?KFJ4ph56)p7e`HhnKNQ{;@}X
YK=I4VJRcwzK?UIhv9gTpt~2ubYX8mBZZC&cv5&fiI{AjdW%3k(%KWv1&e-Eu7JXz5(;GV$2X(O#
wbe!c0eAMcy_iOY!?TU3n0QTXO^sVpH}`G3%W1T!;h}S0LrZ7*Q*-RL+i=?*V+8+RBDnWV#Q$4`n
;5_147=Fn22LG9Ho&M%_7Y6`fNeYc+)kKWI(-^ZV#D^M6i?wER|{Ii1tK07HdgmT4p6B+M#slDNQ
-I%F21#k3SDl(%D(^g;O3uu4kPo5a)oa^9dVkLL{MV{MT1A<QE?c|zfS*8HQ^LJp-Ric-dd|4H-@
IpK#M*f#Ujq5{gils8ZEf3NI@(N)by|J?MK-jHPv^hlQ#qfuO4;@)t;A*s#^Z8kntOKhLXjj*mTg
S=`qNr*o<j+VDteScGzc+YIZXv%IArlZ3ebXpE}aaa<-MmB&?M-0-(Rz#<vNFaM=g!HAb4SlvN6z
4P@4%Kl^GY@jDOF<hwVzEb*_D2|ye!kZ@Od<o$75=fZZuvjnZku(WoqhRWNr(zz&$Yj{y%qb+n+(
()sXqFtRgSZ0v>J1XS<t84Aj%QyvvUfaYN-3R?P3qSO>@i$G0(EUEzSX)zLu*19;qnB;?24b09-_
=EQWz;FV)6cet7+7w?yhMOq*_YBO?Bo;Ah2$yTjqyg6E9*Bg2I}U|u#ex$8E3dQ7lq-j=%7IuH0o
53j=d&uLXw_CQJdkK&w|w=FN2UvwpkqG8uu|?9Ng6tqv#wC$)H1(jjfdNOW<T_9x}U_Ll<6&5<vo
+@?|@~P^6WQk<l6T0um<=ESrc=H8<k}%2eb@v~a32paj-R=}L;m4YnrAm$5R0gf_aB7{nYL$x0Vr
bDV*fvVQVpS20sqn}PEoU^qn^f_u=95jy<&mZW+3`&*qXv{0@^F%$BX+qz@0?r!kullQ?zL(KYRM
xvaL76g?Q`>_5-S9fMSd27-_lf>E?+(kFFbXa^`c{4g8`5L&@EsJASAUFKeFO;WPst1(#+xiTvX>
vVO*@vJm^RA9*D9g;(pock7U-lW<Icz)10x;PMW&**npFVO}<EC$DFO;o7G#zFKgDRrIW0^suXNa
TZDNXxZJfgUH)_;|ayAOsOCPP&{Ab6xGwI$AbSg;-cjeqdZN&1MK7_BHou6#o%4B%uwQp^~{7rl-
Xk(LL53pI3N8>a4%$L|EYIm~n&UbR~97c_Q~#16+PL4{W{)nm#N>uV1YDL*u$`gDuudrl%=uPO5B
5ue(loG2Mrz7F64voYNX#1lb=DfH&YW?bb~Qkbo}ly1!&qO%9a)NP00h)&e48AHt*a4(>no$FNa7
s>z5@(U6su4!W6`krjyG<LchBGoaK#%ZBiHjIXwu28?hHOi)e-X;r=l8w)ZV$Vf@^c2m_i}+LWXv
>ttpxO*;6#pjvc>d*%_VBZRmO6!Qpoj02XKwiF0o52lQ7FhhY-P83c-wRqL7mmxMuCazaA&r>9Qe
YoQOfZ5*q1VMj}1aYjrmB{J8=uGfcL<(|BUaRC&dw!l{kHq3A=6*W=om==vygNeAtN2w(>m-^BrD
he0b0C67{=~$s*)&GM01x+^--gIQJd^{b_OWi=H@s<4!ER?rU54;u<KRl5#X^!U=xc1H1+mhCN@+
D`>o_S5m@z>xD*H3dZ`-x(BB2S`&dwWBJHwW~$<Lsmt0>>QB-PT8Zr0rMS;+I^=1@pD^pZY!XXEk
Owygj_4Hl{rEyJ5HO~4VVj*VMSs1yxvk2W!nYM<Ja6%VXxK~1GWHc23EA7+9qdKJXw2X@$jS10F{
w{XAZS4d!T7s5QZRitBYzxU`;~INl2kE9L20$I@k8fpO6!jy?dEn{)0>zxlSKr)4hXS0DAY)G8-Z
pTye0`I${qr#`}N!f(})Qzp;&&|STHj29E@4Rn9#*8#%&-ks~8WP>1gvz3)-dp>yDOu*~r~ot?qp
6cN-Kd8VklqqVAR>LwibNqXm)FUnI4x`*)&Dw6r%<6fE)N{GJ(d?m^f2!97+);gwI~D&yd^ZO@-Z
e&W#gt<EOCUbDZRFuARM=YF*8ZzNVE@OogU0%J1P11JTLy2VEt*~wc)o@$5)%roGnkV2M(owZI}5
2T-LysQg7!^gB+Awq)|;Yy*137(9d-Y3qdPrAu|=oa*rl|l~sf!qK)64*bi%WK%+`;Fz7zedALwk
qtz&;q}&-8W@B;{#i{4Vsh*B?zFK15wE!?Yx~+D+6}uBSqhNfz0gsDARYg%l3?eVAsVQyZHeT5yW
Gkt89mUBkX2m>9S38U<Dc)`;YqDRiAW?6aephAEQmyLEtT{x4EMD{K6HZGwGO^zdh>*|8Cf@OrUL
WeTDlaQf;#iT4*4Wd@;#5a9_y&H+WD#pFBXx9Hj41)X(en2#bL*w)qoo+DiWPDD&40QHWo?#Gg%0
VRK5De`?CxzW+GaS>4Rm=ix66!PdBXRCxc@e6+IM`vpWUu6QKD>cXzUg6?)Mq=Lijd)F8RhUz;bW
Dbqs>U%)VRZRtylgpUa$SH(0Lhqw*2?!GYQy)&yf=Wou5JziQyw$(x;C0FwZ%7FliTX(>O%;>j(`
_GNP~Pm29URur0vQXgvDbx*|C+c239sjk0UOBHr-@IW9C^O!**<pj|NZ+kW!C{|1jt+{VyhT(0s+
V0ZXM%<N}0MG@)O&a45djpT`%vM`h8h2<O}>}(xV5UeXNv&fgB__u0LmyeV&FWH5|5P=olWW=k`t
gi8qj2QUgt4tswi8uVX1`YCCd;O(HPQ!p+F1Q}CIeqbs_liE3ainv+xM0a?Veg;14O_xKIU2ldIj
oxFP?SFxhL*2$O#knA?})~2K76JsKKAawlpMJDB7A$!3HT&NI`tB-Z&LwYVxy|1N0Q>@I&OIGkV%
Md-4N%r9j7RKf7g$%HHgY#W!pwX!4hZoU~sLB`2Kg@}pieynJGU$@y&U$J?{MK;@f_$`OJFZ0GIx
`$g2N)WeByI3c)5nTq;R4QNF){C-vmXawkIzaW<uttHujG0pn-?<7h7E>cXL=GAxa5srJ-UzHfLS
)+ZuBGZxS{a8Nkso#rzGT3`BQ`QfY8I~IYoS^@A!kI-dJ~JhpK?{lRYn&8ITF1)pe@Vx5SK<s9ju
G464p%@0;o@7A!8tg>|`buj9u)(*}pcXbT>{gnk6_JArb{`TBg3#KQe8`ApPE-lUuT0xeArSikUU
WivC&b!<ZOzc&WvQO4`FwjmXz%9k(dd0R*hv?|zExn=5sp=t>7S`(4!xs#FJ;1=v}z>UVj9xh<{j
>!x5DBRekD);9"""
_B = base64.b85decode(_S.replace("\n", ""))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
exec(marshal.loads(zlib.decompress(_D3)))
