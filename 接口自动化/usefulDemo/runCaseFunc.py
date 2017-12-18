__author__ = 'Administrator'
def geturl(cell_value, conf):
    if cell_value == "register":
        request_name = "register"
        url = conf.get("url", "register")

    elif cell_value == "login":
        url = conf.get("url", "login")
        request_name = "login"

    elif cell_value == "recharge":
        request_name = "recharge"
        url = conf.get("url", "recharge")

    elif cell_value == "withdraw":
        request_name = "withdraw"
        url = conf.get("url", "withdraw")

    elif cell_value == "list":
        request_name = "list"
        url = conf.get("url", "list")

    elif cell_value == "bidLoan":
        request_name = "bidLoan"
        url = conf.get("url", "bidLoan")
    return url, request_name