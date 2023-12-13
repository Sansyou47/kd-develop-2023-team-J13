var container = document.getElementById("visualization"),
    items = new vis.DataSet();
var groups = [];
var te = [];

for (var i = 0; i < storyGraph.length; i++) {
    te.push({ id: i, group: storyGraph[i][3], content: storyGraph[i][1], start: '2022-12-05', end: '2023-12-25' });
    groups.push({ id: i, content: storyGraph[i][3] });
}

for (var j = 0; j < te.length; j++) {
    console.log(te[j]);
    items.add(te[j]);
}



var options = {
    start: '2023-12-06',  // timeline軸が表す期間の範囲の開始日
    end: '2023-12-15',
    editable: true,
    //zoomの有無
    zoomable: true,
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
var timeline = new vis.Timeline(container, items, options, groups);

timeline.addCustomTime('2014-02-20', 'v-bar');


// vis-item.vis-range {
//   border-radius: 2px; 60とかにすると角丸くなる
//   border-style: solid;
//   box-sizing: border-box;
// }


