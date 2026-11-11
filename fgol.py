""" FOL-FC-ASK(KB, q)

1. Repeat until no new facts are found:
      new = {}

2. For each rule in KB:
      Match rule conditions with facts in KB.

3. Apply substitution to the rule conclusion.

4. If the conclusion is not already in KB or new:
      Add it to new.

5. Check whether the conclusion matches query q.
      If yes, return success.

6. Add all new facts to KB.

7. If query is not proved:
      Return false.

 """

def match(p, f, s):
    if p[0] != f[0] or len(p) != len(f):
        return None
    s = s.copy()
    for a, b in zip(p[1:], f[1:]):
        if a.startswith("?"):
            if a in s and s[a] != b:
                return None
            s[a] = b
        elif a != b:
            return None
    return s

def get(pre, i, s, kb):
    if i == len(pre):
        return [s]

    res = []
    for f in kb:
        t = match(pre[i], f, s)
        if t is not None:
            res += get(pre, i + 1, t, kb)
    return res

def fc(kb, rules, q):
    while True:
        new = []
        for pre, con in rules:
            for s in get(pre, 0, {}, kb):
                f = tuple(s.get(x, x) for x in con)
                if f not in kb and f not in new:
                    new.append(f)

        if not new:
            break

        kb += new

    return q in kb

kb = [
    ("Owns", "A", "T1"),
    ("Missile", "T1"),
    ("American", "Robert"),
    ("Enemy", "A", "America")
]

rules = [
    ([("Missile", "?x")], ("Weapon", "?x")),
    ([("Missile", "?x"), ("Owns", "A", "?x")],
     ("Sells", "Robert", "?x", "A")),
    ([("Enemy", "?x", "America")], ("Hostile", "?x")),
    ([("American", "?p"), ("Weapon", "?q"),
      ("Sells", "?p", "?q", "?r"), ("Hostile", "?r")],
     ("Criminal", "?p"))
]

q = ("Criminal", "Robert")

if fc(kb, rules, q):
     print("Robert is Criminal")
else:
    print("Robert is not Criminal")
 