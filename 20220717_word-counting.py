# https://ranpy4e.slack.com/archives/C03N3FVJQ05/p1658042369568109

def postpositions(word):
    if word.endswith(pp4):
        pp = word[-4:]
        word = word[:-4]

    elif word.endswith(pp3):
        pp = word[-3:]
        word = word[:-3]

    elif word.endswith(pp2):
        pp = word[-2:]
        word = word[:-2]
        
    elif word.endswith(pp1):
        pp = word[-1]
        word = word[:-1]

    else:
        return word

    counts[pp] = counts.get(pp,0) + 1
    return word


#name = input('enter file name: ')
name = 'C:\\Users\\HyeAnn\\Documents\\codes\\BoostCourse\\KakaoTalk_20220717_1623_19_105_준한.txt'
handle = open(name, 'r', encoding='UTF8')

handle.readline()   # xxx 님과 카카오톡 대화
handle.readline()   # 저장한 날짜 : xxx
handle.readline()   #

# https://www.korean.go.kr/front/etcData/etcDataView.do?mn_id=46&etc_seq=61&pageIndex=44
# postpositions
pp4 = ('으로부터', '에서부터')
pp3 = ('으로써', '으로서', '로부터', '에게서', '야말로', '한테서', '에다가', '이나마', '에게로', '는커녕', '라든가', '은커녕', '라든지', '한테로', '마따나')
pp2 = ('에게', '까지', '부터', '처럼', '로서', '밖에', '한테', '께서', '조차', '에다', '로써', '이든', '이니', '더러', '이며', '에서', '따라', '에의', '마냥', '에로')
pp1 = ('를', '뿐')

counts = dict()
for line in handle:
    if line.startswith('--------------- '):    # --- xxxx년 xx월 xx일 x요일 ---
        continue
    if '선물을 보냈습니다. 지금 확인해 보세요!' in line:
        continue
    if '선물과 메시지를 보냈습니다.' in line:
        continue
    if line == '지금 확인해 보세요!':
        continue
    
    words = line.split()
    
    if len(words)>2 and words[1] in ['[오전', '[오후']:     # ['[xxx]', '[오전/오후', 'hh:mm]', ...]
        words = words[3:]
    
    for word in words:
        if word == '이모티콘':
            continue

        word = postpositions(word)
        if word == '':
            continue

        counts[word] = counts.get(word,0) + 1

result = sorted(counts.items(), key = lambda item: item[1], reverse = True)

print(f'Total {len(counts)} words')
#print(result[:30])
for i in range(30):
    print(f'# {i+1}: {result[i][0]} ({result[i][1]})')