drop table if exists users;
create table users(
    userNumber  int auto_increment primary key,
    userId	varchar(50),
	userName	varchar(50) not null,
    kana	varchar(50) not null,
    password    varchar(2000),
    gender  int,
    gitAccount  varchar(50),
    userIcon    varchar(200),
    class   varchar(10)
);

INSERT INTO users(userId, userName, kana, password, gender, gitAccount, userIcon, class) VALUES('kd1297401@st.kobedenshi.ac.jp', '嫁阪雄大', 'ヨメサカカズヒロ', 'scrypt:32768:8:1$VZxfAUUjh2pszMZt$17489509bff761a9785b4970d2a23199b2c8f12ad146ffe7a2445ba2c6ab7a28c538e40547cff7e77c27362c85bbfa4c66a9ddcfe1891cb3fd4235a6370aa21f', 0, 'Sansyou47', 'thumb.png', 'student');
INSERT INTO users(userId, userName, kana, password, gender, class) VALUES('kd1323949@st.kobedenshi.ac.jp', '中川浩太郎', 'ナカガワコウタロウ', 'scrypt:32768:8:1$Yi8rt9mSA9ZMky5s$12347afc795e57ca589ca92a83f92b83824f4d818487e06859fc01d939a896a0ccf1788d1c591d6ee71fa6238b34052a87f6b0e9d0e8814cd6b0119c6229d9b7', 0, 'student');
INSERT INTO users(userId, userName, kana, password, gender, class) VALUES('kd1293049@st.kobedenshi.ac.jp', '中井禅', 'ナカイゼン', 'scrypt:32768:8:1$onB8u37TCPnrwQLh$f3861a96e6d7a9aa53a8221d0e7f0ba66a60b30fd7367d88a454e566fdc56a63e70990c2422b76d8f7f881c45df8fa6517a62c05564359c59441cb48efee651d', 0, 'student');
INSERT INTO users(userId, userName, kana, password, gender, class) VALUES('kd1299164@st.kobedenshi.ac.jp', '橋本俊平', 'ハシモトシュンペイ', 'scrypt:32768:8:1$byfc1LS3xJyTrxCB$6739f9c929beb23c0549c298f275948cf0506df6db47d01475d5f605f4f31f0ccdf610e7e64df649351f2a98f1f77b6165ecfdb9614b2ee3cdb143c5db9ebae8', 0, 'student');
INSERT INTO users(userId, userName, kana, password, gender, class) VALUES('kd1334632@st.kobedenshi.ac.jp', '林敦啓', 'ハヤシノブヒロ', 'scrypt:32768:8:1$YFOF58vV6KrvfaJ9$91f033aaf573cdee4205125032428971047de6be96d4a215f66ca0a3052ebdc7887266becc850e0d94665c4aa73a8cd51d928ab7633d29b858e8886c72057f52', 0, 'student');
INSERT INTO users(userId, userName, kana, password, gender, class) VALUES('kd1334992@st.kobedenshi.ac.jp', '山田真豊', 'ヤマダマナト', 'scrypt:32768:8:1$ZM50DjEFuu3yhuo7$e53f0e89ef03af15855237b35f41f87eefc29ad0152f0dba806e65918e0ad35ef9d8a94e41d981bd1e6718d28f5dc3dd66c629498324bfa0eae7d7437338bb50', 0, 'student');
INSERT INTO users(userId, userName, kana, password, gender, class) VALUES('kd1329246@st.kobedenshi.ac.jp', '米津大也', 'ヨネヅダイヤ', 'scrypt:32768:8:1$hFMD67rQ4UYQE2W6$f945fdf490bfe657b987b8d1d887dba2e988ef54573728a1e14863520f457edd6f7650ed2ba8e7acca4b84ed22f20595a3194b7c6786e8a21bfcb9c18fc4f930', 0, 'student');

drop table if exists project;
create table project(
    projectNumber  int auto_increment primary key,
    name    varchar(100),
    owner   varchar(100),
    start_date  DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_date DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    finish_date DATETIME,
    github  varchar(200),
    googleDrive varchar(200),
    logo    varchar(200)
);

INSERT INTO project(name, owner, finish_date, github, googleDrive, logo) VALUES('開発支援アプリ', '橋本俊平', '2024-01-15', 'https://github.com/Sansyou47/kd-develop-2023-team-J13.git', 'https://drive.google.com/drive/folders/0AOWOMUXeZizTUk9PVA', 'bird.png');
INSERT INTO project(name, owner, finish_date, github) VALUES('タスク管理アプリ', '中井禅', '2024-01-15', 'https://github.com/Sansyou47/team-J13-shooting-range.git');
INSERT INTO project(name, owner, finish_date, github) VALUES('シフト表作成支援アプリ', '嫁阪雄大', '2024-01-15', 'https://github.com/Sansyou47/PythonWebApp.git');
INSERT INTO project(name, owner, finish_date, github, logo) VALUES('マインクラフトサーバー', '嫁阪雄大', '2024-01-15', 'https://github.com/Sansyou47/Minecraftserver-for-Docker.git', 'minecraft.png');
INSERT INTO project(name, owner, finish_date) VALUES('音楽再生ソフト', '米津大也', '2024-01-15');
INSERT INTO project(name, owner, finish_date) VALUES('音楽編集ソフト', '米津大也', '2024-01-15');
INSERT INTO project(name, owner, finish_date) VALUES('音楽リミックスソフト', '米津大也', '2024-01-15');
INSERT INTO project(name, owner, finish_date, logo) VALUES('原神聖遺物計算アプリ', '中川浩太郎', '2024-01-15', 'java_logo.png');
INSERT INTO project(name, owner, finish_date, logo) VALUES('原神ガチャ課金計算', '中川浩太郎', '2024-01-15', 'java_logo.png');
INSERT INTO project(name, owner, finish_date, logo) VALUES('原神キャラクター育成計算', '中川浩太郎', '2024-01-15', 'java_logo.png');
INSERT INTO project(name, owner, finish_date, logo) VALUES('原神武器育成計算', '中川浩太郎', '2024-01-15', 'java_logo.png');
INSERT INTO project(name, owner, finish_date, logo) VALUES('原神素材計算', '中川浩太郎', '2024-01-15', 'java_logo.png');
INSERT INTO project(name, owner, finish_date, logo) VALUES('ビジュネル暗号計算機', '林敦啓', '2024-01-15', 'lambda_logo.png');
INSERT INTO project(name, owner, finish_date, logo) VALUES('ビジュネル暗号解読機', '林敦啓', '2024-01-15', 'lambda_logo.png');
INSERT INTO project(name, owner, finish_date) VALUES('デレステキャラ育成計画表', '中井禅', '2024-01-15');
INSERT INTO project(name, owner, finish_date) VALUES('デレステガチャ課金計算', '中井禅', '2024-01-15');
INSERT INTO project(name, owner, finish_date) VALUES('デレステガチャ確率計算', '中井禅', '2024-01-15');
INSERT INTO project(name, owner, finish_date) VALUES('デレステガチャユニット編成表', '中井禅', '2024-01-15');
INSERT INTO project(name, owner, finish_date) VALUES('ブルアカロリボイス集', '橋本俊平', '2024-01-15');
INSERT INTO project(name, owner, finish_date) VALUES('ブルアカガチャ課金計算', '橋本俊平', '2024-01-15');
INSERT INTO project(name, owner, finish_date) VALUES('ブルアカガチャ確率計算', '橋本俊平', '2024-01-15');
INSERT INTO project(name, owner, finish_date) VALUES('ブルアカユニット編成表', '橋本俊平', '2024-01-15');
INSERT INTO project(name, owner, finish_date, logo) VALUES('漫画感想共有アプリ', '山田真豊', '2024-01-15', 'flask_logo.png');
INSERT INTO project(name, owner, finish_date, logo) VALUES('漫画価格一覧アプリ', '山田真豊', '2024-01-15', 'flask_logo.png');
INSERT INTO project(name, owner, finish_date, logo) VALUES('漫画ガチャ課金計算', '山田真豊', '2024-01-15', 'flask_logo.png');

drop table if exists task;
create table task(
    name    varchar(2000),
    status  int default 2,
    manager varchar(50),
    story varchar(2000),
    sprint  int,
    start_task_date  DATETIME DEFAULT CURRENT_TIMESTAMP,
    finish_task_date DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    comment varchar(2000)
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
    project varchar(100),
    priorit int
);

INSERT INTO story(name, project,priorit) VALUES('ファイルを一括で管理したい', '開発支援アプリ',0);
INSERT INTO story(name, project,priorit) VALUES('各員の進行状況を逐次把握したい', '開発支援アプリ',1);

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
INSERT INTO project_users(projectName, userId) VALUES('開発支援アプリ', 'kd1323949@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('開発支援アプリ', 'kd1293049@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('開発支援アプリ', 'kd1299164@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('開発支援アプリ', 'kd1334632@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('開発支援アプリ', 'kd1334992@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('開発支援アプリ', 'kd1329246@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('タスク管理アプリ', 'kd1297401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('タスク管理アプリ', 'kd1323949@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('タスク管理アプリ', 'kd1293049@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('タスク管理アプリ', 'kd1299164@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('タスク管理アプリ', 'kd1334632@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('タスク管理アプリ', 'kd1334992@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('タスク管理アプリ', 'kd1329246@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('マインクラフトサーバー', 'kd1297401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('シフト表作成支援アプリ', 'kd1297401@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('原神聖遺物計算アプリ', 'kd1323949@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('原神ガチャ課金計算', 'kd1323949@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('原神キャラクター育成計算', 'kd1323949@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('原神武器育成計算', 'kd1323949@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('原神素材計算', 'kd1323949@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('ビジュネル暗号計算機', 'kd1334632@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('ビジュネル暗号解読機', 'kd1334632@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('デレステキャラ育成計画表', 'kd1293049@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('デレステガチャ課金計算', 'kd1293049@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('デレステガチャ確率計算', 'kd1293049@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('デレステガチャユニット編成表', 'kd1293049@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('ブルアカロリボイス集', 'kd1299164@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('ブルアカガチャ課金計算', 'kd1299164@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('ブルアカガチャ確率計算', 'kd1299164@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('ブルアカユニット編成表', 'kd1299164@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('漫画感想共有アプリ', 'kd1334992@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('漫画価格一覧アプリ', 'kd1334992@st.kobedenshi.ac.jp');
INSERT INTO project_users(projectName, userId) VALUES('漫画ガチャ課金計算', 'kd1334992@st.kobedenshi.ac.jp');

drop table if exists skill;
CREATE TABLE skill(
    userNumber INT,
    skill1 INT DEFAULT 2 CHECK (skill1 >= 1 AND skill1 <= 3),
    skill2 INT DEFAULT 2 CHECK (skill2 >= 1 AND skill2 <= 3),
    skill3 INT DEFAULT 2 CHECK (skill3 >= 1 AND skill3 <= 3),
    skill4 INT DEFAULT 2 CHECK (skill4 >= 1 AND skill4 <= 3),
    skill5 INT DEFAULT 2 CHECK (skill5 >= 1 AND skill5 <= 3),
    skill6 INT DEFAULT 2 CHECK (skill6 >= 1 AND skill6 <= 3),
    skill_TEXT TEXT
);

INSERT INTO skill(userNumber) VALUES('1');

drop table if exists achievement;
create table achievement(
    userNumber  int,
    scrumMaster int default 0,
    productOwner int default 0,
    developer   int default 0,
    presenter   int default 0,
    teamLeader  int default 0
);

INSERT INTO achievement(userNumber, scrumMaster, developer, presenter) VALUES(1, 3, 1, 3);
INSERT INTO achievement(userNumber, developer, presenter) VALUES(2, 3, 1);
INSERT INTO achievement(userNumber, developer, productOwner, presenter) VALUES(3, 3, 1, 1);
INSERT INTO achievement(userNumber, productOwner, developer, teamLeader) VALUES(4, 3, 1, 3);
INSERT INTO achievement(userNumber, developer, presenter, teamLeader) VALUES(5, 3, 4, 3);
INSERT INTO achievement(userNumber, developer, presenter) VALUES(6, 3, 1);
INSERT INTO achievement(userNumber, productOwner, developer, presenter) VALUES(7, 3, 2, 1);