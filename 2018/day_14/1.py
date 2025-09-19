def main():
    with open('input.txt') as f:
        expected_recipes = int(f.read().strip())
    # expected_recipes = 2018
    rec = [3, 7]
    e1_ix = 0
    e2_ix = 1
    while len(rec) < expected_recipes + 11:
        # Make new recipe
        new_recs = [int(r) for r in str((rec[e1_ix] + rec[e2_ix]))]
        assert len(new_recs) in (1,2)
        # Append to recipes
        rec += new_recs
        # Advance elves
        e1_steps = rec[e1_ix] + 1
        e2_steps = rec[e2_ix] + 1

        e1_ix = (e1_steps + e1_ix) % len(rec)
        e2_ix = (e2_steps + e2_ix) % len(rec)
    
    return ''.join(str(i) for i in rec[expected_recipes: expected_recipes + 10])


print(main())