import argparse

from core import *

def checkArgs(args):
    if args.eseries not in [3, 6, 12, 24, 48, 96, 192]:
        raise ValueError("Invalid E-Series specified! Use one of these instead: 3, 6, 12, 24, 48, 96, 192")
    
    if args.value >= 1000:
        raise ValueError("Please use a value smaller than 1000. If possible convert the value to the next SI Prefix.")

def main():
    parser = argparse.ArgumentParser()
    #parser.add_argument("-t", "--type", help="specify component type") #TODO: needs work
    parser.add_argument("-v", "--value", help="Specify the target value. Values smaller than 1000 are allowed", type=float)
    parser.add_argument("-e", "--eseries", help="Specify the e-series. Possible values are: 3, 6, 12, 24, 48, 96, 192", type=int, choices=[3, 6, 12, 24, 48, 96, 192])
    parser.add_argument("-c", "--config", help="Configure which combination mode is used.", choices=['S','P','SP','PS'])
    args = parser.parse_args()

    #checkArgs(args)

    values = createSeries(args.eseries)
    target = args.value
    target, factor = norminalizeValue(target)

    buff = getNextClosestValue(values, target)
    series = calculateSeries(values, target)
    parallel = calculateParallel(values, target)

    target = denorminalizeValue(target, factor)
    value = denorminalizeValue(values[buff], factor)

    seriesValue = denorminalizeValue(series[2], factor)
    seriesVal1 = denorminalizeValue(series[0], factor)
    seriesVal2 = denorminalizeValue(series[1], factor)


    parallelValue = denorminalizeValue(parallel[2], factor)
    parallelVal1 = denorminalizeValue(parallel[0], factor)
    parallelVal2 = denorminalizeValue(parallel[1], factor)

    miss = calculateError(target, value)
    seriesMiss = calculateError(target, seriesValue)
    parallelMiss = calculateError(target, parallelValue)


    print("Target Value: ", target)
    print(f"Closest single Resistor Value: {value} with a miss of {miss:.2f} %")
    
    print(f"Closest series Value: {seriesValue} with a miss of {seriesMiss:.2f} %")
    print(f"Used resistors for Series: {seriesVal1:.2f} and {seriesVal2:.2f}")

    print(f"Closest parallel Value: {parallelValue:.2f} with a miss of {parallelMiss:.2f} %")
    print(f"Used resistors for Series: {parallelVal1:.2f} and {parallelVal2:.2f}")
    
if __name__ == '__main__':
    main()

    
# TODO : add better way to deal with floats, better output