def multivariable_division(f, lfi, R):
    # paso 1
    r = R.zero()
    p = f
    s = len(lfi)
    q = []
    for i in range(0, s):
        q.append(R.zero())

    # paso 2
    while p != R.zero():

        # paso 3
        i_chosen = None
        for i in range(0, s):
            ltp = R.lt(p)
            ltfi = R.lt(lfi[i])

            # si el resultado pertenece al cuerpo de fracciones de R, el R.mod falla
            # y entonces capturamos la excepcion y deducimos que no es divisible
            try:
                if R.mod(ltp, ltfi) == R.zero():
                    i_chosen = i
                    break
            except ArithmeticError:
                continue

        if i_chosen is not None:
            ltp = R.lt(p)
            q[i_chosen] = q[i_chosen] + R.quo(ltp, ltfi)
            p = p - R.mul(R.quo(ltp, ltfi), lfi[i_chosen])

        else:
            r = r + ltp
            p = p - ltp

    # paso 4
    return q, r
