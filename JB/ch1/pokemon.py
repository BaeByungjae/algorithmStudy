import sys

n, m = map(int, sys.stdin.readline().split())
pokemons_name = {}
pokemons_index = {}

for i in range(n) :
    pokemon = sys.stdin.readline().rstrip()
    pokemons_name[pokemon] = i+1
    pokemons_index[str(i+1)] = pokemon

for j in range(m) : 
    problem = sys.stdin.readline().rstrip()
    if problem.isnumeric() :
        print(pokemons_index[problem])
    else :
        print(pokemons_name[problem])




