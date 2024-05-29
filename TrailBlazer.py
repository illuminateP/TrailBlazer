# 구동부
# init 기능 추가 필요

from screens import MyApp

if __name__ == '__main__':
    # 호출 시 자동 init     
    myapp = MyApp()
    myapp.run()