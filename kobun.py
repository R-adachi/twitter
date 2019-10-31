from janome.tokenizer import Tokenizer

t = Tokenizer()

s = ''

print(type(t.tokenize(s)))
# <class 'list'>

print(type(t.tokenize(s)[0]))
# <class 'janome.tokenizer.Token'>
flg=0
target=[]
purge=['空白','サ変接続','括弧開','括弧閉']
for token in t.tokenize(s):
    if(flg):
        if(token.part_of_speech.split(',')[1] not in purge):
            target.append(token.surface)
    if(token.part_of_speech.split(',')[1]=='副詞可能'):
        flg=1
        target.append(token.surface)
    if(token.part_of_speech.split(',')[2]=='組織' or token.surface=='ab'):
        flg=0
print(target)
