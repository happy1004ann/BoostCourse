# https://ranpy4e.slack.com/archives/C03N3FVJQ05/p1658042369568109

#name = input('enter file name: ')
name = 'C:\\Users\\HyeAnn\\Documents\\codes\\BoostCourse\\KakaoTalk_20220717_1623_19_105_준한.txt'
handle = open(name, 'r', encoding='UTF8')

handle.readline()   # xxx 님과 카카오톡 대화
handle.readline()   # 저장한 날짜 : xxx
handle.readline()   #

counts = dict()
for line in handle:
    if line.startswith('-'):    # --- xxxx년 xx월 xx일 x요일 ---
        continue
    words = line.split()    # ['[xxx]', '[오전/오후', 'hh:mm]', ...]
    for word in words[3:]:
        if word == '이모티콘':
            continue
        else:
            counts[word] = counts.get(word,0)+1

result = sorted(counts.items(), key = lambda item: item[1], reverse = True)
#print(result[:30])
for i in range(30):
    print(f'# {i}: {result[i][0]} ({result[i][1]})')