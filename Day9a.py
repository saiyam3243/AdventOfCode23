
from functools import reduce


a = "18 38 67 109 184 355 767 1698 3622 7284 13787 24691 42124 68905 108679 166064 246810 357970 508083 707369 967936"
a = "14 14 10 -1 -22 -56 -106 -175 -266 -382 -526 -701 -910 -1156 -1442 -1771 -2146 -2570 -3046 -3577 -4166"
a = a.split()
a = list(map(int, a))
b = []
# for i in range(len(a)-1):
#     b.append(a[i+1] - a[i])
# c = []
# for i in range(len(b)-1):
#     c.append(b[i+1] - b[i])
# d = []
# for i in range(len(c)-1):
#     d.append(c[i+1] - c[i])
# print(c)
# print(d)
# list_last_elements = []
# while True:
#     for i in range(len(a)-1):
#         b.append(a[i+1] - a[i])
#     a = b.copy()
#     list_last_elements.append(a[-1])
#     b.clear()
#     if len(set(a)) == 1:
#         break
# print(list_last_elements)
# print(a)
# print(reduce(lambda x, y: x+y, list_last_elements))

split_lines = """18 38 67 109 184 355 767 1698 3622 7284 13787 24691 42124 68905 108679 166064 246810 357970 508083 707369 967936
7 1 -5 0 28 99 260 616 1373 2893 5761 10864 19482 33391 54978 87368 134563 201593 294679 421408 590920
10 9 2 -15 -46 -95 -166 -263 -390 -551 -750 -991 -1278 -1615 -2006 -2455 -2966 -3543 -4190 -4911 -5710
20 32 46 66 96 140 202 286 396 536 710 922 1176 1476 1826 2230 2692 3216 3806 4466 5200
-1 -2 -2 15 92 314 825 1846 3693 6794 11704 19117 29874 44966 65531 92844 128299 173382 229634 298603 381784
12 13 27 74 186 417 862 1691 3222 6087 11587 22386 43760 85695 166218 316447 587960 1063209 1869843 3199954 5335422
2 13 39 92 189 343 563 876 1398 2507 5206 11812 27200 61078 132444 279062 578616 1196207 2488643 5225686 11042357
17 21 25 29 33 37 41 45 49 53 57 61 65 69 73 77 81 85 89 93 97
0 15 52 126 256 465 780 1232 1856 2691 3780 5170 6912 9061 11676 14820 18560 22967 28116 34086 40960
-1 -1 -2 7 44 143 374 876 1921 4051 8362 17058 34491 69099 137060 269273 524754 1016242 1958841 3762132 7204913
9 18 34 74 169 375 807 1705 3534 7119 13832 25892 46927 83119 145614 255675 455820 834043 1576527 3081961 6207774
-1 3 11 23 39 59 83 111 143 179 219 263 311 363 419 479 543 611 683 759 839
24 48 86 149 273 527 1011 1848 3179 5180 8146 12741 20620 35852 68051 139121 297498 647452 1407478 3022601 6372667
-9 -2 12 38 88 190 415 924 2029 4259 8439 15848 28648 51003 91674 169428 323387 631524 1241950 2423498 4644472
14 14 10 -1 -22 -56 -106 -175 -266 -382 -526 -701 -910 -1156 -1442 -1771 -2146 -2570 -3046 -3577 -4166
-3 -3 -8 -15 -9 51 270 897 2475 6120 14066 30770 65140 134867 274479 549784 1083364 2100078 4011315 7579078 14250852
20 37 66 107 160 225 302 391 492 605 730 867 1016 1177 1350 1535 1732 1941 2162 2395 2640
18 23 25 32 71 211 611 1609 3867 8581 17752 34488 63270 110102 182588 290504 448913 689368 1092188 1867509 3540350
10 37 79 134 192 227 200 85 -73 -63 632 3059 9239 23188 53297 117585 254504 543721 1143797 2357112 4736946
19 28 51 105 218 434 822 1505 2737 5066 9643 18802 37193 74068 147894 295427 588889 1167081 2289039 4421338 8369642
14 25 49 99 191 340 567 926 1552 2715 4845 8476 14059 21651 30674 40420 53152 84499 192726 554776 1654431
2 5 8 7 4 17 107 444 1446 4054 10267 24182 54016 116022 242018 493737 989930 1957059 3823050 7388361 14133212
-3 -7 0 45 171 447 988 1987 3768 6891 12398 22425 41702 81076 165390 350270 756279 1635465 3495924 7326473 14988333
19 42 75 134 246 458 856 1597 2971 5541 10469 20255 40367 82787 173686 369952 794398 1709403 3667214 7808107 16434187
16 33 65 112 174 251 343 450 572 709 861 1028 1210 1407 1619 1846 2088 2345 2617 2904 3206
9 21 29 35 42 55 91 200 494 1174 2535 4926 8680 14189 22752 39904 85251 217439 591485 1580961 4023442
5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 105
5 -2 -10 -19 -31 -42 -12 215 1087 3685 10326 25558 57715 121243 240056 452234 816433 1420440 2392374 3915107 6244557
10 32 66 114 186 322 640 1418 3225 7145 15199 31173 62215 121781 234799 446291 835156 1535382 2767632 4884948 8437248
2 11 34 77 150 275 506 980 2030 4406 9668 20836 43406 86868 166892 308381 549626 947837 1586366 2583983 4106614
10 30 57 88 123 171 256 423 744 1324 2307 3882 6289 9825 14850 21793 31158 43530 59581 80076 105879
10 9 16 55 161 380 772 1417 2424 3943 6180 9415 14023 20498 29480 41785 58438 80709 110152 148647 198445
16 27 47 72 100 147 283 711 1930 5044 12307 28041 60151 122626 239736 453276 835496 1512897 2710915 4838366 8646034
14 28 38 46 71 162 413 980 2100 4112 7480 12818 20917 32774 49623 72968 104618 146724 201818 272854 363251
10 26 44 63 81 95 101 94 68 16 -70 -199 -381 -627 -949 -1360 -1874 -2506 -3272 -4189 -5275
8 30 59 92 126 158 185 204 212 206 183 140 74 -18 -139 -292 -480 -706 -973 -1284 -1642
11 20 40 86 182 362 671 1166 1917 3008 4538 6622 9392 12998 17609 23414 30623 39468 50204 63110 78490
16 20 22 33 75 181 395 772 1378 2290 3596 5395 7797 10923 14905 19886 26020 33472 42418 53045 65551
12 26 40 54 68 82 96 110 124 138 152 166 180 194 208 222 236 250 264 278 292
10 9 3 -11 -27 -15 115 586 1895 5094 12359 28118 61207 128858 263914 527717 1032948 1983791 3745823 6965923 12774469
3 11 24 51 108 231 509 1147 2583 5710 12302 25834 53061 107036 212755 417332 807452 1537611 2873008 5250748 9363097
-7 -12 -5 28 101 228 423 700 1073 1556 2163 2908 3805 4868 6111 7548 9193 11060 13163 15516 18133
10 14 17 33 88 220 479 927 1638 2698 4205 6269 9012 12568 17083 22715 29634 38022 48073 59993 74000
12 26 55 106 195 356 650 1184 2168 4059 7868 15745 32032 65152 131121 260369 511320 997436 1940253 3771284 7324165
7 11 30 75 159 301 541 987 1925 4035 8770 18971 39809 80165 154581 285939 509051 875371 1459070 2364747 3737083
-4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
6 20 48 90 146 216 300 398 510 636 776 930 1098 1280 1476 1686 1910 2148 2400 2666 2946
-4 -7 -12 -17 -18 -9 18 73 168 317 536 843 1258 1803 2502 3381 4468 5793 7388 9287 11526
9 26 47 74 119 213 420 864 1781 3621 7272 14602 29797 62571 135536 300376 671857 1496536 3286449 7070194 14849115
8 13 37 104 247 508 938 1597 2554 3887 5683 8038 11057 14854 19552 25283 32188 40417 50129 61492 74683
-2 3 25 79 199 454 972 1974 3825 7118 12826 22613 39559 69973 127900 245775 498018 1050003 2253897 4827005 10170057
16 21 33 67 147 311 620 1184 2226 4213 8091 15669 30205 57255 105854 190106 331268 560421 921829 1477095 2310231
-7 -2 16 46 81 113 153 274 685 1844 4618 10498 21877 42399 77387 134358 223633 359050 558788 846310 1251433
10 30 62 113 197 341 591 1018 1724 2848 4572 7127 10799 15935 22949 32328 44638 60530 80746 106125 137609
2 15 46 114 249 492 898 1553 2634 4581 8529 17293 37464 83665 186932 410909 882860 1853053 3809290 7700094 15373333
16 19 35 88 215 466 904 1605 2658 4165 6241 9014 12625 17228 22990 30091 38724 49095 61423 75940 92891
-6 -10 -14 -18 -22 -26 -30 -34 -38 -42 -46 -50 -54 -58 -62 -66 -70 -74 -78 -82 -86
12 38 88 174 308 502 768 1118 1564 2118 2792 3598 4548 5654 6928 8382 10028 11878 13944 16238 18772
13 26 44 76 139 273 576 1274 2861 6373 13907 29594 61466 125205 252005 505428 1017433 2063728 4216366 8641688 17660849
9 9 7 3 -3 -11 -21 -33 -47 -63 -81 -101 -123 -147 -173 -201 -231 -263 -297 -333 -371
27 53 105 198 364 681 1315 2575 4995 9482 17611 32236 58798 108206 203230 392479 780188 1588126 3281998 6827145 14203997
9 22 56 126 255 489 921 1719 3163 5720 10236 18433 34138 66174 134853 285979 620071 1351903 2929923 6273448 13240457
16 33 71 144 284 565 1135 2257 4374 8242 15234 28028 52077 98556 189977 370574 725367 1415470 2744428 5284011 10112441
12 36 72 116 170 254 421 775 1492 2844 5226 9186 15458 24998 39023 59053 86956 124996 175884 242832 329610
-3 5 27 78 200 482 1083 2269 4490 8538 15842 28971 52431 93857 165716 287652 489619 815963 1330629 2123684 3319362
11 21 46 111 257 552 1113 2144 3995 7247 12828 22165 37377 61514 98847 155214 238427 358745 529418 767307 1093585
26 48 86 153 281 534 1020 1902 3408 5840 9582 15107 22983 33878 48564 67920 92934 124704 164438 213453 273173
17 23 36 64 106 150 176 164 108 40 75 502 1975 5932 15588 38482 93251 227409 562026 1397980 3454736
6 2 -3 -13 -31 -45 1 261 1094 3285 8489 20070 44585 94256 190881 371758 698334 1268444 2233173 3819557 6360537
26 55 97 162 268 440 722 1207 2097 3834 7404 15019 31537 67197 142535 296718 600996 1179537 2240587 4121696 7353682
6 12 30 67 133 241 407 650 992 1458 2076 2877 3895 5167 6733 8636 10922 13640 16842 20583 24921
11 32 64 121 243 512 1070 2137 4035 7237 12471 20920 34594 57076 95221 163387 294246 566017 1168977 2562142 5829004
6 10 27 67 145 288 540 963 1631 2609 3898 5307 6187 4961 -1485 -17952 -48504 -85702 -77763 156357 1125665
-8 -7 14 84 254 600 1221 2231 3744 5851 8588 11894 15558 19154 21963 22881 20312 12045 -4886 -34360 -81346
-2 4 29 96 251 570 1172 2257 4195 7703 14168 26211 48646 90075 165481 300342 536996 944246 1631511 2769210 4617517
-1 5 16 41 108 282 700 1627 3537 7223 13940 25585 44918 75828 123648 195523 300835 451689 663464 955433 1351456
14 33 72 141 250 409 628 917 1286 1745 2304 2973 3762 4681 5740 6949 8318 9857 11576 13485 15594
16 14 21 60 166 399 867 1759 3388 6244 11057 18870 31122 49741 77247 116865 172648 249610 353869 492800 675198
-9 -8 11 60 145 259 378 477 596 1002 2519 7151 19249 47791 111139 247539 538929 1164780 2521143 5475354 11891237
8 2 2 19 64 148 282 477 744 1094 1538 2087 2752 3544 4474 5553 6792 8202 9794 11579 13568
11 38 88 172 318 584 1075 1984 3696 7032 13792 27923 57948 121831 256376 534886 1099813 2222846 4415788 8635986 16667142
5 16 34 58 103 223 539 1281 2879 6174 12869 26420 53717 108187 215448 423453 820289 1564532 2935372 5412630 9800235
15 37 72 120 181 255 342 442 555 681 820 972 1137 1315 1506 1710 1927 2157 2400 2656 2925
20 37 78 155 292 540 1001 1866 3477 6450 11969 22525 43716 88399 185742 399929 866926 1863473 3931132 8090733 16199912
11 33 72 146 288 546 983 1677 2721 4223 6306 9108 12782 17496 23433 30791 39783 50637 63596 78918 96876
2 9 28 65 126 219 355 560 939 1875 4504 11689 29846 72215 164652 355992 736916 1474701 2877208 5509337 10400818
8 21 46 101 231 519 1091 2125 3884 6807 11713 20196 35303 62597 111793 199583 355660 637525 1167496 2220671 4420067
24 44 73 123 224 432 845 1631 3072 5628 10025 17371 29304 48176 77277 121103 185672 278892 410985 594971 847216
18 39 80 160 309 570 995 1631 2506 3662 5364 8778 17715 42573 108530 271640 649338 1477097 3212716 6727728 13658113
3 1 -4 -6 2 34 132 420 1218 3249 7972 18061 38013 74792 138282 241107 397053 616865 899556 1216516 1484604
11 30 70 160 341 679 1289 2364 4199 7204 11927 19176 30468 49305 84307 156250 312951 659322 1415688 3026920 6359843
10 25 53 107 213 420 813 1537 2865 5376 10353 20583 41884 85987 176034 357241 717879 1431084 2839328 5627696 11184166
20 30 40 50 60 70 80 90 100 110 120 130 140 150 160 170 180 190 200 210 220
-2 1 16 61 158 327 581 929 1397 2080 3241 5476 9967 18848 35712 66290 119336 207755 350014 571879 908524
29 56 92 133 175 214 246 267 273 260 224 161 67 -62 -230 -441 -699 -1008 -1372 -1795 -2281
14 33 60 109 216 447 902 1715 3050 5093 8040 12081 17380 24051 32130 41543 52070 63305 74612 85077 93456
-1 3 22 68 158 325 645 1289 2610 5286 10577 20840 40609 78811 153054 297327 574704 1096313 2046073 3706006 6466767
25 46 86 159 276 446 687 1058 1727 3106 6133 12897 28036 61773 136243 298209 644000 1367849 2855463 5865990 11887947
-6 -11 -16 -21 -26 -31 -36 -41 -46 -51 -56 -61 -66 -71 -76 -81 -86 -91 -96 -101 -106
3 -2 -6 12 95 318 801 1725 3351 6042 10288 16734 26211 39770 58719 84663 119547 165702 225894 303376 401943
20 38 74 142 269 501 903 1552 2522 3860 5552 7478 9355 10667 10581 7848 688 -13342 -37498 -76018 -134311
11 22 36 68 154 364 823 1747 3518 6849 13121 25010 47583 90179 169698 316547 585653 1076944 1972906 3605736 6573832
1 7 13 19 25 31 37 43 49 55 61 67 73 79 85 91 97 103 109 115 121
2 10 33 83 182 374 742 1428 2654 4742 8131 13389 21218 32450 48032 68998 96426 131378 174821 227527 289950
20 39 74 137 250 445 764 1259 1992 3035 4470 6389 8894 12097 16120 21095 27164 34479 43202 53505 65570
2 9 25 50 84 127 179 240 310 389 477 574 680 795 919 1052 1194 1345 1505 1674 1852
-5 1 16 54 155 404 969 2172 4608 9338 18217 34497 63994 117359 214384 391849 717225 1311647 2387022 4304008 7659965
17 25 33 38 45 80 201 514 1218 2729 5971 12975 27998 59466 123161 247215 479647 899385 1631957 2871316 4909587
18 30 42 54 66 78 90 102 114 126 138 150 162 174 186 198 210 222 234 246 258
16 41 85 155 258 401 591 835 1140 1513 1961 2491 3110 3825 4643 5571 6616 7785 9085 10523 12106
26 37 54 85 141 241 429 813 1633 3363 6856 13556 25832 47541 85005 148696 256068 436161 736834 1235767 2056711
14 20 21 17 8 -6 -25 -49 -78 -112 -151 -195 -244 -298 -357 -421 -490 -564 -643 -727 -816
14 25 40 53 53 36 40 221 1002 3345 9218 22355 49437 101856 198262 368135 656670 1131313 1890340 3073929 4878237
10 7 8 29 94 237 511 1007 1893 3502 6533 12494 24653 50072 103979 219129 465456 990022 2095254 4386920 9046876
21 42 86 165 291 476 732 1071 1505 2046 2706 3497 4431 5520 6776 8211 9837 11666 13710 15981 18491
21 46 87 143 222 360 649 1274 2551 4955 9133 15920 26449 42661 69084 118068 223478 473442 1083274 2548681 5952613
16 36 70 117 182 288 489 894 1723 3427 6915 13942 27723 53849 101592 185697 328770 564382 941020 1527027 2416684
18 31 56 103 182 303 476 711 1018 1407 1888 2471 3166 3983 4932 6023 7266 8671 10248 12007 13958
18 34 60 108 200 381 746 1485 2950 5746 10858 19881 35576 63315 114616 215054 420554 848658 1735088 3531130 7064424
7 1 0 14 51 129 303 705 1602 3504 7409 15361 31624 64939 132516 266576 524338 1002342 1856195 3328275 5791334
-5 -7 -8 -8 -7 -5 -2 2 7 13 20 28 37 47 58 70 83 97 112 128 145
13 34 63 100 145 198 259 328 405 490 583 684 793 910 1035 1168 1309 1458 1615 1780 1953
23 36 63 118 215 381 687 1307 2631 5482 11517 23923 48543 95591 182210 336521 605039 1068456 1877703 3336024 6078383
4 15 38 76 142 275 579 1307 3032 6979 15642 33892 70916 143541 281849 538633 1005571 1841886 3327493 5965491 10683981
20 40 65 101 179 368 792 1662 3342 6492 12394 23715 46283 93106 193109 409298 874864 1861928 3907303 8034265 16130755
-6 -6 -10 -23 -50 -96 -166 -265 -398 -570 -786 -1051 -1370 -1748 -2190 -2701 -3286 -3950 -4698 -5535 -6466
16 36 61 105 205 433 913 1853 3608 6798 12521 22728 40872 73043 130082 231956 417692 768824 1464161 2903083 5970539
-2 8 32 90 213 452 902 1744 3305 6131 11074 19434 33299 56414 96191 167819 301764 556102 1034832 1912158 3460117
13 24 46 100 209 394 670 1057 1635 2695 5084 10936 25167 58477 133332 295892 639929 1355066 2824234 5819656 11892637
-2 6 33 102 258 578 1179 2224 3926 6550 10413 15882 23370 33330 46247 62628 82990 107846 137689 172974 214098
7 10 30 84 193 377 663 1132 2043 4084 8812 19356 41469 85027 166085 309612 553039 950766 1579786 2546596 3995577
3 10 29 80 193 421 883 1852 3903 8136 16489 32156 60125 107851 186079 309832 499579 782598 1194549 1781272 2600825
1 -3 -2 20 91 259 617 1369 2976 6443 13846 29261 60344 120896 234759 441187 801179 1402773 2360430 3798614 5801457
8 6 7 24 79 203 436 827 1434 2324 3573 5266 7497 10369 13994 18493 23996 30642 38579 47964 58963
10 22 57 125 236 400 627 927 1310 1786 2365 3057 3872 4820 5911 7155 8562 10142 11905 13861 16020
20 42 82 146 248 420 731 1337 2608 5410 11671 25455 54947 116078 239103 480508 944627 1823254 3469238 6535165 12237391
11 11 16 36 102 293 792 1985 4623 10094 20911 41619 80456 152254 283218 518404 933138 1650942 2874449 4946091 8479901
13 18 33 70 136 240 405 695 1295 2738 6472 16133 40214 97471 227748 513630 1123720 2398645 5020050 10337495 20989375
-5 4 24 52 96 184 369 727 1346 2320 3808 6308 11442 23777 54606 129413 302463 685622 1506034 3222034 6754390
5 20 47 86 137 200 275 362 461 572 695 830 977 1136 1307 1490 1685 1892 2111 2342 2585
24 49 99 195 369 664 1134 1844 2870 4299 6229 8769 12039 16170 21304 27594 35204 44309 55095 67759 82509
12 19 37 64 106 189 374 791 1731 3878 8835 20208 45669 100632 214454 440425 871246 1662221 3065017 5475584 9500684
9 34 79 160 314 623 1248 2467 4703 8517 14530 23241 34763 48680 64652 85220 123673 222012 487101 1157014 2714108
15 30 45 60 75 90 105 120 135 150 165 180 195 210 225 240 255 270 285 300 315
5 15 44 110 253 552 1147 2265 4251 7613 13116 22026 36757 62516 111301 211254 427809 909947 1988012 4373634 9554773
13 9 2 -4 12 111 431 1250 3091 6887 14224 27678 51258 90961 155437 256752 411225 640301 971406 1438712 2083720
27 40 57 79 119 223 500 1176 2699 5934 12499 25305 49375 93029 169534 299330 512955 854804 1387869 2199619 3409191
13 23 34 53 103 232 526 1142 2383 4853 9780 19721 40132 82797 173001 363787 762893 1581319 3217290 6396097 12395433
8 4 7 32 106 267 563 1050 1796 2917 4714 8074 15487 33383 77111 180919 416972 930078 1998813 4139728 8280052
15 20 25 29 49 148 483 1380 3451 7786 16293 32338 61983 116402 216650 403270 756055 1435104 2765597 5409391 10702549
-6 6 27 57 109 227 522 1238 2866 6328 13266 26519 51009 95602 177298 330776 629642 1231950 2473625 5052189 10373797
-3 -2 -3 3 38 149 436 1098 2510 5374 11038 22151 43924 86403 168329 323352 609601 1124088 2024885 3568501 6182104
13 24 56 132 290 586 1104 1980 3439 5829 9621 15346 23486 34463 49125 70568 108825 190974 380654 812928 1753002
17 28 43 62 83 102 113 108 77 8 -113 -302 -577 -958 -1467 -2128 -2967 -4012 -5293 -6842 -8693
11 31 55 86 148 303 674 1487 3155 6432 12675 24305 45734 85460 160932 309442 611099 1234381 2521471 5140328 10344144
-6 0 12 26 38 44 40 22 -14 -72 -156 -270 -418 -604 -832 -1106 -1430 -1808 -2244 -2742 -3306
4 4 7 29 103 294 732 1683 3691 7837 16174 32410 62924 118213 214881 378294 646038 1072330 1733545 2735035 4219429
14 35 83 185 385 747 1355 2318 3803 6137 10040 17075 30428 56161 105114 195668 357620 637463 1105409 1864541 3062531
18 32 46 60 74 88 102 116 130 144 158 172 186 200 214 228 242 256 270 284 298
-7 -13 -23 -38 -59 -87 -123 -168 -223 -289 -367 -458 -563 -683 -819 -972 -1143 -1333 -1543 -1774 -2027
9 8 7 10 30 97 288 794 2051 4998 11604 25959 56499 120402 251948 517810 1044001 2061752 3983193 7522660 13886120
26 43 61 73 67 29 -52 -182 -372 -679 -1312 -2851 -6621 -15194 -32772 -64653 -113732 -169311 -178015 24099 859185
-6 -11 -12 -4 10 9 -46 -190 -394 -442 297 3292 11700 32245 79586 186469 426693 965345 2165463 4809616 10553881
22 48 100 197 374 707 1357 2637 5106 9694 17862 31801 54674 90905 146519 229537 350430 522636 763144 1093149 1538782
19 39 84 176 361 736 1500 3055 6200 12481 24783 48276 91856 170254 307021 538635 920017 1531787 2489638 3956256 6156267
7 16 25 34 43 52 61 70 79 88 97 106 115 124 133 142 151 160 169 178 187
9 21 36 55 77 99 116 121 105 57 -36 -189 -419 -745 -1188 -1771 -2519 -3459 -4620 -6033 -7731
19 44 96 184 318 512 791 1220 1986 3584 7204 15535 34482 76883 170466 374420 812761 1739272 3659940 7557174 15289610
15 19 27 55 129 284 563 1016 1699 2673 4003 5757 8005 10818 14267 18422 23351 29119 35787 43411 52041
13 36 87 189 385 748 1403 2571 4643 8290 14613 25335 43035 71422 115645 182633 281457 423704 623851 899625 1272333
16 42 91 173 311 555 1000 1810 3250 5728 9849 16483 26849 42617 66030 100048 148516 216358 309799 436617 606427
11 16 30 75 197 478 1051 2115 3951 6951 11690 19096 30805 49827 81695 136322 230851 393850 671278 1134729 1892549
14 28 53 105 223 481 1011 2053 4061 7929 15471 30411 60336 120375 239879 474323 926592 1785966 3401881 6427277 12100501
3 15 49 119 238 421 688 1062 1567 2248 3261 5129 9361 19849 45921 108883 255792 587924 1318562 2888478 6193977
26 36 56 114 249 511 969 1745 3109 5695 10949 22042 45762 96502 204688 434398 919503 1936098 4043952 8355067 17028216
15 28 46 85 178 385 822 1732 3642 7689 16261 34203 71025 144900 289889 568978 1097441 2084130 3903024 7214353 13164596
6 -2 -1 34 151 432 1004 2050 3820 6642 10933 17210 26101 38356 54858 76634 104866 140902 186267 242674 312035
11 9 20 54 130 292 634 1333 2693 5215 9728 17644 31436 55482 97470 170619 297039 512629 873996 1467970 2424390
12 16 24 48 116 281 651 1451 3132 6568 13451 27129 54360 108826 217884 435197 864140 1701236 3317090 6407154 12270444
27 38 44 53 88 200 493 1162 2557 5313 10628 20828 40430 78001 149213 281611 521743 945448 1672260 2885063 4856324
24 37 50 63 76 89 102 115 128 141 154 167 180 193 206 219 232 245 258 271 284
15 28 53 93 152 239 372 582 917 1446 2263 3491 5286 7841 11390 16212 22635 31040 41865 55609 72836
19 34 57 91 143 243 475 1020 2211 4600 9037 16761 29503 49601 80127 125026 189267 279006 401761 566599 784335
11 29 69 146 278 486 794 1229 1821 2603 3611 4884 6464 8396 10728 13511 16799 20649 25121 30278 36186
13 26 38 49 53 36 -22 -126 -197 88 1604 6305 18055 43862 95628 192542 364257 655006 1128826 1876073 3021425
5 14 24 39 80 211 577 1460 3366 7173 14404 27743 51988 95755 174504 316109 571807 1039028 1910236 3576603 6841876
10 25 52 107 228 484 979 1862 3378 6028 10953 20728 40862 82469 166828 332917 649522 1234227 2282530 4111553 7224376
7 16 33 66 122 204 311 444 612 824 1049 1135 730 -575 -2159 1661 33636 165397 595608 1831797 5095949
14 34 56 74 79 59 -1 -119 -316 -616 -1046 -1636 -2419 -3431 -4711 -6301 -8246 -10594 -13396 -16706 -20581
6 15 44 114 269 586 1185 2239 3984 6729 10866 16880 25359 37004 52639 73221 99850 133779 176424 229374 294401
3 13 44 125 312 700 1435 2726 4857 8199 13222 20507 30758 44814 63661 88444 120479 161265 212496 276073 354116
17 36 71 136 253 447 742 1159 1717 2438 3357 4538 6097 8233 11268 15697 22249 31960 46259 67068 96917
17 33 63 124 252 522 1085 2229 4485 8840 17195 33331 64851 126910 249126 488031 948981 1823879 3454739 6438490 11796050
14 32 73 141 236 354 487 623 746 836 869 817 648 326 -189 -941 -1978 -3352 -5119 -7339 -10076
-6 -11 -14 2 76 286 788 1892 4190 8757 17464 33477 62074 112002 197732 343173 587706 995837 1672398 2786116 4605608
17 28 44 70 120 222 426 832 1668 3464 7392 15876 33621 69283 138176 266899 502094 928936 1713089 3198344 6132145
13 11 10 15 37 98 241 553 1220 2657 5804 12765 28111 61413 132021 278002 573032 1159057 2311077 4568183 9000938
9 16 20 21 19 14 6 -5 -19 -36 -56 -79 -105 -134 -166 -201 -239 -280 -324 -371 -421
15 31 68 146 305 628 1282 2591 5163 10101 19336 36128 65789 116690 201622 339589 558119 896187 1407852 2166718 3271337
11 19 50 116 228 410 740 1441 3058 6779 15003 32355 67561 137062 272240 534180 1044012 2045045 4029096 7991715 15945731"""

# split_lines = """0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45"""

split_lines = split_lines.splitlines()

def calc_oasis():
    answer = 0
    for line in split_lines:
        list_last_elements = []
        a = line.split()
        a = list(map(int, a))
        b = []
        while True:
            for i in range(len(a)-1):
                b.append(a[i+1] - a[i])
            
            list_last_elements.append(a[-1])
            a = b.copy()
            b.clear()
            if len(set(a)) == 1:
                if set(a) != {0}:
                    list_last_elements.append(a[-1])
                break
        print(list_last_elements)
        #print(a)
        answer += sum(list_last_elements)
    print(answer)
    return answer

calc_oasis()