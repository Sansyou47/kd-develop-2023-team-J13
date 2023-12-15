class User(UserMixin):
    def __init__(self, user_id: str) -> None:
        """user_idにはユーザーを一意に特定できる値を指定し、その他の項目は任意で設定する

        Args:
            user_id (str): ユーザーを一意に特定できる値
        """
        self.user_id = user_id

    def get_id(self):
        """このメソッドは必要に応じて定義する必要があり、デフォルトではself.idの値が返されるので、
        self.id以外の値を返したい場合はget_idのメソッドを上書きする
        self.get_idで返す値はユーザーを一意に特定できる値を返すこと
        仮に単一の項目では一意の値とならない場合は複数項目をTuple(ハッシュ化可能な値)で返すと良い

        def __init__(self, user_id:str, group_id:str):
            self.user_id = user_id
            self.group_id = group_id

        def get_id(self):
            return (self.user_id, self.grop_id)
        """
        return self.user_id