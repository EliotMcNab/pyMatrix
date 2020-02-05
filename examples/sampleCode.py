from matrixHandler import matrix

# TEST: genere des matrices aleatoires 3 x 3
matrice1 = matrix.Matrix()
matrice2 = matrix.Matrix()

# TEST: verifie les operateurs de matrices
print("|| TESTING: print() and matrice1[1][2] and len()")
print("\\/")
print(f"\nprint(): \n{matrice1} \n{matrice2}")
print(f"\nmatrice1[1][2]: {matrice1[1][2]}")
print(f"\nlen(matrice1): {len(matrice1)}")
print("\n")

print("|| TESTING: + and -")
print("\\/")
print(f"\nmatrice1 + matrice2: {matrice1 + matrice2}")
print(f"\nmatrice1 - matrice2: {matrice1 - matrice2}")
print(f"\n-matrice1: {matrice1}")
print("\n")

print("|| TESTING: *")
print("\\/")
print(f"\nmatrice1 * matrice2: {matrice1 * matrice2}")
print(f"\nmatrice1 * 0: {matrice1 * 0}")
print(f"\nmatrice1 * 2: {matrice1 * 2}")
print(f"\nmatrice1 * 1.2: {matrice1 * 1.2}")
print("\n")

print("|| TESTING: *=, += and -=")
print("\\/")
matrice1 *= 0
print(f"\nmatrice1 *= 0: {matrice1}")
matrice2 = matrix.Matrix([[2, 2, 2],[2, 2, 2],[2, 2, 2]])
matrice1 += matrice2
print(f"\nmatrice1 += matrice2: {matrice1}")
matrice1 -= matrice2
print(f"\nmatrice1 -= matrice2: {matrice1}")
print("\n")

print("|| TESTING: == and !=")
print("\\/")
print(f"\nmatrice1: {matrice1}")
print(f"\nmatrice2: {matrice2}")
print(f"\nmatrice1 == matrice2: {matrice1 == matrice2}")
print(f"matrice1 != matrice2: {matrice1 != matrice2}")
print("\n")