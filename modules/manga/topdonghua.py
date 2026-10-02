# Protected
import base64, marshal, zlib, os, sys
_EXP = "topdonghua.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("239cb5530b91e3eccad4d7fbaad738e3f64e073a69576a00eac6c4670a3ca819")
_K2 = bytes.fromhex("6f490486cd7fce42d67a4b05045a663f5d27418d6959ed79b069a9160bfa600c")
_K3 = bytes.fromhex("5b44ab0858d408eb94dffe2bef3503990dfb7f755a9d9eb9c60ba7beeb2caa2a")
_S = """Z%f~Y<yJn7@veua2$q78bpVXK6EW;y0unzx_pgu>PF_Kb3R!Lwp#x6@=kO=|n#)x|@cT%J>#gqUe
X{joXWjTc=2I(ToH)tXNLXEHM36jqVA&6^e`JgyYRZZL<qVt4W0}o~cu?qfj`k1n6srO`m!!u0B0
Uv2C*7GAfnq(Dp@rQl7+nJbaH6t;9!4r9DrXI`zEIx0h#GdvTx-5TDlpg0a}*z^4>qsY*f4ejb2&
@32{^cg)3EL$?y8&I<kNJ&;D|GiS|%qG$HB|d0?303^~~dFPmk84G5H^GI&U*{FVd^W&1;S?Hi%K
r5+1GAID(MKI7rJ~P44^G7(=jK-taHLT=4cs8?U^)JW%%F{d`8m0JNkc_U$eIV2edzjCl}_ai~+j
zXGgG;E<L7#+VJhOPa;{)s$HS{#sLOY9E%-rW=>EmQfFyJqj7uk*d#Z)K$Gwe*SiU^c`75=K({RO
oQ~J092psP=nWX>Giz<Uvo=TKXrZk2BRce?-&i}o?s`-43E*VRG!b1;(O;wP%au#5?qe35I5^~9+
!0WK}P<AdZp!Vb<SK+#hKLUF0V~Y+l<ujS@+(qRWZ^UqFy0{CU-Yxj!w{LQeSbQ9o|<-!)p8hEw(
_!5qP&s^duO8t;1A^JW#p&tiQ`DJGop?R4%6jd3W+BihO~#Xx_~NKVheyZxJ8|SiI~usQRG_A?Ui
U&zsP6p}2<fauZJe*cJb)i)w9&ls}%Uptib~<v9+ALaeh`N*F8l2lJc?pzKRBd5I`XsDQXGNdRC9
0tiofT_)Ww<1ye3WTuEyMwSvSCJ8R&J#AWByirCX_gpbtHMX<CEHYPNr>GE5&IgS&O5Pu++Wx&q%
<Wb>y57kd7JQ-MrWh}8wBZ?EzL5&zL`DQH!R-8|CM5jJcipvMl<>i8(Xi9bXY~Y_vQC0_Yp{^^0c
!^T3&>D{U1YA;h3KSHf`<roR(naE*Zzy{;aDoA7F!3AYkM3wbGt_u&r2lS&FFaaR9Gd{(A%!)VNo
;q-m_D(#cPeM&?E6oQgWMXHW6a4(|fPX*{<m!nxpxW5c1TbIZs%BD+X|BG<u59yKUvNoe@WGok|Y
o90Zv<yRIJKBR)lr0pL>L@0=S#|28ea>FKv;PoS<Cc&YIlT;t=?&>G`VvEww%UiH^4Vd>?d#-KM#
CdM(MUxt7DjK>IIm&$b8WF5g4E?Z=aahLnG#j80gmOj=5xa_dtvXM*^#%e5nD~2BUve_g}qPb&dN
5$M6CmOxN;8BIbprxF>X1#LqqNyd_7AC_T*BM%Wt+OwYzJl;ZUlCuzU@u6s&dC4+JX4IwAAyFijY
fq`@<habrYKy)sJCkD?<Y^y@3Z2~75@u)sTupt*I^}%{$YJpis1qP-YTi!0>Sc50$=O~u~ze(-{i
veQf!vZYX0bCs+s-IT5rm(Bm3&l8Q#G5*YW!$Iu>OR&SBG8VL!gNUyFF&T(R7~x`aX!v_--*WdDr
TvBI5v$(JRTRNP(qKN9Y4OXE*a7$ryDVkS0>5lOB|ZA*2Nr5AG>88|M!r1DEMGt%=nnaWR&$82kl
XM(s)ES*G0-z_@UQ&NrEhI}`jPRDp;K+R&4T;Wpw0*&O%kPFy$%El;b2nHaacu=o8<nW$&Ai%e4z
&EmhKy6g4G6;nCq^SKp%Wj3pt)l~+>`J0#AbT;7FJ&#y&AL&b(GH`KaparWx+c4U6uOY{hQ_pO{s
SGG<F~JkBRDJZ6{U?2zN;01738P*_1g>%@j4;FZ(-4>oIW>>(tZPO>K}p9=1CL*W?Gsj3oY!}WU^
F`&|$qaJrVUPm}TF#DTR3d<UIKQw)BXe0C-_KeHCWtV;{J2k=nBZ(+aT8INLyi>)eaR9O>_|V$4u
4Ec*0YVe8*lOBQ>!{vCCg2p?=XaqpY~_eKecP;sD5G;Q(bLv>ZBRwjvXDn%9De|+|seuR`*qt~lx
eRFapAoSIKN<I2jeFxnNfi2wtmHqxZILW)It`i2=IRmCD5CFZdDa&u5CllA+Fm&AlErv$S-=6p4K
IDV>*l1pN0e0?NbDy=g2mQ6jzzh=_rd3k3Z&viU2x_UY2d}Fbd^$mmAjx^Bp(g#;Y1!=ItyrT3bQ
phgd;y|wC<C8o%e?u<YDDuiv2;`MXtdxU5(y<-wDviJfgKJ}CaM+H+O>@Nn);4JS?qkE+lv^zI1e
Bt!Q)pY<NiJ8foFaW(^ov&sj_0`mrGl&a$J+)S*Dpv>~mp>kt9tV)v!9=KNiKx#y$V&Di(yM1ZZg
x7lws=d6)af2>C8&ZKED=*mYesfY;~*+090mNLhwW8TKqh)ZifV1y#>Rks1M}7_Cv;l9guy->agt
|1-YOW{z>6BmXG*?mQ+N#hWpbe&6{t+QH*@j3H4s@%6iJM=-sGK@sh;Q57z|(N(CSHS;itAE&E;$
bM#VsjfDa@qMRROS8=Oq4wM)yWaN#o}Y?ytPM<t*QR)1#hD4#(x7E0-Z3lL`fzIo^qEzIl%e=Y1F
w0~b99CLI!!(Zhn_%w=~O#SFbl(caFl248x7_J?&Lg@h{t#g$_ioPZinR?{gxD<rtT)^d|0L{zZi
8tre&458QtLoQ#l&n^-gZmme^Lh^gH1n8K{i#??Piw;#(j%MTAH#aI1}afRLWkdDS#xTjA8{A56p
O8mj5i!7U8yAv@;D+avyJ#Mxdbe=7kAPJ+MkNoQ3UC7}^;sqI>1F5uHy?F;;r@5A_|@<9}~?f|@|
L=-G76?HFf@_BTi5D(K}3+gIME`;m)!h+AXiduQ(`$v_kY<DP=u(mxv&&O@H!8TlxO^15P8MoI1?
$55*v?RiN%BJCxd##<pf)D>3=h$P@QYv~s24Q3E5Up9~Y9v1;-hVIhKFR0d0wpL`PL~i{?%K@8dw
62Q5czV^K3+o;`4yX>37KWjYSUsAJQFws72qNjtiD-<!Tn@ZPg064Z-YOaZn(gg0qTae9g&pb`ML
fVlWp!;*_3ppO>LMVf0&my^4@kzDzpFUhhx9H+N1F2zJC6Op+g)?Ud(-bCX(5=wbu%m(~!=8ybJw
ZF({=f&3~G|07W0A3$HzVaD+&RyF`}e?F}mGHeqM_J0bt28lfaY)s9>>u#wU4(2c6|T=71f;<w8M
-F^|SiYeE?3ok^{!a25>I*{d~Uiq7}iriVls0qr=1zkyAK2UMf`rk2i)_pq!IE1j`O0ulr-?mC9b
i`<+VyJ4MhM^!#eAqF)-9L>8|9S_4vH$>BsyAcF<r@2cX>2Y&(W9>Wq&q=XuRjz5pe8)qNeLgv9F
$YUGqbiC#BVD{q)aW<E>RR(q=J<$#bs0U0VF&77zfJpfoI9IJQ@LeDa2XqX8<8CGiO5_AKz~Twy!
{W-#&d6eD*Et%{0wV=i+E#Mg<}{uk<`Jh|UI-GsMFdaI1$J8w5|$c8u!FlaXd_%WB2S)9n(VJ~UF
D(|Q$);mvtp7KyHXyL?2d01FN7^xlX_>%goV|3Utz7kIy438n=wE|-}Q5brA;5wrlQ#;;Tx-pg=~
H1fZ8aY>YN1evs{S#nK+=K=B+#yOBI<qg65H=83i4Fql*A{z8)#dNI$D6g|1e21Fsw%Y2$%t!<B5
H>W$r!YH%@_(;x(7#E|*6)LNRoZFM8WsWMZC`VV$K@qc3iptLQQp0Z-gX0HeYQ%^6`Y@z3fGirPj
XjvpK({bY(>a)hV9V-6KqQij1I|xzsx`Fm6!>sql37BJ;CN=B*XycZhD;oDJS}z_u%SQf4sM@jE?
(kk0BI=%U)YWy_30<Ug#IWvj1R@Pp{IeIsXfWIx62S(T8hP@timHXk9tpCQ$yR9<cJd*#w&->)Ls
ODneg>g(l&Yj+L7ZQ^F<LJ2Aif=BsG=$4YX~b8;8Lh1}y^ethJ}CPmJq6|dQ~w|9LF$Vq=B8oLE~
c)$s_A)V9TGf)V)`C^Hcrx@Y%Ue#yh#Wd*IYvP;Y%N#o9v67iZNM?mraiV=y4(8(}Plwe!kVj89&
%$yS)cx+cxVD(}IHCH6P=4=d4m>=BdUNS#p;r_qGq244{GLnl%{3Y<-j^XQsFc(4!*5W=ge8sD{l
#{YlWMRJ6{7W;#-~5?N@o0<&LmOhzYeEG`I4lJA!W;jR~Zub6Y07iF32?}m$wPwSX60cTf6-!ymb
4u&f#QHvD4LCkWqIBW>9C4h%vbbyXmRs&aQ*51umts<tt_t%s~KQi9Nvlb&Q>0&m%R?_Sd%GQ05K
Iq$EVXe0ij7eGpv?0ZjKL*gblDLZZx3FxoV=S4&E%PkM<$>Eo4hkG0stlSMb=fbr1Ex~&gRcB>n%
lw)D176~&hk_*KMaQVax+#hGeIO>Q{iD^IPLU*Tn?%rA+4f69+k<nP=G<rn#g&b&2Vqr8oBo^rm+
hB7xR$LN`=;wAUmis#u7b2hL5I*TRy}=LM$;eHD(+VI7j|bE#>iWe)d-unevk%-3<O^6nLKle*DL
|AEO}V<Zei<6cU3QDY1T1MJalS$$`S|NxrAbu?*ja$(=yI5lawllSvzXI3PVY;Nq=BTC3PdGhvOd
X3Rq%ciMzCo55?xJ9sp|;_Q*H>RzoI5c6(()VT`XZW<2`z&4rwH7+k=ah{@5GP)0tDc_~o?*XSZ{
Z6^?t@<A!XeUxw_)_y(B@(wm`L&i+-D?2db7(-wcw3SVb~JV4D6)&@sC@9#Uy2s2a@<y9qSCrDv&
5U(oVJ!nx<TD)B_sQ#cJhiVp?Q4}>S!-Qk%tqD;7wFd?@ecIhYZrpZlwHn?Iv~vAbzg;zO45Lj@E
FMT_jyWIbRcEhe(m~XnPj_hD9r3wscpSDe6cSJ|>UVy?G~}2Img;PBTDXP!;4AmibQ=pLGGs`e0E
uxdDg?k|Z!m9B_}3vgIuXv;=J#MCk&ocR8d>n%F-JaD4L)9-n(ahqq*Vgj$YwaDW)ijE8iVb?09J
^#4HFs2q!(S+Os%?_WYna;{*gQ<WQ;Sr8>h$Z68X%tsoFgD@I_%-;=aK89-V|$iVEKyigk8KH_}%
j%f@)I4bT}x8u^k66fcZQeo-Jf<u+EU)fYguJL#x?d*f$dQ@d<3bwqIX*Z8iNu=sFy1K+FEOxQv=
r|Q*hVwP~|gi;sYPV`;eag?hXfwb9v=!_P;tYV+pDe<3Jz`pQYX?Jfrf!WSbVIP4jvVbNQ+^(uc0
wJECH1pK|n5qA8P7-vJ3_Na(`kAQ!e~!~i+NXmnf=Y&W^L~D47R!WoqHg;Y)!YC8LpC#xd2nl39)
K)_LN@#xP4Y&TWq|FwHP8b?H3!=&Do$t6k85bp?eXo&Cmwa8ZaPG!qQS;^2_CHGDw;DN#PbROvb^
%?0}n(n#4BzDaG9mA9vShHt0HwaJdC0GW1h413)97CYldaQ=RU=S3W=m^=Ka?lM110}yQ3{|7=#a
uD{H*miU<cXu~+%E#)r6xy`)kfJ9a3ap3KOHaoDH#n`TT?IelKhoj7<O0|9_1RKu6RTNH}9?zEGi
>A|%g7Dhq?*d>hFGu9$v&c`sBi7|RyG&MlwE8<X+LNF?eC=Y<;!Tx8fVXM8Fx6yAtVy<D}z|+%-d
BRAzmGgT%g0PL-$`HhTpD9x@!&zy5Q|D7je$M(m^~bGAm0N`k)<a8TAjQ_!Am|Jf`)Fmj8jYA!s;
&Y1njAmEVOA1HWm53u?Me9S4qgd3yF>#HztR39;@`v=@(#!b)1(_x#>&Bv5l(8Oy$}&T*0b5o;NT
)H9{6mViFU2jsnlz&3qV+_>A_GWC;5qyDsWGvbIT6U)u6i&V)=#&|2<ab^0Y*~A~ds-@kkoKA-%Y
@N0}Q=6Ml?Ixb9yCa}&)B-@W!E52HC%wXR&+Cu?s~HHK-=P!mhDacUV}shIvon#QXfuleA#0ImZ`
)n0|-Q!D-vNt!UV=E`=|9O1Uf15a4Q*!2OJX}9~w$3vXBu;mb48nK4&*d@|YIfPfqx(%lLh)c>(l
saWyM3yif5IQQg=k7$bY#V7U2>k(KQ_N>)W;&<t>ga*fubaWyJLc!z<4%I(jLBn33U#F3(fC@*CM
NKojGG_)4C-n#bZ*B4r?<N{q)!KeapGoLcEG8XCfhXuE{mpTFNlB8*G5nS+!kgjb971$C{hv_M_m
I6(|t`MxH6l;U?85Wg+;CBs6##b*D?5^lXnlLE0x4ZuLd^qUMU-0J$CYWEnA0&T1R748Au1j0JFB
Y(vFK6n^y1eHiP4sH>RwtBJlKa1{^C0T&JsW0`4IZNl!@FZ(0s+XJf~B?+?dgc<t-G>F9UvqkJ^`
{d2?+Z6)i1FUCwJl^uYW?M<luPw+n41Eh;Nh36dn>BS#L=6pvlo1LL<CfZN?SO-2s$6>JDZr*&TA
CU(91SFK|1LSnt_SH#j>gEczVM!}^tgb{CDhlCl0khNr!FvQq%?sF?5T=G4b5g@}kYl<?!nOA$*Z
v*rWx%ZaadL#hWDST)qrcA%mJ}^<I0_h~*Iwr^?g;S#82?X%v4<+r&Po>R2gV(ZTkkWIRfm=?z|9
!F3C3S2bt6(jKK<l?xLm^C<V{~@GGy-NRji(E+##aPcd7OoeA?E~4lAtC!!u@zI-Ju3u@JctY6KB
$2LL?_P*oW|Z{>O2LdsBMT09MZn=TyVpH2*dp^u^r_eqAH({K|uS!9`L?nBFfLsGxyh8qJWtJaS0
FX$4Tjp(Lcv$+!*XKH}W^oq-XzL-$zRI~Mtm%_Z|$X9j*<&lCRvnV@({nb;3{0;aTFv;?|4Biqt+
hje}#C~BBJvsos6@?@z=39BQdtQ15sNy$6PdaU+(m<_e*(6HIE^f<ia<=0Ce1@vf;VsABi0b2k|D
;QhM9&b&?xDpq#J=vmd220rO!Yq5JhyC+jTMD{X3Bkizk!{8U~|6hPsDGH%hsS@)#Z=^)Sh%Ni)H
+9^%TF`*WNo=n&{B0g20A87;tI7W~wecY;+Nk(V=dgEv1#6vEE<6eY%YwJyCRNvoV4h4RZ-|)P)g
#y|_2j%7Fm_RoIkf3Qg8oGlp%R!+iHFZF^A(_nOvQn;%v}_EKo-eyZ2LrSt#MJBlMU5pa%0V;8B@
TAdKt=wC%k>1rV0#f0sWwx*tCWmC!U&TNjmCGF!@a=)koo0au!gwAhAJc-k$`T7Z-qqtQyx9B_Mr
V$B~<wgQ1^_IsL#NwtgI^eW|{(FB51j@v=#d(yL1)Mw38TVoLU2dcDL^_c2>+2SQwHsI6nICVF&g
M8(L8B`!NJFRc36fzBdcIfS`B5%n$X0Uw^{k&8ZEJDlnlptcIB=r80W3sU`bgOJZ$lYpS@}Mi=>c
mLcU#My{JwD"""
_B = base64.b85decode(_S.replace("\n", ""))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
exec(marshal.loads(zlib.decompress(_D3)))
