drop table if exists users;
create table users(
    number	int auto_increment primary key,
	name	varchar(50) not null,
    gender  int
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
    name    varchar(100)
);

INSERT INTO project(name) VALUES ('開発支援アプリ');
INSERT INTO project(name) VALUES ('タスク管理アプリ');

drop table if exists task;
create table task(
    name    varchar(2000),
    status  int default 2,
    manager varchar(50),
    project int
);

INSERT INTO task(name) VALUES('プロジェクト選択画面');
INSERT INTO task(name) VALUES('新規プロジェクト設定画面');
INSERT INTO task(name) VALUES('ストーリー登録画面');
INSERT INTO task(name) VALUES('タスク登録画面');

drop table if exists story;
create table story(
    name    varchar(2000),
    project int
);

INSERT INTO story(name) VALUES('ファイルを一括で管理したい');
INSERT INTO story(name) VALUES('各員の進行状況を逐次把握したい');