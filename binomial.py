import tkinter as tk
import sys


sys.setrecursionlimit(1500)


def factorial(n):
    if n == 1:
        return n
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    def submitpress():
        smaller = 0
        total = int(float(total_trials.get()))
        probability = float(prob.get())
        truths = int(float(number_trials.get()))
        ncr = (factorial(total))/ ((factorial(truths)) * (factorial(total - truths)))
        equal = ncr * pow(probability, truths) * pow(1-probability, total-truths)
        while truths > 0:
            truths = truths - 1
            ncr1 = (factorial(total)) / ((factorial(truths)) * (factorial(total - truths)))
            full_prob = ncr1 * pow(probability, truths) * pow(1-probability, total-truths)
            smaller = smaller + full_prob
        smaller_e = smaller + equal
        greater = 1 - smaller_e
        greater_e = 1 - smaller
        equal_ans = tk.Label(text="P(X=x)", master=frame_body, bg="light coral")
        equal_ans_f = tk.Label(text=equal, master=frame_body, bg="light coral")
        equal_ans.grid(row=4, column=0)
        equal_ans_f.grid(row=4, column=1)
        smaller_ans = tk.Label(text="P(X<x)", master=frame_body, bg="light coral")
        smaller_ans_f = tk.Label(text=smaller, master=frame_body, bg="light coral")
        smaller_ans.grid(row=5, column=0)
        smaller_ans_f.grid(row=5, column=1)
        smaller_ans_e = tk.Label(text="P(X<=x)", master=frame_body, bg="light coral")
        smaller_ans_e_f = tk.Label(text=smaller_e, master=frame_body, bg="light coral")
        smaller_ans_e.grid(row=6, column=0)
        smaller_ans_e_f.grid(row=6, column=1)
        greater_ans = tk.Label(text="P(X>x)", master=frame_body, bg="light coral")
        greater_ans_f = tk.Label(text=greater, master=frame_body, bg="light coral")
        greater_ans.grid(row=7, column=0)
        greater_ans_f.grid(row=7, column=1)
        greater_ans_e = tk.Label(text="P(X>=x)", master=frame_body, bg="light coral")
        greater_ans_e_f = tk.Label(text=greater_e, master=frame_body, bg="light coral")
        greater_ans_e.grid(row=8, column=0)
        greater_ans_e_f.grid(row=8, column=1)
    window = tk.Tk()
    frame_t = tk.Frame(master=window, bg="light coral", width=400)
    title = tk.Label(text="Binomial Calculator", master=frame_t,
                     bg="light coral")
    title.pack(fill=tk.X)
    frame_t.pack(side=tk.TOP, fill=tk.X)
    frame_body = tk.Frame(height=400, width=400, master=window,
                          bg="light coral")
    trials_l = tk.Label(text="Total Number of trials:",
                        master=frame_body, bg="light coral")
    trials_l.grid(row=0, column=0)
    total_trials = tk.Entry(master=frame_body)
    total_trials.grid(row=0, column=1)
    total_trials.focus()
    number_trials_l = tk.Label(text="Number of successes:",
                               master=frame_body, bg="light coral")
    number_trials = tk.Entry(master=frame_body)
    number_trials_l.grid(row=1, column=0)
    number_trials.grid(row=1, column=1)
    number_trials.focus()
    prob_l = tk.Label(text="Probability of success(%):",
                      master=frame_body, bg="light coral")
    prob = tk.Entry(master=frame_body)
    prob_l.grid(row=2, column=0)
    prob.focus()
    prob.grid(row=2, column=1)
    submit = tk.Button(text="Submit", master=frame_body, command=lambda: submitpress())
    submit.grid(row=3, column=1)
    frame_body.pack(fill=tk.BOTH, expand = 1)
    window.mainloop()


if __name__ == "__main__":
    main()