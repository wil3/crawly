import numpy as np
import argparse
def mean_confidence(data, zscore=1.96):
    #http://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_confidence_intervals/bs704_confidence_intervals_print.html
        n = float(len(data))
        mean = np.mean(data)
        std = np.std(data)
        confidence = zscore * std / np.sqrt(n)
        return mean, confidence 

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')
    parser.add_argument("file",  help="")

    args = parser.parse_args()
    rate = []
    damage = []
    with open(args.file, 'r') as f:
        for line in f.readlines():
            r, d = line.split(",")
            rate.append(float(r))
            damage.append(float(d))


    m1, c1 = mean_confidence(damage)
    print "Damage Mean ", m1
    print "Damage +-", c1


    m, c = mean_confidence(rate)

    print "Rate Mean ", m
    print "Rate +-", c

