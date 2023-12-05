# kd-develop-2023-team-J13
神戸電子専門学校総合開発演習　チームJ13
### データベースのテーブル
デバッグのためにデフォルトで値を格納しています。各テーブル内に入っているデータは以下を参考に。

|テーブル名|説明|
|---|---|
|users|登録されているユーザーの情報を格納する。ログイン処理の際にはこのテーブルからIDとパスワードを取得して処理を実行する。|
|project|登録されているプロジェクトを保存するテーブル。|
|task|登録されたタスクを保存するテーブル。|
|story|登録されたストーリーを保存するテーブル。|

各テーブルの項目について以下に説明する。  

1. usersテーブル

|項目名|型|例|説明|
|---|---|---|---|
|~~number~~userId|~~int~~varchar(50)|~~100000~~kd00@st.jp|~~ユーザーが追加されたら自動で割り当てられる。~~メールアドレスをIDとして利用する|
|~~name~~userName|varchar(50)|岸辺露伴|ユーザー名を格納する。not-null|
|~~mail~~|~~varchar(50)~~|~~kd0000000@st.ac.jp~~|~~登録されているメールアドレスを格納する。~~当該項目は削除|
|kana|varchar(50)|キシベロハン|ユーザー名の読みがなを格納する。not-null|
|password|varchar(300)|None|パスワードをハッシュ化して格納する。ハッシュ化はPythonスクリプトで実行する|
|gender|int|0:male, 1:female, 2:none|性別を整数値で格納する。|
|gitAccount|varchar(50)|Sansyou47|GitHubアカウントを持っていればアカウント名を登録する|
|class|varchar(10)|student|ユーザー登録時にclassテーブルから選択する。教師、生徒、企業など。|

2. projectテーブル

|項目名|型|例|説明|
|---|---|---|---|
|number|int|1|自動割り当ての項目。主キー|
|name|varchar(100)|開発支援アプリ|プロジェクトの題名|
|owner|varchar(50)|木下秀吉|プロジェクトを作成した人の名前が入る。後から所有者を変更できる必要あり？|
|start_date|datetime|2020-10-10|プロジェクトが作成された日付|
|update_date|datetime|2020-10-10|プロジェクトが更新された日付|

3. taskテーブル

|項目名|型|例|説明|
|---|---|---|---|
|name|varchar(2000)|プロジェクト選択画面|タスクの名前（内容）が入る。2000文字必要？|
|status|int|Task:2, Doing:1, Done:0|タスクの現在状態を整数値で格納する。例外状態は4かな？|
|manager|varchar(50)|木下秀吉|タスクを担当する人の名前が格納される。項目名はownerの方がいいかも？|
|project|varchar(100)|開発支援アプリ|そのタスクが属するプロジェクトの名前を格納|
|sprint|int|1|そのタスクは第何スプリントのものなのか格納する|

4. storyテーブル

|項目名|型|例|説明|
|---|---|---|---|
|name|varchar(2000)|ファイルを一括で管理したい。画面が多くなり移動が面倒だからだ。|ストーリーを格納する。|
|project|varchar(100)|開発支援アプリ|そのストーリーが属するプロジェクトの名前を格納|

5. classテーブル  
このテーブルには項目が"name"のみのため、項目に格納する値について説明する。なお、このテーブルについてはデプロイする際にもこの値がデフォルトで格納される。

|項目値|説明|
|---|---|
|student|学生|
|teacher|教員|
|company|会社員|
|recruiter|採用担当者|