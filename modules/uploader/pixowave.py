# Protected
import base64, marshal, zlib, os, sys
_EXP = "pixowave.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("3e2a7bc1f0e118a7fa63e9583446665d8bc54047b412bc686240b95ab18c558a")
_K2 = bytes.fromhex("c10d7efb65228cf0d595b1ad34fa389926b8c1e0f2486a57814986f6e8205897")
_K3 = bytes.fromhex("bb55a18db5812fc46bf04686dfe060f4067195fecca8285ccf28925374317637")
_S = """Jg6z}eG;HVQMk1(wyDAQ6an>1x~l(2HxX&c>mC@}S5ZHkI0{3;6Vx0SiFaE^&P>NJ^BRiN_b;7}D
@O{Ac;L;@;<g$9dSkeXwnBRpq-a<F#t~;N@@e4Mw0YiL6EF-HLJ3_>@3r~uq_T(CHRDevhk(H4VB
VphEwTF}1QQweYPBO5?Ymf^cVQ6G1KZ$Bx2U%`g~?4qmxCz?Z=qhzX?+!ZGlUK7_1xOEjOpo|t(V
g~mX4_$_qVIK)i}aEux?m|cc!X7#g%l~gPz6;j5x*(jcr9R@eLU12Rf2{ZX5BF!%t|rg<cx>6Q8E
!u<*XCBw>{2T7ja30L=3oUu=A&&gQ6iOqJ;p7ZmkDz9tB;5aMWbinvk$8iU*w%pTtb`pKrSEHVfr
9CZ9~Vf(nDeW1KLm2B1GO#eCLENy<U`c8tD=Y~!B)(whA><g|3dZilp%vf;5PbGz=l=SBoH>)#U2
Su|&XFLbtPq<(x;Y>prd*y|Ei_!}iAuv~;N4<xWlbAbiFd8;EOo2~oHE|P<tpndLazWu?RYW-75R
AndyV5h_xfk_heKz(?$Iqn`IaaU^fj*YC1BxTG>_3Qf=Un;&saxhbW*Tx=Rqx=0f2;2o{m3ZOiUK
lcTz|GQz8{_uWJOy#MXNIt_DlRSUi;u=-%lliyo+ikpwHPqz?tK)8PnDKPJ%TC7#hjJo2Exid&CD
K2;iP@kyFzA8fXvf)M!UyE+2{io`)kX2SRPubRlECE;s$>oeqvLI~dkw%o2+&&CK)ixWah2ROz!e
S?+cpS4QmTY`YQA(+vYvx1tG)y%FF~MuFj+Xhg<K!$EbV!x~M!vyu4N-#_OFr1N_9c7noEYq*58w
zJ4NR~Na3)&0-mdSlgGK%{cTe5LHtzE}Vp035fA>L@WG1&{SPO4cGj;uK2LH+JEUlvB}iig`!>-L
n?11K<2gY3}W4PI~?nN3srFF+K-2;b5G{3)83p?vS))lAi<$m?PSq&a5$;C0x`^(3x0LSC|hkO^T
$pmo_k!ZIJkI;9bu%;IG5<o+3R1>r1@@=bZ6F+U2-VOL;RH9@ZSDn$?|w#KeUK1EczJ(~xz%v!m`
tne({EDTVJarSap;)a*;~{K7rJ$U*O+M?w@{W7b`5*=9G?Pw4~8@_4BrY&j(Rq$)B6jc=HJ?p{P5
8f`L58I~g+YC(z^NB~p&7Cx{WXq!G%O)<nOgSTj0p`_SboN|jdctqg4xfD|e3Avupu2-JIa(?;eo
!RuG2Lr@=Ng<yl`l<z&WKri1FUxG3iWC30j`l24f2mun=ub$^j;qmAL*}(QCye%@)*cva|1}(7;`
uP9_|F6GWtU1b%EVhf-zJXUYrF3_tUzzEMcu_#RY#|qMuXRdeyyhO%l}YW=m*Gb2a>-G6{l!lt1c
%3NoNXpU}zy#e_XwI8pFRgQuTX1!P>p?fqZ?db8&J!f?96ah($hu{K?4vtU0W>ua^jMDu57#DIsZ
4hS=u#4W#O^Ik_2?Mn(VZ4h$qPmr^*R3@Vmdk9>1{va~@Knp=eswyOW!9ie8D+)I!v_J4Fo)mg2Q
DH(bN6=l{0Qha*IwEaoHAE{jN&>purS29;2ikq+q|0EpRSZm(vExUBoXE;kj&i;w8&moCh9Cx!9t
v(CW5}>Lg>9k&T8~Q@-;>L=;j`(*G9@<tdz4QkUM^B-&l*LQp_Ad`LZYi+q=_7>T5Th4gaX^)zxl
tJt&WG?sg~<!BCZ!m4q2Fn#PMDHw6Lpk*1lKhn=YrPc_Y#meM=`C)2<O~|e(}=w6sS~4j<71N3lT
l(lXuanuqT)CJds%z*ThAu);5z@SIzqH+jisxsetDW$tIW!QuYc`d8q4)2CdG}RN~#lf=S{2l?(O
r_-*YP#xOgq3aHa$rZpJSY&D_b$z$*P{R~rQ(m)R=76}@=<f7zj%+1L4GI-vX)O)th?3C40WZRrt
50Sak<mcTj@g~SK+^ewDw!;{mVB0n4D|;60XlKnkMglL=ni?*EAd5I->APecmDfy(M|CX^nUVuJ0
GKd=kfsfd+9aaQykIl&NWhQg(us&%wPj>LZ1~)2y+iu_3q_Z!j#G(vQXS@lAhH+ZJ+50j{lLfNi#
YN3Rntn1bD<g8y5~b+j2ZfWlOo^SSCoVa4pB0@wZ!0M(N393^Nl8Nz^>Vu!iU!BPTYN+50OEMrp<
Z_0D*T4mx^DCsjoKo&r(0F<@=2|{U7%&eM5RACAi><<mpJF31lR22X#)XMZw}Bh|rl&GMWogdOm9
&*r+k6Mi(%5?C(4*wve4JK7CZ7^++j_ef?`(&c2*m&tC$dm_PdVwy4Zv+t`O5g_F6ZwhP)GpUdye
eKd0YjK+cBWF)>WCJA4hx(V~fWt_+r>|d#kssWl727|mCyXokg0S3S5G*%*IW`Wbv%(XbM=8{>$8
y%A%Z@}^7$$G@>c~FDKCmN(IYyUMr7<`X$K$<<A%0bF{;ZbfC$R=U{pX&(kSOlj=Ui~kr&Ki+Z?i
GMdaR^E=x{{cBulbJ=Hu0M!3z*ZoaM9pRN3VZgucA<|oBIzxz?XrIP7seT#ug9VABWFENGzA(ody
i+GvKw*==)o3w}r-~(n!9B-<20Pl1$o<M!p_XL$n$Na%Fk33&{m)LZM4E2tU6C(*nB@6b7iji8hc
I&XQdrwQDr%qZwZ|hc?0M@fK^%6wWUZifQy{4iYZy-{v}RLqX{ppx0g|#$ddzHy{T?!9XcyL99ik
jNlFQF^C=U&45hK*czJkN*y#FDvj|@qT7m%H4lSbV*b>t0xKy4y2{ouUZyob<K9Ylgm21@M63Vi+
;<il^!d4=nB7700EHX$YAbPV*7wVrI<)r|577ZHkjC^Q8zpfwa4-^^yNuZ=aV?)wq&YYaxNwYq-s
@G|;2=Y3SNVx{Mt8CPNs1uUpp=tme#sIlT^V&P;PvQHX7m3&&hxx9_U59<SLMLT0PB>&sr2=mOX!
I9`nN?VYO-`D_Ez|VIp@<X6JTLl6!_5hEUyU4pP}@Qe<KSROtZjTGSs2YCa9=SqqLxE`Ejqd8y$I
Yk>EitcZ&h9;e5~fmEbE`{R&QC4^cT;c#h78--VkmUXX1LEbCXNE3$$@hTS7C3XyAYWH{aj9EpCZ
8GG;**pLk^vHjx-6AXxB_x7ZsP4V`RNha-#$!(ZfuZO=w<^s9Rn6IPnH${J@WwMbZjlwlc+KhJrr
6qT;wDAm+#RZP{(+y&$zYXLYMp0S0X+*fUQd0xrm;%9~YJFPXv+DqjyYfUnsByr@@gWY9@Xa(jy4
F^r^{TO>|9Eyzr{PC{ev_Ia0Vi66YYMZ36W;3gt_ilPe940K%?6q!5yMzZ1hsN}Zhj+h_j!U(@`m
>&_35$gL(Emgp*MoBGg^_};DOCK9clZvRZ8>O-4iTfc=!7ug-=rU;Y?8+RGU=nOFB(in`ULjM(td
2OvB@$4BG_jMC@)Ktg@6_xmVj&YX{^MB~Ip!sr)|)bjMDOEK{~?Q<E|M4#aO=mxxg$k7#n{0u;aJ
71<Tad8JThUherqjY7)3YP55mGSmT<XQYcM7-Bv(oH;Muvy*$valLci0Tu{Bk<DFho&(T9XqFj;N
bL!M)U%r4J46HgOd&)&e&wP)K#T8KmwKCBOa<1&AYKGym~a"""
_B = base64.b85decode(_S.replace("\n", ""))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
exec(marshal.loads(zlib.decompress(_D3)))
