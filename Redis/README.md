
## **連接HomeStead**

* 修改redis配置文件（默認路徑/etc/redis/redis.conf）
    * requirepass yourpassword ----設置任何你想要的密碼
    * bind 127.0.0.1 修改為 bind 0.0.0.0
    * 複製代碼修改完配置後重啟redis，執行命令
    * sudo service redis restart
    * 複製代碼查看修改情況
