
## **打包exe**

* pyinstaller -F .\hello.py

* 參考
    * https://medium.com/pyladies-taiwan/python-%E5%B0%87python%E6%89%93%E5%8C%85%E6%88%90exe%E6%AA%94-32a4bacbe351
    * https://www.zhihu.com/question/22977098

## **網頁異常提示處理**

* 此網頁上的問題導致 Internet Explorer 關閉並重新打開該選項卡

    * 第一步
		打開IE
		工具->Internet選項->高級->重置
		彈出窗口
		選項"刪除個人設置"打上勾
		確定重置
		回到原始默認狀態
	
	* 第二步
		禁用smartscreen
		打開IE
		工具->Internet選項->安全->選擇Internet->自定義級別
		找到使用 SmartScreen 篩選器
		選擇禁用
		然後確定
		
	* 第三步
		打開IE
		工具->Internet 選項
		點擊高級標籤
		在"加速的圖形"下
		"使用軟件呈現而不使用GPU呈現"
		前面打勾。
	
	* 第四步
		重啟瀏覽器
		不需要重啟電腦
