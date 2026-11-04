
from itertools import product

print("P\tQ\tR\tQ->P\tP->~Q\tQVR\tKB")

models = []

for P, Q, R in product([True, False], repeat=3):

    # Knowledge Base sentences
    s1 = (not Q) or P       # Q -> P
    s2 = (not P) or (not Q) # P -> ~Q
    s3 = Q or R             # Q OR R

    KB = s1 and s2 and s3

    models.append((P, Q, R, KB))

    print(P, Q, R, s1, s2, s3, KB, sep="\t")


# Check entailment
def entails(query):
    for P, Q, R, KB in models:
        if KB and not query(P, Q, R):
            return False
    return True


print("\nEntailment Results:")

print("KB entails R:", entails(lambda P, Q, R: R))

print("KB entails R -> P:",
      entails(lambda P, Q, R: (not R) or P))

print("KB entails Q -> R:",
      entails(lambda P, Q, R: (not Q) or R))
