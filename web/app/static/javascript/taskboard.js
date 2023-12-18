window.onload = function () {
    var tasks = document.querySelectorAll('.Task p');
    var doing = document.querySelector('.Doing');
    var done = document.querySelector('.Done');
    var taskname;

    tasks.forEach(function (task, index) {
        task.id = 'task' + index;
        // "ストーリー登録画面"のタスクだけをドラッグ可能にする
        if (task.textContent === task.textContent) {
            task.draggable = true;
        }
    });

    [doing, done].forEach(function (element) {
        element.addEventListener('dragover', function (e) {
            e.preventDefault();
        });

        element.addEventListener('drop', function (e) {
            e.preventDefault();
            var id = e.dataTransfer.getData('text');
            var taskname = e.dataTransfer.getData('taskname');
            if (id) {
                var elem = document.getElementById(id);
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
                });

            }
        });
    });

    tasks.forEach(function (task) {
        task.addEventListener('dragstart', function (e) {
            console.log('Drag started, target id:', e.target.id); // 追加
            e.dataTransfer.setData('text', e.target.id);
        });
    });
};