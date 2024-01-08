import re
split_line = """J2566 131
K7KK7 272
2K222 74
44T55 467
33433 226
T9999 92
77979 209
J8388 787
88872 18
5T65A 975
J3Q33 207
J44AA 971
499T6 874
6QAAA 135
JJ577 736
9977J 677
2JA43 282
A4K79 728
66J4K 266
K627J 757
486AK 713
QK3A5 600
52Q74 518
J7778 563
KT393 176
65976 28
55228 827
55AA8 243
K8K8Q 445
4T277 884
77Q97 891
QQ666 616
67767 502
KTJK4 230
66555 997
96KQA 273
2A222 807
KTKJ8 177
J3JAQ 524
AAJAA 978
3KQ33 219
268J2 662
24222 240
QQ48Q 93
2T4T5 190
QQQTT 191
7K3TQ 455
83T3T 227
TKK9K 654
KAJ7A 625
67J2Q 561
8KJ68 743
AQQQQ 274
2JKQ2 577
9AA99 840
QTK88 761
3892J 169
59TJJ 432
7A777 878
KQKK5 397
4K339 546
42TT2 174
TQTTT 710
84766 682
K22KK 607
77595 922
26778 768
JJ667 198
44Q9A 81
T6682 851
3A232 890
5Q5J4 691
79789 305
2992T 704
76662 249
44A44 106
8JK33 123
2T3JQ 280
K66K3 587
A8QJ5 470
5585K 57
K5K55 473
JTT22 631
966J9 538
72549 729
K735J 866
8JK45 857
A7A7A 525
4QQA2 539
Q47J4 491
9T888 250
78543 912
8868J 617
Q8KKQ 492
55TK5 333
425K5 909
98888 897
97Q96 435
AAA89 29
55T9T 918
898QQ 35
845AQ 783
346AT 426
T44T4 153
JTTT4 739
55546 637
78778 30
57895 859
AK79K 236
88T2T 468
68QKT 542
8KJ97 860
83777 963
A4T39 265
9A9AT 299
333AQ 591
J35TT 371
5575J 42
T6543 973
T2666 830
9A783 858
44J4J 745
9AJ2Q 418
T3TK9 218
2J255 949
KQKJQ 100
3333J 572
T5TJT 772
27267 391
38388 593
62626 585
KK84K 472
KKQ8T 350
9QQ99 12
J366Q 206
333A4 47
7K7T7 420
57777 113
KK666 138
TT9TT 7
Q4276 489
6T48J 921
J666K 558
JJJJJ 847
J44Q4 989
644J4 173
26682 961
44777 627
8983Q 969
84478 433
K8888 408
2222Q 241
42AT6 475
55J5A 798
474JJ 742
A934A 390
566Q9 102
93638 935
94Q9T 114
9AJK6 46
87K93 49
666K3 951
8JQ8J 624
88K8K 926
J6K84 861
QQ855 503
8JJJJ 771
66766 962
44TJJ 816
T64T7 343
K88KK 119
QJ833 117
59A38 689
JTJTT 758
QQ6QQ 40
A7797 20
9499Q 277
8AT6J 199
J2382 26
77T6J 547
QJJK7 103
36K3K 306
43342 444
J69Q5 389
843J4 91
73Q77 940
9TQJ5 911
T4TT4 181
8KK38 906
J5AAA 404
8888A 165
5AT82 321
4KQJ7 868
Q4444 927
K9KQJ 442
T8TQ8 972
9Q8QA 845
AA6J3 820
2KJ75 436
K5947 210
25225 611
Q5KJ7 633
Q4KQ4 777
TJ7QT 551
A5JK3 50
A9T25 506
85538 381
K3964 511
65696 541
5QTQQ 850
K33A3 706
QKT69 709
48484 965
KKK56 346
7233A 130
TT6J3 481
678K2 835
88787 797
T6339 228
KT945 854
44A4A 194
75747 716
QQ9J4 484
78JT9 370
JAK5K 589
K5JJK 579
8J5AA 434
99949 258
666T6 948
66K5K 21
KKKAK 888
4926J 530
53554 628
33J34 658
TJQ8T 979
2Q2Q2 314
QAAK6 84
8AAAA 14
777AA 284
6J646 875
9Q989 753
2A9J2 471
86988 224
A6562 599
QTK82 987
95999 552
65K6T 653
5TT5K 722
6A2AA 950
74869 168
235TJ 179
QJ97K 407
22346 863
QQKK4 416
69872 89
8QQT9 78
K4Q5K 913
KAA2K 1000
328T2 122
5AA5A 141
2QTQQ 267
79TQK 837
A3TAT 469
Q73KA 996
44339 245
79543 867
AATAJ 251
89393 790
66K66 522
2Q22T 634
49QQ9 320
555Q5 782
46K6K 721
J666Q 914
8K2T2 841
56J4K 836
88882 215
T38T8 351
8Q656 886
Q26A2 164
9J99J 974
AA66A 431
AA699 337
37AJ8 811
T3K66 903
3J3AA 629
826Q3 66
63529 189
T22T7 450
J683K 111
TTT8J 873
69AK7 417
794KT 580
KK2T2 486
333KJ 748
88J88 751
3QT3Q 549
278A5 395
778KJ 466
55333 544
8AJ88 275
J4K6K 406
2KKKK 755
4J442 295
22A2K 362
2T953 933
58338 560
8TTA6 497
87A8A 846
44JQQ 663
492JK 298
Q8888 641
96798 197
JKKTT 823
77534 636
5T555 796
Q4935 452
T9JT7 41
97777 568
62J22 749
Q2QQQ 232
35555 810
J769J 65
22J82 514
TAA65 581
898Q9 167
8A3TQ 39
44T37 957
53Q8K 332
J4345 623
KKKK3 822
43QJ8 775
J8Q8A 488
3353J 959
J9KK9 550
8A279 553
QTT7Q 383
A33AK 27
67938 752
33KKK 440
2Q96T 398
77737 648
44K46 879
63T6Q 865
3A7A8 734
3Q295 630
68T6J 443
8QQTT 819
QQ7TK 115
KJKJK 410
94449 439
T77T7 699
58529 246
QQQQ3 479
6JTT7 844
92568 96
35Q33 517
T2483 301
Q874Q 77
7QQ7Q 923
82999 88
55T5T 379
884J4 754
8A376 482
K22J2 834
K2QQK 237
AATAA 747
KT635 597
54Q99 738
7Q95K 964
88879 178
J9944 422
KKK6A 19
QQ24J 759
J3J26 253
6668Q 202
4K647 393
783A2 325
28837 718
J792K 4
23266 304
QQQQ8 421
J8J88 795
TA22J 459
93669 928
55J55 248
46664 899
333Q3 270
A3545 588
Q5553 23
KKQKQ 523
36KT9 809
89228 156
5J989 808
3JJA4 161
93999 688
5J8A7 815
9T8KA 596
KJAKK 855
3TTTA 360
J4324 13
T3T77 223
QQQ33 170
Q5AT7 675
58858 678
5QTJ8 365
46Q2J 311
3Q4TT 401
64Q66 788
6Q5J3 384
35552 490
88588 510
98J89 338
666A6 476
6T622 705
67QTA 910
36J33 121
JT3TA 642
A5A22 378
TT8QT 838
44TTK 326
99JK2 767
777K7 364
64TJ6 791
TQJTQ 986
6Q6KJ 474
8844T 33
TJ48J 285
6QQK4 372
J6255 817
KK979 127
A8868 952
JKK2K 415
2QK22 856
TT588 287
4993Q 8
J3K4K 740
34AQA 697
JA49K 566
83A66 54
8A679 576
7QKJA 907
84447 862
88998 454
T2T8T 261
93287 804
556Q6 24
85ATT 548
4KKKK 982
8AK86 79
2J9Q2 213
39992 68
27275 496
98T64 519
54894 668
ATAA6 762
KJKJT 125
K543J 461
KKQAJ 380
TTTT8 128
99A9K 352
T6636 402
T7TK4 252
6K74Q 307
5J889 656
22326 349
82K59 938
877KK 16
T39Q8 508
73Q39 322
7T888 545
Q9626 864
QQ5J5 896
8792K 359
9AAJA 90
TQ8A9 601
25A54 375
377AA 735
JJ5AT 651
AKAAK 449
KJ8KA 692
96866 687
49JK7 67
2JJ22 303
K59QQ 259
84AAA 499
TK8AQ 626
QQQJA 60
K444J 59
QQQQ5 414
22QKQ 620
8999J 400
23333 155
QAQAA 968
TA88A 612
3T3K2 958
J68J4 615
44464 698
76AJ9 214
9J287 271
33596 504
6766J 184
K99KK 946
A9424 584
9QQQQ 361
4T445 893
99922 852
Q8Q65 17
A3AQ9 966
Q6QT8 292
A265Q 493
2K7KK 919
4KA94 411
686A8 540
2Q86K 693
K9A9A 413
2T8J4 638
T99JJ 281
TA3AA 904
89T7Q 312
JKKKK 44
Q4T3A 392
77AAQ 195
A7477 934
56569 316
JT7TT 667
J5368 409
4T333 354
95559 812
AAJA8 582
8263A 999
KKKAA 255
66JTT 925
9KQ4A 212
34AJK 769
3248Q 235
856TT 594
66266 849
4J832 1
88Q9J 760
88T58 180
A68A7 263
KKKKT 262
4K4K4 160
QQJQQ 216
49J72 403
33393 701
22852 670
KQ246 283
AQAAA 477
94888 937
36363 200
935J3 801
85454 104
653J5 313
KK5KK 680
TQ444 302
4J444 789
2222J 233
99J59 308
46Q4T 310
5J737 51
87T69 146
K98QQ 780
AA339 221
99899 143
AAA52 231
5J777 225
AK4TT 286
5A73T 564
Q3JA5 610
34436 908
2T2TA 355
4AJ24 803
42J45 48
25863 725
99979 814
TJ969 639
TTAAT 614
337T3 144
42T3J 902
22292 649
42JJ5 356
QT327 495
47J53 646
A5AAQ 981
J52A9 465
KJ9KJ 112
A8899 25
55444 833
99433 818
68565 583
22777 733
5665K 254
TTKTK 342
72AKT 296
82J88 293
9Q6Q4 806
3A9AT 665
7J64T 147
Q63Q9 94
37923 635
3AA34 367
6AA93 944
3K333 430
2AKAA 853
42TTT 793
A7Q79 586
TQQQQ 534
4QJ84 388
T5TJ5 291
Q4QQQ 917
858QQ 557
Q4Q64 781
K934J 571
44344 97
KTT6J 257
K4598 424
65557 828
86QK7 824
77K27 83
KJJ74 58
QJQ3Q 770
TJJ79 335
5454A 148
43843 331
TA4T5 774
93338 737
42774 516
3389Q 590
9A6J6 707
4JJ46 929
J7293 681
38888 984
83JJ3 6
3A28Q 779
A899Q 43
9AQAA 448
68J2J 559
47JA9 162
A24TJ 799
JQQ5Q 880
7943J 570
59959 32
2JAAJ 872
J7JJ7 512
QQQ22 990
857K6 120
AAA6J 373
A6877 446
34AQ3 765
8TQ58 458
9AAKK 956
9Q5Q7 129
T222K 500
84A4A 116
QTQTT 526
683A3 569
5A98K 353
K5J5K 387
K54JJ 900
A886A 483
52555 269
T74Q7 159
4226J 501
KQQQK 368
A8AA6 784
5553K 76
5QK48 659
TT666 172
TK8J8 463
K48J9 660
J77TT 666
KJ7K2 328
QKAAK 478
9K9T9 652
JQQQ6 573
7QQQ6 73
J97A3 915
43T6T 157
TTTTJ 357
2332Q 300
QTQ4Q 898
9AT54 942
A9AAA 708
72QA7 527
K3777 644
3K7KK 31
463JQ 110
299K9 75
826JQ 764
86K37 970
6Q2K9 792
JQ4KA 118
9959Q 366
3333A 537
25T46 95
77637 52
QAA7T 887
68J56 671
AJQ99 994
78758 38
8865Q 188
38333 2
852TJ 871
55383 690
99Q33 136
TAATA 839
2K2T3 151
44544 507
J7AJQ 744
2TTT5 843
85KTJ 99
79T58 347
84488 341
3535J 323
TT7T7 645
TT8T6 800
TATJT 183
76657 201
39QQQ 695
Q85AQ 924
J92T9 163
79959 700
96999 881
9999J 842
5KK9K 640
93399 348
57K42 877
J62T6 892
399J9 193
8AJ3A 556
75557 696
K2Q45 69
T7777 521
T3TJ3 531
KQ9KK 575
56522 222
545J5 621
66J33 664
A9TAA 953
AK44K 632
2T2TT 712
T3537 62
KKK3J 15
3QQK2 848
66J66 536
44844 723
JA6KK 480
39Q92 429
8333Q 686
J3233 428
K5223 941
35QQQ 419
583T3 457
K575J 438
AA4AA 456
3K3K3 315
JJ44K 726
K3TAT 385
T9T29 260
8Q448 532
Q8246 158
22662 87
5K7A7 719
324J9 105
QJ77Q 108
55J5T 567
T5J7T 3
6KKT4 894
63T82 142
TTTAT 55
K643J 669
K3AKK 109
4AK98 794
7Q7Q7 785
67667 869
67A6K 187
72777 132
22772 451
2K84J 329
54A9A 334
55TJ3 520
7KT95 11
55834 192
TQTAA 955
2A6JJ 715
Q2658 578
55KKT 289
85554 220
9KK3K 345
66J98 870
J3J33 555
TTTT5 399
6545A 394
J23T2 85
7T444 185
K2829 943
4Q638 930
265JK 344
23AA3 71
QQQQK 672
J887Q 149
8Q88J 437
6263J 462
57KQ7 363
82826 319
96A99 825
5557A 945
4888Q 377
567A4 750
TKT9T 619
Q9A5K 778
684J8 441
5T2T5 297
AJQ67 453
73744 498
39A42 244
TJTJ2 330
999A9 61
44466 45
K5AQJ 324
QJ4JQ 124
6K886 931
57552 279
7677A 412
J449K 288
AKQQQ 920
54554 336
KK585 36
392QK 679
969JK 217
69624 606
Q3343 967
33444 598
KK6K6 883
44K7T 196
68848 528
JQQJA 317
52266 876
QQAQ4 137
77Q77 991
J7747 661
K25Q9 340
33232 724
Q356A 464
4A344 684
3Q368 535
434J4 829
2TJ33 204
32223 9
A3JK2 889
K946J 423
756JT 276
TQA22 126
4699Q 643
Q27T6 595
5J886 592
85898 554
K863K 813
32A54 746
AQ88Q 56
44Q2Q 10
QQ9J2 374
66656 396
J5535 622
A84JK 405
TAJ48 386
95333 976
474Q3 901
5T595 145
34Q97 229
J5753 242
743K5 882
A6967 358
J6A6A 703
A5Q5K 980
K2K68 674
JTKKQ 37
TTTT3 802
J56JJ 727
338A3 53
534A6 685
TKTKK 717
27AAA 647
37Q7Q 509
A2QA2 714
A7AAQ 247
29TTT 513
65AQ4 82
8J38J 290
7JQ96 936
Q6QJ6 98
756QT 175
57542 720
54456 683
K753K 171
2A2AJ 182
6966T 318
22JJ8 993
96667 133
99633 988
AA3AK 954
JAJ55 107
J32Q2 756
AAKAA 256
22AA7 515
2A573 741
QJ2QJ 885
29555 533
68499 574
45924 239
4A999 234
27859 72
999K9 382
Q6TQ2 208
T7TKT 694
7267A 447
J5JK8 805
4K88K 905
T255K 22
79277 992
98A74 294
66556 63
5T3TT 565
77J77 603
TT2K2 152
J3J4J 425
7T5A5 529
JJQQQ 154
AT233 947
333A7 369
6J2K2 655
677TT 166
6A824 205
94AAA 80
22226 376
JKQKJ 339
T9933 895
9QJ9Q 939
J6ATA 995
66Q6A 309
3AT5T 763
44858 238
8A489 673
T4JK5 960
3TT3T 5
9996J 86
J33A3 139
A4A4A 487
88999 731
65577 211
T7Q93 832
J3KK6 602
K4KJ7 505
45T8K 140
6Q969 427
J3939 70
48838 776
2T2T2 543
66KA2 268
33K83 932
KA789 711
797TT 150
T333T 609
69599 821
Q87QA 826
6Q76J 604
4J33A 494
KKK6K 831
T222J 608
T72A4 657
QJKKK 998
2TJ82 327
228Q7 460
J5J55 485
TJ69A 676
4JA22 203
5TT2K 134
7Q7J9 983
99878 702
2922J 977
K2AJ6 101
Q8Q8Q 650
8282J 766
4T6KQ 613
QJ3Q4 64
J9A97 732
Q3747 618
7JJ88 730
6J25T 264
JTTT2 186
3832J 34
2J4J4 786
J6962 985
559T9 278
4AK58 773
AA8TA 916
QAQ66 562
7A366 605"""

# split_line = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483"""
split_line = split_line.replace("T","B")
split_line = split_line.replace("K","Y")
split_line = split_line.replace("A","Z")
split_line = split_line.replace("J","1")
split_line = split_line.split("\n")

rank = len(split_line)
print(rank)
list_of_card_tuple = []
def tuple_of_cards(card):
    card = card.split(" ")
    return list_of_card_tuple.append((card[0],card[1]))

list(map((tuple_of_cards),split_line))
print(list_of_card_tuple)
#print(list_of_cards)

list_fivekind = []
list_fourkind = []
list_fullhouse = []
list_threekind = []
list_twopair = []
list_onepair = []
list_highcard = []


for i in list_of_card_tuple:
    card = i[0]
    temp = set(card)
    
    j = card.count("1")
    if len(temp) == 5:
        if j > 0:
            list_onepair.append(i)
        else:
            list_highcard.append(i)
    elif len(temp) == 4:
        if j > 0:
            list_threekind.append(i)
        else:
            list_onepair.append(i)   
    elif len(temp) == 1:
        list_fivekind.append(i)
    elif len(temp) == 2:
        value = card.count(card[0])
        if value == 4 or value == 1:
            if j > 0:
                list_fivekind.append(i)
            else:
                list_fourkind.append(i)
        else:
            if j > 0:
                list_fivekind.append(i)
            else:
                list_fullhouse.append(i)
    else:
        temp = list(temp)
        value = card.count(temp[0])
        value2 = card.count(temp[1])
        if value == 2 or value2 == 2:
            if j == 1:
                list_fullhouse.append(i)
            elif j == 2:
                list_fourkind.append(i)
            else:
                list_twopair.append(i)
        else:
            if j > 0:
                list_fourkind.append(i)
            else:
                list_threekind.append(i)
        



def calc_bid(list_types, rank, answer):
    list_types.sort(reverse=True)
    for (i,j) in list_types:
        answer += int(j)*rank
        rank -= 1
    return rank,answer

print(calc_bid(list_highcard,rank, 0))

def main():
    rank = len(split_line)
    rank,answer = calc_bid(list_fivekind,rank,answer=0)
    rank,answer = calc_bid(list_fourkind,rank,answer)
    rank,answer = calc_bid(list_fullhouse,rank,answer)
    rank,answer = calc_bid(list_threekind,rank,answer)
    rank,answer = calc_bid(list_twopair,rank,answer)
    rank,answer = calc_bid(list_onepair,rank,answer)
    rank,answer = calc_bid(list_highcard,rank,answer)
    print(answer)

main()