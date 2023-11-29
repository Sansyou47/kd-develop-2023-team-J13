USE scrum;

INSERT INTO users(name, gender) VALUES('嫁阪雄大', 0);
INSERT INTO users(name, gender) VALUES('中川浩太郎', 0);
INSERT INTO users(name, gender) VALUES('中井禅', 0);
INSERT INTO users(name, gender) VALUES('橋本俊平', 0);
INSERT INTO users(name, gender) VALUES('林敦啓', 0);
INSERT INTO users(name, gender) VALUES('山田真豊', 0);
INSERT INTO users(name, gender) VALUES('米津大也', 0);

INSERT INTO project(name) VALUES ('開発支援アプリ');
INSERT INTO project(name) VALUES ('タスク管理アプリ');

INSERT INTO task(name) VALUES('プロジェクト選択画面');
INSERT INTO task(name) VALUES('新規プロジェクト設定画面');
INSERT INTO task(name) VALUES('ストーリー登録画面');
INSERT INTO task(name) VALUES('タスク登録画面');

INSERT INTO story(name) VALUES('ファイルを一括で管理したい');
INSERT INTO story(name) VALUES('各員の進行状況を逐次把握したい');