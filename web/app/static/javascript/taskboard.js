window.onload = function () {
    var tasks = document.querySelectorAll('.Task p');
    var doing = document.querySelector('.Doing');
    var doings = document.querySelectorAll('.Doing p');
    var done = document.querySelector('.Done');
    var taskname;
    // tasksとdoingsを一つの配列に結合
    var allTasks = Array.from(tasks).concat(Array.from(doings));

    // allTasksの各タスクに対して処理
    allTasks.forEach(function (task, index) {
        task.id = 'task' + index;
        task.draggable = true; // すべてのタスクをドラッグ可能にする
    });

    allTasks.forEach(function (task) {
        task.addEventListener('dragstart', function (e) {
            e.dataTransfer.setData('taskname', e.target.textContent); // タスク名を保存
            taskname = e.dataTransfer.getData('taskname');
        });
    });


    [doing, done].forEach(function (element) {
        element.addEventListener('dragover', function (e) {
            e.preventDefault();
        });

        element.addEventListener('drop', function (e) {
            e.preventDefault();
            var id = e.dataTransfer.getData('text');
            if (id) {
                var elem = document.getElementById(id);

                element.appendChild(elem);

                var st = element;
                if (st === doing) {
                    st = 1;
                    location.reload();
                }
                else if (st === done) {
                    st = 0;
                    location.reload();
                }
                console.log('taskname:', taskname, 'Type of taskname:', typeof taskname);
                console.log('st:', st, 'Type of st:', typeof st);
                // POSTリクエストを送信
                fetch('/taskboardjs', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ st: st, taskname: taskname }),
                });

            }
        });
    });

    allTasks.forEach(function (task) {
        task.addEventListener('dragstart', function (e) {
            console.log('Drag started, target id:', taskname); // 追加
            e.dataTransfer.setData('text', e.target.id);
        });
    });
};