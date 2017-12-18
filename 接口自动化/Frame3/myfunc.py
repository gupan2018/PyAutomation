__author__ = 'Administrator'

#组装查询sql语句
def assemble_sql(mode, str, sql):
    case_list = mode.getList()
    case_len = len(case_list)

    #组装查询条件
    str = "WHERE case_id = %s"%case_list[0]
    for i in range(1, case_len):
        str += " OR case_id = %s"%case_list[i]

    #组装查询sql
    sql = 'SELECT * FROM test_data %s'%str#组装sql语句
    return sql

#存储查询到的数据
def store_data(res, test_url, test_method, http_data):
    test_url.append(res[3])
    test_method.append(res[1])

    mobile_phone = res[4]
    regname = res[5]

    data = {
        "mobilephone":mobile_phone,
        "regname":regname,
        "pwd":"123456"
    }

    http_data.append(data)