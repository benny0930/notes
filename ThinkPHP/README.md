
## **連接HomeStead**

* 修改redis配置文件（默認路徑/etc/redis/redis.conf）
    * requirepass yourpassword ----設置任何你想要的密碼
    * bind 127.0.0.1 修改為 bind 0.0.0.0
    * 複製代碼修改完配置後重啟redis，執行命令
    * sudo service redis restart
    * 複製代碼查看修改情況
	
## 一鍵CRUD 

* 首先  在數據庫中創建一個表，假設這個表是 fa_testtwo

* 然後  進行一鍵crud的生成操作，具體方法是：

         在項目的目錄下， 

         使用命令：php think crud -t testtwo

         創建成功之後會出現提示：Build Successed

* crud 生成之後，再生成菜單，具體方法是：

        在項目的目錄下，

        使用命令：php think menu -c testtwo

        創建成功之後會出現提示：Build Successed


## 關於頁面有上角生成的導出,切換,列.搜索.

如果不需要的話可以在對應的js文件中添加如下代碼.即可屏蔽

* 切換卡片視圖和表格視圖兩種模式
showToggle:false,
* 顯示隱藏列可以快速切換字段列的顯示和隱藏
showColumns:false,
* 導出整個表的所有行導出整個表的所有行
showExport:false,
* 搜索
search: false,
* 搜索功能，
commonSearch: false,
* 表格上方的搜索搜索指表格上方的搜索
searchFormVisible: false,