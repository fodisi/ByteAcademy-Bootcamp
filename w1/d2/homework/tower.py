
#!/usr/bin/env python3


#Solves the Hanoi Tower problem and returns the number of steps required for solving the problem
def hanoi_tower(n, source, aux, target):
    steps = 0
    if n > 0:
        #move top disk from source to auxiliary, so it is out of the way
        steps += hanoi_tower(n - 1, source, target, aux)

        #move the nth disk from source to target
        target.append(source.pop())

        #display progress
        print(source_rod, aux_rod, target_rod, '--------------', sep = '\n')

        #move top disk left on auxiliary to target
        steps += hanoi_tower(n - 1, aux, source, target)

        #increments number of steps required
        steps += 1

    return steps


if __name__ == '__main__':
    #asks user input for number of disks
    print("type the number of disks")
    n = int(input())
    
    #creates and populates source_rod with n disks [1,2,..,n]
    #reverts the list order[n,n-1,.., 1)
    source_rod = list(range(1, n + 1))
    source_rod = source_rod[::-1]

    #creates auxiliary and target rods
    aux_rod = []
    target_rod = []

    #displays rod's initial configuration
    print(source_rod, aux_rod, target_rod, '--------------', sep = '\n')
    
    #solves the hanoi_tower puzzle and gets the number of steps required for it
    s = hanoi_tower(n, source_rod, aux_rod, target_rod)

    print('Steps required: {0}'.format(s))
