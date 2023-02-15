import asyncio
import discord
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse
client = discord.Client(intents=discord.Intents.all())

# 디스코드에서 생성된 토큰을 여기에 추가
token = "MTAxNDA0MjkyMTc1NjAyMDgzNg.Gp8reI.wdlkoXFd_V_A57NVnCLDL3a1h-vE_EAfjyNqpA"

# 아래는 봇이 구동되었을 때 동작하는 부분
@client.event
async def on_ready():
    print("Logged in as ") #봇의 아이디, 닉네임이 출력
    print(client.user.name)
    print(client.user.id)

# 봇이 새로운 메시지를 수신했을때 동작하는 부분
@client.event
async def on_message(message):
	# 아래는 로스트 아크 홈페이지에서 아이디로 페이지를 읽어 레벨을 가져오는 부분
    url = "https://mhf.inven.co.kr/dataninfo/mhw/item/?code="+parse.quote(message.content[1:])
    print (url) # 로그 성 출력
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    tmpContent = bsObject.select_one('#mhwDb > div:nth-child(2) > table')
    searchLists = tmpContent.select('tbody > tr > td > a')
    result = []
    for searchList in searchLists:
        if searchList.get_text() not in result :
            result.append(searchList.get_text())
        str1 = '\n :point_right:  '.join(result)
    #tmpContent = bsObject.find_all("div", {"class":"mhw board board02"})[0].find_all("span")[1].text
    
    if message.author.bot: #봇이 메세지를 보냈다면..
        return None #걍 무시.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.
    if message.content.startswith('!안녕'): #만약 해당 메시지가 '!안녕' 으로 시작하는 경우에는
        #await client.send_message(channel, '안녕') #봇은 해당 채널에 '안녕' 이 라고 말합니다.
        await channel.send('안녕')
    else: #위의 if문에 해당되지 않는 경우
        # 로스트 아크 홈페이지 웹크롤링 한 부분을 출력
        await channel.send("**:arrow_down:  __\""+message.content[1:]+"\"__**  아이템을 주는 몬스터  :arrow_down: \n\n >>>  :point_right:  "+ str(str1) + "\n\n**:mag: 자세한 정보는 ? :mag:**\n" + str(url))
client.run(token)

