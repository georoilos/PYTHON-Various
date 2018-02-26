from pylab import plot,show
def calc_mean(nums):
    S = sum(nums)
    n = len(nums)
    mean = S/n
    return mean

def find_diff(nums):
    mean = calc_mean(nums)
    diff = []
    for num in nums:
        diff.append(num-mean)
    return diff

def calc_variance(nums):
    diff = find_diff(nums)
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff/len(nums)
    return variance

scores = [1000,1060,1070,980,1100,1120,960,1010,1010,1060,1100,1050]
variance = calc_variance(scores)
print('Variance = {0:.3f}'.format(variance))
SD = variance**0.5
print('Standard Deviation = {0:.3f}'.format(SD))
'''
Variance = 2389.000
Standard Deviation = 48.877
'''