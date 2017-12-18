def http_req_test(test_url, test_data, http, flag):
    #根据传入的flag的值确定执行GET请求还是POST请求
    if (flag == '0') | (flag == 0):
        return http.get_req(test_url, test_data)

    if (flag == '1') | (flag == 1):
        return http.post_req(test_url, test_data)