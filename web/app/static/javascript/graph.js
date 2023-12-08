var container = document.getElementById("visualization"),
    items = new vis.DataSet();

//ここ配列
items = [
    { group: 'a', content: 'c', start: '2023-12-05', end: '2023-12-25' },
    { group: 'b', content: 'd', start: '2023-12-10', end: '2023-12-31' }
]
//idの名前表示(一番左の部分)
const groups = [
    { id: 'a', content: 'CC' },
    { id: 'b', content: 'DD' },
];


for (var i = 0; i < items.length; i++) {
    //配列から追加しとるやつ
    items.add = items[i].id + items[i].content + items[i].start + items[i].end;
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
var timeline = new vis.Timeline(container, items, groups, options);

timeline.addCustomTime('2014-02-20', 'v-bar');


// vis-item.vis-range {
//   border-radius: 2px; 60とかにすると角丸くなる
//   border-style: solid;
//   box-sizing: border-box;
// }
