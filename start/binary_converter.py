def dec_to_bin(dec):
    if dec == 0 or dec == 1:
        return str(dec)
    else:
        m = dec % 2
        n = int((dec - m) / 2)
        return dec_to_bin(n) + str(m)


print(dec_to_bin(100))
