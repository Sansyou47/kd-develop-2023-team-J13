drop table if exists users;
create table users(
    number	int auto_increment primary key,
	name	varchar(50) not null,
    mail    varchar(50),
    password    varchar(300),
    gender  int,
    class   varchar(10)

) auto_increment = 100000;

INSERT INTO users(name, gender) VALUES('嫁阪雄大', 0);
INSERT INTO users(name, gender) VALUES('中川浩太郎', 0);
INSERT INTO users(name, gender) VALUES('中井禅', 0);
INSERT INTO users(name, gender) VALUES('橋本俊平', 0);
INSERT INTO users(name, gender) VALUES('林敦啓', 0);
INSERT INTO users(name, gender) VALUES('山田真豊', 0);
INSERT INTO users(name, gender) VALUES('米津大也', 0);

drop table if exists project;
create table project(
    number  int auto_increment primary key,
    name    varchar(100),
    owner   varchar(100),
);

INSERT INTO project(name) VALUES('開発支援アプリ');
INSERT INTO project(name) VALUES('タスク管理アプリ');
INSERT INTO project(name) VALUES('シフト表作成支援アプリ');
INSERT INTO project(name) VALUES('マインクラフトサーバー');

drop table if exists task;
create table task(
    name    varchar(2000),
    status  int default 2,
    manager varchar(50),
    project int,
    sprint  int
);

INSERT INTO task(name) VALUES('プロジェクト選択画面');
INSERT INTO task(name) VALUES('新規プロジェクト設定画面');
INSERT INTO task(name) VALUES('ストーリー登録画面');
INSERT INTO task(name) VALUES('タスク登録画面');
INSERT INTO task(name) VALUES('タスクを受ける画面');
INSERT INTO task(name) VALUES('進捗状況のグラフ化');
INSERT INTO task(name) VALUES('タスクボード出力画面');

drop table if exists story;
create table story(
    name    varchar(2000),
    project varchar(50)
);

INSERT INTO story(name) VALUES('ファイルを一括で管理したい');
INSERT INTO story(name) VALUES('各員の進行状況を逐次把握したい');

drop table if exists class;
create table class(
    name    varchar(20)
);

INSERT INTO class(name) VALUES('student');
INSERT INTO class(name) VALUES('teacher');
INSERT INTO class(name) VALUES('company');
INSERT INTO class(name) VALUES('recruiter');
