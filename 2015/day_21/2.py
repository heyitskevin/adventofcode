import itertools

HITPOINTS = 100
FILENAME = 'input.txt'

WEAPONS = {
    'Dagger': (8, 4, 0),
    'Shortsword': (10, 5, 0),
    'Warhammer': (25, 6, 0),
    'Longsword': (40, 7, 0),
    'Greataxe': (74, 8, 0)
}

ARMOR = {
    'Naked': (0, 0, 0),
    'Leather': (13, 0, 1),
    'Chainmail': (31, 0, 2),
    'Splintmail': (53, 0, 3),
    'Bandedmail': (75, 0, 4),
    'Platemail': (102, 0, 5),
}

RINGS = {
    'Damage +1': (25, 1, 0),
    'Damage +2': (50, 2, 0),
    'Damage +3': (100, 3, 0),
    'Defense +1': (20, 0, 1),
    'Defense +2': (40, 0, 2),
    'Defense +3': (80, 0, 3)
}

def calc_damage(a, d):
    res = d - a
    if res < 1:
        res = 1
    return res

def calc_rounds(hp, dmg):
    return (hp // dmg) + 1 

def get_boss():
    res = []
    with open(FILENAME) as f:
        for ln in f.read().split('\n'):
            v = ln.split(':')[-1].strip()
            res.append(int(v))
    return tuple(res)

def make_combination():
    # 1 Weapon, 0-1 Armor, 0-2 Rings
    c = []

    # make ring combos
    ring_combos = list(itertools.combinations(RINGS.values(), 2))
    for r in RINGS.values():
        ring_combos.append((r,))
    
    ring_combos.append(((0,0,0),))

    for w in WEAPONS.values():
        for ar in ARMOR.values():
            for ring_set in ring_combos:
                ring_gold = 0
                ring_dmg = 0
                ring_arm = 0
                for rr in ring_set:
                    ring_gold += rr[0]
                    ring_dmg += rr[1]
                    ring_arm += rr[2]
                c.append((
                    w[0] + ar[0] + ring_gold,
                    w[1] + ar[1] + ring_dmg,
                    w[2] + ar[2] + ring_arm
                ))
    return c
    

def func():
    boss_hp, boss_damage, boss_armor = get_boss() # 104, 8, 1
    self_combos = make_combination()

    losing_golds = []

    for sc in self_combos:
        self_gold, self_dmg, self_armor = sc
        damage_i_deal = calc_damage(boss_armor, self_dmg)
        damage_boss_deal = calc_damage(self_armor, boss_damage)

        rounds_i_die = calc_rounds(HITPOINTS, damage_boss_deal)
        rounds_boss_die = calc_rounds(boss_hp, damage_i_deal)
        
        curr_health = HITPOINTS
        curr_boss = boss_hp

        while curr_health > 0 and curr_boss > 0:
            curr_boss -= damage_i_deal
            if curr_boss <= 0:
                break
            curr_health -= damage_boss_deal
        if curr_health <= 0:
            losing_golds.append(self_gold)
    
    print('max', max(losing_golds))


func()