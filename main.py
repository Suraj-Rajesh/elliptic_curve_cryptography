from ecc.ecc import EllipticCurve
from ecc.galois_field.galois_field import GaloisField
from ecc.galois_field.generic import is_prime

points = list()
orders = list()

top_k_points = list()
top_k_orders = list()

gf103 = GaloisField(103)

for a in range(gf103.p):
    for b in range(gf103.p):
        elliptic_curve = EllipticCurve(a, b, 103)

        order = elliptic_curve.order_of_curve()
        if is_prime(order):
           orders.append(order)
           points.append((a, b))

print(max(orders))

for i in range(10):
    maximum = max(orders)
    maximums_index = orders.index(maximum)

    top_k_orders.append(maximum)
    top_k_points.append(points[maximums_index])
    
    del orders[maximums_index]
    del points[maximums_index]

# Print top-10
for i in range(10):
    print("{} : {}".format(top_k_points[i], top_k_orders[i]))
