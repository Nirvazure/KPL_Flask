from app import app

#加入这个if语句，保证本地和云端的部署都能正确执行我们的代码

if __name__=="__main__":
    app.run(debug=True)