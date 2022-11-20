# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Fri Oct 28 11:48:34 2022

# @author: gakusei053
# """

# # ソケットライブラリ取り込み
# import socket
# # スレッドライブラリ取り込み
# import threading
# # db参照
# import sqlite3

# # サーバーIPとポート番号
# IPADDR = "127.0.0.1"
# PORT = 49152

# # AF_INET：IPv4形式でソケット作成(省略可)
# sock_sv = socket.socket(socket.AF_INET)
# # IPアドレスとポート番号でバインド、タプルで指定
# sock_sv.bind((IPADDR, PORT))
# # サーバー有効化
# sock_sv.listen()

# # クライアントのリスト
# client_list = []

# # データ受信ループ関数
# def recv_client(sock, addr):
#     while True:
#         try:
#             data = sock.recv(1024)
#             # 受信データ0バイト時は接続終了
#             if data == b"":
#                 break

#             print("$ say client:{}".format(addr))

#             # 受信データを全クライアントに送信
#             for client in client_list:
               
#                # 学籍番号　XXXXX
#                 col1 =  data[:5]
#                # 日時分　ｄｄTTMM
#                 col2 =  data[6:]
#                 col_list = [col1,col2]
               

# #example.dbを使用するデータベースに入れ替えてください

#                 conn = sqlite3.connect('example.db')
#                 c = conn.cursor()
# #usersをテーブル名に入れ替えてください
#                 c.execute('SELECT * FROM users')
#                 flag = 0
#                 # 学籍番号と時刻が一致しているか確認　時刻は今のままだと顔認証した時間と完全一致しないといけないのでなんとかしてください
#                 for row in c:
#                     if c[row] != col_list[row]:
#                         flag = 1
#  # データベースへのアクセスが終わったら close する
#                 conn.close()
# #example.dbを使用するデータベースに入れ替えてください
#                 if flag == 0:
#                     conn = sqlite3.connect('example.db')
#                     c = conn.cursor()

# #usersを使用するテーブル名に入れ替えてください
#                     c.execute('SELECT * FROM users')
#                     for num in c:
#                         plus = int(c[num])+1
                    
#                     # データ更新
#                     # fooテーブルのnameカラムの形で書きかえてください
#                     # クエリを作成
#                     sql = ("""
#                            UPDATE  foo
#                            SET     name = %s
#                            """)

#                     param = (str(plus))
       
#                     # updateを実行
#                     c.execute(sql, param)

#                     # 挿入した結果を保存（コミット）する
#                     conn.commit()

#                     conn.close()
                  
                
                
                

#          # 切断時の例外を捕捉したら終了
#         except ConnectionResetError:
#             break

#     # クライアントリストから削除
#     client_list.remove((sock, addr))
#     print("- close client:{}".format(addr))

#     # クライアントをクローズ処理
#     sock.shutdown(socket.SHUT_RDWR)
#     sock.close()

# # クライアント接続待ちループ
# while True:
#     # クライアントの接続受付
#     sock_cl, addr = sock_sv.accept()
#     # クライアントをリストに追加
#     client_list.append((sock_cl, addr))
#     print("+ join client:{}".format(addr))

#     # スレッドクラスのインスタンス化
#     thread = threading.Thread(target=recv_client, args=(sock_cl, addr))
#     # スレッド処理開始
#     thread.start()