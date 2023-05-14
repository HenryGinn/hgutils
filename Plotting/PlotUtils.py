import math

import numpy as np
import matplotlib.pyplot as plt

def get_acceptable_indexes(data, tolerance=4):
    if data.size < 3:
        acceptable_indexes = np.arange(len(data))
    else:
        acceptable_indexes = get_acceptable_indexes_non_trivial(data, tolerance)
    return acceptable_indexes

def get_acceptable_indexes_non_trivial(data, tolerance):
    deviations = np.abs(data - np.median(data))
    modified_deviation = np.average(deviations**(1/4))**4
    accepted_indexes = np.abs(deviations) < tolerance * modified_deviation
    return accepted_indexes

def update_figure_size(width=10, height=6):
    plt.gcf().set_size_inches(width, height)

def adjust_subplots(bottom=0.1, top=0.9,
                    left=0.05, right=0.95,
                    wspace=0.3, hspace=0.3):
    plt.gcf().subplots_adjust(bottom=bottom, top=top,
                              right=right, left=left,
                              wspace=wspace, hspace=hspace)


def get_prefixed_numbers(numbers):
    powers_of_1000 = [get_power_of_1000(abs(number)) for number in numbers
                      if number != 0]
    power_of_1000 = min(powers_of_1000)
    prefix = prefix_lookup(power_of_1000)
    numbers = [int(number / 1000**power_of_1000) for number in numbers]
    return numbers, prefix

def get_power_of_1000(input_number):
    power_of_1000 = np.log(input_number) / np.log(1000)
    power_of_1000 = np.floor(np.round(power_of_1000, 5))
    return power_of_1000

def prefix_lookup(power_of_thousand):
    prefix_dict = get_prefix_dict()
    prefix = prefix_dict[power_of_thousand]
    return prefix

def reverse_prefix_lookup(prefix):
    prefix_dict = get_prefix_dict()
    reverse_prefix_dict = {value: key
                           for key, value in prefix_dict.items()}
    power_of_thousand = reverse_prefix_dict[prefix]
    return power_of_thousand

def get_prefix_dict():
    prefix_dict = {-5: "f", -4: "p", -3: "n", -2: "$\mu$", -1: "m",
                   0: "", 1: "k", 2: "M", 3: "G", 4: "T", 5: "P"}
    return prefix_dict
