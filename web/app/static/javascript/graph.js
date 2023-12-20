    // tasks配列を定義
    var tasks=[];
    //受け取った日付データをJSで処理できるように再定義用の関数 
    function formatDate(dateString) {
        const date = new Date(dateString);
        return isNaN(date) ? null : date.toISOString();
    };
    
    // storyGraphにあるデータをtasksに格納
    for (var i = 0; i < storyGraph.length; i++) {
        tasks.push({
            id: i,
            name: storyGraph[i][0],
            description: 'test',
            start: formatDate(storyGraph[i][5]),
            end: formatDate(storyGraph[i][6]),
            progress: 100,
        });
    };
    // console.log(tasks);デバッグ用
    
    // ガントチャート表示
    var gantt = new Gantt("#gantt", tasks, {
        });