import re
import time

KANA_MORSE_MAP = {
    "ア":"－－・－－", "イ":"・－", "ウ":"・・－", "エ":"－・－－－", "オ":"・－・・・",
    "カ":"・－・・", "キ":"－・－・・", "ク":"・・・－", "ケ":"－・－－", "コ":"－－－－",
    "サ":"－・－・－", "シ":"－－・－・", "ス":"－－－・－", "セ":"・－－－・", "ソ":"－－－・",
    "タ":"－・", "チ":"・・－・", "ツ":"・－－・", "テ":"・－・－－", "ト":"・・－・・",
    "ナ":"・－・", "ニ":"－・－・", "ヌ":"・・・・", "ネ":"－－・－", "ノ":"・・－－", 
    "ハ":"－・・・", "ヒ":"－－・・－","フ":"－－・・", "ヘ":"・", "ホ":"－・・",
    "マ":"－・・－", "ミ":"・・－・－", "ム":"－", "メ":"－・・・－", "モ":"－・・－・",
    "ヤ":"・－－", "ユ":"－・・－－", "ヨ":"－－",
    "ラ":"・・・", "リ":"－－・", "ル":"－・－－・", "レ":"－－－", "ロ":"・－・－",
    "ワ":"－・－", "ヲ":"・－－－", "ン":"・－・－・",
    }

PG_NAME = "【モールス符号変換PG】"
EXPLANATION = "\n変換する文章をカタカナで入力して下さい。\r\n\r\n"
ALARM_MSG = "カタカナ以外の文字を含めないで下さい。\
    \r\nスペースや記号も含めないでください。"
ERR_MSG = "濁音や長音などを抜いて入力して下さい。"

kana = input(PG_NAME + EXPLANATION)
KANA_CHARACTER = re.compile("^[ァ-ヶ]+$")

# ファイルをインプットとして利用する場合
if "INPUT.txt" in kana::
    f = open(kana, "r", encoding="UTF-8")
    kana = f.read()
    f.close()

try:
    # カナ文字判定
    if KANA_CHARACTER.fullmatch(kana) is not None:
        # 二分割用の数値算出
        LEN_MID_KANA = len(kana) // 2
        LEN_MAX_KANA = len(kana)

        # 二分割したリスト作成
        FIRST_LIST = kana[:LEN_MID_KANA]
        SECOND_LIST = kana[LEN_MID_KANA:LEN_MAX_KANA]

        # 変換処理の開始
        START_TIME = time.time()
        ENCODED_FIRST_LIST = \
            [word.replace(\
                word,KANA_MORSE_MAP[word]) for word in FIRST_LIST]
        ENCODED_SECOND_LIST = \
            [word.replace(\
                word,KANA_MORSE_MAP[word]) for word in SECOND_LIST]
        ENCODED_ALL_LIST = ENCODED_FIRST_LIST + ENCODED_SECOND_LIST

        encoded_strings =""
        for encoded_string in ENCODED_ALL_LIST:
            encoded_strings = encoded_strings +"　" + encoded_string
        # 文頭のスペース削除
        encoded_strings = re.sub("^　", "", encoded_strings)
        # 変換処理の終了
        END_TIME = time.time()
        TOTAL_TIME = END_TIME - START_TIME
        print(encoded_strings)
        print(f"TOTAL TIME: {TOTAL_TIME}")
    else:
        print(ALAR_MSG)    
except:
    print(ERR_MSG)

