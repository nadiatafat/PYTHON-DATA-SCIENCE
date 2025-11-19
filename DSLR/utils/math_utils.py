import math


class Calculator:
    def __init__(self, *args):
        self.values = self._validate(args)

    def _validate(self, args):
        if len(args) < 2:
            raise ValueError("Missing values")
        try:
            return [float(x) for x in args]
        except ValueError:
            raise ValueError("All values must be numbers")

    def mean(self):
        return sum(self.values) / len(self.values)

    def median(self):
        sorted_vals = sorted(self.values)
        n = len(sorted_vals)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
        else:
            return sorted_vals[mid]

    def _get_median(self, lst: list[float]):
        m = len(lst)
        return (lst[m//2 - 1] + lst[m//2]) / 2 if m % 2 == 0 else lst[m//2]

    def quartile(self):
        sorted_vals = sorted(self.values)
        n = len(sorted_vals)
        mid = n // 2
        lower = sorted_vals[:mid]
        upper = sorted_vals[mid:] if n % 2 == 0 else sorted_vals[mid+1:]
        return (self._get_median(lower), self._get_median(upper))

    def variance(self):
        m = self.mean()
        return sum((x - m) ** 2 for x in self.values) / len(self.values)

    def std(self):
        return math.sqrt(self.variance())
    
    def count(self):
        return len(self.values)

    def min(self):
        return sorted(self.values)[0]

    def max(self):
        return sorted(self.values)[-1]



def ft_statistics(*args, **kwargs):
    try:
        calc = Calculator(*args)
        for val in kwargs.values():
            if val == "mean":
                print("mean :", calc.mean())
            elif val == "median":
                print("median :", calc.median())
            elif val == "quartile":
                q1, q3 = calc.quartile()
                print("quartile :", f"25%: {q1}, 75%: {q3}")
            elif val == "var":
                print("variance :", calc.variance())
            elif val == "std":
                print("standard deviation :", calc.std())
    except Exception as e:
        print("ERROR:", e)
