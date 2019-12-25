

def chinese_reminder(m_list, u_list, phi, reciprocal, mul, add, sub):
    gamma_list = [12121]
    for k in range(1,len(m_list)):
        product = phi(m_list[k],m_list[0])
        for i in range(1,k):
            product = phi(m_list[k], mul(product,m_list[i]))
        gamma_list.append(reciprocal(product,m_list[k]))
    v_list = [u_list[0]]
    for k in range(1,len(m_list)):
        temp = v_list[k - 1]
        for j in range(k - 2, -1, -1):
            temp = phi(m_list[k], add(v_list[j],mul(temp,m_list[j])))
        v_list.append(phi(m_list[k],mul(sub(u_list[k],temp),gamma_list[k])))
    u = v_list[len(v_list) - 1]
    for k in range(len(v_list)-2, -1, -1):
        u = add(mul(u,m_list[k]),v_list[k])
    return u