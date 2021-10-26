# 共通の設定は以下のファイル
from .common_settings import *


try:
    # SECRETKEYなどの公開してはいけない情報は以下のファイル
    from .local_settings import *
except ImportError:
    # deploy用の設定は以下のファイル
    from .deploy_settings import *
