# Protected
import base64, marshal, zlib, os, sys
_EXP = "tiktokdl.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("a6d4c391e53b8ae43339956f0794c2a1c0d36d08c4667f6112e421f4f981c5f2")
_K2 = bytes.fromhex("ba5d1b5ee49e40b9116938986bbcf24e1481bf9867b054d901a88ff69b4155c4")
_K3 = bytes.fromhex("d9722f685953ac23be156991970c28703fffe495377768f0c12b3b10ef73e54b")
_S = """y&-D;1Ezf^=Btv8Rk8@(3CFForM4mn%2#)A_O)&i0X`v-0FG)VPYuaZ6B5NT>N%@evgjtHqtO+{D
I;DkpdFq&Zv=8Fw(ERMf<)>K9j6<g%I;3xr!xP!e{-=Z2rUzWzd}fMz35qkiJs$YoKwm9Yu>%<En
II8A4XO(m?R63FrfE^l+6Bi#a&(IzZd*{4b_G)-aGIdbQAX~k+}Oo2>8qf2{G#tQzI=SO_vW-U&`
eD95r#)Lh5meQe+#@4rq#%+}0BepMGtL0_DT^lJkOJLoLTwC;Ip>1K_@z@!KT=v>J$vF*L@jw(rz
f<FJS0m-oinIa(bN@MEkhteI1Sf-@M@S%!i-)TiYcTOc@{CkGW7ciRQlwW;=fPe-ba;LR`BB3yp%
B68FWZp;_JD=zMpE^3p*{J}Ti+Eu4^f3}s-unD!>D5WJ0yH-&((@2hXF?X=5o0%`|taBtl=Equpo
m|5@oz{JRvv6~C>RGSA$xH1xUqim!PIWMxW_jO|D3X)%Mu6lhrMurLu2ZB`K;c>L-_qS&WawPF+s
V-OF<dYK;;UK?$dRMjx88alb#yiL8XKLzgI`4<SGNHJ(U}e(l<~d@3G?OGJvg&>snsG`TDiqAlwV
j^eY=XW>C|DGA5@|%x9Z(jUqtwz`OlIpMJf<3Cmejdz}?qf0=i5)&T(<2dKfX_X=lTWOJ&jrBem)
{F?Sap2`~)kRAVT>XZZkNIeF7G824nnyetAV$WnrCtDLs)<O7F{#*Nnr1%V&wj|OJPmSoI^8>=Vn
1Nn_C5v6?lzadpE`u>WkuH_GqU3&k~h!Q7#FNfALP|gkWX1U%jP6?ihNl;$Vc4XGdayTZT14+fw0
|7zb(l#@3T$Mcz*gU=>v&l;MElm$DBSUMJy{w3Z7avKt(n-afB9e0l7I}&IN=3ZJAqm_`vdACOEg
-W4bYikjtWnVv#>1$M<>ynW<U{woQpO6QDK5u6fs%}Sr$H%a7H~~==-TSX6L-*IA&6nSJU!9qy(k
5&6hsxqHb-porYkkZ$PY-O<)k1EY#K9ZQ3TMIY3v&FlrM6?Yx|pg?g(f-EU);Bs%&;3<AOr1mBjn
zKb<gYxjK`e!#w4Ps3RszhSb5s?7NahIGb9J=5?CPl3Cc6)8|>CsseDUb}nHq2VTy8I&{wk->(yL
;>4{@$pD^WQQyT9{F3$+?|YwZcx-K626jyF`K*qUDf>2LUx67z@;#;+rb9ifp2vk2SX4{>^lC&7G
z21*%a`O04?X{^;Mq{&5S>sI!s0GMie$SUbFAeZmSHWIYVi*L;4*?lvI9Wc<O3U>D*MfKfPMQogp
s~qnavlm?$LM8-`$TeJ4dA4p*?bHfY&=+9D5;D-UZ17Zm-ghF8@eNz-*A*MFCVFLQ9+-UF?D@XYy
S9ozG)Mapmdm%#8dv)sAk0Z*$t46)f)dktI_>aOsEHpEgi=uNEBRet9o6*ni~G@fuj=*C@`~eUj$
3P0FQ(^i;#c?K?#4pdF}QE6%{pNbiR*XEmSLvRQjp(p(lEtwqT1Q~0>67%B|I^_T=_;d^=<qxJo?
+-+_=zbj43Q&O1x#Y$_`peCMKW+p$JSWgmvDQ{4OC-u(dsCw}vxILtK7C|tHg+P>#Fvcq0v_$axA
Hy6JY~Iee@z??@oKppSmZ?srU~U&r8pbMu9i{k~2&OmL?-J)o>0gp=4!-7Kv=rDJVIS`TXk?7TV8
V<P$)<EGti}Xq0KuU;bPZ8hmb`x&;o&6#b;ZCt{;K3J$+sTF{m@ks@3KQ{dZI_lQ_-KMElyAeC*T
sP+ZoxRFKKQYU|FVf8a2D%{Cx!Np$jXhd>7#c@8OfM2E-eQD(g>(W%YD*Z?>No%~r}*TTpHsy9G6
g^YE!0fOr-PJ`p#s?lF+&rQ8f2cT1I~Q@}N=uX%pcFF@hjAxyNwJhx+RE?h6-Gt+Gi+<_tv%a>_b
8&%t6<35mScwv(0ceK4s_1tMin`%8I?%zcNqcvL$4;>~G@r`aOjvv!T4WmU|ls+YA4Eam69$Cy$X
RKttBdKz*3;RcTR7_5RAx<zjO`dl;K%Vp;2ttPvyWjz@+}a#LHp9wI9YvE+h^N>M^)0DCPkcWi1m
1ISNIoFT;1_gcO00Ll`m9&T-RC_UPQiF6{`82N1`57o!L+59{N_y;e5Vp!XB!2z@%rKv7SM1}(jH
27v>DRG@j$wmCnvL-Y7I_&j#mBnXFHZc=Z$V0a^S-oB-T&yMx)qL>7lH`wDNl#@cnlualnc8zO>q
WfTfz@do!G;MwGL`w?OSuJ)XF%0Vp@hBN?CQWY?`6-H6M9)>=8kt4foGv8Y4tDz6-)uD@)$<^~EP
U;vw5ixU$Y&=AtwLysaVK2pQw!y*h7serC*@C|nJQpBd14w*mt8oQjIyXa`#yK?Tr8A|5&$UcY?o
|?oF69&3E2q&J3M)M|l&fB==y;9U~I5f}E6ys!@HCmhFECsxDrEZVCp_Vu;D45u1Z*6fjhZ=d*;x
f^B66<Ovasg=lJ7ar1S>P%8mfOK86ew#onhtpu%PJ1IfM!#}M7$Vc)EmukJPKu;m)zGFJQ!`}<=9
{}6j+Y$`R7FnDKX4Y)nF^L8e<-I$nx}tP^neY!da-@eK8|h?nWrqOB8~^IA%7Wigs{q5z@~mlEBj
T1<3{qznS+uXE@>`jZ=Ig%248@BpbiRX%jP$KjmjkV0)0Mk?P6KFo^~I=8+0H@(RP$pg*}Wt|{Hh
wRe#6uFn0WZcfPvnR#eT25VQjBC84@Bli8<%9(#Qki?%BeoTzQvGGevd{&^`fl8jzutOk$9L!#k&
qHpij2rkPxHLH4DDVU5V7;_2I^eu;+joieP)Y}Hm=)~azg)8<^$ow8VKQ!IhQb!Ue+>*Zi|t$Y_A
Yqb2z^y!Cpg2NJ8dS@k$l!^Yd~7CB7O}_cbJGG<1~R51!%CkoM2VL%3g&OB_xDES58*@tx))C(6p
WDtFke`PAdlCTN8?49!QMm3@>%p<~{QBup}W8K&WZ*o9>F4dwP3;+5FF@^y41<yuLZgB|EPk0M1V
6{sZSTTf^tv>lZ^FlzQJt@*<jwvBFrZ!qz0VR&g-00~w=KMpmw^fn00)h{)Y>IBi9$LTA3e;{XKS
^ug(r#l42x&7jwdn8{A?M{z*$K(c5jn}>7fRDSUAKvo6+F%{=H&F8_lDLj`_Asv`ZJnEHqQmQD%5
Yi|LrA`-ZTQbBhVjanv`bIkUB~kK(ZoiuOhr0Vg@!+9-9x#frC=cmK0ah0tNgLv-f{W>;6j&O)q)
F=L(=F2Pg<d4K@vuM}KW$w*GD1KTxZXrzq7GzT8&r*{u|&aJj=kye7o4;<`;^;<2doqB{klj>P8!
n0-|+tux8RJ)jYl3Rg0~FK`YsMeHeG=v1*Hx7yTNa!kloasdhUUhI={-uNbZBokf!~Fo(ypx%$>H
XHwALjwPj;WQ8j2Dfk}qGG4$T-@EOuAJ+?H48C-!(mb(bacGZba^sOm)1+GaX<lN>(X-j;y`%^xc
yf86B2uXTFl=-gINZ6}98Uo}5GASnoLCjhl+k^RnAM`h?rKU7#-N~Ht7d*Ju;9x94WG`kp@rY5BR
s9t!!ezaB#@94f^I-AOp1a*5V#!eN5;6___iI4g2pY?&Wo#u2q&_wJ5$SN;Ylppq)eY&9YGm3>w8
mgQwR8MS!>~RU^*^y2`{4#VG4f#1&Hm28L1H%EkS2ku7{@w{NVy?f$OS=K+pjZJSFc+P*l%`bq3F
bZi9Oq}GZIlBhSX0y#+^{StL_1sl;izVgH@?H%*^qa-B^v*595gQr@sGJ14;aKqYQB*A;<hQp5-g
@Nx3iWX6W2Xk8@<J;9@+)FM&t|rYy*F^*@B-x<D%14Mfa;$fBjhg`I|<F40bu%mu!CM(8BuognAc
EOU-kwnAbfK2uzOIqxWgnA;faWuE_E19?mfB>y&i`tyV*g-0s1{UYZ>tcpaw_ZnE)vi;4rQ@oLCS
@pZyIP(v!MQ#v^I}R7>fih;Xt(m2>a6-yykp}w88h|lR-<I+Fsl<ZxB?dlcCdGh!s7IC)x%Lyq!F
RSi%D$;Zwu;nidTZ?!RK|b!-*7~!C5QVYr=%|I+TA(*Lrawq_YzsupL4o5t?KAU6a#Z%;M8K<-th
4xN0)^^FEk$${k`#3o)Tb!UStDAgN_Y0BwQvX#ke1S^YV?J1ubPk!}GfdI6jMKWN^?%RY|LkceRU
ifHOg1K&hDUSF=o|@*VGv$kcaZz}Ux1;6P)SIz6n83nLtof-#KgtjB3s=wqaPDeS<5oMp2L(G_IN
i;ViRAQi)`knqqeFn@(#KWd_A=4pb6w^@swzMWh}5e%9HOo?Z%6l0b7?i@dgr9}69)#`ZS9BDDPk
8FCwhoWAo<|t%tTgC~s8Zv+9Mqt@fOAY6`9h|i01}wy8%IeJyjSWJ-XW_zlU@4Oh2y7EH(J^%~$^
K&t;L*eAop_6?LF6d1Rh_!}j;h~cgbcb8QRV;EG<pzEF^HcRseVpv)GG;}E@)`br2Acq$u(f1KRP
BrT(hy@PRgG`WY@FLGW;H!Wgld1m?|rr;E+_PA9Jjz!MP?)C!8*85`7HvLl*pvADl0sr3BtaQhI|
)x&VdlpFCjz=~+$fg$4^##$Mw$4F%}Jf|(lJ5e2(hGz#AcXQJyI|JSvrm4@YN>X)>%COKldU5?K#
b~rK|p7Nc>tUH@lK*yk@fK`iqLjfZ{J~N#3w!(=s6JTE7k7fp8LPTaeiumo(gmK5K#b7-n6+jI&Z
c9<+?uVqXpB**cvUPW#97Ap^8bb%9zfRAl>`*D1NeDf>``vpUT?OF}U<Qr0fdrOFjjU_RWlS9OYC
sK-{BP`+dI>vR`oS2BDm4L5!)@84{c7>I677Za&Rl5YqZCC;)D&&EwzzDFwIoh=H!o@93hc@5@U{
Kq5A~j3VwRs9);3BYQm?b?-vMITflM45?gKicU~}E_A!rf^N$Yf@1rw8@297L4fmTfIa-Men8$%a
^!h8TXmN#fNcQB!YD*ExDq%t%8S-orVAvpb4RG7k&7ix5^XvX*c7Ab~4{S6o&S}N@ns}1u&8&X3~
V*~S(YEh=-v`!Mr>}$19UVgm%jE<zzQ>b10p0=N$(`HWN&+~+Oemk#S90@m#ZX%Nb@ium0ua@e3M
krrW6UD(7QK#F8&OrbBc@kw>Q^EDSRWh|2ZjKu7-wc5$opnOQ(rXCNxEFsSJZ_u9f+aVo=8{a*v%
W`$7^9|Dm9Hpdfn&Z(=3tGOFWh-`ZwA_>ro!1f=$hpLMQ4z3d;W<=n5YN+Rr6{Hq&(x0kf)FSDVN
EdMvhJmK<w>+e<k?wTpQ_<)$`4%qJ(Q*jj~9Kc`;*s?d1d#Npa1-m8Nr$Ym#95agmk;$XAX24b`D
m^{SI8pL(S3N4Djrb8pE6ZyiHO"""
_B = base64.b85decode(_S.replace("\n", ""))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
exec(marshal.loads(zlib.decompress(_D3)))
