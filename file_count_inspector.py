import os
import syslog

# 集計対象のディレクトリリスト
dirslist=['/tmp', '/usr/lib']

def main():
    counter_tmp=[]
    # ディレクトリのリスト内の要素ごとにファイル数を集計し二次元リストに格納する
    for dir in dirslist:
        counter_tmp.append([dir, file_count(dir)])

    output_log_info(create_message(counter_tmp))

# 与えられたディレクトリ配下のファイル数を集計する関数
def file_count(dir):
    file_counter=0
    for dirpath, dirname, filepath in os.walk(dir):
        file_counter+=len(filepath)
    return file_counter

# メッセージを組み立てる関数
def create_message(counter_msg):
    message=''
    for count in counter_msg:
        message += count[0] + '=' + str(count[1]) +', '
    return message


# LOCAL0.INFOで引数msgのsyslogメッセージを送信する関数
def output_log_info(msg):
    # 第１引数:アプリケーション名, 第２引数:ログオプション, 第３引数:ファシリティ
    syslog.openlog('file-count-inspector',syslog.LOG_PID,syslog.LOG_LOCAL0)
    # INFOレベルでmsgを送信する
    syslog.syslog(syslog.LOG_INFO,msg)
    syslog.closelog()

if __name__ == "__main__":
    main()
