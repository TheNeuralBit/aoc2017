def do_insertions(state, steps, N):
    pos = 0
    for i in range(1, N+1):
        pos = ((pos + steps) % len(state)) + 1
        state.insert(pos, i)
    return state, pos

steps = 343
state, pos = do_insertions([0], steps, 2017)
print(state[pos+1])
