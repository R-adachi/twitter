from janome.tokenizer import Tokenizer

t = Tokenizer()

s = '◎あなたのサークル「第2コンドル採掘場」は、金曜日　南地区“シ”ブロック－30a に配置されました。スペースいただけたので、こんな感じの深海棲艦本作ります。進捗ﾀﾞﾒﾃﾞｽ'

print(type(t.tokenize(s)))
# <class 'list'>

print(type(t.tokenize(s)[0]))
# <class 'janome.tokenizer.Token'>

for token in t.tokenize(s):
    print(token)
