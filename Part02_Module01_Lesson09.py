import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def probability_uniform(low_range, high_range, minimum, maximum):
    ## Calculate the probability of an event occurring between
    ##     low_range and high_range.
    probability = (high_range - low_range) / (maximum - minimum)
    return probability


def probability_range_improved(low_range, high_range, minimum, maximum):
    if (isinstance(low_range, str) or isinstance(high_range, str)):
        # print a message to the user and return none
        print('Inputs should be numbers not string')
        return None

    if (low_range < minimum or low_range > maximum):
        # print a message to the user and return none
        print('Your low range value must be between minimum and maximum')
        return None

    if (high_range < minimum or high_range > maximum):
        # print a message to the user and return none
        print('The high range value must be between minimum and maximum')
        return None

    probability = abs(high_range - low_range) / (maximum - minimum)

    return probability


def uniform_distribution_height(x_minimum, x_maximum):
    height = 1 / (x_maximum - x_minimum)
    return height


def bar_height(intervals, probabilities, total_probability):
    heights = []
    total_relative_prob = sum(probabilities)
    for i in range(0, len(probabilities)):
        bar_area = (probabilities[i] / total_relative_prob) * total_probability
        heights.append(bar_area / (intervals[i + 1] - intervals[i]))
    return heights


def gaussian_density(x, mu, sigma):
    return (1 / np.sqrt(2 * np.pi * np.power(sigma, 2.))) * np.exp(-np.power(x - mu, 2.) / (2 * np.power(sigma, 2.)))


def plot_gaussian(x, mu, sigma):
    for i in range(-10, 10):
        y = gaussian_density(i, mu, sigma)
        plt.plot(i, y, 'r')

    plt.title('Gaussian Probability Density Function')
    plt.xlabel('x variable')
    plt.ylabel('probability density function')
    plt.show()


def gaussian_probability(mean, stdev, x_low, x_high):
    return norm(loc=mean, scale=stdev).cdf(x_high) - norm(loc=mean, scale=stdev).cdf(x_low)


plot_gaussian(0, 0, 10)

print(probability_uniform(2, 6, 0.3, 0.6));
