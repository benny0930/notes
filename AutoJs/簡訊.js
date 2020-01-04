"auto";
events.observeNotification();
events.on("notification", function (n) {
    var reSendMsg = n.getText();
    var reSendMsgArr = reSendMsg.split("，");
    var index = reSendMsgArr[0].indexOf("验证码");
    var code = reSendMsgArr[0].substr(index+3);
    log(code)
});