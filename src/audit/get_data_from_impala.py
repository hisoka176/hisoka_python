#encoding:utf-8
import sys
import datetime
import os

# @version 1.0
# @author libin
# @function 该脚本的主要作用是按天从impala数据库当中拉取数据
def main():
    start_date = '2017-01-01'
    start_date = datetime.datetime.strptime(start_date,'%Y-%m-%d')
    end_date = '2017-07-03'
    end_date = datetime.datetime.strptime(end_date,'%Y-%m-%d')
    next_date = start_date
    while (end_date - next_date).days > 0:
        string_date = next_date.strftime('%Y-%m-%d')
        load_data(string_date)

        next_date = next_date + datetime.timedelta(days=1)

def load_data(data):
    string = """
    impala-shell -i 10.30.1.88 -k -B -q "
    set request_pool=root.bi.da;
    select * from tlbb3d_audit.audit_chat_info where dt='{date}'; " -o ./audit_data/audit_{date}.txt --print_header --output_delimiter=',' """

    os.system(string)