# Protected
import base64, marshal, zlib, os, sys
_EXP = "detik.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("53e61a243a481dd5dc71b8f75229d05790f2f6768e87db4546119dea81dc7423")
_K2 = bytes.fromhex("1a1ebb312407926a30ff93a5f47d4922e909b78cede2c31e29b8c69f602421e0")
_K3 = bytes.fromhex("f88de0e1db872354a59dbdc348cf983d5d2d9fc8f029c57af5ecfaebcec045c8")
_S = """$*<I-n3%UbT&+FK6E=lx09RVSUiM8v`(&7gY*e5EsjwmV<3oUXOLc&F^ewII={WS#{(e44{eLm4E
bRG<7VAij4N%}WV4Ub#tvyUz8=~ZR-@su2$>T`U30Eln{Z1_FzrR_m#Q`yzRHWwCS2$<YPjLeHHH
8mZyVDQl5tD07!Jq*A0m_I1-Zs_&9(x%VkGW@mI0BA$L~IVXW~CxvNfI;zeC7_coz_?0upaL~BVI
9Bltkre!JQxFYCbA5ceSDOdJU9Z*D+=5(L_T8Lkb6F0W32p|8A-$`8`iABgy{KBvd=%BHlXIS;t-
~nhfYU=~G1YzeT0dej>klkI-C-14@DQyoq{o;oJLRuWrTezE;BwtWdZV)o0OX?r(@<UR;n8=c6J{
MuxnVke#`GylN}XN7RguxI7O6;;lLe(er0fzj5(+zh3)Q*CzdKr#6-Do3&DpCzE%cb8U63JmIRAX
?jIh57SXC_(8!+J4;q;tHa;$nETvv5s|cZ2kAbdz1cHHry1%KmZriKUKz)l86UC}i`Ec4jyjd%hg
ny+$5r@IfKF2Yf!C2G{Sa#p_W!whADE=4g3F5+C65mkFM>IV-_2Y<iM@pQ1dw><v2k3jVb2{u1Jc
(}w12v`>xhhBqhu0VKS75o$mHd!Hd_Oj!;IxPH@1fDW?&kX6HkR$`OAV4X|3HcmAWc57*{V7oU25
sY_p%Ct<*Ia5_3~?sRv}_Pe#&bSG+WqHyr0-5QL{_tJbIM7bMKbR`9si<MjrTF39<?CCIOC(`Nt_
pj1acjyOdaHLs{MK~zw0RU^p6jtHyBofw2V|5bj*c)%d>>|chyO2gRRetHZ53y56x$NU>PtD#g_M
Qp7a(iE?yB5S$smI`FUd243X?AU#XtzbiO<MxJU3fj^Pj1D$<-9y8MjVsQ?EWL8phh|}vpdc|8jV
8_8{cgaoQaDg4B{sgXftwd6s@FgjRcT<2ku2LL+X41&&)21xC;RDvl8if8xM>ugBh-&pYmgGXYSk
fsrPidOyo2m_+~VHzdmm#B6m6hxvE?^+!m%wOZvZpUX|Npu#tQGH4Jb<7^^!4kP*XbHGZeN=WSpr
oLwW=A`|NCM1OAddO?4r~T9pFx!x@^M$I^j85uuJ?0V{s)VKro?DxnA;^{{D0v{2xp!}5c<UJR~)
GUIDE>k6It&0DB?Y9lFKB_&4zmd*a1k2G(EDU;hQ037d-OFVZURTrLUazdU`l3rQolbP&)O@+Z3$
C_Ub2^8FSy#3E6kH^A|{K~_}InTv#M%!emz#2dv7cwImVcVJrs=QEoU)i7matRsxRAE)olnIMU?T
aj{Y1!gm%_UTWw3q}uIKriC6%v$@YG56(>CU~Gc{#sTi=QmQEuT|Wgmp!6>SMRfXK8W|_~{@~><u
h=cPR<;;8v^QJ#(O~#*Nveid1K}iNx{RtyeJVA<U;S217}NFFNleVy+gyIE&8p-fRixfmlGl6YHA
+?XVY<6QcZg3J(j<HQ5wJ(-0r^X8Yozf=_-@Y<{Mz`nPY8;^yE+X)+8W+sbHHJQAe9ca2n5#o$fw
08Aq<kon6o`zT4-BZ@js#3b@9%63m5Vz$~)c;BiyzmoHX3~(;A`rYGiBYwZ9)VO6C1%vRs!AOn(l
+%9G#qyIH6%uIl@5~Kve#4sfKi(6!p<*i2Yv4k)y6;}b#0sni8|=agBC=sv8;oy}N&%zN#QB9hk$
6(0q}fjd)!qAVGrvFp&t5!a-7)lX)kimk@9Q&f|G#y9b5|A?P`ABtP$~ISUrOn?vqo@--U?mMQ@O
|2)lZoswz9hJAkfeNWER){t_3F@DIlE^ZhM-XF8Y;;i9G1Q3@-JsFS7&|t_M<Zgrpcer*xhWGq^*
Hj<UVgB>vk)&SoYiC?lPl9QxU8CQa^kEMfA~QM*CsCJ{2<GNNJ)SXyT(Si7-S{3~3=l7xCXa4x$&
=ew<_dG<OPX@#V;)QF8i)xS#$BcsK*ysRL-0NeqaALS^(q=6#%Ta-~jO&1!*p3iNQE(o)R4#!|M|
1N%-QFbU14im7V2SasZmVGsLZKugDiXwoFlH=JEHbNJ)w{=Dc{hfZ-p@q*-EW_8au6(UAuxjY(i>
IXDrN*`9JC)9C+XxtA`js8YUF<>+-Y?$S-8%^>#>UqQrRkU5ZbGO0!7PpmwUJ{w)5FJN-bA=3TM~
=1F3R%^g;ZY<fR2<_GOJpY!_IqTJWR<Y5x2A7lUx#TIY+MOWbl^wSchA(r%W9!08DIMny|+ekR67
aO^6s7Z_z1QktYv{ti>;jjjyg2dzwUb6rz=uu5L6?l1I+9n3-wOBG5$omLA9OX=>fk&y0WIw{Srs
IQ(*;a*|iL>y^(FOnj1RAAL5Fk0{wB6*mLY%E&yI_SNxzqVW~#O&8>7stJnewoXH?0gCz=ynl=-n
YVb)C|nnIQOLa|z+)PF;2wIjj8_iAgL%&lTg6lGVYOCFDg4nM&(9g($HfGbEL3pC0HIRW%j2D|(T
gn`&J2UA^L$ADk>ZU`yOh)^%c>~iT43OH4azJi947KKn8xnVM6;40O@4QC732=v3Oz_}8W*fLqeI
yvD0XdFw^5pcfN=Ae$?u76a#~*p>=q?0c~%r?9o_G!I$#zNsed9eqqz^g7jM7mV>gq;l&-kH0Lo3
u$_Aghm1Q>moH7w?=sbX`gV+S1!yDf|W{HhsU{qIeR#XsQcjUp8LwW-L8*n?q1aF8c<DN%IPCJ0o
l!;w*=TSd#+8URjlDao?_>BnV<e6d1!0D>l<Z(*i#FX?C=j=?o;{Z08rQ@__dNFTon*Vc4mJKMcQ
vKa<G>UX>EcCofVZvx2e-2Omr@0yT+%Ny~E=({x5DJ*M+{oYXPrMZ?R!cO$asjMr%LIy|bl5Xw=1
(sA9rWAM8e{A4CV3LTK~s8MrojVb1<<w)^5jwwpWzBin*RFE%>qc7b(S<3Ns`x5x$ULfj;h`&(lB
uGmAyVM-!JR6`3@AfCLgr+6Z}uJz?sF!+UT}OMD4C>)6gr!RoSj8k0UXlxZ`saKlmU~GC34`+0-B
bKpp!vG<qZc15UO7*`=Au{KVQ@%23_<EnR+oK5h<K*P+ua)YniiUzY0ark5E7-eJ=8Eentnp#KRy
fJ?83&IL9E8KcICYOz6yjT`y)bs(@skDW=%4=*iB{F_T%RIpiabO_P%q<c9&#!fuCB5v;BTeP^?X
PEmfn^BFUgKGXV(gXLU%iB8>vD>+;7aHh~@Q8;t)(C43iw7rOQm@b#bTg_pye>J@{xuhB8P9s8<Z
<+krU0K2wa!@r70#R)LX&8`v77qe#1=`iX<mt5pDDQh^E}SPF#?1~oV`dm<1h`xvjkT?NmlJWpNv
0USu%7cLXoXuYg1j%#c&p$P|*x06R$!Xfa^18Nc_I{!7=s|@B$uae;Q&egk;$aa36+8*Wv=_o|(o
?hBjRy_}a&G&^QtET$B"""
_B = base64.b85decode(_S.replace("\n", ""))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
exec(marshal.loads(zlib.decompress(_D3)))
