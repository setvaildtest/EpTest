#!/root/.jenkins/workspace/api_test/venv python
# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/22 0022
@File : run_all_discover_cases.py
@describe : 执行所有鉴权v2.0case

"""

import os
import unittest
from time import strftime, localtime, time
from ep_common import HTMLTestReportCN
from ep_common.SmtpUtil import send_mail, newReport


def run_all_discover_cases():
    case_path = os.path.join(os.getcwd(), "testCases")
    print(case_path)
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern="test*.py",
                                                   top_level_dir=None)
    # print(discover)
    return discover


# run_all_discover_cases()
if __name__ == "__main__":
    now = strftime("%Y%m%d%H%M%S", localtime(time()))
    report_path = os.path.abspath("testReport")
    file = report_path + "\\" + now + '_' + "Epass_api_test_report_2.0.html"
    print(file)
    with open(file, "wb") as f:
        runner = HTMLTestReportCN.HTMLTestRunner(stream=f,
                                                 # verbosity=2,
                                                 title="Epass_Api_Test_Result_v2.0",
                                                 tester="王晶",
                                                 description="-" * 350)
        runner.run(run_all_discover_cases())
        f.close()
        new_report = newReport(report_path)
        # send_mail(new_report)
