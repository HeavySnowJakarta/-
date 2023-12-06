# 这是本项目的配置文件，存储了本项目所使用的配置性变量。
# 请勿注释以下任何变量，本项目可能没有针对它们设置默认值。

# service 变量存储使用的翻译库。可用的翻译库可以在 ./tran_services/list.txt
# 中找到。
service = "translate"

# from_lang 变量指定源语言。
from_lang = "zh"

# language_list 定义将源文字翻译成何种语言。语言的定义使用 ISO 639-1 格式。
language_list = ["en", "ja", "ko", "ru"]

# get_console_source 变量定义是否从控制台读取源字符串
get_console_source = True

# source 变量定义源字符串。当 get_console_source 为 True 时，此变量无效，程序
# 改为从控制台读取源字符串。
source = "哥，这条删了呗，我是无所谓的，但是我一个朋友可能有点汗流浃背了，他不太舒服想睡了，当然不是我哈，我一直都是行的，以一个旁观者的心态看吧，也不至于破防吧，就是想照顾下我朋友的感受，他有点破防了，还是建议删了吧，当然删不删随你，我是没感觉的，就是为朋友感到不平罢了，也不是那么简单破防的"

# source_bold 变量定义输出结果中的源字符串是否加粗。
source_bold = True