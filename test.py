# !/user/bin/env python3
# -*- coding: utf-8 -*-

def bq_code():
    # 补全客户编号
    with open("./zn.csv", encoding="utf-8", mode='r') as f:
        for i in f.readlines():
            a = i.split(",")[0]
            print("000" + a)


def filter_code():
    # 账期去重
    with open("./zn_all.csv", encoding="utf-8", mode='r') as f:
        result = dict()
        for i in f.readlines():
            a = i.strip().split(",")
            if a[1] not in result:
                result[a[1]] = a

        for i in result.values():
            # print(",".join(i))
            print(i[3])


def filter_hz():
    sheet4_code = list()
    with open("./hz_gs.csv", encoding="utf-8", mode='r') as f:
        for i in f.readlines():
            sheet4_code.append(i.strip())

    hz = 0
    count = 0

    with open("./bad_hz.csv", encoding="utf-8", mode='r') as f:
        for i in f.readlines():
            a = i.strip().split(",")
            if a[3] in sheet4_code and a[2] == "2000":
                print(a[2])
                hz += float(a[8])
                count += 1
    print(hz)
    print(count)


if __name__ == '__main__':
    filter_hz()
    # PATENTES TALGO, S.L.U.(IN
