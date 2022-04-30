EESchema Schematic File Version 5
EELAYER 36 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 3
Title "MainCircuit"
Date "2022-04-15"
Rev ""
Comp "UNAL"
Comment1 "Easyrun"
Comment2 ""
Comment3 ""
Comment4 ""
Comment5 ""
Comment6 ""
Comment7 ""
Comment8 ""
Comment9 ""
$EndDescr
Connection ~ 5025 1950
Connection ~ 6700 3850
Connection ~ 6700 4300
NoConn ~ 1950 3000
NoConn ~ 1950 3100
NoConn ~ 1950 3500
Wire Wire Line
	1875 1500 2150 1500
Wire Wire Line
	1875 1600 2175 1600
Wire Wire Line
	1875 1700 2150 1700
Wire Wire Line
	2125 3400 1950 3400
Wire Wire Line
	2125 3550 2125 3400
Wire Wire Line
	2150 1425 2225 1425
Wire Wire Line
	2150 1500 2150 1425
Wire Wire Line
	2150 1700 2150 1825
Wire Wire Line
	2150 1825 2225 1825
Wire Wire Line
	2175 1600 2175 1625
Wire Wire Line
	2175 1625 2225 1625
Wire Wire Line
	2175 3200 1950 3200
Wire Wire Line
	2175 3300 1950 3300
Wire Wire Line
	4350 1950 4350 2050
Wire Wire Line
	4950 1950 5025 1950
Wire Wire Line
	5025 1500 5025 1600
Wire Wire Line
	5025 1900 5025 1950
Wire Wire Line
	5025 1950 5075 1950
Wire Wire Line
	5675 1750 5800 1750
Wire Wire Line
	5675 4625 5675 4550
Wire Wire Line
	6300 1825 6300 1950
Wire Wire Line
	6300 1950 6275 1950
Wire Wire Line
	6300 3850 6700 3850
Wire Wire Line
	6325 1825 6300 1825
Wire Wire Line
	6325 2650 6275 2650
Wire Wire Line
	6400 2050 6275 2050
Wire Wire Line
	6400 2250 6275 2250
Wire Wire Line
	6700 3250 6700 3850
Wire Wire Line
	6700 3850 6700 4300
Wire Wire Line
	6700 4300 7750 4300
Wire Wire Line
	6700 5300 6700 4300
Wire Wire Line
	6925 1825 7000 1825
Wire Wire Line
	6925 2650 7250 2650
Wire Wire Line
	7400 4700 7750 4700
Wire Wire Line
	7400 5700 7750 5700
Wire Wire Line
	7450 3650 7750 3650
Wire Wire Line
	7450 3850 7750 3850
Wire Wire Line
	7450 4900 7750 4900
Wire Wire Line
	7450 5900 7750 5900
Wire Wire Line
	7750 3250 6700 3250
Wire Wire Line
	7750 5300 6700 5300
Text Notes 9100 2950 0    50   ~ 0
Los pines para los lectores están en este orden:\n1. SDA (SC)\n2. SCK\n3. MOSI\n4. MISO\n5. RQ\n6. GND\n7. RST\n8. 3V3\n
Text GLabel 2175 3200 2    50   Input ~ 0
Prog_Rx
Text GLabel 2175 3300 2    50   Output ~ 0
Prog_Tx
Text GLabel 6400 2050 2    50   Output ~ 0
Prog_Rx
Text GLabel 6400 2250 2    50   Input ~ 0
Prog_Tx
Text HLabel 5025 1500 2    50   Input ~ 0
3v3
Text HLabel 5800 1750 2    50   Input ~ 0
3v3
Text HLabel 7450 3850 0    50   Input ~ 0
3v3
Text HLabel 7450 4900 0    50   Input ~ 0
3v3
Text HLabel 7450 5900 0    50   Input ~ 0
3v3
$Comp
L power:GND #PWR?
U 1 1 625ABF88
P 2125 3550
F 0 "#PWR?" H 2125 3300 50  0001 C CNN
F 1 "GND" H 2130 3377 50  0000 C CNN
F 2 "" H 2125 3550 50  0001 C CNN
F 3 "" H 2125 3550 50  0001 C CNN
	1    2125 3550
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 626CCBB2
P 4350 2050
F 0 "#PWR?" H 4350 1800 50  0001 C CNN
F 1 "GND" H 4355 1877 50  0000 C CNN
F 2 "" H 4350 2050 50  0001 C CNN
F 3 "" H 4350 2050 50  0001 C CNN
	1    4350 2050
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 626B993A
P 5675 4625
F 0 "#PWR?" H 5675 4375 50  0001 C CNN
F 1 "GND" H 5680 4452 50  0000 C CNN
F 2 "" H 5675 4625 50  0001 C CNN
F 3 "" H 5675 4625 50  0001 C CNN
	1    5675 4625
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 626D7EE3
P 7000 1825
F 0 "#PWR?" H 7000 1575 50  0001 C CNN
F 1 "GND" H 7005 1652 50  0000 C CNN
F 2 "" H 7000 1825 50  0001 C CNN
F 3 "" H 7000 1825 50  0001 C CNN
	1    7000 1825
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 626DDABC
P 7250 2650
F 0 "#PWR?" H 7250 2400 50  0001 C CNN
F 1 "GND" V 7255 2522 50  0000 R CNN
F 2 "" H 7250 2650 50  0001 C CNN
F 3 "" H 7250 2650 50  0001 C CNN
	1    7250 2650
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR?
U 1 1 00000000
P 7400 4700
F 0 "#PWR?" H 7400 4450 50  0001 C CNN
F 1 "GND" V 7405 4572 50  0000 R CNN
F 2 "" H 7400 4700 50  0001 C CNN
F 3 "" H 7400 4700 50  0001 C CNN
	1    7400 4700
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR?
U 1 1 00000000
P 7400 5700
F 0 "#PWR?" H 7400 5450 50  0001 C CNN
F 1 "GND" V 7405 5572 50  0000 R CNN
F 2 "" H 7400 5700 50  0001 C CNN
F 3 "" H 7400 5700 50  0001 C CNN
	1    7400 5700
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR?
U 1 1 00000000
P 7450 3650
F 0 "#PWR?" H 7450 3400 50  0001 C CNN
F 1 "GND" V 7455 3522 50  0000 R CNN
F 2 "" H 7450 3650 50  0001 C CNN
F 3 "" H 7450 3650 50  0001 C CNN
	1    7450 3650
	0    1    1    0   
$EndComp
$Comp
L Device:R R_up_en
U 1 1 626D4D5A
P 5025 1750
F 0 "R_up_en" H 5095 1750 50  0000 L CNN
F 1 "10k" H 5095 1705 50  0001 L CNN
F 2 "" V 4955 1750 50  0001 C CNN
F 3 "~" H 5025 1750 50  0001 C CNN
	1    5025 1750
	1    0    0    -1  
$EndComp
$Comp
L Device:R R_prog
U 1 1 626E07EA
P 6475 2650
F 0 "R_prog" V 6475 2675 50  0000 C CNN
F 1 "39" V 6359 2650 50  0001 C CNN
F 2 "" V 6405 2650 50  0001 C CNN
F 3 "~" H 6475 2650 50  0001 C CNN
	1    6475 2650
	0    1    1    0   
$EndComp
$Comp
L Connector:Conn_01x03_Male Conn_Power
U 1 1 625A3C7E
P 1675 1600
F 0 "Conn_Power" H 1783 1881 50  0000 C CNN
F 1 "Conn_01x03_Male" H 1783 1790 50  0000 C CNN
F 2 "" H 1675 1600 50  0001 C CNN
F 3 "~" H 1675 1600 50  0001 C CNN
	1    1675 1600
	1    0    0    -1  
$EndComp
$Comp
L Device:LED LED_prog
U 1 1 626D97DE
P 6775 2650
F 0 "LED_prog" H 6550 2650 50  0000 C CNN
F 1 "LED" H 6400 2600 50  0001 C CNN
F 2 "" H 6775 2650 50  0001 C CNN
F 3 "~" H 6775 2650 50  0001 C CNN
	1    6775 2650
	-1   0    0    1   
$EndComp
$Comp
L Connector_Generic:Conn_01x03 J?
U 1 1 00000000
P 9250 3550
F 0 "J?" H 9350 3600 50  0000 L CNN
F 1 "Conn_01x03" H 9350 3500 50  0000 L CNN
F 2 "" H 9250 3550 50  0001 C CNN
F 3 "~" H 9250 3550 50  0001 C CNN
	1    9250 3550
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x03 J?
U 1 1 00000000
P 9250 4100
F 0 "J?" H 9350 4150 50  0000 L CNN
F 1 "Conn_01x03" H 9350 4050 50  0000 L CNN
F 2 "" H 9250 4100 50  0001 C CNN
F 3 "~" H 9250 4100 50  0001 C CNN
	1    9250 4100
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x06_Male Conn_Prog
U 1 1 625AA319
P 1750 3200
F 0 "Conn_Prog" H 1858 3581 50  0000 C CNN
F 1 "Conn_01x06_Male" H 1858 3490 50  0000 C CNN
F 2 "" H 1750 3200 50  0001 C CNN
F 3 "~" H 1750 3200 50  0001 C CNN
	1    1750 3200
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_DIP_x01 ESP_Reset
U 1 1 626C84CB
P 4650 1950
F 0 "ESP_Reset" H 4650 2217 50  0000 C CNN
F 1 "SW_DIP_x01" H 4650 2126 50  0000 C CNN
F 2 "" H 4650 1950 50  0001 C CNN
F 3 "~" H 4650 1950 50  0001 C CNN
	1    4650 1950
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_DIP_x01 ESP_Prog_Enable
U 1 1 626D6A20
P 6625 1825
F 0 "ESP_Prog_Enable" H 6625 2092 50  0000 C CNN
F 1 "SW_DIP_x01" H 6625 2001 50  0000 C CNN
F 2 "" H 6625 1825 50  0001 C CNN
F 3 "~" H 6625 1825 50  0001 C CNN
	1    6625 1825
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x08 J_Lector_1
U 1 1 00000000
P 7950 3450
F 0 "J_Lector_1" H 8050 3450 50  0000 L CNN
F 1 "Conn_01x08" H 8050 3350 50  0000 L CNN
F 2 "" H 7950 3450 50  0001 C CNN
F 3 "~" H 7950 3450 50  0001 C CNN
	1    7950 3450
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x08 J_Lector_2
U 1 1 00000000
P 7950 4500
F 0 "J_Lector_2" H 8050 4500 50  0000 L CNN
F 1 "Conn_01x08" H 8050 4400 50  0000 L CNN
F 2 "" H 7950 4500 50  0001 C CNN
F 3 "~" H 7950 4500 50  0001 C CNN
	1    7950 4500
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x08 J_Lector_3
U 1 1 00000000
P 7950 5500
F 0 "J_Lector_3" H 8050 5500 50  0000 L CNN
F 1 "Conn_01x08" H 8050 5400 50  0000 L CNN
F 2 "" H 7950 5500 50  0001 C CNN
F 3 "~" H 7950 5500 50  0001 C CNN
	1    7950 5500
	1    0    0    -1  
$EndComp
$Comp
L RF_Module:ESP32-WROOM-32 U1
U 1 1 626B0839
P 5675 3150
F 0 "U1" H 5475 3675 50  0000 C CNN
F 1 "ESP32-WROOM-32" H 5575 3500 50  0000 C CNN
F 2 "RF_Module:ESP32-WROOM-32" H 5675 1650 50  0001 C CNN
F 3 "https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32_datasheet_en.pdf" H 5375 3200 50  0001 C CNN
	1    5675 3150
	1    0    0    -1  
$EndComp
$Sheet
S 2225 1225 775  775 
U 6259D68B
F0 "PowerModule" 50
F1 "PowerModule.sch" 50
F2 "3v3" O R 3000 1750 50 
F3 "5v0" O R 3000 1475 50 
F4 "Ph" I L 2225 1425 50 
F5 "N" I L 2225 1625 50 
F6 "R_Gnd" I L 2225 1825 50 
$EndSheet
$EndSCHEMATC
