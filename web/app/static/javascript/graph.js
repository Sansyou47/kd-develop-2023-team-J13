//HTML要素の取得
var container = document.getElementById("visualization"),
    //データセットの初期化
    items = new vis.DataSet(),
    groups = new vis.DataSet(),
    task = [];
//storyGraphの各要素に対して処理
for (var i = 0; i < storyGraph.length; i++) {
    //taskに必要な情報を格納
    task.push({ id: i, group: storyGraph[i][3], content: storyGraph[i][0], start: storyGraph[i][5], end: '2023-12-30' });
    //これ例"プロジェクト選択画面",2,null,"ファイルを一括で管理したい",1,"Tue, 12 Dec 2023 11:59:50 GMT","Tue, 12 Dec 2023 11:59:50 GMT"
    // groupsに既に同じcontent(例:プロジェクト選択画面)があるかを確認
    var existingGroups = groups.get({
        filter: function (item) {
            return item.content === storyGraph[i][3];
        }
    });

    // なければ追加
    if (existingGroups.length === 0) {
        groups.add({ id: storyGraph[i][3], content: storyGraph[i][3] });
    }
}

//itemsにtaskの値を渡す
for (var j = 0; j < task.length; j++) {
    items.add(task[j]);
}

var options = {
    start: '2023-12-01',  // timeline軸が表す期間の範囲の開始日
    end: '2023-12-30',
    editable: false,
    //zoomの有無
    zoomable: false,
    //時間の配置場所
    orientation: 'top',
    zoomMin: 1000 * 60 * 60 * 24 * 7, //1週間
    zoomMax: 1000 * 60 * 60 * 24 * 31 * 3, //3カ月
    itemsAlwaysDraggable: {
        item: false, //選択なしでアイテムをドラッグできる
        range: false, //選択なしで範囲を変更できる
    },
};
//timelineに表示する項目を書く
//groupsを書かないと一番左のCC,DD等が表示されなくなる
var timeline = new vis.Timeline(container, items, groups, options);

timeline.addCustomTime('2014-02-20', 'v-bar');


// vis-item.vis-range {
//   border-radius: 2px; 60とかにすると角丸くなる
//   border-style: solid;
//   box-sizing: border-box;
// }


