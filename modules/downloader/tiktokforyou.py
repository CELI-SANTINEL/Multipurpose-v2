# Protected
import base64, marshal, zlib, os, sys
_EXP = "tiktokforyou.py"
if os.path.basename(__file__) != _EXP:
    print("[!] JANGAN RENAME FILE INI!")
    sys.exit(1)
_K1 = bytes.fromhex("a5e6a8760a62ea23d3d7554face2068688eaded28ac5bf070b66a5a73a853f57")
_K2 = bytes.fromhex("4bf1eef59222c71ac6e0df3a9dc1e822dacce6d557ec6f577b8f881de668e039")
_K3 = bytes.fromhex("dcb6d5192ca13dd80f520dd3fd50c5cd6c3b55fedafb90b6b60ed89f971d99fa")
_S = """N_#fK>8%U6jN4+2GmJ2Md|%DOxSvAM*7av)*@lMT?xj$UIx-_*Vs1R78D|BaOJpw-X16Iq)02;&_
-)(rhKwGshswb-uA#X~=KR=E>{mukC)*vZ?LHW^F$>Eu5lmc3D!T3<8w&8?N4MU<P0~;f+o_Hl2w
nm{9|Ix2&EIT++>`j%_|3QUhRnY!|FTS#zm#i|-3BB?t!fvg*p+~+>C!ughf@KI8{eVaGf?y<MQ<
f@OlrmqJwA%f3X1f3Sba00F>AO)a1g(X+JPXkcB5{N8+-15gk;fYuHKA05bUw{E`VNl7<K)1>*BV
A*uw@wTQ%8zv%qcermaI%ALEa--d^6%j=hcOUjzB79*a_D@@WPP3Zg|PxHDbGxaIyor;gBK^)|Jd
8Tpj?n8ZWA#*M3OZu8`}{${qT7v)4cm+1$cPe5rSZyGC{QbuIhwlON;^^FzS7epw7g7bA+p_$rS;
6vq{$gXA{eF>R{{L1_i&KXz5J3X#RQ{H2*DPWYZ?cRevDts*XJT&F#*h4WP<aji`g5j$@qnBd_zn
h4OxrziGq8ITit|97OVowGi)M}4r0VC<o_?MPuAfe;`m^)s#rZr^xs=+;PoRDtB)Yhn~UEv$8Q89
E>ak&RjFwU+|rx#G54#zZ|MnuhK6iHzj6buFgtox@7&!<)!sjfn!vCr$UV0Y&PCe!GKjV&|M06hY
!L3CG|%9Xe$;9y9v*C*fUZ$~+T)h~_CgXn+%E%XgZj0n3C;mjD8BhpWDH=$eYG*98)o%Cl3*DDnv
LwOQPebX(X39Oc#j^2wJip(d6>Tyt1Gav)AtSocNw!EOs%&0#ASBor2X~G$UNd6Q_GmBak&12JPd
J057K%bSv&Ruy9a6-$o!NU!zMsDx~cNWZgwH1}XaFCvj15=y322Y4!X%L%w)o`r2&A@Hxo#%0FBc
4>A>>D-C0dAS*<{=3zw(WEzP$nPJ27+sUn=n-exeL+lwwYL0lXJVIzUG5?-=~`DaMy~a-+>G5D|A
z`OP(?AEV%OGa+1@BwMt^ikmII!@`q({_5(p#8xm0$LJ9VjrQB=A-}QItV6S`UW%9v`Bmht0j1B>
}q}6h9^9=R5AdzPo9m+lfum{7VW^)ll)8o%=5qLuatS>KjcVJcA<R2zxU*)7i>%r<pw}slrvI@!)
eB&B_8&@Bm-A<I~<9N)lS}nIcQqNXjaj`~hV5uoU03NDikkIPg=0V{kq`>NxQ}5kVN5hb>TJwMZ0
KD61>jOP~zD8^>^~GeoURU)DeWb_T)Mu|IZL1A$ph^3O{CN!HI`L?H?fvVl#eISkO`DCCI%XvjuQ
m6M2tG>-q1$}{);dh?oC)=zj)@OO9+ADoUI9ZEE<cs@j8?ewH{E6FR$)R;jFv~aJwpKXzi5+K-bZ
=hk#C6kPUGo!Zj$0@K@BP7^h*oUMb-y1>&hj9vtgrtl9+&h7;o|0MvHLfKFppNJ1VmFG;EzD&W(g
d2L4D8<R5qmI%Flr<sQ^n;G8#zzAPJ`G-j4c*9bN<A<~rz__35hWi~;&(?p}!Vj=PKs5&?cc@!PV
V5(m@4i7G0(iv<}5xkefMDrHADz(<t*$R`}Y*Kq-r3LEy^)GEcpnjRanh6xpY4sEVkd1l#Sv)A*m
488;SJ1z~BF*V1l{g%*8^Kthr=m8Q4W&NG&=6``DM_|=8q*F$ieL<1=Cn9S<3Z5Y8T^r>Yw2pPI`
H$iGmlCWQIy*zzn;0MX>ha-y|^TcksKX4S=}eiA^By!<<b<F^R`or)4Vj)PxbRMF25V6ZVIf_QXj
xQebdHD?`glQ2KqPvIn+42$O-#}0X5?<7|k=*R0?W5=M1T!ay)luy-44|)^|<m6@20pZJ9PAGrv+
*&87osubV1+mdmshLgMxw2PPPc$@#Qkyj^Ps3Hro-`eSMk!E1H>6}&W{6ljWxOM;?6fCMp}M*327
>$HOkAk*mGo>=$rj{Irif~8weqTWQesaFB04DbiNcwG$GDzSjpbJ*P5mv2&lY&EHqK2iDajMbHtj
4xr9+N@9CBU8|r<n`LD_?gREP^csdT`cw38xV7E_@KAPekiq->fBuiw)~teQ5!BY@hnw}s3O<sbF
PmxTqDUFbj=~$9l<9Cu(|~%61?-z1L#{~fQVSD%R)fGg#e{pL+3kPat~QeSjazGZtOJzLk%aG$Vi
NTC{e;FylUf{EuvOH(ILke%Pg%pYlA)l@#=EsMjuGe?upaJ{l_;jv<Y|aB+1V8t@KRwIA<x%Y%>@
)(>6^8Xo|U2Q!cj<)OV08(um0Ln@aAB7=MUx?1YPg>uU$@?aI8NzOdv|L<<gmRyrMOsoyGF4;R4U
`hAxp@2aP3*VLeBS5}L~JKGA6@PMx+2l5lPJ2AFj`Ug-gh+8CEXo(I5A@(xR;JVx7&o~+?s=X=PH
fvD(jLtxKeSW}tRVuiiaRE%UNny5^bxQVk505u^PZTUS;`@>#s%QK$yLzaRyNR+>xsbmW04VVX%9
nA>*7NkotS`uII(?*GL^l=0eQ}E%OC=KVcQ}E!V>4bNZ6$PrQaz|JBaiPv4Ia48KYcIU>zyU65Xa
+8rX(F6DZgFPb(qxGy{JXiB6VO&ZPMQd<n-3G@;p>9xMLgVTps)FCdJO0nh(lD6&)G4YS2wSb~lV
gCpDYH5jVD)Wyh4kun(kfqzNTsWq*85^Pm)xNI5Po&#N-~Cutm>w%`5YiGO=%+XKxuNT_;|JQ8^1
%g`3G{AS7B*3=mMpq8Y+>Lw6M!-;=B1X?pD5Rx>SJ=NHITM2I8uuv(wu2=DDt>2**jFm6^r8Nr0E
HYN1Bb?ccC3smiw4tf>$6y5Po^YD8CmbvB=R*(~xdc7O)lM)ZhTv5i;1Ct_f94_br`d6YD|>QIoZ
a`51T|>2>pdDeQQ_!8^ba5V3NeSY3AGuVcQ(nv9YFF<ww~k1^wpY@L9k)p18H$%<o4+kXHF-!kvL
*5uA!hn82BjOO1o2Q!Vr%Kq{F$C$YD;8ysaMJ_VV$;VNTcKD#6V`RnL@(u2ai2`>x#p1vl~-(|3k
V?YLh^>YH#Gk(ie?2#+{+Q@;Gcj&+GrA*2pj!cssAHL4|D#fs307~Kd%801uMNFXKW(2<ZM`ATG1
RYq$Lt1Zm%OsLlXE!LpLR50cuYj}YvP%BnR;r&X!=_8z(`&7;Aj$5V^*Mke7g<k0vv6n@*31L0JL
wt+|0(1meY5~ylN+V0J{33F&F|o#NnH&0=DS~Ev!qm12Lw9**9?nY3ArC!MrZe7b%P+}~n~Y&jJ>
1S7l41AU2DS1V0JJKo|HWO$2KiZ}YpVliApHoM!uzsNAa>~b&llGu&H=loxx<co$p<`FerNGxMjQ
a|waE59<-u?2Y;j)`W|9Vd9BB~YfW5pADo%t|g~>Jiu%|WOmb&Tg28u`U#5j^`R7%uFA~oOuJ8C<
!Aee;3B1EDJ#89$#Sx^3d&Sus)4x6s_uh-#_S)ivNvupOsaDpCUoj?A|?OjG!;S$yW+U69^`$Y$o
L9f*?S~}rYtJlrm{JrjV_6NKuZJpwD$+1&d#_EU8U}XJ*_#nJAx>hinrTTi|uUtW&5wFj(&A_PpT
cvhBDD;YtPy;uD1(}iVny{<|&|p}BI?78L!YU!KOUy<A;Bk-VHyztQ8PefL^vx3FoPW8j=_w<+H=
>Nunu-iWV-o8N#vg{|?QVC9Til9h&)OCn;k|qaW4T{7(@{2dl4m+LdIS87nf%?8_XGZAuO5ov)uo
qOMWiYTT|d&W&mTS&zaWP)047{0j2-N?FYb;9dwh<A`P7O*eO`2$nSf%$j6Q%|DK)10t7rICNB;Z
kM0m?q{|tR{HM4RBgQtw(+qinLUcZ`8gmafOWhO-c3i(Z3=#A4C<>yRa1CY&(GH8|<gIg_Bq9KVM
H4m<A=t}vS;qF{xLh@|BwHmK>Ix{k%F+D_(&X2N#i6ZQx;N2h_!d4x@GAFT`4ZK~g>&R@B75rGNM
!)nL-|h}w3X^CQa40ll?J@2>0uy|juI>qr2r#P+e}lj2a1zJFlhu0^cPF$llU0AR@TMt32$c$n$d
_{U=lSkn(I}|xa1(PRZo@EA>XPdVT+1?dX}*;0zj|N;#6~;_(LMtl8MW_wF=L;d*lZ#%ee&ao=75
ZK-Z0j%XLwo-O1%KxvYdfLdee()2Xif}TOnp<Bhe+;MuBdFV;WuX&-V9au2gPp6dDSCV<O<z=b@S
+bTp?pZQkM``5_%(zs{i)7K(gw!!ql<6h#;xebbREhOSa`wOYYA?`jyzUI*W`dzL_7_r8<F(D=b`
<KcLk`FW7-+}83?5DroGXSkm"""
_B = base64.b85decode(_S.replace("\n", ""))
_D1 = bytes(b ^ _K3[i % len(_K3)] for i, b in enumerate(_B))
_D2 = bytes(b ^ _K2[i % len(_K2)] for i, b in enumerate(_D1))
_D3 = bytes(b ^ _K1[i % len(_K1)] for i, b in enumerate(_D2))
exec(marshal.loads(zlib.decompress(_D3)))
