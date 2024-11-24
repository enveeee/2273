def towerOfHanoi(n, source, destination, auxiliary):
    if n==1:
        print("Move disk 1 from Source", source, "to Destination", destination)
        return
    towerOfHanoi(n-1, source, auxiliary, destination)
    print("Move Disk", n, "from Source", source, "to Destination", destination)
    towerOfHanoi(n-1, auxiliary, destination, source)
#Driver Code
n=4
towerOfHanoi(n, 'A', 'B', 'C')
