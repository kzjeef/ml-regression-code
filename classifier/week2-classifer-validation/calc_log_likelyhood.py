import numpy as np;

def calc_likelyhood(x, y):
    xys = zip(x, y)
    acc = 1.0;
    for i in xrange(len(xys)):
        ix, iy = xys[i];
        if iy > 0:
            t = 1 / (1 + np.exp(-(1 * ix)))
            acc =  t * acc
        else:
            t = 1 / (1 + np.exp(-(-1 * ix)))
            acc = t * acc
    return acc;

def calc_log_likehood(x, y):
    points = map(lambda(v) :  1 /( 1 + np.exp(-(1 * v))), x);

    indicator = lambda (yv) : 0 if yv == -1 else 1
    sum = 0.0;
    for i in xrange(len(x)):
        vv =  (x[i] * (indicator(y[i]) - points[i]));
        print "v: %f for x: %f y:%f p:%f" % (vv, x[i], indicator(y[i]), points[i])
        sum += vv;
    return sum;


print calc_log_likehood([2.5, 0.3, 2.8, 0.5], [1, -1, 1, 1])

print calc_likelyhood([2.5, 0.3, 2.8, 0.5], [1, -1, 1, 1])        
        
    