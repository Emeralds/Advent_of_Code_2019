import math

#part 1
fuel_module = 0
fuel_total = 0
with open('input1.txt') as fp:
    line = fp.readline()
    cnt = 1
    while line:
        #print("Line {}: {}".format(cnt, line.strip()))
        fuel_module = int(line.strip())
        line = fp.readline()
        #print(fuel_module)
        fuel_total += math.floor(fuel_module/3)-2
        cnt += 1
print('answer 1: ',fuel_total)


#part 2
module_weight = 0
fuel_for_module = 0
fuel_for_fuel = 0
fuel_total = 0

with open('input1.txt') as fp:
    line = fp.readline()
    cnt = 1
    count = 1
    while line:
        divisible = 1
        #print("Line {}: {}".format(cnt, line.strip()))
        'setting initial weight for fuel calculations'
        module_weight = int(line.strip())
        #print('module weight: ', module_weight)
        'setting initial fuel calc based on module weight'
        fuel_for_module = math.floor(module_weight/3)-2
        'determining first calculation of fuel for fuel'
        fuel_for_fuel = math.floor(fuel_for_module/3)-2
        'while loop to add additional fuel for fuel'
        while divisible:
            #print(cnt,':',count)
            count += 1
            #print('fuel for module: ', fuel_for_module)
            'adding the current fuel for fuel to the total module fuel'
            fuel_for_module += fuel_for_fuel
            #print('fuel for fuel: ', fuel_for_fuel)
            'calculating the new fuel for the jsut added fuel'
            fuel_for_fuel = math.floor(fuel_for_fuel/3)-2
            # determining if the calculation should continue on
            if (math.floor(fuel_for_fuel/3)-2) <= 0:
                divisible = 0
        line = fp.readline()
        # final calculation to add in last fuel for fuel calc
        fuel_for_module += fuel_for_fuel
        # adding the end module fuel to the fuel total
        fuel_total += fuel_for_module
        cnt += 1
print('answer 2: ',fuel_total)