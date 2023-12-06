from translate import Translator as t

class Translator:
    # 一个 Translator 对象的成员变量包含一个 translator 字典，该字典的每一个
    # value 都是 translate 库中的一个 Translate 对象，它们有着不同的 to_lang
    # 参数，输出不同的语言。它们的 key 是 ISO-639 格式的语言代码字符串。
    # translate 库允许指定不同的服务提供商（microsoft 或 deepl），此时
    # provider 参数为二者之一，secret 参数为你拥有的 key。
    def __init__(self, from_lang, language_list, provider='', secret=''):
        self.translator = {}
        if provider != '':
            for language in language_list:
                self.translator[language] = t(from_lang=from_lang, to_lang=language, provider=provider, secret_access_key=secret)
        else:
            for language in language_list:
                self.translator[language] = t(from_lang=from_lang, to_lang=language)

    # translate 方法承担实际的翻译过程，source 参数为被翻译的字符串，to_lang
    # 参数为被翻译成的语言，方法返回翻译结果字符串。
    def translate(self, source, to_lang):
        return self.translator[to_lang].translate(source)