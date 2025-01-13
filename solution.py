s = "LXVI"  # Add Roman num here

z = list(s)


I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

numerical_list = [0] * len(z)


for i in range(len(z)):

    if z[i] == "I":
        numerical_list[i] += I
    if z[i] == "V":
        numerical_list[i] += V
    if z[i] == "X":
        numerical_list[i] += X
    if z[i] == "L":
        numerical_list[i] += L
    if z[i] == "C":
        numerical_list[i] += C
    if z[i] == "D":
        numerical_list[i] += D
    if z[i] == "M":
        numerical_list[i] += M


num_val = 0
a = 0

if len(z) == 1:
    if numerical_list[0] == I:
        num_val = num_val + I
    if numerical_list[0] == V:
        num_val = num_val + V
    if numerical_list[0] == X:
        num_val = num_val + X
    if numerical_list[0] == L:
        num_val = num_val + L
    if numerical_list[0] == C:
        num_val = num_val + C
    if numerical_list[0] == D:
        num_val = num_val + D
    if numerical_list[0] == M:
        num_val = num_val + M
else:
    for i in range(len(z)):
        a = a + 1
        if a == len(z):
            if numerical_list[i] == I:
                num_val = num_val + I
            if numerical_list[i] == V:
                num_val = num_val + V
            if numerical_list[i] == X:
                num_val = num_val + X
            if numerical_list[i] == L:
                num_val = num_val + L
            if numerical_list[i] == C:
                num_val = num_val + C
            if numerical_list[i] == D:
                num_val = num_val + D
            if numerical_list[i] == M:
                num_val = num_val + M
            break
        else:
            if numerical_list[i] >= numerical_list[a]:
                if numerical_list[i] == I:
                    num_val = num_val + I
                if numerical_list[i] == V:
                    num_val = num_val + V
                if numerical_list[i] == X:
                    num_val = num_val + X
                if numerical_list[i] == L:
                    num_val = num_val + L
                if numerical_list[i] == C:
                    num_val = num_val + C
                if numerical_list[i] == D:
                    num_val = num_val + D
                if numerical_list[i] == M:
                    num_val = num_val + M
            else:
                if numerical_list[i] == I:
                    num_val = num_val + (-I)
                if numerical_list[i] == V:
                    num_val = num_val + (-V)
                if numerical_list[i] == X:
                    num_val = num_val + (-X)
                if numerical_list[i] == L:
                    num_val = num_val + (-L)
                if numerical_list[i] == C:
                    num_val = num_val + (-C)
                if numerical_list[i] == D:
                    num_val = num_val + (-D)
                if numerical_list[i] == M:
                    num_val = num_val + (-M)

print(num_val)  # output
