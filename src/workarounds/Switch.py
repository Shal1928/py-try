value = 20
s = {
    value <= 20: "<=20 0",
    5 <= value <= 10: "5-10",
    value <= 20: "<=20",
    value != 0: "!=0",
    value <= 20: "<=20 2",
    }[True]
print(s)