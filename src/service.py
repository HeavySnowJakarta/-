# 本文件把可用的不同翻译库导入到一起，并封装为统一的 Translator 类，本程序其余部分
# 将直接调用本文件的 Translator 库，并通过 service 参数告知本文件将使用哪种翻译
# 库。

# tran_services 位于父文件夹。
import sys
sys.path.append("..")

import tran_services.translate_module as translate

# service 未知时，程序将抛出 ServiceError 异常。ServiceError 类定义此异常。
class ServiceError(Exception):
    def __init__(self, service):
        self.message = 'service "{}" unknown. See ./tran_services for available services.'.format(service)
        super().__init__(self.message)

    def __str__(self):
        return self.message

# Translator 类的核心实现。其作为成员的成员 translator 所属的类由 trans_services
# 目录下的文件提供。
class Translator:
    # service 参数接受一字符串，其可取值可从 trans_services/list.txt 中找到。
    # language_list 参数接受一列表，包含 ISO 639-1 格式的语言代码。
    def __init__(self, from_lang, service, language_list):
        if service == "translate":
            self.translator = translate.Translator(from_lang, language_list)
        else:
            raise ServiceError(service)
    
    # trans_services 下调用各库的各类拥有统一的构造函数与 translate 方法，方便
    # 这里封装。
    def translate(self, source, to_lang):
        return self.translator.translate(source, to_lang)