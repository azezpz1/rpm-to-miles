import argparse
import math

parser = argparse.ArgumentParser(description="Converts indoor cycling RPM to distance")
parser.add_argument("--rpm", type=int, required=True, help="The average RPM of the ride.")
parser.add_argument("--diameter", type=int, required=True, help="The diameter of the wheel in inches")
parser.add_argument("--time", type=int, required=True, help="The time spent cycling in minutes")

args = parser.parse_args()

circumference = math.pi * args.diameter
distance = args.time * circumference * args.rpm

INCHES_IN_A_MILE = 63360

print(f"{distance / INCHES_IN_A_MILE} miles")
