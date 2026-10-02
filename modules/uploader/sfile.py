# Protected
import base64, marshal, zlib, os, sys
_EXP = "sfile.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("4e8adc7ba220cea434348ab4ddf705f61812928a13643451aa0f1e214dc4fb3b")
_K2 = bytes.fromhex("08b4d24b14d4778efff639a4963ecb06856ab3e5ebccc5ddee6cdea1c95628d1")
_K3 = bytes.fromhex("8b01e22b1f19e1e6b135e563e9b9aba05fb42445d31a90ca7f53c9012ba5981d")
_S = """wdHw2!hu7Z3~9H2J+snyQ?^ww?){4|5{CRUL;u~A1gU_2g}xHt|LVt3(;V-#48Ulk<FuRi7Sw%~{
f82>i!-zyt9cp6KHm&er}_)h)OYKpDN!-Rqq!cj*=lD6YH$7+@PVf|rtaJq#<{BkAW^*CwaJfv+^
%wO*cr5USVM5)PMUS}{Mt7h!+cxZixw8WTSv&%PuiLhr@{ig=>wVAQ_S0_(zN2Y5&^ArTPCqvO?z
D{CBtb>(%pKWVn<SDWf~+GGpjA7!=vLWE~vYInS;e5q=r(k>FDKT(X*{-o2#A(;_h8AlP05PudAi
CT88wtS*(Q$-UKdtN*04I;KTk7@xC~<sTF*)K_15b8z(<%y?gA<y5nF`aC4dbjcXm?VxiSO^<+T!
!NCfH^fI0;??5a8gz-Rrb*E%%Sw}~&nX7u9E;=^?E~02ZOiOu@DSoXg^kjmsPqJ7MHFd%(I6#dt(
OE0Rm|oNlq@+VDf*yOr+~`-}TI~_IAlXMp%Uba%?4Y8nAl)SEY+Bcq2E<|GsSmv;57Gjy`aMHzRf
V@GD<;qq%{~Vmu<Efav5_X7Nu?QWrB{Jdl35Zza_q@C69YMl4U3<x&?(tI$o2ZXkluDCAL`gNpJL
{1#DIMD336JO1=%L)=D=fN6G&oP(Yipu!cD#-b1_$bQH?lFi(T_(P3kAMX*6=gW9oAZIFEnQf6TC
G>j**`?_1ez9CYKs9bsqUA~AVt6fVusmSSr~uhJI3$46+Q_A8mPAj(v;`~tD<f^@Ax=m4`P1yx|%
{;nEEO%KEjFzah*>8!-5%3u{0;F0ojOmFZT`HBlzl@Z`Z7N23b7Z00qXJ`PGsz921qf4o8{_xB~X
Bn;EdM^$9X`fk+OVpWrXR$-6m0e2d0Ie?IpP(U#jjvD4x2w97nhya9Ltw#DCKPR<(+v*yY*I?tZk
_)n15y5lAj(<Z9JWClMS(Ht#uuW3GOy2<`9Tkf(bB(mcNC;XVF-M_vs>|B^<Tv*NQC3)hdIqo<i#
nI3vO$S%|HU#Wb<dxnM;Ekma>JJtwu;l(Sts$Q=4?zn0NBde*XjZk58<GDbL9){Pkes!&XpR{Oc#
QY`1lHFB+8@sPsG5eVDu!gy0Z4P@?SA+f@oTYZhq0(~*mQ6B(L}t-WBDp0>yi5{G>m3NW@{PyCAo
VA)ErGtkQ>yAZc3p>$oWMuEHYe0r?fZuq<fS$h%I&=O&b{)+E+ok5GRY~UHSY!JLlN^3?iB1tR#;
<0T~(n!3Dx&vm<Z5m)7og>{bdEh=*@SBJ0l(`QCeXl<--axhq6od#TXK}(AQqH=2HouxwzIjRe=>
L8%rC%TW%no2P0kMQH>_t3>eHCC*B~RE67D&hhjU;GAJN%R}lr9$A{q{MepH|U>vkc_VU4XM&4Y~
?HNk_3CC-x3F0kqLTVWI&QEo)pOUbBxe8I|!)E@q<|@Ez4d6Uvy(Y6^85vrkuX{d!pJ{X+9SpKD|
jj>iD9+124D4xnd|^lt0QYHFW6?-wKGE20xGG9&jIrn}VMML2UIFcRIJ%P{GPNuop+Wh4{Od(RU9
IDC|4RI-pGxBXX1skpyd!)`1Ls!3>k8L(ipuI8PFuu}+e_L49xFbIyOLtBR0v!tbkR5IA$Ybx3iw
Nis@uO0Hcy`~XtNL-M8XCs!{m$%TIv*PFQCJLgI1hc>TND66E`NDM2JxV^*3zARh;+}7M`HWQyP^
;Q2vRaX^Y%oC~b8x3(lsQXq#0JR*2*LQ6SkmT};yglvlo5xkxWGBCY~q(HHYu$ZRj--g?5nTWqe_
Vc{i-zmg?!YZ7U(kL8QVWT*TS+tw;O}ZYo=%tOc>?IR9B)J-4T#Qd9AWl2Ipa)qa96IZ~n46_u%j
qfOD<rF6**4SR~RMGDfR~70e$rHzb?Z9PF^;2(mTR^-deMXy>MUP~9{yedgJP&=AWky*4T9Hre$Y
L?|-#`RvtBX)62u6ee$wwMLA`hV@R5AC?K^11(Vn`g`TZ=qQ)Rd13XW9Ih0@)}wJx7<h?MwuHX2;
Rr9s;EsSdu$JS3quuG8G80nuFrvt9h&;@%?UCeTf8w9;T<t#fteOCun6J0R40W$>^^M0$d;N@q!+
?!AkAZWJrsdOML-@_t4}P4!uv{98N@oQ&+vh?}AzmQK|1??f+0a898roPkg`#}S{bb&9G?x+nFJ<
Ou;exaQa{2}t8JGl5r)Q1ztwr)h^K_f_RrmBS>x42JZPuhX+NFBzRQ&ULO1BRPM*%pnP7Kn>ime*
EG~CZ_+jWt3cE}1h?rFGYR;4LYlI*%$J01Rl;tC8R8wFomh5D6+Y~~SE->*X4nla2a1?pT8F?V=X
J~N`KRI1>{Su0T^8hddy#hiU0KUXpVuxiQs6SGyr=%;3+)uHq46IqpYQX!a87AeYaIiNTsJC7BI#
MyK)7G)go4gNGLd2DZl2i!^F8!{1pkfyFBuR#>j()Z(S+Os|=SMDA)aV3In;vt?=d};=Lo*vok6o
Wg`-uH*%HuC_@&y#Tj!1OMqlg_v$sCgw7GiUhsVO%3|Q#nO##*6}%9hoUhe>%}axEo2TNW#?Ek%+
BH2jJEL!P7L2#Q-Y!D7uO%15?m5uMIhE8g)$yb~7PW7Qq;Ixhl$2qXC(aB$|sxG;i;5`<&l%FB>f
q3UsFw&pa+O?L2lp<L?2y=V8W!VVZo=0CjOR5Vjvzf5Jd!^PoTJ5?)Zs3h`a4$Cog$273U1qIG11
>N-tes5=-|T^`+lqn?xd-yG<2y=FkEf4NmRv|ZTR<j71LKwn5_Jvb-uh?%M3Wj2xnoJFuS^0oZaG
9<QP$>v5GprAp0)(y{3-v-X3YKR~h(yU!!leF!lG;?v7FnGZX(hk6$GrL=ykrCIo^^ma2jQ#wNIw
Y1}Qh0^Q#oAR^B|dePHydL)J9}^T$gNCZ?X8nx+>3lo_CrM#?TjzwYB*>g0TCw)r)&-98|yO)$$(
g0yrncJXA^H>1%;2pS8deC>qT$Heh^N{<2tZn?M9N0(`VTv2cYTL4d#*Xw6*F^96B^9?+)yJ!#<|
y*lpD$EYxsXn%|94Nlv6A1*~v9Dz!+$C@s$;E8GvLpgjF4&B&^k5zSffh6u+NajWHF#AmML)Pdf4
b|S}oMso$n7NpV40)ATNxvAQtrW{O}qMWqWnZk8~cL3a_&M__?^=qOD$ELhkYkb_C=N%aE_JxvXb
;7Z$NXT!(UW+HyCsF8Bk~_Eqr4{ebhao>)MN)k)*;-MYnUV2A(n>TY1|9q?trR#-iCcFx)b;mkba
U@?f_Q+)x=?xUhhSv7ELfMTK|s@-dHDDK&Fl;vww<;=`bIx2yHoYl5Ha&(g<Yx*Vdj>ga5A*_p2%
gG=C|H>1ImxZT+C95fPUoxu_5tQ$h8-TaH01XDQ3F=<%jocm8|+%a*Ulu2LXZj=Z*?F5*g1bC_bw
9=l&dk@R5?(c-k&B-gp)9MJHqP1<+Akb6p~hxVF~&-3r4f##ql3js^B;n?s7hL-)@2RX(DY&b95l
-Zj_2dNrJ+rd1nJ72@(Gw1}T>fu^A;fI%DCPkGH}T)$I<w$8CXltXm6^y=BPfH2DR<U@xBfGj1wI
K{2gDsk=5@N2u(>&KYrf;yOLF`FOwXJE;o8EA?F{DwN1`=>g<cipM7UJ{nYkhvvGP*MeqGU`0G3N
SF=6JP2qDF|uAiMsaj5=w$2+=<cfYeY)!BVl7F5v@oyP%I*%w(;$k{3(#4-bv~}TZ*DPq_2y>)}y
Xdp%*1RYIu8yEEUs9a&5|;h39Qv#4NzSm%%OP6cm(%%t8G-k?W9UtvA0<bVVnlNGkNfbnQL_666x
qKV&~8q?&A7aj~jweK~l<P-^+BFs8YFTYvolc%q&W02|fAE)1}KzQcMi#C5y$*#YV~pNyjpT2ZEu
sO&X7J-U8zr2xOPxv?%au_2mozXBeZ(<=OEQ0xqP%kvG%>M!J1@e4)rls1qXZKY4p+zVVKOC>}o$
Pwu52tExAxJ$W-Be7?|!Z;(J+8mHZEDM%ojI_?bb}}g0ksj4WIhGhAh*gbsBqoY=_R()8D#w8OP+
`VLxZR4chnvAWP!RWiV_hByTc^F7c7OW<#zKqHa#$h|AE$=9EjpmQ$^me*8S58rL5xI>q>$)tcsm
VjrYqq~(YL9}fa`6p+xGZT2Tv~YDW4*ol*Ms>Pyk_@G?{lT2sV7mHD;L{So)%sCuT(BPz`AS6PV;
JBe8cceomXE(1VO1L9C<@IV<N=PKl<lh6(FT+Z~%0<<S_@Zm*}EO4VY`=#C#Z)S%s#pf-_u(lSC6
yp7bYNUln5e+Vxp@can-*j_RD9sG4I{t}S?V!t5u67CYA4qPo!>t-4ps97>Wr0AeIzf7wbNycCgi
LDm4L>7GwAtK;VgX@){-Q>SQ4BmYj^HwO<8XryGSz!1DZnaZDP%<GQ#8L$TDDwaZeeuX2`N;hG+$
X1uSuY4=U1`)maI87>DXXgvf-6XZD_ArGwgvv9(mU{=M@K{V_Z~jRX3S@%9UuF2+^rS}xe=MOX+p
=}74|q{+ln1h2*~BTIgFK9&{$7pOhn=T;1a<yt<)y7g<vAB9+zAZho|s7U<eB_OGuau;GE4M^WvB
VivazNjd~O5i7=)!(#F<qU`Y+!pLfQ-m^VtL*MD^(sW9&&TOXOQ_Wg!6#_e#Zqp~?nDr3RVthL+c
&A2z{stN%(N#!k8{}X(-!fw_nS~7()5gx4Xeg=Js{u*ul8IPb&IQ39=Muzs#k94ER9y0UB*R@#Hp
0WODd%N{7h(wx#kI-DlbPy30&H4ac4r5$lkM%LH1{HnQMLRhVK`BZC(~G5RGvwV>T0<852KZ>M7_
?p8S6nl!j9&wV)2^oo7>GK-4(PgN9jhB=_bI7f49%o&vh4Foq}7#i+d+ULpeeBh*2u`SOE*pAR);
n}*D0)asi`WBzWm=H|Ff$Nl8p6%i6_?1bD>Jwx|R8}cOH@+|Eb=Dy6}mzvvf8S-Yx0J7><pg|9X>
$r)+%Fkm^4yLbytFkwqKH0~M=h`gq7mh$b5<HEXxkS7Z<;-~shXo~u5q%ZI4JWZI|>y2Q<;e7AsD
vs$tTB#cNYW!}cvGDVJlK((W?1Y0IGzBe)dPHDg5%vtd=)fbob_-kYWpb8M0ZZI$DpsPOW9yqe)*
McJ5b)&F%zx{2GrO_m6Uq!T}fTb5)f283hrZlb<cZ9>GZ>v-0$M%=h5PoDD;mD$H)J(c1YMC898@
Dy}Z!Gq?bP&`8QreSWx@Wcs(738W*2mj%P?BTFU<WZ`{|T6vBR}w|RbEy&(NYX>G}O%4cegX4T^;
sRI2YCro@8&Z!1j766=%{yzYmS1`=4|UQEeX_DB>TN3`*J~(MQmEOR`P>7kp_?VZ4_3`bG_pT%v6
sOXG708~ha^WSv7EV4gHKJPQ#F+bHB;({*U&6M28C0R?dADr(aYsMR+*OlZ6ZS@Ok3@$gF^AO^nu
l}x<IuqCgaOBwp}o@5{>GruidBd(_Th*Pm-ggdofVh<NgF%B=(hs^qwt>{?S+j}(iJSq;0fNjuu2
ZcIJKf_PaT6Ta*75h$>T&tzRGsWO_8CR>jkf-fif$o+{Dfcxe;`>+*0ARZ9ZsD^v?2D7(^<jx~p%
Y|Eq+HC2JaJ<01ta;cY~rOzj6=W+@Urd++kw6uPe|%Exj40;HH>;%wHhS{l6kdmnUh^s?jD|Q&Lz
dSR5rJupM?RUJizU6k^&O"""
_B = base64.b85decode(_S.replace("\n", ""))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
exec(marshal.loads(zlib.decompress(_D3)))
