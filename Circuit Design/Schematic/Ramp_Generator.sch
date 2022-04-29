EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 3 3
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Device:R R?
U 1 1 626B4DC0
P 1150 3100
AR Path="/6259D68B/626B4DC0" Ref="R?"  Part="1" 
AR Path="/6259D68B/626B3C33/626B4DC0" Ref="R+_div1"  Part="1" 
F 0 "R+_div1" H 1220 3146 50  0000 L CNN
F 1 "1M" H 1220 3055 50  0000 L CNN
F 2 "" V 1080 3100 50  0001 C CNN
F 3 "~" H 1150 3100 50  0001 C CNN
	1    1150 3100
	1    0    0    -1  
$EndComp
Wire Wire Line
	4550 3025 4475 3025
Wire Wire Line
	4550 2925 4475 2925
Text GLabel 4550 3025 2    50   Input ~ 0
-batt
Text GLabel 4550 2925 2    50   Input ~ 0
+batt
$Comp
L LF353DRE4:LF353DRE4 OpAmp_Triang?
U 1 1 626B4DCA
P 3775 3325
AR Path="/6259D68B/626B4DCA" Ref="OpAmp_Triang?"  Part="1" 
AR Path="/6259D68B/626B3C33/626B4DCA" Ref="OpAmp_Triang"  Part="1" 
F 0 "OpAmp_Triang" H 3775 3995 50  0000 C CNN
F 1 "LF353DRE4" H 3775 3904 50  0000 C CNN
F 2 "SOIC127P599X175-8N" H 3775 3325 50  0001 L BNN
F 3 "" H 3775 3325 50  0001 L BNN
	1    3775 3325
	1    0    0    -1  
$EndComp
Text HLabel 1150 2875 1    50   Input ~ 0
Ph
Text HLabel 1750 2875 1    50   Input ~ 0
N
$Comp
L Device:R R-_div1
U 1 1 626B6B9D
P 1150 3525
F 0 "R-_div1" H 1220 3571 50  0000 L CNN
F 1 "10k" H 1220 3480 50  0000 L CNN
F 2 "" V 1080 3525 50  0001 C CNN
F 3 "~" H 1150 3525 50  0001 C CNN
	1    1150 3525
	1    0    0    -1  
$EndComp
Wire Wire Line
	1150 2950 1150 2875
Wire Wire Line
	1150 3250 1150 3325
$Comp
L power:GND #PWR?
U 1 1 626B7111
P 1150 3750
F 0 "#PWR?" H 1150 3500 50  0001 C CNN
F 1 "GND" H 1155 3577 50  0000 C CNN
F 2 "" H 1150 3750 50  0001 C CNN
F 3 "" H 1150 3750 50  0001 C CNN
	1    1150 3750
	1    0    0    -1  
$EndComp
Wire Wire Line
	1150 3675 1150 3750
$Comp
L Device:R R?
U 1 1 626BB8C0
P 1750 3100
AR Path="/6259D68B/626BB8C0" Ref="R?"  Part="1" 
AR Path="/6259D68B/626B3C33/626BB8C0" Ref="R+_div2"  Part="1" 
F 0 "R+_div2" H 1820 3146 50  0000 L CNN
F 1 "1M" H 1820 3055 50  0000 L CNN
F 2 "" V 1680 3100 50  0001 C CNN
F 3 "~" H 1750 3100 50  0001 C CNN
	1    1750 3100
	1    0    0    -1  
$EndComp
$Comp
L Device:R R-_div2
U 1 1 626BB8C7
P 1750 3525
F 0 "R-_div2" H 1820 3571 50  0000 L CNN
F 1 "10k" H 1820 3480 50  0000 L CNN
F 2 "" V 1680 3525 50  0001 C CNN
F 3 "~" H 1750 3525 50  0001 C CNN
	1    1750 3525
	1    0    0    -1  
$EndComp
Wire Wire Line
	1750 2950 1750 2875
Wire Wire Line
	1750 3250 1750 3325
$Comp
L power:GND #PWR?
U 1 1 626BB8CF
P 1750 3750
F 0 "#PWR?" H 1750 3500 50  0001 C CNN
F 1 "GND" H 1755 3577 50  0000 C CNN
F 2 "" H 1750 3750 50  0001 C CNN
F 3 "" H 1750 3750 50  0001 C CNN
	1    1750 3750
	1    0    0    -1  
$EndComp
Wire Wire Line
	1750 3675 1750 3750
Text GLabel 1800 3325 2    50   Output ~ 0
N_div
Text GLabel 1200 3325 2    50   Output ~ 0
Ph_div
Wire Wire Line
	1200 3325 1150 3325
Connection ~ 1150 3325
Wire Wire Line
	1150 3325 1150 3375
Wire Wire Line
	1800 3325 1750 3325
Connection ~ 1750 3325
Wire Wire Line
	1750 3325 1750 3375
Text GLabel 3000 3225 0    50   Input ~ 0
Ph_div
Text GLabel 3000 3325 0    50   Input ~ 0
N_div
Wire Wire Line
	3075 3225 3000 3225
Wire Wire Line
	3075 3325 3000 3325
$Comp
L power:GND #PWR?
U 1 1 626CD9F8
P 2575 3425
F 0 "#PWR?" H 2575 3175 50  0001 C CNN
F 1 "GND" H 2580 3252 50  0000 C CNN
F 2 "" H 2575 3425 50  0001 C CNN
F 3 "" H 2575 3425 50  0001 C CNN
	1    2575 3425
	1    0    0    -1  
$EndComp
Wire Wire Line
	3075 3425 2575 3425
$Comp
L Device:R R_in_triang
U 1 1 626CF1B6
P 5625 3575
F 0 "R_in_triang" V 5525 3375 50  0000 L CNN
F 1 "510" V 5625 3500 50  0000 L CNN
F 2 "" V 5555 3575 50  0001 C CNN
F 3 "~" H 5625 3575 50  0001 C CNN
	1    5625 3575
	1    0    0    -1  
$EndComp
$Comp
L Device:R R_fb_triang
U 1 1 626D0007
P 4600 3575
F 0 "R_fb_triang" V 4500 3350 50  0000 L CNN
F 1 "10k" V 4600 3500 50  0000 L CNN
F 2 "" V 4530 3575 50  0001 C CNN
F 3 "~" H 4600 3575 50  0001 C CNN
	1    4600 3575
	1    0    0    -1  
$EndComp
$Comp
L Device:C C_fb_triang
U 1 1 626D060E
P 4975 3575
F 0 "C_fb_triang" V 4825 3375 50  0000 L CNN
F 1 "8.2u" V 5125 3500 50  0000 L CNN
F 2 "" H 5013 3425 50  0001 C CNN
F 3 "~" H 4975 3575 50  0001 C CNN
	1    4975 3575
	1    0    0    -1  
$EndComp
Wire Wire Line
	4475 3325 4600 3325
Wire Wire Line
	4600 3325 4600 3425
Wire Wire Line
	4975 3325 4975 3425
Connection ~ 4600 3325
Wire Wire Line
	2925 4000 2925 3525
Wire Wire Line
	2925 3525 3075 3525
Wire Wire Line
	4975 3725 4975 4000
Connection ~ 4975 4000
Wire Wire Line
	4975 4000 4600 4000
Wire Wire Line
	4600 3725 4600 4000
Connection ~ 4600 4000
Wire Wire Line
	4600 4000 2925 4000
Wire Wire Line
	5625 3225 5625 3425
Wire Wire Line
	4475 3225 5625 3225
Wire Wire Line
	5625 3725 5625 4000
Wire Wire Line
	4975 4000 5625 4000
Text GLabel 5100 3325 2    50   Output ~ 0
triang
Wire Wire Line
	4600 3325 4975 3325
Connection ~ 4975 3325
Wire Wire Line
	4975 3325 5100 3325
$EndSCHEMATC
