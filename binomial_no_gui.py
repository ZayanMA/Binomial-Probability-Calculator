import math


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


def main():
    total_trials = int(input("Total number of trials: "))
    successes = int(input("How many successes: "))
    prob = float(input("Probability of success: "))
    ncr = (factorial(total_trials))/ (factorial(successes) * factorial(total_trials - successes))
    equal = ncr * pow(prob, successes) * pow(1 - prob, total_trials - successes)
    print(equal)


if __name__ == "__main__":
    main()