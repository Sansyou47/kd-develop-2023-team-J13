//HTML要素の取得

    // var tasks = [
    //     {
    //         id: 'id1',
    //         name: '確定申告する',
    //         description: '必ずやる!!',
    //         start: '2021-01-01',
    //         end: '2021-01-7',
    //         progress: 100,
    //     },
        
    // ];
    


    var tasks=[];
    function formatDate(dateString) {
        const date = new Date(dateString);
        return isNaN(date) ? null : date.toISOString();
    };
    

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
    console.log(tasks);
    //これ例"プロジェクト選択画面",2,null,"ファイルを一括で管理したい",1,"Tue, 12 Dec 2023 11:59:50 GMT","Tue, 12 Dec 2023 11:59:50 GMT"

    var gantt = new Gantt("#gantt", tasks, {
        });