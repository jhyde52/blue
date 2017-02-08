# plots a cellular automaton shape


from cellular_automaton import cellular_automaton


def plot_cellular(string0, pattern, generations):
    print string0
    for i in range(1,generations):
        print cellular_automaton(string0, pattern, i)

plot_cellular('....................x....................', 126, 100) 

#