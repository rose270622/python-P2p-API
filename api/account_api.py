import app


class AccountApi:
    def __init__(self):
        self.account_url = app.BASE_URL + "/trust/trust/register"
        self.recharge_url = app.BASE_URL + "/trust/trust/recharge"

    def open_account(self, session):
        response = session.post(self.account_url)
        return response

    def recharge(self, session, paymenType="chinapnrTrust",
                 amount="10000",
                 formStr="reForm",
                 valicode="8888"):
        data = {"paymentType": paymenType,
              "amount": amount,
              "formStr": formStr,
              "valicode": valicode
              }
        response = session.post(self.recharge_url, data=data)
        return response