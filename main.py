import pytest, time, os, sys
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib



if __name__ == '__main__':
    date = time.strftime("%Y-%m-%d", time.localtime())
    alluredir = '--alluredir=allure-results/' + date
    allure_report = 'allure generate allure-results/' + date + '/ -o allure-reports/' + date + '/ --clean'

    pytest.main(['-q', '-s', alluredir, '--clean-alluredir'])
    os.system(allure_report)  # 生成html的测试报告
    report_url = 'http://localhost:8000/allure-reports/' + date + '/'
    print(report_url)



