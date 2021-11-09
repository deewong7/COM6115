import pylab

values = []

filename = "pulse_data.txt"
with open(filename) as f:
    for each in f:
        values.append(float(each))

# print(len(values))

values.sort()

# pylab.plot(values)
# pylab.show()

minval = min(values)
maxval = max(values)
vspan = maxval - minval

BINS = 50
ids = {}

for each in values:

    binid = int(BINS * (each - minval) / vspan)
    if binid == BINS:
        binid = BINS - 1

    try:
        ids[binid] += 1
    except KeyError:
        ids[binid] = 1


# pylab.plot(ids.keys(), ids.values(), ".")
# pylab.bar(ids.keys(), ids.values())
pylab.bar(ids.keys(), ids.values())
# pylab.hist(values, BINS)
pylab.show()
