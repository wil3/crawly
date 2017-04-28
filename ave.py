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
    with open(args.file, 'r') as f:
        data = [float(line) for line in f.readlines()]

    m, c = mean_confidence(data)
    print "Mean ", m
    print "+-", c

