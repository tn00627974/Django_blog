#1 
先確認環境是否有安裝
python3 --version
brew install python

python3 --version
pip3 --version
pip3 install --upgrade pip

 安裝 Django 模組的指令
pip3 install django==3.1.7

 查看 Django 模組是否已在列表中
pip3 list

 
#2
建立 Django 專案
 建立 Django 專案語法
django-admin startproject firstproject
\firstproject
  |-- manage.py
  |-- \firstproject
      |-- __init__.py
      |-- asgi.py
      |-- settings.py
      |-- urls.py
      |-- wsgi.py


 firstproject: 主目錄。
 manage.py: Python 命令檔。為專案管理功能，包含建立 app 、啟動 Server 和 Shell 等。
 下層 firstproject: 包含專案設定、url配置、網頁伺服器介面設定檔。
 __init__.py: 該資料夾為 Python package。
 asgi.py: asgi 網頁伺服器和 Django 的介面設定檔。
 settings.py: 設定檔。
 urls.py: url 配置檔。
 wsgi.py: wsgi 網頁伺服器和 Django 的介面設定檔。


建立 Application 應用程式
 建立 Django 專案後，可以建立 Application 應用程式。
 語法如下：
python manage.py startapp myblog
\firstproject
  |-- manage.py
  |-- \firstproject
      |-- __init__.py
      |-- asgi.py
      |-- settings.py
      |-- urls.py
      |-- wsgi.py
  |-- \myblog
      |-- __init__.py
      |-- admin.py
      |-- apps.py
      |-- migrations
      |-- models.py
      |-- tests.py
      |-- views.py


 appname: 應用程式名稱。
 __init__.py: 該資料夾為 Python package。
 admin.py: 管理介面設定檔。
 apps.py: 應用程式設定檔。 
 migrations: 資料庫版本控制。
 models.py: 資料模型設定檔。
 tests.py: 測試檔案。
 views.py: 網頁介面設定檔。


#3
 在專案目錄下建立 templates
md templates

 將圖形檔、CSS、JavaScript 存放在此資料夾
 在專案目錄下建立 static
md static 

視圖 (view) 與 URL
環境設定
 設定檔位於 firstproject/firstproject/settings.py
 開啟 settings.py 並修改以下設定：

 1. 設定語言
LANGUAGE_CODE = 'zh-hant'

 2. 設定時區
TIME_ZONE = 'Asia/Taipei'


 3. 設定資料庫
 開啟 settings.py 並修改以下設定：

 4. 設定資料庫
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

 5. 設定靜態檔案
        STATIC_URL = '/static/'
        STATIC_ROOT = os.path.join(BASE_DIR,'static')     靜態檔案的儲存位置       

 6. 設定開發者模式
 開啟 settings.py 並修改以下設定：
 開發者模式可以讓你看到更多的錯誤訊息，並且可以看到所有 Django 內部的資訊。

 7. 設定開發者模式
DEBUG = True  開發模式,不用重開伺服器就能看到更新的內容