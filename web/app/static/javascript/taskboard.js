window.onload = function () {
    var tasks = document.querySelectorAll('.Task p');
    var doing = document.querySelector('.Doing');
    var doings = document.querySelectorAll('.Doing p');
    var done = document.querySelector('.Done');
    var stories_color = document.querySelectorAll('[class^="story-"]');
    var tasks_color = document.querySelectorAll('[class^="task-"]');
    var doing_color = document.querySelectorAll('[class^="doing-"]');
    var done_color = document.querySelectorAll('[class^="done-"]');
    var taskname;
    // tasksとdoingsを一つの配列に結合
    var allTasks = Array.from(tasks).concat(Array.from(doings));
    var storyNames = [];
    var taskNames = [];
    var doingNames = [];
    var doneNames = [];
    var i = 1;
    while (true) {
        var storyElements = document.getElementsByClassName('story_name_' + i);
        var taskElements = document.getElementById('task_name_' + i);
        var doingElements = document.getElementById('doing_name_' + i);
        var doneElements = document.getElementById('done_name_' + i);

        if (storyElements.length === 0 && taskElements == null && doingElements == null && doneElements == null) {
            break;
        }
        if (storyElements.length > 0) {
            var storyName = storyElements[0].value;
            storyNames.push(storyName);
        }

        if (taskElements != null) {
            var taskName = taskElements.value;
            taskNames.push(taskName);
        }

        if (doingElements != null) {
            var doingName = doingElements.value;
            doingNames.push(doingName);
        }

        if (doneElements != null) {
            var doneName = doneElements.value;
            doneNames.push(doneName);
        }
        i++;
    }


    //console.log(storyNames, "story");
    //console.log(taskNames, "task");
    //console.log(doingNames, "doing");
    //console.log(doneNames, "done");

    for (c = 0; c < storyNames.length; c++) {
        try {
            var hue = c * 360 / stories_color.length;
            co = 'hsl(' + hue + ', 100%, 75%)';
            stories_color[c].style.backgroundColor = co;

            for (let index = 0; index < taskNames.length; index++) {
                let taskName = taskNames[index];
                //console.log("t")
                //console.log(taskName, "a")
                //console.log(storyNames[c], "b")
                if (taskName === storyNames[c]) {
                    tasks_color[index].style.backgroundColor = co;
                    //console.log(tasks_color[index]); // Add this line
                    //console.log(co, "sssssss"); // Add this line
                    //console.log(taskName, "taskName");
                }
            }
            for (let index = 0; index < doingNames.length; index++) {
                let doingName = doingNames[index];
                //console.log("tt")
                //console.log(doingName, "c")
                //console.log(storyNames[c], "d")
                //console.log(doing_color[index]); // Add this line
                if (doingName === storyNames[c]) {
                    //console.log(doing_color[index]); // Add this line
                    //console.log(co, "sssssss"); // Add this line
                    doing_color[index].style.backgroundColor = co;
                    //console.log(doingName, "doingName");
                }
            }
            for (let index = 0; index < doneNames.length; index++) {
                let doneName = doneNames[index];
                //console.log("ttt")
                //console.log(doneName)
                //console.log(storyNames[c])
                if (doneName === storyNames[c]) {
                    done_color[index].style.backgroundColor = co;
                    //console.log(doneName, "doneName");
                }
            }
        } catch (error) {
            console.error('An error occurred:', error);
        }
    }
    //いまは各種要素の取得を別別に行いページの更新後も正しく動作したいな

    // var stories = document.getElementsByClassName('Story');
    // for (var i = 0; i < stories.length; i++) {
    //     var hue = i * 360 / stories.length;
    //     stories[i].style.backgroundColor = 'hsl(' + hue + ', 100%, 75%)';
    // }


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
                console.log(id); // 追加
                element.appendChild(elem);

                var st = element;
                if (st === doing) {
                    st = 1;

                }
                else if (st === done) {
                    st = 0;

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
                })
                    .then(function (response) {
                        if (!response.ok) {
                            throw new Error("HTTP error " + response.status);
                        }
                        // リクエストが成功したらページをリロード
                        // 下のリロードのlocationを無効にしたらDoneからDoingに戻る処理が増えるけど画面のリロードが要らなくなる
                        location.reload();
                        console.log('reload');
                    })
                    .catch(function (error) {
                        console.log('Request failed: ', error.message);
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