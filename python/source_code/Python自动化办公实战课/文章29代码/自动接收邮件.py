import imaplib
import email

conn = imaplib.IMAP4_SSL(host="imap.qq.com", port = 993)

conn.login("username@qq.com","password")

# 查看都有哪些文件夹,邮件默认放在INBOX文件夹中
print(conn.list())

# 默认为INBOX
conn.select("INBOX")

# 搜索邮件，ALL为全部，可以按照发件人使用FROM过滤，也可以使用日期过滤
_, data = conn.search(None, 'unseen') 
print(data)
for mailid in data[0].decode().split(" "):
    # 取回每一封未读邮件的内容
    # data = [b'1 2 3 4 5']
    _, maildata = conn.fetch(str(mailid), '(RFC822)')

    # 对每一封邮件的内容进行解析
    msg = email.message_from_string(maildata[0][1].decode('utf-8'))
    # 取得标题
    subject_tmp = msg.get('subject')
    # 为标题解码
    sj_decode = email.header.decode_header(subject_tmp)[0][0]
    #打印每一封标题
    subject = sj_decode.decode('utf-8')
    print(subject)



    # 将邮件标记为已读
    conn.store(mailid, '+FLAGS','\\seen')