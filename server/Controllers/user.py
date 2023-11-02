import mysql.connector as sqltor
conn  = sqltor.connect(host="localhost", user="root", password="66121200", database="FEDRAFEED")
cur = conn.cursor()
def  insertUser(user_data):
    try:
        name = user_data['name']
        email = user_data['email']
        phone = user_data['phone']
        password = user_data['password']
        cmd1 = "insert into users(name,email,phone,password) values(%s, %s, %s, %s)"
        cmd2 = 'select user_id from users where phone = %s'
        cmd3 = 'insert into user_preferences (user_id) values(%s)'

        data = (name,email,phone,password)
        cur.execute(cmd1,data)
        cur.execute(cmd2,(phone,))
        output = cur.fetchone()

        cur.execute(cmd3,(output[0],))
        conn.commit()
        return output[0]
    except Exception as e:
        print("Error :",str(e))

def insert_saved_news(news_data):
    try:
        user_id = news_data['user_id']
        news_headline = news_data['news_headline']
        img_url = news_data['img_url']
        news_body = news_data['news_body']
        news_url = news_data['news_url']
        cmd = "insert into saved_news(user_id,news_headline,img_url,news_body,news_url) values(%s, %s, %s, %s, %s)"
        data = (user_id,news_headline,img_url,news_body,news_url)
        cur.execute(cmd,data)
        conn.commit()
        print("Data inserted")

    except Exception as e:
        print("Error :",str(e))

def insert_user_preferences(user_preferences_data):
    try:
        user_id = user_preferences_data['user_id']
        category = user_preferences_data['category']
        cmd = f"UPDATE user_preferences SET {category} = {category} + 1 WHERE user_id = %s"
        cur.execute(cmd,(user_id,))
        conn.commit()
        print("Data inserted")
    except Exception as e:
        print("Error :",str(e))

