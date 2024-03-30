$(function () {

    // 滚动条下拉到底
    function scrollConversationScreen() {
        $("input[name='message']").focus();
        $('.messages-list').scrollTop($('.messages-list')[0].scrollHeight);
    }

    // AJAX POST发送消息
    $("#send").submit(function () {
        $.ajax({
            url: '/messages/send-message/',
            data: $("#send").serialize(),
            cache: false,
            type: 'POST',
            success: function (data) {
                $(".send-message").before(data);  // 将接收到的消息插入到聊天框
                $("input[name='message']").val(''); // 消息发送框置为空
                scrollConversationScreen();  // 滚动条下拉到底
            }
        });
        return false;
    });

    // WebSocket连接，使用wss(https)或者ws(http)
    const ws_scheme = window.location.protocol === "https:" ? "wss" : "ws";
    const ws_path = ws_scheme + "://" + window.location.host + "/ws/" + currentUser + "/";
    const ws = new ReconnectingWebSocket(ws_path);
    // 监听后端发送过来的消息
    ws.onmessage = function (event) {
        const data = JSON.parse(event.data);
        if (data.sender === activeUser) {  // 发送者为当前选中的用户
            $(".send-message").before(data.message); // 将接收到的消息插入到聊天框
            scrollConversationScreen();  // 滚动条下拉到底
        }
    }
});

/*
// WebSocket构造函数，用于新建WebSocket实例
var ws = new WebSocket('ws://ip:80', 'websocket');

返回实例对象当前的状态
ws.readyState
CONNNECTING: 值为0, 表示正在连接
OPEN: 值为1, 表示连接成功, 可以通信了
CLOSING: 值为2, 表示连接正在关闭
CLOSED: 值为3, 表示连接已关闭, 或者打开连接失败

switch (ws.readyState) {
    case ws.CONNECTING:
        // XOXO
        break;
    case ws.OPEN:
        //
        break;
    case ws.CLOSING:
        //
        break;
    case ws.CLOSED:
        //
        break;
    default:
        // ...
        break;
}

// ws.onopen  用于指定连接成功后的回调函数
ws.onopen = function () {
    ws.send('连接成功！')
};

// ws.onclose  用于指定连接关闭后的回调函数

// ws.onmessage  用于指定收到服务器数据后的回调函数
ws.onmessage = function (event) {
    if (typeof event.data === String) {
        console.log("received string")
    } else {
        console.log("xxx")
    }
};

// ws.send()

// ws.onerror  指定报错时的回调函数
ws.onerror = function (event) {
    //
};
*/
