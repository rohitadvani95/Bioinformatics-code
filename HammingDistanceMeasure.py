def hamming_distance(s, t):
    dh = 0

    for i, c in enumerate(s):
        if c != t[i]:
            dh += 1
 
    return dh


if __name__ == "__main__":

    
    large_dataset = open('C://users/kirby/Downloads/rosalind_ba1g.txt').read()

    s, t = large_dataset.split()
    dist = hamming_distance(s, t)

    print(dist)
