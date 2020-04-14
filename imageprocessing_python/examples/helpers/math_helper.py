import matplotlib.pyplot as plt


class MathHelper():
    @staticmethod
    def getMinMax(array):
        max = min = array[0]
        for item in array:
            if(item > max):
                max = item
            if(item < min):
                min = item
        return min, max

    @staticmethod
    def normalizeWithMinMax(x, min, max):
        y = (x-min) / (max-min)
        return y
