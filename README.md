# Primality-test
Miller-Rabin primality test is probalblistic test used to determine whether a given number(odd) is probably prime or composite.
If p is the given odd number we can write it as p = (2^K)*m +1 .
Consider 'a' such that 1<=a<p ,if a^m(mod p) = 1 or-1 then p is probably prime.
now for any i = 1,2,...k-1
if a^((2^i)m)(mod p) = -1 then p is probably prime
If none of the above condition holds then 'p' is composite and 'a' is a witness that 'p' is composite.
And if 'a' is not a witness then p is probably prime
