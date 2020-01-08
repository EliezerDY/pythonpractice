from statistics import mean,variance,stdev
def stat(a):
    return max(a),min(a),mean(a),variance(a),stdev(a)

print(stat({1,2,3,4,5}))
