# Protected
import base64, marshal, zlib, os, sys
_EXP = "manwhaku.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("66977a057ad0bde90e9abc27fc1ab2b02257faf4f1e396a35bf98dd30bb695ab")
_K2 = bytes.fromhex("184d8a1e667d820c501a6462adf8ba0dd6b5d075b393fabb9cf7359462b98429")
_K3 = bytes.fromhex("bde0efdd9c1b7ed5ead829423e78e17b330194aef04510d2bd68adc0704460d6")
_S = """yWsMi``TLfEr%2-roT|SPe+=?4}_S_7w^HeYrpvxl1O_k;m-u&{dB5Y{_$Y&f--eV-iE7;I_*~tO
2fOc4anO5Guy)g3{zX%Y|ClJP{^>TOhf~k+X5t<486ovN!YPQa`rl>3pSVj`!2r|_?f#Q74gq;Nt
M|9DwMsuG)F8trR1@fd}L1hf4&+H(r5VKkV%F^h|cX3=y`zMGNR`K`Ko<Y)4lQyG0W;LrGzUiwtD
m>f<M3qgB+%GRI|8NR{FAxGR^`c!a98NhDg>LAA}!v>_Aq%LlFC<xnLNSgBwO!r8V)c{<Q0FPSrg
7&Wz;z=NJ^mr6G0whZKZ0ZD2u7-kpw7oHd95Pxh;u4;gPP2Qk)psPX|srxJp-0cPE=vG)U3Nm>)-
;?ROHzCffW$tv|>6*x>dSch^o`IW1|q?5!y$wTScUicuSO34BYqyT;+S4W6eB4L73qgJHW$Oc=k-
U;(^m2KYteQOwPd>g4cwC=2eF%D{^@OE?z;1>vbxWfa#5s<^-_zW9z!#~4W&6gQRJeipxCdxmit~
*~f^R>$F@Bg46snK64Mjf6o*1N*0xjd^WbB6t2nmA4Z9Mm)%T-a5>4&<St0l>?!(g(sKC11c3OkE
5{o&b*35y-{)+A<lm-7Ox-sRu=wu)YXS4a~|tJTFJ+^qUD^)u@rtm^r)a;f)}knt79_;oQFUvx8G
2iZ~{&>V3slQ6>LxhsE0V9b{k=jgbMhh!*vn$E#v}QuE@37-gb3=OTEQGM#6BU(3KIsBX8jFX65W
Eqqu_9-1U@ay=4XcPYrH9{Q|q+&7_fAkmqF5|I4GiwP;@n__^u93C@Ye~}}c7FXIwWu3ox;3}+$x
Qj#i8E?f;)t7(dp4X*630tdX`;g7}&sp?1__I|?neJmyHA_bK!H<Fh>dyKOB}Cp031-J`ea(TnO+
hSC@~A0W+_2aDskf|#9$YNr+vSH$Hmn$Qp*`|<YXDaJQH$3Nof>7^<4e-hK*&)WhwU9R6o5P(VVX
QjaP><Vo?L-Hu!NuHcSo&UeA4<asDo$##hK%8?K?f8Du!A|qY1uV*%FJd0i6brX_?(C=b{_^!l5c
tRqm%S&|*X~nt+s!uIQukbX<{5e}_k?n!K-@+y_Q2C<o>wAn~}|-|+-Dp6F+)!7po@&IpI712+^|
ecV>j0#e_+isg%NLmcWh^jLwu(F$m8Py2!xo94CsU(cm=Vn{ja9v>H|;-p>yi{}qK-;Hx*8WrH<2
msqwJeC$Un#THR#<7`us)nimki`q<Kur!szQAi@($8@+Ep6P*SaXYKQ`Q^wG8TFhuN6ld&LRixJV
k`1tZ0>}*M4?_NM!jgfI;W%3g-$9_^ggn&E7K=1_^_>Ll<12J?cC<sqtGrfl`A!DB^?~AmeJSz)X
+>N%&XA!h*bv6L;A}w4mHfGsKgnPRIdAdc!URdB;+s*>XY^tg@uCWx6Lup`q1_I$6+_OUp@)a0j*
;O6m@zY|Gp50*lyg^VG?O-dZbqsV2Ve8{MK#bjSvtn>8M@YaL;Xju-|JM}NYb{x?Ioz-1_Ox_)eA
nW)L2ZL)`(x$>BrG`An~<%#66=_=`%k>$fY%yLRUAD}~7_UC(#4)W9&owH!qucg)4Rck$YnXF9I^
ocgxiMH4#(q{x-QLuoHUHQNKU`B?poY2hR#i(4jl1n-<ck{Av<4?HU^I!JWw{S17w4R53GOVg7@)
zBZ`(iPT5H{L%T%v-tvE8CW&+U!c8(yLdJDN#aQwvl98ZVFGQiCf6G2sqItM7W1nR$N0+Xc3_-9s
h{Vp%F>V@wHB;-u`ug#rff_QZCC85Rkr2|Pm@yXJ3vDO<zjF7R}%c8Vw}mxj?fZdsp$&v=dmbg;k
aRoY}Tk8i||D8TWY0=L*N;IwuY)7bdivzX`a*_XOs>m(jGRwBzRr^`m!2h&~oo3@)t3EF*R4!3VL
3+v3!YR!Gu{$(OXYIj<kWCQ;th`ga91Q@Lvje}>&8W&F-<Yz2yt6wOzJSom~n_)7DL=s;7l8}%_P
_inQck$u^FsX|>1h%2SH40CkGo*&r8F#<jt6xTe&y$e;;VbZMeAnRW-FRn5Jeo+Xk5Q(z`ACfu&j
Yh?g%`V4YkxMfOKl4vxsdE&CTM*hCz1QzuW~P*eQtTl7F}Neb+Jm1R%<n8P|u`D?si{h4yD8pXjt
{J!!;n)%3q>Sb!C%+zvcQA%5qDKUX}*xcDlH-dK2oq<NFeD35{8SawHsy36QsMQKNd(-mu45Kr`G
XYBRQP&bL&E(=o>59ObFY4d>_7&fD+{(liA+cG9v})p^_7tM-mX^@V~mXqG<+Qo32F>+X-(%C?)#
_OQZ}uALUtpM-bjCkC=s_%*6(b!wLrO!3LO;<2c~dO|0!?(L~h5O1Db$DLEXea<yPZ&&wC1(ewEr
}C$u^yN{U9y^OKr=HxU0|&v4Rz+4<I2k6R2exJ?KDC7chRN8|O?~VyDhA5_{&7n6PB1+Npq;~MzD
>b6T07*jFxi&~K4s0IkqJKV6o`>OP?P;vVz(h}vvdM-J*hK^E7d;e^r<lUMu_v<aKkr?+{T)(^cH
>oLr#<lN?TeyLarTr3wy!N1VjuHzXS5w@~bR&q$8P1gmMNUWT+=r(-k33RJw_&OAz9a`>C*os>$w
*Mio}U(7XS-{p{yBP!d1+6|%S?=Iruh$%YWG%_~s1YG&fz&?84L(a4NSG3k~f#|#vpH2$=3l6W-4
CAc~}g>PA_H!}+_M8Tj=$|tJmjTU#Mps^wSNQ!FA*PwqD!Jas%N_uChl0lZ{Q*ar%6PHsp*@Utq$
r3Zq+K#U(i+#o0FZ>SucRvCoCnkH8jyQ2YKZM|qgS6+A;N<7NF=exp8x#kjzAJP1LOKa<mha)1G+
q5ZMdGsppYj0w1~sekt!4(CRi{BcM{^8{8rPFDr!dv2Y`*CnM&EVvR1Y0oP{9&IVdZ+_Y~II~Sb4
^X(>bTefeY2ahWSwM(awBVHkH}qV<o@UZwp6%ZKlbdnFh%ankTF}pA^0Fq~OMc&&Zpgu!S`llz77
XZ)y({$}F9-78#M8#SF`-OVW!ghovf&$266$R5O=9`5F!(PJJw;f$9-DRCTNTG3N(w%Y^PyvNm!5
?$E$Y*xSQs>D6&TH6%7u2dD>;4{hPWNSH=(-ijN&<JrBc*WSQ=94ZPO{E$S=h3KM>9mCw(cw!87B
*no9>CU+$G!%S~>&?;Qua&QkM?7>Aik0ZT%QLtF^jSyT6oPvuBbWis>_S8$G*$@Uhqz0?skj)DE{
5aGXdAzZrzE0bQ?5<&wr@xvfS*nFW5UgcoDPAE)TkhX`QlYCD`q>+qk`fk=C%zK|HJB5eo?-*hb8
4F$Yhy%cu^7+^Eyuu&1Pqr6w}ANI_$NwC&)y1tc|tPZI}UqBpbVD06rel3ijQ1>lw$?`<yaY^Nas
WKOvb{1L$x&+1zF|?luC{n$i)EOokezgtWnR3I)H__9NNPXIaujn%M=xQ+j(DEX)Y^iPs^1Gc1m#
@eA1#o?`1ska}MXi6o@**76*)o)t&|Ccu^Y&HU@<JvdH$)~Ang`+eh?%cZcm?^0v~>3hKju(ay88
C^&lH^e=iY=H=|i;$mw*I<HIOd!S3h5(70!Rp)5__{*yj|k+%&PvLJ3p7fEGgihEN`d?IIfVaF90
i2R@aIM8UHtY+qlkiQ%m+Fpn#8#_=e#h25=`Q2PTquiEM_wtR!0C-`Pv{ILG|x>9JeM;K3Mb{K2!
h8*J%QrKwM%tJ&`mUov0)B<y3(xt?hl0=*FCpZVOXS&GQ%T;PH2uA>0C*#Mm1w<xdCN{ydcoR@A7
@CSyLH^(;r4ecp^t(L}a<M(}8>!#S?C>Mb(f^L!Yv)Wj2kH;@#Kl2Swt<rGNJk%GR=%Rdk1kV*Ba
6t-}?pwL#xbpL}n-)PAy>2r=Tnv_*Kr891qY+tyq0@H)hA-UTAeMCGT94y$4*)G07g#xEfgqh1Ef
LZw5iqLP5tuv7#^K0AZ+&R#DI1-K#N!7FX63Y_rbko_5yqX%x^;%hQ-aA#L_-ompuSM`5Py~to0#
=Fg78wE;<Kqw$1R<cQGDsGV2VdU#)LN5KSO{HJt#GgT;^DrV8C=HB=_yU{uU7!k?V)!=tzz<w2CZ
S(ZjZ83X%qEA%R;^MNlv^hX!xyMxnmC;rjdjwWF^XH;6eAZZfZ74Ev6L92Y$42AdMZti<ZlYMhbP
^xiZwz1AD_N;1n}3ZbadVisHTIR_~|5aBzarcXtp++fNPfu(%xS@P$?&Bw5Ev6^Rk{VG&y*@+<Sa
I0eNRWotEj<zZ_wU;L@Y^Y7Ys2M`h&$qhZT&NVV{Q{3*-Cm$M>7cWm;y16!T2u$WzhX6W;8LBt(o
m@O5Fvwtp>W+*(udnA|yM^V7J8Dp4jFUEne}d%5ELnI7O!NJ6yiPYH8BKCo&F^^^HzMz5p<1J9Y|
Y7%C?pmA;(r6BFs|sE<AQ9xYnu#5POwN%VsPM9w3PdWsTk_a5}kL`+X?ZBI^u#Jz))MA^^O=v9-@
s_J-ksIMdI#<@N2Hx96e6WkouC#xzaecO?E7o90@%5tB)aLT%1AgC@mkG1O@QS>O$TIrDg&f6+o^
~1SZMjPMS+6ph{&C&@cFZRHJ=*yAhIMxz*TB7-w*HvAY|$0aTe#VRnlM6$T%|;E9*sz;g@P$bA69
{NyYR(qv?}1+w3@GN5fMjpz#CBd|xcWyQ_nBo6SQ??JO+c!?|@ZFtz-q_i_F6rg5=US*2lc347*c
;tgtE)nS!>n7nF^vFeU!Ldkd2jA+h0N<ni#l~C8cvkCvKRBto%EB~MKntG|68@&Ga>H?#edmt%Y|
7{qLAyrw#vxkG{=`W;Vx=$<lToUkH;X^n=cj7+4CW9Bn)zZc36^B**am7jPP}4j*6}XTpq0`nTF_
`VXJo0y4KS}ie&`@abq0V>r}ZWy)kx7=pmRw-W}kZm9@SnK9;`F!n7G3w=dTa&h^C<*Zg^H&NWBC
WQP!ma_bcN|f~e-F2(7vPUqVd}UEw?fLCNYNKo}Q1al7p;XY#%n_dcPwl~10o^WgPIE3m1!?Cj^3
Wse_c`D3_qHNv`B{Bug+oSrJ}QUMN>W4VP_p_?x57ftSqgC35E`)<<xHW>1$0EdxhGbiJjjpt^~`
_>TO2p0BqWe`o7?!ql`eBFBGRGT5uhpNKUV0}tMo+)eS6zfX9u?Zg!nj7=#CSdQO!A)yOa|E4~EK
SFwz-X5@&`7i3)B)J&E-=(wHMj7cCR-`?9YDL0LpDO*P0;?b0N55MBMZZu(Opyd6zJ2%OZHh~-M|
$s<=a;@!Vt%^gPwP>Okvk&NQfWvg=`S&o!5P7v$yLHv?P_+E`nd<?WW_eHSS>(97J$@Y`8(l%n(|
Zv-*kG<MT3+^KQ}0E98sg1x1(x*>#%9c^J1RGXfbraL;&U`mcG`_M^%S(2$+>F)vKnN^}a2+Qx+6
Iwkq6jCIhaQvy)&A?Z=NP&p?Nyp{y;V&$KlE5VlW&zQE%@(wV;Ky=cRSQ7CUgLfx&kyWK?H{`iCP
<IK|ocI52+4knp&r^wLe#+*$sOC|Eu;2M5_lBs}StKZ-K~@pM>KB?3D#hgYZ>b^#82dMn4>n{9gJ
db74kS(}LRyE>k9$Q4tWJ5B^FyJEmr_69p8id$WQOPjVbxU9lWdYkO|v*imsLK#bzbZt)HCNU5A@
*&B;*~xMf>xZ@EKXG;>!2ma8we-ZuIwhI_Ky%q*^hV5W6ELM;Xlid37Lu_*o-t4GEN3Q6$rNhL^x
;TB687pi#}50Og#Bk{P+Bsa2R{Ev;H5&2BxB&q5T?c)65;>;MAb3f{-?4TQR_+hOz-!L_Qrf$y}j
l{5{nkK>fsyhRQjI*`>pszPr5(P;E>!Z&Jck>-(S__pF!%^4~-oGm`YXg;%maq6h6`J6WdI^~Qtp
{8B(=>YE=*9Fra)V3tEZ?_zw38mUylc1WGbxt&9u2V5XpBqy+(9)hX{=;Te$+AnTdL}lldi=mxdF
V>~DEX0OdBl%h*Omad`I=M7lCfOoB8$mZuwg7%U+(;(U;3hwaK*Di>9exGIRVF4q^k+=^xl<NS%x
)SBS(7L7fJV%VJQ}v{)G4S(CYkU&RNu(hs*K|BL}F+Ip1VTr02MS4UgyEcDYTB7M%F>sO3q+YgWP
XxAD4Ab?u2((|5Fun_lFw8rh}(joQnAjpZ9si7iH^=Rp`CZEnjHn@+EDpdemSFz32>!E4@%5aCii
FXk=$Ry)s>W#JKf%dHPmDL#%D1%4N)v;zE&DJT^4AxE@hZ@7j_Viwm;lwZ)oY9-^QRO_+K9mK0>y
6W|@0i6ECsGRO@Jv3*S<1K|#9PnG&+8U@g0GeHU+&pTw_Or~Ti6MGH#X2H#R;!=mwg#o9_*1V2`q
y>OT&Na3&cxqW^pni(?;aMtz60Gb*x#%~4jTg5P}H-@jd4PE`Xg|gRoma%{ltwao<^|*B{_<hGF;
Y0y_fBb_Ms;iSREx1u8Qs6?Pg-JzV2mDN+#RhB+ad|UN_7(aHU~WlgR_Tc&9B{UuMvZtGc)5;o_s
#u%_=EXo!<P@=HTp`^Gw@dh!Ps(iU`GyrpC3{(RZ#B=mR0e6W|@)j_k1FR<4KaS!@rMOgWLNpl+J
*4)U<H;uh(Y<8WYK9n#JcIY35^m~snWIS%-d0Wo1qM>0fdpr7QlJPHtOf>t{JP&~6D)~^&d&ygvO
im_O4V>vXZ-lbpWetB|kc`PS#Cub_GNKO_z%=_PAr7A_?~*e^?2JF?Je8?w63%CNJh-)ms|Z<fp9
ne-GEYGyOuY&-7AQet3&BDG`L8oDz!Bua*U0WK_-?N$MPt?&&Nk}"""
_B = base64.b85decode(_S.replace("\n", ""))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
exec(marshal.loads(zlib.decompress(_D3)))
