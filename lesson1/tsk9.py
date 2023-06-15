for i in [2, 6]:
    for j in range(2, 11):
        for x in range(4):
            print(f"{i + x} X {j:2d} = {(i + x) * j:2d}", end='\t\t')
        print()
    print()
