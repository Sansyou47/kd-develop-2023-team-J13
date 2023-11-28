drop table if exists users;
create table users(
    number	int auto_increment primary key,
	name	varchar(50) not null,
    gender  int
) auto_increment = 100000;

insert into users(name, gender) values ('嫁阪雄大', 0);
insert into users(name, gender) values ('中川浩太郎', 0);
insert into users(name, gender) values ('中井禅', 0);
insert into users(name, gender) values ('橋本俊平', 0);
insert into users(name, gender) values ('林敦啓', 0);
insert into users(name, gender) values ('山田真豊', 0);
insert into users(name, gender) values ('米津大也', 0);

drop table if exists project;
create table project(
    number  int auto_increment primary key,
    name    varchar(100)
);

insert into project(name) values ('開発支援アプリ');
insert into project(name) values ('タスク管理アプリ');

drop table if exists task;
create table task(
    name    varchar(2000),
    status  int default 2,
    manager varchar(50),
    project int
);

insert into task(name) values('プロジェクト選択画面')
insert into task(name) values('新規プロジェクト設定画面')
insert into task(name) values('ストーリー登録画面')
insert into task(name) values('タスク登録画面')

drop table if exists story;
create table story(
    name    varchar(2000),
    project int
);

insert into story(name) values('ファイルを一括で管理したい')
insert into story(name) values('各員の進行状況を逐次把握したい')