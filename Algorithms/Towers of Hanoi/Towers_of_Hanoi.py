def TowersOfHanoi(n, source, destination, auxiliary):
    if n==1:
        print("Move disk 1 from peg",source,"to peg",destination)
        return
    TowersOfHanoi(n-1, source, auxiliary, destination)
    print("Move disk",n,"from peg",source,"to peg",destination)
    TowersOfHanoi(n-1, auxiliary, destination, source)