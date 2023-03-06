import app


class TenderApi:
    def __init__(self):
        self.loan_url = app.BASE_URL + "/common/loan/loaninfo"
        self.tender_url = app.BASE_URL + "/trust/trust/tender"
        self.tender_list_url = app.BASE_URL + "/loan/tender/mytenderlist"


    def loan(self,session,id="1153"):
        data = {"id": id}
        response = session.post(self.loan_url, data=data)
        return response

    def tender(self,session, id="1153", depositCertificate="-1", amount="1000"):
        data = {"id": id, "depositCertificate": depositCertificate, "amount": amount}
        response = session.post(self.tender_url, data=data)
        return response

    def tender_list(self,session,page="1",status="tender"):
        data = {"page": page,
                "status": status}
        response = session.post(self.tender_list_url, data=data)
        return response