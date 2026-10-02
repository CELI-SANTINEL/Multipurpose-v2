# Protected
import base64, marshal, zlib, os, sys
_EXP = "tinypng.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("5980942f17ff89412d96216fa1def7f51fd857f7d74c2b0f26fea9316b82347a")
_K2 = bytes.fromhex("68e0736ebb387b127a089eda62c841db725804abb9b9e3f5b69b98f48f3b86fd")
_K3 = bytes.fromhex("149365dbb66ad072a3b49fb2a4458c9df2065168ee2e1cd6476f69f5888a2a37")
_S = """T`3>KLE$-gZiJG|-!BbonS~=7Qj!!cyGT$VWRfA3_42@t&7(Dnm_3+<PUw+&lKyl;7);5;4j=g0@
gp%675phbzwj>#8A4m4u^rWap|%Z=s=17pd^zJ-O5yTv&7CHM?-R}#5g{%=!$u+G3Q7C>{}nCcsP
ksSD;IOsX)ZlmOR0NjQadv0BG=xoiq`v@kk2M@{vw%ey|`@{A!dP4GS<;sAgKD5^OQf&m6<MdPG=
rH2V`aIQfuG_i0#ir2W7U4=!0*vZ7C?AlOjk25~6Un6GK&*Nk%*_5o1KN8N?tyhhMf4Rm>K{G=mX
cshQ9pz7LN~zBM+rcI7ZCbFpLHt}dB}D@LY&eujBW%O&imDIIP+RASL>Jdu0KimR=QwV;KBHW+%N
UHY-_t?M{`PnRvpF2G3}9O+-g(3)kEid_gR->N!vFZJDB$D>Y%zLouHO(}A}U~1wDXmVEc=D$M=j
9eE(TShWPJq>~Pm5ScBmL>WDge}W1oo-`Wc-;PAW2E<}5-1rt#6BsqHuUCNPWx10;m%mC4c{=l^#
l}1-2Cmbns!e((dfYIbBqv4fenYPGf`)bN^05(bt94KATP2Wxq^6Q@LX3o)Rgy$!*<pA^l7{hhah
s2fc|K-QgC@@t6lI)>vlhSg9Wq_>~2iF3U+HUC-y<<)B0ixNFxr0uwy^e7=lu{11@EA9|yk?%UdG
}=%~s&T&pVr#A_iLZbuX=8m?AKCtG?rn*Qg}^}?mqhU>H9WqwE8Az+l}4(ywOK=?~|u$EjcDVggC
d-MNSb~n*SZ)}T9)i+Oy!@74nBlS=KtBT$w4>m7wO-y`F;JJGW#<uK3O}J?o^~XP4#L9(MnSOG2`
LI62!#B!fM*?md2~J*J0Z(y!h|rIoNO^LjrKS<3*_G57!uf3IexEV_SMr29nr}y_8TMh`L>aA*u8
DnDE1=+GLX&iONghd4zrnG+O9(qEE%h#xo{rlVrN;0LfgEO^#2+Sf4_{aoW)!EJn$>IOB^fq~>J<
aUpQX_R(UP9yV{m(yFEtT62K8`685MbQgzPH(=xb<hR4;YWI*c6*XEpeIo(6o^TYapw+8t%da^E~
W)|&Kr@UtH=3sH=|f&WH^X4-*V3;2R7Bunnv5Ri|s1Nt6ggBvT6l>^^H;orA)zZFWrsSIcoWw4!9
m$@P2b4u-|x-9zr8*oI70GIe?ixese&+eTMESe}2m(vluLMc%y01tvI!WA&Tz3R(bW2%5<rW@@7&
NIG4O}fX82&KNFu<Y>=9e^j({d&s+g}(}D>52(Bs-mdr|6uE6#7mfX=Mn<I9ES%{O>9D`-Oa&pKR
WGtCm=q4?x(D+Xu`@e^R8qNb2Zz%1WJ<1TcYh{onz&<*G8!f2l~r-b8qYU9Low4MG(Z`ciyt(JB`
OAoJ<xcFRD}O&+I;m&|kp_LN@u7@-#INbIRAt)~J*&T1wwm@>n3VLna6GjX_i`xr|`_{t;aJeQN-
4^XQ~DjAQe<Z&)Scv1dM<>1*U>{kj2Q)`Q3>L)MN?FA|0=c5S?*xZLW)hmZ`#0)NRhJ8_8ai7L5E
0fx=(Vfqyq(8E}Ub#VskG#Qix*tPM=`zK&QB><Z~<<QL)(IQe0IW2UTmYB6$6C#oCJxa}d>shLT?
PC_Rtm<RyY7}S%tGLoJ7!>IA`^oUM<4187PyTjstq_53m?N7^0Qx!h8ixMf6O~US0B<Y{x6NJJ4V
MEqn&_$1j(asEDoBkCSOnxs>29ge)Ri%5TV<+DeS^bZfU5R%X~Y%bKHlk58;kn0$aUUgT({x82vl
hN&s@NL2XE`adVupWCj5HUj7&q}0MajRD9lFRxD}V)df~5A3Ne<3ibQWQHDuwsm+Uqc2r9cMNQxa
UzM){*RK>R4{t?|@#=uE;oyXn=%hu5dP{zSo&8}Q#GnOe{DVd>N<6HMVJRAyQhwi^$Sxc4Xz#j4L
80_DBmZWHuS<Q|0qvu^W-yu(Xy-scCLrj;xKMH3LGv}?C;XGGkKxjRUWlljB)rWIa_?w(k-OQLC5
Rc%%LwxpLObSZ;jNIQZ<6IQqBSn|1LHPd1Dw&yZvtnW3-5I@Ve`CFmzPUg9cYvT%vuVH4*PB0*Ah
jFK-MvMxM~-e9?#vJ-eCgeV7q%^n)2rj@SVH=f3Wwbg5u#w&GkVOWiR{0l$5#6dMsqB75C|yer;m
&Xjf@Efyo~-WeaZ5fVm5knA$E#`UnMi%s48t<mcRi2f<lr9G>kYEnZY7nuB8)i!1L7|(}c`Lo}u6
MuWPj|lG+r<on+2NpDiBtj<3cSRz!gi>u1zfKy4R8if4}j#d^?E0}Y&0w7?g)cmmCeppi}jX$+ex
ZHDY~jiy{T%xG!*J0qTZng}AV=${9aB;*}9|8*(+&!s@G$Er~woWH*WoiZISdbooWnm_g|+WN&c-
u)f=rnb8-xWtc+-ws{rGfM096g)sbEQg#f!^K?VskeC$)XM7J6wmd*Ph_lwQNYL{uNyJ`-<u{%v7
Gvb7w5DXBn=icZi{sdj5ClEV*?u=u$E)fWRKv?19=aSjv3$?p^0)7><mn~@Dm4X<i@Em*3Qtk^bu
8P|2bcvv<hHNCm#gjSO1}v{C^r!dl$4JvEMk*j1mED<~=lKrJ!rTZlvRM`NQIOzfhT(^fCAjlKl8
odLZv;nRR&egbYj{DxP0t-4AUJ=yspH%!(x`k0GnKp^<3Fnx0~YXGJ1Euv;YmqfiPiu*>VdpzgU%
3}+oUTja*Ux;wk;PR*|TUw|2JYoL>k)tvei(UJXNgjL!0dM~T?Jze6@w^zkI0Y7^c&$h^HA?2-D&
cpa9ubY%B>&j_;nankt0jRZscy<cUW(FY~wEb5*lf*?1&RlC|eI2$h0M)`o@jVrv{;;-l8dEK})x
VxG<KVyogU5pYG=rjAh1=IM`l9JuwgXIGXCL4+cZ)6#9dJx3QQ_+ZWYHCvGqbcc$dbg7y&a{ob&R
_ls4p1zLqBH0{l9f9pt}Xbz`DIKkyM>cisI^L>DW1wfIYop>N2i}T~Z1}zL8FIour}V)?d8bC95^
mLoi2TjkYz5)b9HW-L|Y8`$x(RIy1bw?Qc<;9Ny}&C!TavlEx(`Fr|p^0%T{MZ!ooNOaP$gsdatX
+Udugk>2{87$(N}REjD6{ig-1OdiW+&_m=__|PP8Agy>mTRaSDXU}<}jCLVD`QCgi`&PTTSRmQeL
%#Zn>kluW&swbDemUuBqOMW9S8$P|Qf95B2nTg1I!<@oRf^i5RkyzRVRi>mVKELL_0{*mr8L;)_o
E8d;H7S3Np}j8&XH#=$HwyKr*0U!@`n&&fnyl}RX|9TMSaRjr;qlq-wlj219>d%`Jb9QRZ?n`_8A
{--Rl98O-KRy7h7=x2>csv*=P>q>$O4f-no-zVAh6`Zep|DWs2#MB{`Z~%MDo506r1hT%#oK^Arg
{6CY3)P!d?$MONwycG@fAdxR>9d+I3X!KA#4FV&6cm~z$HEy)MpxbL~PWZur}Sr0I=M<Q{yKN9w0
Kc~tJ8&chM3ZC2^Dqf3IcDj3?@Vvn!(7VB&m5QE5U{Vx`@)62q)Ht*p+)|Q=ov$pCR{LGq3{5$-5
rd|`u}rt_=&FvXxPv;Ea+iRvWXF+))_*P|UTSpi&B(LSTYHS>az;&V+U_}~QRdh3H`~#H%EF;!>K
BcrY(r=z_!J;SB}XZM$%-6ecsh{rK@!&LZ46GXSosC+)vH~%rTTcxtegkH!`3Cg;FQ*obf?44&^A
zKf%@*+E}apo%%vmG;@-XttxIEkZ*kVdCL=+Mnge9Vd<x|`?OXZ_(WBKrS6kKE-tvaaqA`KKB&#%
D83PSK*dK394GhSH_h$4cL(#|pdREyy=`-Zh=dU|989!0+=8nm?tEi|u)4){hBg@yseVw{l#A06c
7v1rEYk1J5l-;o>hp-52TE%PN<x2TzBs#jIN`E??0OaE%Gquk#slNy(XKL=L0A<(#O<Yc+9<4ins
)bEUKphVdhdf_t8fHs@GLU^o4um&|1I5B{o*v|@M4g~!jCmeilIKy(ETZ@+TfOC5h^fCXGfAb#FO
)3|3Qiyr94FhmTqny9d~W@@$-OboVR@R^PcA~4Dc>f6h{+}n%Sv1(>|>?QSlM6xhggS3mo;k=P*;
@KX|%hE!B11EmZmL6CmEY}PB>b$KfC05M1RwDZDtAQ(7#)Y(A$QhqBX~HVXD~Hx(?*Q`Ox5PLMVa
m!72$&1~+=XP$xB`A_)t&H>RBveZ-eIFx%{XocrbNjxQ&NZ2a3kK3|{Xse4pQ8Bj{Mpw4#}HVNUq
YwIa#uSp-$FThR~I)rrs-qz7!;KZV2Ij>9Bvb)?SCl7j3qD4cx>SrY4l*eu({wPRyvtsIgd)L!n+
vY_aD*2VYHC4;_Tg?*hH}nUmcqr^bqhHmGYkcO7U4)BNc_hWMjaZymtJJK?+3ptYWbglC^^!6MQt
u&%kD{}rVtr)J*i^jWC(4}i_d+C5YBZQ$M$xVby5=g;Fy?pOkPpVeL=KNm7&2J>$vjElG$*nfWQc
v<8)7K{8<hD0W8JooAbj5Sdf2UQI^C}9%Z94u{r#gx{oSBv1`D-x_RBbnlH=<e)i<oVASs}BGJ_}
Bnl5K$Cg5#mpS&W9hoX0|i`~t`+QYP06#0V`82FZ5nEB*tt`OaXX?!n5ExPZ&@b68~3T$*4sG{fs
LyIfYi8V$gJzEkY6iKzT*$BnQi7DCONW*CG1N<LMwA23`d2MxhEYhC_@NgeFJy{wh)FAOLDSihM%
Iv#z%3_J-ULh-G>21u&cc@(ABR*)GIPr?`W?h7V<45Ktq8o_h@bPp$9->7%2J3?#nnA4oznR2mKq
%SSDbQ`SL*NOp2=${$fvdKXCs7F>v*^6R*Q849`{7r=AdA)ki48a^7#Lg}crftI$l4$WZtfUy0IQ
&Lj`m%alDKvsvHR3mA8lyf>&UnJQU"""
_B = base64.b85decode(_S.replace("\n", ""))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
exec(marshal.loads(zlib.decompress(_D3)))
