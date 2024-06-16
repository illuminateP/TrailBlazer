# 폰트 import 하는 파일 #
from kivy.core.text import LabelBase
from kivy.resources import resource_find


def register_fonts():
    # 청소년체 'youth'라는 이름으로 사용
    youth_font_path = resource_find('fonts/Youth.ttf')
    LabelBase.register(name='youth', fn_regular=youth_font_path)
    
    # 궁서체 'chosun'이라는 이름으로 사용
    chosun_font_path = resource_find('fonts/Chosun.ttf')
    LabelBase.register(name='chosun', fn_regular=chosun_font_path)