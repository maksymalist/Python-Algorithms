import math

def main(s, p):

    s, p = int(s), int(p)
    sx, px = int(math.sqrt(s**2)), int(math.sqrt(p**2))
    mx = max(sx, px) + 1
    limit = sorted(list(set([-x for x in range(mx)] + [x for x in range(mx)])))
    #print(limit)

    hm = {}
    found = False

    for i in limit:
        if i in hm:
            #print("sum", i, hm[i], i*hm[i])
            if i * hm[i] == p:
                print("found: ", i, hm[i])
                found = True

        else:
            hm[s-i] = i
    if not found:
        print("No results where found")

su = input("Enter sum (b): ")
prod = input("Enter prod (a * c): ")

main(su, prod)
