

def chinese_reminder(m_list, u_list, R):

    gamma_list = [None]

    for k in range(1,len(m_list)):
        product = R.phi(m_list[k],m_list[0])
        for i in range(1,k):
            product = R.phi(m_list[k], R.mul(product,m_list[i]))
        gamma_list.append(R.reciprocal(product,m_list[k]))
    v_list = [u_list[0]]

    for k in range(1,len(m_list)):
        temp = v_list[k - 1]
        for j in range(k - 2, -1, -1):
            temp = R.phi(m_list[k], R.add(v_list[j], R.mul(temp,m_list[j])))
        v_list.append(R.phi(m_list[k], R.mul(R.sub(u_list[k],temp),gamma_list[k])))
    u = v_list[len(v_list) - 1]

    for k in range(len(v_list)-2, -1, -1):
        u = R.add(R.mul(u,m_list[k]),v_list[k])
    return u