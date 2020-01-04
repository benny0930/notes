console.trace();
var w = floaty.window(
    <frame gravity="center">
        <button id="stop" text="點擊停止腳本運行"/>
    </frame>
);
w.setPosition(200, 850);
w.stop.click(function(){
    w.close();
    toast("脚本终止，手动关闭！");
    frequency = 0;
    exit();
});

var index = 0;
while(1){
    index ++;
    log(index+""+index+""+index+"");
    sleep(1000);
}