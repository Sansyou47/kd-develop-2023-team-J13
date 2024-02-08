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

INSERT INTO users(userId, userName, kana, password, gender, class) VALUES('kd0000001@st.kobedenshi.ac.jp', 'デバッグ一郎', 'デバッグイチロウ', 'scrypt:32768:8:1$L2mjfpTmVhyNbN2q$5bf4d6b94f85e10c3fa9a63adddecdd9c2cb919162164bdea0713af1da5fd042578115b0759fd2a1812ff970b6da4318ee3fd369ef5e3e4afa0791ea13948d75', 0, 'student');
INSERT INTO users(userId, userName, kana, password, gender, class) VALUES('kd0000002@st.kobedenshi.ac.jp', 'デバッグ二郎', 'デバッグジロウ', 'scrypt:32768:8:1$L2mjfpTmVhyNbN2q$5bf4d6b94f85e10c3fa9a63adddecdd9c2cb919162164bdea0713af1da5fd042578115b0759fd2a1812ff970b6da4318ee3fd369ef5e3e4afa0791ea13948d75', 0, 'student');
INSERT INTO users(userId, userName, kana, password, gender, class) VALUES('kd0000003@st.kobedenshi.ac.jp', '神戸太郎', 'コウベタロウ', 'scrypt:32768:8:1$L2mjfpTmVhyNbN2q$5bf4d6b94f85e10c3fa9a63adddecdd9c2cb919162164bdea0713af1da5fd042578115b0759fd2a1812ff970b6da4318ee3fd369ef5e3e4afa0791ea13948d75', 0, 'teacher');

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
    logo    varchar(200),
    sprint  int
);

INSERT INTO project(name, owner, finish_date, github, logo, sprint) VALUES('開発支援アプリ', '神戸太郎', '2024-01-15', 'https://github.com/Sansyou47/kd-develop-2023-team-J13.git', 'default.svg', 3);

drop table if exists task;
create table task(
    name    varchar(2000),
    status  int default 2,
    manager varchar(50),
    story varchar(2000),
    sprint  int,
    start_task_date DATE,
    finish_task_date DATE,
    comment varchar(2000),
    projectNumber int
);

drop table if exists story;
create table story(
    name    varchar(2000),
    projectNumber int,
    priorit int,
    sprint  int
);

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
    userId    varchar(50),
    projectNumber int
);

INSERT INTO project_users(projectName, userId, projectNumber) VALUES('開発支援アプリ', 'kd0000003@st.kobedenshi.ac.jp',1);

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

drop table if exists persona;
create table persona(
    projectNumber int primary key,
    name    varchar(50),
    age     int,
    gender  varchar(10),
    job     varchar(50),
    hobby   varchar(50),
    income  int,
    family  varchar(50),
    note    varchar(2000)
);

INSERT INTO persona(projectNumber, name, age, gender, job, hobby, income, family, note) VALUES(1, '神戸太郎', 20, '男', '学生', 'ゲーム', 50, '父、母、姉', 'KD学生であり、スクラム開発に興味がある。');

drop table if exists student;
create table student(
    userNumber  int primary key,
    studentNumber   varchar(10),
    class   varchar(10),
    number  varchar(10)
);