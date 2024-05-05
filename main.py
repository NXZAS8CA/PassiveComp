import math
import argparse
import itertools


def createSeries(n):
    values = []
    for m in range(0 , n):
        k = math.pow(math.pow(10,m),1/n)
        #k = math.ceil(k * 100) / 100
        if n <= 24:
            k = round(k,1)
            match k:
                case 2.6:
                    k = 2.7
                case 2.9:
                    k = 3.0
                case 3.2:
                    k = 3.3
                case 3.5:
                    k = 3.6
                case 3.8:
                    k = 3.9
                case 4.2:
                    k = 4.3
                case 4.6:
                    k = 4.7
                case 8.3:
                    k = 8.2
        else:
            k = round(k,2)
            if k == 8.3:
                k = 8.2
        
        values.append(k)
    return values

def getNextClosestValue(list, value):
    buff = []
    for i in list:
        buff.append(abs(i-value))
    return buff.index(min(buff))

def norminalizeValue(value):
    factor = 1
    if value >= 10 and value < 100:
        value /= 10
        factor = 10
    elif value >= 100 and value < 1000:
        value /= 100
        factor = 100
    return value, factor

def denorminalizeValue(value, factor):
    return value * factor

def calculateError(target, value):
    return (((value - target) / target) * 100)

def seriesResistance(list, value):
    buff = []
    for i in range(0, len(list)):
        for j in range(i, len(list)):
            total = list[i] + list[j]
            total = round(total, 1)
            buff.append((list[i], list[j], total))

    out = getNextClosestValue([x[2] for x in buff], value)
    return buff[out]



    #out = [list(x) for x in itertools.combinations(list, 2)]
    #return out, buff

def parallelResistance(list, value):
    buff = []
    for i in range(0, len(list)):
        for j in range(i, len(list)):
            total = (list[i] * list[j]) / (list[i] + list[j])
            total = round(total, 1)
            buff.append((list[i], list[j], total))

    out = getNextClosestValue([x[2] for x in buff], value)
    return buff[out]

def checkArgs(args):
    if args.eseries not in [3, 6, 12, 24, 48, 96, 192]:
        raise ValueError("Invalid E-Series specified! Use one of these instead: 3, 6, 12, 24, 48, 96, 192")
    
    if args.value >= 1000:
        raise ValueError("Please use a value smaller than 1000. If possible convert the value to the next SI Prefix.")

def main():
    parser = argparse.ArgumentParser()
    #parser.add_argument("-t", "--type", help="specify component type") #TODO: needs work
    parser.add_argument("-v", "--value", help="Specify the target value. Values smaller than 1000 are allowed", type=float)
    parser.add_argument("-e", "--eseries", help="Specify the e-series. Possible values are: 3, 6, 12, 24, 48, 96, 192", type=int)
    args = parser.parse_args()

    checkArgs(args)

    values = createSeries(args.eseries)
    target = args.value
    target, factor = norminalizeValue(target)

    buff = getNextClosestValue(values, target)
    series = seriesResistance(values, target)
    parallel = parallelResistance(values, target)

    target = denorminalizeValue(target, factor)
    value = denorminalizeValue(values[buff], factor)
    seriesValue = denorminalizeValue(series[2], factor)
    parallelValue = denorminalizeValue(parallel[2], factor)

    miss = calculateError(target, value)
    seriesMiss = calculateError(target, seriesValue)
    parallelMiss = calculateError(target, parallelValue)


    print("Target Value: ", target)
    print(f"Closest single Resistor Value: {value} with a miss of {miss} %")
    
    print(f"Closest series Value: {seriesValue} with a miss of {seriesMiss} %")
    print(f"Used resistors for Series: {series[0]} and {series[1]}")

    print(f"Closest parallel Value: {parallelValue} with a miss of {parallelMiss} %")
    print(f"Used resistors for Series: {parallel[0]} and {parallel[1]}")
    
if __name__ == '__main__':
    main()

    
