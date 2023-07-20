#### A quaternion's library implemented in python

<pre>
Quaterion symbolic definitions and operations:

pure:           (0, qxi, qyj, qzk)
real:           (r, 0, 0, 0)
modulus:        √(r²+qx²+qy²+qz²)
conjugate:      (r, -qx, -qy, -qz)
versor:         √(r²+qx²+qy²+qz²) = 1
scalar product: a*q = (a*r, a*qx, a*qy, a*qz)
trace:          q+q' = 2r
negative:       (-r, -qx, -qy, -qz)
inverse:        1/q = q'/(q*q') = q'/|q|²
add:            q1 + q2
sub:            q1 - q2
product:        q1 * q2 = (r1,u1)*(r2,u2) = (r1r2-u1·u2,r1u2+r2u1+u1xu2)
division:       q1 / q2
exp:            e^q = e^r*(cos(|u|) + u*sin(|u|)/|u|)
log:            ln(q) = ln(|q|) + u/|u|*cos-¹(r/|q|)
rotation:       v*p*v-¹
</pre>