drop table if exists users;
create table users(
    userNumber  int auto_increment primary key,
    userId	varchar(50),
	userName	varchar(50) not null,
    kana	varchar(50) not null,
    password    varchar(300),
    gender  int,
    gitAccount  varchar(50),
    class   varchar(10)
);

INSERT INTO users(userId, userName, kana, password, gender, class) VALUES('kd1297401@st.kobedenshi.ac.jp', '嫁阪雄大', 'ヨメサカカズヒロ', 'test', 0, 'student');
INSERT INTO users(userId, userName, kana, password, gender, class) VALUES('kd1397401@st.kobedenshi.ac.jp', '中川浩太郎', 'ナカガワコウタロウ', 'test', 0, 'student');
INSERT INTO users(userId, userName, kana, password, gender, class) VALUES('kd1497401@st.kobedenshi.ac.jp', '中井禅', 'ナカイゼン', 'test', 0, 'student');
INSERT INTO users(userId, userName, kana, password, gender, class) VALUES('kd1597401@st.kobedenshi.ac.jp', '橋本俊平', 'ハシモトシュンペイ', 'test', 0, 'student');
INSERT INTO users(userId, userName, kana, password, gender, class) VALUES('kd1697401@st.kobedenshi.ac.jp', '林敦啓', 'ハヤシノブヒロ', 'test', 0, 'student');
INSERT INTO users(userId, userName, kana, password, gender, class) VALUES('kd1797401@st.kobedenshi.ac.jp', '山田真豊', 'ヤマダマナト', 'test', 0, 'student');
INSERT INTO users(userId, userName, kana, password, gender, class) VALUES('kd1897401@st.kobedenshi.ac.jp', '米津大也', 'ヨネヅダイヤ', 'test', 0, 'student');

drop table if exists project;
create table project(
    number  int auto_increment primary key,
    name    varchar(100),
    owner   varchar(100),
    start_date  DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_date DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    github  varchar(200),
    googleDrive varchar(200),
    logo    varchar(200)
);

INSERT INTO project(name, owner, github, googleDrive) VALUES('開発支援アプリ', '橋本俊平', 'https://github.com/Sansyou47/kd-develop-2023-team-J13.git', 'https://drive.google.com/drive/folders/0AOWOMUXeZizTUk9PVA');
INSERT INTO project(name, owner, github) VALUES('タスク管理アプリ', '中井禅', 'https://github.com/Sansyou47/team-J13-shooting-range.git');
INSERT INTO project(name, owner, github) VALUES('シフト表作成支援アプリ', '嫁阪雄大', 'https://github.com/Sansyou47/PythonWebApp.git');
INSERT INTO project(name, owner, github) VALUES('マインクラフトサーバー', '嫁阪雄大', 'https://github.com/Sansyou47/Minecraftserver-for-Docker.git');
INSERT INTO project(name, owner) VALUES('音楽再生ソフト', '米津大也');
INSERT INTO project(name, owner) VALUES('音楽編集ソフト', '米津大也');
INSERT INTO project(name, owner) VALUES('音楽リミックスソフト', '米津大也');
INSERT INTO project(name, owner) VALUES('原神聖遺物計算アプリ', '中川浩太郎');
INSERT INTO project(name, owner) VALUES('原神ガチャ課金計算', '中川浩太郎');
INSERT INTO project(name, owner) VALUES('原神キャラクター育成計算', '中川浩太郎');
INSERT INTO project(name, owner) VALUES('原神武器育成計算', '中川浩太郎');
INSERT INTO project(name, owner) VALUES('原神素材計算', '中川浩太郎');
INSERT INTO project(name, owner) VALUES('ビジュネル暗号計算機', '林敦啓');
INSERT INTO project(name, owner) VALUES('ビジュネル暗号解読機', '林敦啓');
INSERT INTO project(name, owner) VALUES('デレステキャラ育成計画表', '中井禅');
INSERT INTO project(name, owner) VALUES('デレステガチャ課金計算', '中井禅');
INSERT INTO project(name, owner) VALUES('デレステガチャ確率計算', '中井禅');
INSERT INTO project(name, owner) VALUES('デレステガチャユニット編成表', '中井禅');
INSERT INTO project(name, owner) VALUES('ブルアカロリボイス集', '橋本俊平');
INSERT INTO project(name, owner) VALUES('ブルアカガチャ課金計算', '橋本俊平');
INSERT INTO project(name, owner) VALUES('ブルアカガチャ確率計算', '橋本俊平');
INSERT INTO project(name, owner) VALUES('ブルアカユニット編成表', '橋本俊平');
INSERT INTO project(name, owner) VALUES('漫画感想共有アプリ', '山田真豊');
INSERT INTO project(name, owner) VALUES('漫画価格一覧アプリ', '山田真豊');
INSERT INTO project(name, owner) VALUES('漫画ガチャ課金計算', '山田真豊');

drop table if exists task;
create table task(
    name    varchar(2000),
    status  int default 2,
    manager varchar(50),
    story varchar(2000),
    sprint  int,
    start_task_date  DATETIME DEFAULT CURRENT_TIMESTAMP,
    finish_task_date DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO task(name, story, sprint) VALUES('プロジェクト選択画面', 'ファイルを一括で管理したい', 1);
INSERT INTO task(name, story, sprint) VALUES('新規プロジェクト設定画面', 'ファイルを一括で管理したい', 1);
INSERT INTO task(name, story, sprint) VALUES('ストーリー登録画面', 'ファイルを一括で管理したい', 1);
INSERT INTO task(name, story, sprint) VALUES('タスク登録画面', 'ファイルを一括で管理したい', 1);
INSERT INTO task(name, story, sprint) VALUES('タスクを受ける画面', 'ファイルを一括で管理したい', 1);
INSERT INTO task(name, story, sprint) VALUES('進捗状況のグラフ化', '各員の進行状況を逐次把握したい', 1);
INSERT INTO task(name, story, sprint) VALUES('タスクボード出力画面', '各員の進行状況を逐次把握したい', 1);

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

drop table if exists project_users;
create table project_users(
    projectName varchar(100),
    userId    varchar(50)
);

INSERT INTO project_users(projectName, userId) VALUES('開発支援アプリ', 'kd1297401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('開発支援アプリ', 'kd1397401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('開発支援アプリ', 'kd1497401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('開発支援アプリ', 'kd1597401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('開発支援アプリ', 'kd1697401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('開発支援アプリ', 'kd1797401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('開発支援アプリ', 'kd1897401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('タスク管理アプリ', 'kd1297401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('タスク管理アプリ', 'kd1397401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('タスク管理アプリ', 'kd1497401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('タスク管理アプリ', 'kd1597401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('タスク管理アプリ', 'kd1697401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('タスク管理アプリ', 'kd1797401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('タスク管理アプリ', 'kd1897401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('マインクラフトサーバー', 'kd1297401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('シフト表作成支援アプリ', 'kd1297401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('原神聖遺物計算アプリ', 'kd1397401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('原神ガチャ課金計算', 'kd1397401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('原神キャラクター育成計算', 'kd1397401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('原神武器育成計算', 'kd1397401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('原神素材計算', 'kd1397401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('ビジュネル暗号計算機', 'kd1697401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('ビジュネル暗号解読機', 'kd1697401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('デレステキャラ育成計画表', 'kd1497401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('デレステガチャ課金計算', 'kd1497401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('デレステガチャ確率計算', 'kd1497401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('デレステガチャユニット編成表', 'kd1497401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('ブルアカロリボイス集', 'kd1597401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('ブルアカガチャ課金計算', 'kd1597401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('ブルアカガチャ確率計算', 'kd1597401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('ブルアカユニット編成表', 'kd1597401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('漫画感想共有アプリ', 'kd1797401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('漫画価格一覧アプリ', 'kd1797401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('漫画ガチャ課金計算', 'kd1797401@st.kobedenshi.ac.jp');