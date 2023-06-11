import pycorrector
import sys
import time
# 文本纠错
# corrected_sent, detail = pycorrector.correct('眉飞色无')
# print(corrected_sent, detail)

# 错误检测
# idx_errors = pycorrector.detect('眉飞色无')
# print(idx_errors)

# 成语、专名纠错
# sys.path.append("..")
# from pycorrector.proper_corrector import ProperCorrector
# m = ProperCorrector()
# print(m.proper_correct("十全十每"))

# 自定义混淆集
# error_sentences = [
#     '十全十每',
# ]
# for line in error_sentences:
#     print(pycorrector.correct(line))
# print('*' * 42)
# pycorrector.set_custom_confusion_path_or_dict('./my_custom_confusion.txt')
# for line in error_sentences:
#     print(pycorrector.correct(line))

# 自定义语言模型
# from pycorrector import Corrector
# import os
#
# pwd_path = os.path.abspath(os.path.dirname(__file__))
# # 214版本人民日报数据训练的模型
# lm_path = os.path.join(pwd_path, 'pycorrector/datasets/people2014corpus_chars.klm')
# model = Corrector(language_model_path=lm_path)
#
# corrected_sent, detail = model.correct('十全十每')
# print(corrected_sent, detail)

# MacBert4csc模型
import os
sys.path.append("..")
from pycorrector.macbert.macbert_corrector import MacBertCorrector
pwd_path = os.path.abspath(os.path.dirname(__file__))
startTime = time.time()
print("开始处理")
if __name__ == '__main__':
    error_sentences = [
        '百渡',
    ]

    m = MacBertCorrector(pwd_path+"pycorrector/datasets/shibing624/macbert4csc-base-chinese")
    for line in error_sentences:
        correct_sent, err = m.macbert_correct(line)
        print("处理结束,耗时："+str(time.time() - startTime)+"秒")
        print("query:{} => {}, err:{}".format(line, correct_sent, err))