# 폰트 import 하는 파일 #
import os
from kivy.core.text import LabelBase

# 현재 파일의 디렉토리 경로
current_dir = os.path.dirname(os.path.abspath(__file__))

# 폰트 파일의 상대 경로를 생성
## 청소년체
font_path_y = os.path.join(current_dir, 'fonts', 'Youth.ttf')
## 궁서체
font_path_c = os.path.join(current_dir, 'fonts', 'Chosun.ttf')

# 폰트 등록 함수 , init 시 호출
def register_fonts():
    # 청소년체 'youth'라는 이름으로 사용
    LabelBase.register(name='youth', fn_regular=font_path_y)
    # 궁서체 'chosun'이라는 이름으로 사용
    LabelBase.register(name='chosun', fn_regular=font_path_c)