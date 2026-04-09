import three_d   # entire module import

print("1. Cube")
print("2. Cuboid")
print("3. Cylinder")
print("4. Cone")
print("5. Sphere")

choice = int(input("Enter your choice: "))

print("1. CSA")
print("2. TSA")
print("3. Volume")

op = int(input("Enter operation: "))

# Cube
if choice == 1:
    a = float(input("Enter side: "))
    if op == 1:
        print("CSA =", three_d.cube_csa(a))
    elif op == 2:
        print("TSA =", three_d.cube_tsa(a))
    elif op == 3:
        print("Volume =", three_d.cube_volume(a))

# Cuboid
elif choice == 2:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    h = float(input("Enter height: "))
    if op == 1:
        print("CSA =", three_d.cuboid_csa(l, b, h))
    elif op == 2:
        print("TSA =", three_d.cuboid_tsa(l, b, h))
    elif op == 3:
        print("Volume =", three_d.cuboid_volume(l, b, h))

# Cylinder
elif choice == 3:
    r = float(input("Enter radius: "))
    h = float(input("Enter height: "))
    if op == 1:
        print("CSA =", three_d.cylinder_csa(r, h))
    elif op == 2:
        print("TSA =", three_d.cylinder_tsa(r, h))
    elif op == 3:
        print("Volume =", three_d.cylinder_volume(r, h))

# Cone
elif choice == 4:
    r = float(input("Enter radius: "))
    l = float(input("Enter slant height: "))
    h = float(input("Enter height: "))
    if op == 1:
        print("CSA =", three_d.cone_csa(r, l))
    elif op == 2:
        print("TSA =", three_d.cone_tsa(r, l))
    elif op == 3:
        print("Volume =", three_d.cone_volume(r, h))

# Sphere
elif choice == 5:
    r = float(input("Enter radius: "))
    if op == 1:
        print("CSA =", three_d.sphere_csa(r))
    elif op == 2:
        print("TSA =", three_d.sphere_tsa(r))
    elif op == 3:
        print("Volume =", three_d.sphere_volume(r))

else:
    print("Invalid choice")