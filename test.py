import datetime
from models import PerformanceData
from weight_calculator import calc_weights

def test_calc_weights():
    """
    Run this function to test if your implementation of calc_weights works!
    :return:
    """
    ymdh = [datetime.datetime(2014, 8, 1, 0, 0)]*6
    creative_ids = [100, 101, 102, 103, 104, 104]
    imps = [100, 100, 1000, 100, 1000, 10000]
    clicks = [5, 10, 10, 2, 20, 5]

    perf_data = []
    for i in xrange(6):
        perf_data.append(PerformanceData(ymdh=ymdh[i],
                                         campaign_id=100,
                                         creative_id=creative_ids[i],
                                         imps=imps[i],
                                         clicks=clicks[i]))

    weights = calc_weights(perf_data)

    final_weights = {100: 0.274314,
                     101: 0.548628,
                     102: 0.054863,
                     103: 0.109726,
                     104: 0.012469,
                     105: 0}
    # Note that if you sum all of these weights, they add up to 1 :)
    for weight in weights:
        try:
            assert round(weight.weight, 6) == final_weights[weight.creative_id]
        except:
            print "Incorrect weight of %f for creative %d! Correct weight is %f" % \
                  (round(weight.weight, 6), weight.creative_id,
                   final_weights[weight.creative_id])
            raise

    print "Test successful. Good work!"
