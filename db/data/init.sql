drop table if exists users;
create table users(
    userId	varchar(50) primary key,
	userName	varchar(50) not null,
    kana	varchar(50) not null,
    password    varchar(300),
    gender  int,
    gitAccount  varchar(50),
    class   varchar(10)
);

INSERT INTO users(userId, userName, kana, gender, class) VALUES('kd1297401@st.kobedenshi.ac.jp', '嫁阪雄大', 'ヨメサカカズヒロ', 0, 'student');
INSERT INTO users(userId, userName, kana, gender, class) VALUES('kd1397401@st.kobedenshi.ac.jp', '中川浩太郎', 'ナカガワコウタロウ', 0, 'student');
INSERT INTO users(userId, userName, kana, gender, class) VALUES('kd1497401@st.kobedenshi.ac.jp', '中井禅', 'ナカイゼン', 0, 'student');
INSERT INTO users(userId, userName, kana, gender, class) VALUES('kd1597401@st.kobedenshi.ac.jp', '橋本俊平', 'ハシモトシュンペイ', 0, 'student');
INSERT INTO users(userId, userName, kana, gender, class) VALUES('kd1297401@st.kobedenshi.ac.jp', '林敦啓', 'ハヤシノブヒロ', 0, 'student');
INSERT INTO users(userId, userName, kana, gender, class) VALUES('kd1297401@st.kobedenshi.ac.jp', '山田真豊', 'ヤマダマナト', 0, 'student');
INSERT INTO users(userId, userName, kana, gender, class) VALUES('kd1297401@st.kobedenshi.ac.jp', '米津大也', 'ヨネヅダイヤ', 0, 'student');

drop table if exists project;
create table project(
    number  int auto_increment primary key,
    name    varchar(100),
    owner   varchar(100),
    start_date  DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_date DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO project(name, owner) VALUES('開発支援アプリ', '橋本俊平');
INSERT INTO project(name, owner) VALUES('タスク管理アプリ', '中井禅');
INSERT INTO project(name, owner) VALUES('シフト表作成支援アプリ', '嫁阪雄大');
INSERT INTO project(name, owner) VALUES('マインクラフトサーバー', '嫁阪雄大');

drop table if exists task;
create table task(
    name    varchar(2000),
    status  int default 2,
    manager varchar(50),
    project varchar(100),
    sprint  int
);

INSERT INTO task(name, project, sprint) VALUES('プロジェクト選択画面', '開発支援アプリ', 1);
INSERT INTO task(name, project, sprint) VALUES('新規プロジェクト設定画面', '開発支援アプリ', 1);
INSERT INTO task(name, project, sprint) VALUES('ストーリー登録画面', '開発支援アプリ', 1);
INSERT INTO task(name, project, sprint) VALUES('タスク登録画面', '開発支援アプリ', 1);
INSERT INTO task(name, project, sprint) VALUES('タスクを受ける画面', '開発支援アプリ', 1);
INSERT INTO task(name, project, sprint) VALUES('進捗状況のグラフ化', '開発支援アプリ', 1);
INSERT INTO task(name, project, sprint) VALUES('タスクボード出力画面', '開発支援アプリ', 1);

drop table if exists story;
create table story(
    name    varchar(2000),
    project varchar(100)
);

INSERT INTO story(name, project) VALUES('ファイルを一括で管理したい', '開発支援アプリ');
INSERT INTO story(name, project) VALUES('各員の進行状況を逐次把握したい', '開発支援アプリ');

drop table if exists class;
create table class(
    name    varchar(20)
);

INSERT INTO class(name) VALUES('student');
INSERT INTO class(name) VALUES('teacher');
INSERT INTO class(name) VALUES('company');
INSERT INTO class(name) VALUES('recruiter');
