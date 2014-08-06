"""
Calculate your creative "weights" here!
"""
from data_api import CoolAPI
from models import CreativeWeights

def create_performance_data(start, end):
    """
    Gets hourly creative impression and click data from the database
    :param start: datetime.datetime start timestamp for which to get data
    :param end: datetime.datetime end timestamp for which to get data
    :return: List of PerformanceData objects retrieved from database
    """
    ### NOTE: You do not have to change anything here
    data = CoolAPI()
    data._initialize_data()
    performance_data = data.get_campaign_data(start, end)

    return performance_data

def calc_weights(creative_data):
    """
    Calculates weights for a particular campaign based on creative performance
    :param creative_data: List of PerformanceData objects containing hourly
      impression and click data for a given creative
    :return: List of CreativeWeights "weight" objects
    """
    weights = []
    creative_performance = {100: {'imps': 0, 'clicks': 0},
                            101: {'imps': 0, 'clicks': 0},
                            102: {'imps': 0, 'clicks': 0},
                            103: {'imps': 0, 'clicks': 0},
                            104: {'imps': 0, 'clicks': 0},
                            105: {'imps': 0, 'clicks': 0}}

    ###########################
    ### PUT YOUR CODE HERE! ###
    ###########################

    """
    Iterate through the list of resulting PerformanceData objects and store
    performance data using the "creative_performance" dictionary.
    (Feel free to use some other way to store or group creative performance
    data if you like!)
    For now, we will only deal with one campaign, where campaign_id = 100

    If you round, do not round to less than 6 decimal places for accuracy.

    Once you have compiled all the data, compute each creative's weight,
    create a CreativeWeights object for each one, and add it to the "weights" list
    so we can insert all the weights back into the database.
    (HINT: Look at how the "data" object was created above from PerformanceDataAPI.
           How would you create a CreativeWeights object?
    """

    return weights