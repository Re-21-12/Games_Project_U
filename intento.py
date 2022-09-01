
def pythagorean_triples(num):
    triples = []
    c, m = 0, 2
    while c < num:
        for n in range(1, m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            if c > num:
                break
            triples.append([a, b, c])
        m = m + 1
    return triples

print(pythagorean_triples(25))
