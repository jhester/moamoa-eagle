#!/usr/bin/env python

# quick script for MIC841 calculations
# by Josiah Hester
# 9/22/2019

import sys
import argparse
from argparse import RawTextHelpFormatter

#R1= 698000.0
#R2= 619000.0
#R3= 681000.0
#target_total=2000000
#vin_hi = 3.6
#vin_low = 1.91

#hi=3.64705882353 lo=3.13131313131
#R1 = 604000.0
#R2 = 56000.0
#R3 = 340000.0

def calculate_thresholds(r1_0,r2_0,r3_0):
	vin_hi_calc = 1.24 * ((r1_0+r2_0+r3_0)/r3_0)
	vin_lo_calc = 1.24 * ((r1_0+r2_0+r3_0) / (r2_0+r3_0))
	print("Vin_hi=%f, Vin_lo=%f" %(vin_hi_calc, vin_lo_calc))
	

def calculate_resistors(vin_hi, vin_low, target_total):
	r3=(1.24 * target_total) / vin_hi
	r2=(1.24 * target_total) / vin_low - r3
	r1 = target_total - r2 - r3
	print("R1=%d, R2=%d, R3=%d" %(r1, r2, r3))
	return [r1, r2, r3]

parser = argparse.ArgumentParser(
    description='''
    This program helps set resistors and voltages with the MIC841. 
    
    Example usage:

    Calculate the thresholds
    >  ./mic841.py thresh -r1=698000 -r2=619000 -r3=681000
        Vin_hi=3.638062, Vin_lo=1.905785
    >  ./mic841.py res -vh=3.6 -vl=1.9 -rtotal=2000000
        R1=694736, R2=616374, R3=688888
''',
formatter_class=RawTextHelpFormatter
)
parser.add_argument("action", help="calculate actual voltage thresholds by supplying R1,R2,R3, specify `thresh` or `res`", action="store")
parser.add_argument("-r1", help="specify R1 value for calculating Voltage thresholds", type=float)
parser.add_argument("-r2", help="specify R2 value for calculating Voltage thresholds", type=float)
parser.add_argument("-r3", help="specify R3 value for calculating Voltage thresholds", type=float)
parser.add_argument("-vh", help="specify Vin_hi value for calculating resistors", type=float)
parser.add_argument("-vl", help="specify Vin_lo value for calculating resistors", type=float)
parser.add_argument("-rtotal", help="total resistor voltage, R1+R2+R3", type=float)
args = parser.parse_args()


if args.action=="thresh":
	if args.r1 is None or args.r2 is None or args.r3 is None:
		sys.exit('ERROR: missing arguments, define r1, r2, and r3')
	calculate_thresholds(args.r1, args.r2, args.r3)
if args.action=="res":
	if args.rtotal is None or args.vl is None or args.vh is None:
		sys.exit('ERROR: missing arguments, define r1, r2, and r3')
	calculate_resistors(args.vh, args.vl, args.rtotal)
