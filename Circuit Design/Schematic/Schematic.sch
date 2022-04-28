EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 2
Title "MainCircuit"
Date "2022-04-15"
Rev ""
Comp "UNAL"
Comment1 "Easyrun"
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
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
Wire Wire Line
	1875 1500 2150 1500
Wire Wire Line
	2150 1500 2150 1425
Wire Wire Line
	2150 1425 2225 1425
Wire Wire Line
	1875 1600 2175 1600
Wire Wire Line
	2175 1600 2175 1625
Wire Wire Line
	2175 1625 2225 1625
Wire Wire Line
	1875 1700 2150 1700
Wire Wire Line
	2150 1700 2150 1825
Wire Wire Line
	2150 1825 2225 1825
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
NoConn ~ 1950 3000
NoConn ~ 1950 3500
NoConn ~ 1950 3100
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
Wire Wire Line
	2125 3550 2125 3400
Wire Wire Line
	2125 3400 1950 3400
Text GLabel 2175 3300 2    50   Output ~ 0
Prog_Tx
Text GLabel 2175 3200 2    50   Input ~ 0
Prog_Rx
Wire Wire Line
	2175 3200 1950 3200
Wire Wire Line
	2175 3300 1950 3300
$Comp
L RF_Module:ESP32-WROOM-32 U1
U 1 1 626B0839
P 5675 3150
F 0 "U1" H 5675 4731 50  0000 C CNN
F 1 "ESP32-WROOM-32" H 5675 4640 50  0000 C CNN
F 2 "RF_Module:ESP32-WROOM-32" H 5675 1650 50  0001 C CNN
F 3 "https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32_datasheet_en.pdf" H 5375 3200 50  0001 C CNN
	1    5675 3150
	1    0    0    -1  
$EndComp
Text GLabel 6400 2250 2    50   Input ~ 0
Prog_Tx
Wire Wire Line
	6400 2250 6275 2250
Text GLabel 6400 2050 2    50   Output ~ 0
Prog_Rx
Wire Wire Line
	6400 2050 6275 2050
Text HLabel 5800 1750 2    50   Input ~ 0
3v3
Wire Wire Line
	5675 1750 5800 1750
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
Wire Wire Line
	5675 4625 5675 4550
$Comp
L Switch:SW_DIP_x01 SW?
U 1 1 626C84CB
P 4650 1950
F 0 "SW?" H 4650 2217 50  0000 C CNN
F 1 "SW_DIP_x01" H 4650 2126 50  0000 C CNN
F 2 "" H 4650 1950 50  0001 C CNN
F 3 "~" H 4650 1950 50  0001 C CNN
	1    4650 1950
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
Wire Wire Line
	4350 1950 4350 2050
Wire Wire Line
	4950 1950 5025 1950
Text HLabel 5025 1500 2    50   Input ~ 0
3v3
$Comp
L Device:R R?
U 1 1 626D4D5A
P 5025 1750
F 0 "R?" H 5095 1796 50  0000 L CNN
F 1 "R" H 5095 1705 50  0000 L CNN
F 2 "" V 4955 1750 50  0001 C CNN
F 3 "~" H 5025 1750 50  0001 C CNN
	1    5025 1750
	1    0    0    -1  
$EndComp
Wire Wire Line
	5025 1500 5025 1600
Wire Wire Line
	5025 1900 5025 1950
Connection ~ 5025 1950
Wire Wire Line
	5025 1950 5075 1950
$EndSCHEMATC
