def gcd(m,n):
    r = m%n
    if r == 0:
        return n
    return gcd(n,r)

#this needs debugging
def dyn_gcd(m,n):
    m_s = [m]
    n_s = [n]
    r_s = [m%n]
    while r_s[-1] != 0:
        r_s.append( m_s[-1]%n_s[-1] )
        if r_s[-1] == 0:
            return n_s[-1]
        m_s.append(n_s[-1])
        n_s.append(r_s[-1])

print gcd(30,5)
