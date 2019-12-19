#!/usr/bin/env python3

data = '03036732577212944063491565474664'
# data = '59773590431003134109950482159532121838468306525505797662142691007448458436452137403459145576019785048254045936039878799638020917071079423147956648674703093863380284510436919245876322537671069460175238260758289779677758607156502756182541996384745654215348868695112673842866530637231316836104267038919188053623233285108493296024499405360652846822183647135517387211423427763892624558122564570237850906637522848547869679849388371816829143878671984148501319022974535527907573180852415741458991594556636064737179148159474282696777168978591036582175134257547127308402793359981996717609700381320355038224906967574434985293948149977643171410237960413164669930'

data = '59773590431003134109950482159532121838468306525505797662142691007448458436452137403459145576019785048254045936039878799638020917071079423147956648674703093863380284510436919245876322537671069460175238260758289779677758607156502756182541996384745654215348868695112673842866530637231316836104267038919188053623233285108493296024499405360652846822183647135517387211423427763892624558122564570237850906637522848547869679849388371816829143878671984148501319022974535527907573180852415741458991594556636064737179148159474282696777168978591036582175134257547127308402793359981996717609700381320355038224906967574434985293948149977643171410237960413164669930'
data = data * 10000
print(len(data))
skip = int(data[:7])

data_array = []
for v in data:
    data_array.append(int(v))

def get_pattern(phase, length):
    base = [0, 1, 0, -1]
    result = []
    toskip = 1
    while True:
        for i in range(len(base)):
            for j in range(phase):
                if toskip > 0:
                    toskip -= 1
                else:
                    result.append(base[i])
                    if len(result) == length:
                        return result

#patterns = []
#for i in range(len(data_array)):
#    patterns.append(get_pattern(i + 1, len(data_array)))

def transform(input):
    global patterns
    output = []
    for i in range(1, len(input) + 1):
        pattern = patterns[i - 1]
        sum = 0
        for j in range(len(input)):
            sum += input[j] * pattern[j]
#        if sum < 0:
#            sum = -sum
        output.append(sum)
    return output

def transform2(input):
    output = []
    s = 0
    for i in reversed(range(len(input))):
        s += input[i]
        s = s % 10
        output.append(s)
    return list(reversed(output))

print(skip)
data_array = data_array[skip:]
print(len(data_array))

for i in range(1, 100 + 1):
    data_array = transform2(data_array)
    print(i)
    # print('After %d: %s' % (i, str(data_array)))

print(''.join([str(x) for x in data_array[:8]]))
