# !/user/bin/env python3
# -*- coding: utf-8 -*-


"""
总利息=（分期数+1)×贷款总额×月利率÷2，
每期月供=每月应还本金+每月应还利息，
每月应还本金=贷款总额÷分期数，
每月应还利息=[贷款总额-每月应还本金*（当期数-1）]*月利率，
月利率=年利率÷12个月。

各住房公积金业务受托银行：
根据中国人民银行关于下调个人住房公积金贷款利率规定，现就住房公积金贷款利率调整有关事项通知如下：
一、自2024年5月18日起，下调个人住房公积金贷款利率0.25个百分点，
5年以下（含5年）首套个人住房公积金贷款利率由2.6%调整为2.35%，
5年以上首套个人住房公积金贷款利率由3.1%调整为2.85%。
5年以下（含5年）第二套个人住房公积金贷款利率由3.025%调整为2.775%，
5年以上第二套个人住房公积金贷款利率由3.575%调整为3.325%。

二、2024年5月18日（含）后发放的个人住房公积金贷款利率，按调整后的个人住房公积金贷款利率执行。

三、2024年5月18日前发放的未到期个人住房公积金贷款，自2025年1月1日起按调整后的相应档次利率执行。

武汉住房公积金管理中心
2024年5月17日
"""


class HouseLoanCalculate:
    def __init__(self, total_amount, months):
        self.total_amount = total_amount
        self.months = months
        self.interest_rate = 2.85 / 100

    @property
    def interest_rate_month(self):
        return self.interest_rate / 12

    @property
    def gross_interest(self):
        return (self.months + 1) * self.total_amount * self.interest_rate_month / 2

    @property
    def principal_repayments_monthly(self):
        return self.total_amount / self.months

    @property
    def interest_payable_monthly(self):
        """
        每月应还利息=[贷款总额-每月应还本金*（当期数-1）]*月利率，
        :return:
        """
        return (self.total_amount - self.principal_repayments_monthly * (self.months - 1)) * self.interest_rate_month


if __name__ == '__main__':
    total_amount = 1200000
    total_month = 12 * 30
    rate = HouseLoanCalculate(total_amount, total_month)
    print(rate.gross_interest)
    print(rate.principal_repayments_monthly, rate.interest_payable_monthly)
    print(rate.principal_repayments_monthly + rate.interest_payable_monthly)


