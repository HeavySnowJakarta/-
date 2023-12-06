import src.service as translate
import configure as c

translator = translate.Translator(c.from_lang, c.service, c.language_list)

if __name__ == "__main__":
    # 根据配置获取源字符串
    if c.get_console_source:
        source = input("请输入源字符串：")
    else:
        source = c.source

    # 按照 c.language_list 逐一翻译字符串并存储在 result 列表中
    result = []
    for language in c.language_list:
        result.append(translator.translate(source, language))
    print(result)