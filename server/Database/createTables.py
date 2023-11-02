from server import conn, cur

def create_tables():
    cmd1 = '''create table users(
        user_id int not null auto_increment primary key,
        name varchar(20),
        email varchar(50) not null,
        phone varchar(10) not null,
        password varchar(20) not null)'''
    
    cmd2 = '''create table saved_news(
    user_id int not null,
    news_headline varchar(100) not null,
    img_url varchar(100) not null,
    news_body varchar(300) not null,
    news_url varchar(100) not null,
    foreign key (user_id) references users(user_id)
    )'''

    cmd3 = '''create table user_preferences(
    user_id int not null,
    Politics int not null default 0,
    Sports int not null default 0,
    Technology int not null default 0,
    Entertainment int not null default 0,
    National int not null default 0,
    foreign key (user_id) references users(user_id)
    )'''
    cur.execute(cmd1)
    cur.execute(cmd2)
    cur.execute(cmd3)
    conn.commit()
    print("table created")
