# File Count Inspector
指定したディレクトリ内(サブディレクトリ含む)のファイル数を確認して、syslogで出力するやつ

# 使い方
## 下準備
1. `file_count_inspector.py`内の`dirslist`に、監視対象のディレクトリの絶対パスをリスト型で記述する
    ```
    # 集計対象のディレクトリリスト
    dirslist=['/tmp', '/usr/lib']
    ```
2. `file_count_inspector.py`を任意のスクリプトディレクトリに配置する

3. `ServiceFile¥file_count_inspector.service`内の項目を、設置したスクリプトディレクトリパスや実行ユーザを修正する
    ```
    [Service]
    ExecStart=/usr/bin/python3 file_count_inspector.py
    WorkingDirectory=/home/script-user/file_count_inspector
    User=script-user
    ```

4. `ServiceFile¥file_count_inspector.service`内の項目を、実行したい時間間隔に修正する。
    ```
    [Timer]
    OnCalendar= *-*-* *:0/5:00
    ```

## インストール
1. `ServiceFile`内の.serviceおよび.timerファイルを、`/etc/systemd/system/`に配置する

2. systemdデーモンをリロードする。
    ```
    systemctl daemon-reload
    ```

3. .timerをstartおよびenableする
    ```
    systemctl start file_count_inspector.timer
    systemctl enable file_count_inspector.timer
    ```
