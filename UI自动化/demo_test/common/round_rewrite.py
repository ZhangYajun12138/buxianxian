def round_rewrite(data,i=0):
    '''
    四舍五入,解决round(7.35)=7.3的问题
    :param data:
    :param i: 保留的位数,默认0
    :return:
    '''
    if not isinstance(i,int): #i不是整数报错
        raise TypeError('the second param must be int')
    else:
        mi = 10**i
        datax = data*mi
        f = datax - int(datax)
        if f >=0.5:
            res = (int(datax)+1)/mi
        elif f <=-0.5:
            res = (int(datax)-1)/mi
        else:
            res = int(datax)/mi

        if i <= 0:
            res = int(res)
    return res


# data = 1.365
# print(round(data,2))
# print(round_rewrite(data,2))