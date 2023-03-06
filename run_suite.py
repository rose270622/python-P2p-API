import app,time
import unittest

from lib.HTMLTestRunner_PY3 import HTMLTestRunner

from scripts.account import Account
from scripts.approve import Approve
from scripts.login import Login
from scripts.tender import Tender
from scripts.tender_process import TenderProcess

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(Login))
suite.addTest(unittest.makeSuite(Approve))
suite.addTest(unittest.makeSuite(Account))
suite.addTest(unittest.makeSuite(Tender))
suite.addTest(unittest.makeSuite(TenderProcess))

file = app.BASE_DIR + "/report/report{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
with open(file, "wb")as f:
    runner = HTMLTestRunner(f, title="p2p金融接口测试", description="test")
    runner.run(suite)



