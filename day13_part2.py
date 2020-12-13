#!/usr/bin/python3

import loader
import functools

inp = loader.string_list("input_day13")

raw_bus_list = inp[1].split(",")

# If a bus with a given ID (bus_id) must leave i minutes after the desired
# timestamp t, then that means (t + i) is equivalent to 0 modulo bus_id, so t
# is equivalent to negative i modulo bus_id. Note: -i modulo bus_id is tracked
# as a positive number by convention.
data = []
for i in range(len(raw_bus_list)):
    if raw_bus_list[i] == "x":
        continue
    bus_id = int(raw_bus_list[i])
    data.append({"modulo": bus_id,
                 "t_is": (-1 * i) % bus_id})


def modInverse(a, m):
    """
    Finds the multiplicative inverse of a modulo m when a is relatively prime to
    m. That is, a * modInverse(a, m) is equivalent to 1 modulo m. 

    Copied from:
    https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
    """
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1): 
        return 0
  
    while (a > 1): 
  
        # q is quotient 
        q = a // m 
  
        t = m 
  
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
  
        # Update x and y 
        y = x - q * y 
        x = t 
  
    # Make x positive 
    if (x < 0): 
        x = x + m0 
  
    return x 

def r(datum1,datum2):
    """
    Takes a system of two modular congruences and combines them into a single
    modular congruence with the same solutions.

    Example input:
    t is equivalent to v1 mod m1
    t is equivalent to v2 mod m2

    The combination process is as follows:
    
    Multiply each value by the other modulus:
    m2 * t is equivalent to m2 * v1 mod m2 * m1
    m1 * t is equivalent to m1 * v2 mod m1 * m2

    Add the two together:
    m2 * t + m1 * t is equivalent to m2 * v1 + m1 * v2 mod m1 * m2

    Combine like terms:
    (m1 + m2) * t is equivalent to m2 * v1 + m1 * v2 mod m1 * m2

    Find the multiplicative inverse n of (m1+m2) mod m1*m2. This is possible
    because all of the starting modulii are primes, guaranteeing that (m1+m2) 
    will always be relatively prime to m1*m2.

    Fifth, multiply both sides by n:
    n * (m1+m2) * t is equivalent to (m2*v1+m1*v2)*n mod m1*m2

    Sixth, simplify using n*(m1+m2) = 1 mod m1*m2:
    t is equivalent to (m2*v1+m1*v2)*n mod m1*m2

    Seventh, ensure that the new constant is the smallest nonnegative number 
    equal to (m2*v1+m1*v2)*n mod m1*m2. This ensures the final constant can be 
    used directly.
    """
    modulo = datum1["modulo"] * datum2["modulo"]
    t_is = (datum1["modulo"]*datum2["t_is"]+
            datum2["modulo"]*datum1["t_is"]) * modInverse(datum1["modulo"]+datum2["modulo"],modulo)
    t_is = t_is % modulo
    return {"modulo": modulo,
            "t_is": t_is}

final = functools.reduce(r,data)
print(final["t_is"])
