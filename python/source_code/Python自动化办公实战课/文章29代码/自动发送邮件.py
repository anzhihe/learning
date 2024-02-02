import yagmail
conn = yagmail.SMTP(
        user="username@qq.com", 
        password="password",
        host="smtp.qq.com",
        port=465
        )
content = "内容填充"
body = f"模版 {content}"

conn.send("receiver@qq.com", "主题", body, "one.jpg")