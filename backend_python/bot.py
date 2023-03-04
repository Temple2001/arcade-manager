import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from youtube_api import YoutubeAPI
from db_api import MongoDB_API

# 패키지 설치
# pip install discord.py
# pip install python-dotenv

search_keyword = {
    '사볼(일반)': 'AmuseTown+SoundVoltex+Live+stream',
    '사볼(발키리)': 'AmuseTown+SDVX+Valkyrie+model+Live+stream',
    '츄니즘': 'AmuseTown+CHUNITHM+Live+stream',
    '마이마이': 'Amusetown+maimai+DX+Live+Stream'
}

load_dotenv(verbose=True)
BOT_KEY = os.getenv('BOT_KEY')

app = commands.Bot(command_prefix='=', intents=discord.Intents.all())
yt_api = YoutubeAPI()
db_api = MongoDB_API()

# 봇 부팅
@app.event
async def on_ready():
    print('Done')
    await app.change_presence(status=discord.Status.online, activity=None)


# 자동 명령어 버튼 생성
class Menu(discord.ui.View):
    def __init__(self, ctx):
        super().__init__()
        self.value = None
        self.ctx = ctx

    @discord.ui.button(label='사볼(일반)', style=discord.ButtonStyle.blurple)
    async def menu1(self, interaction:discord.Interaction, button:discord.ui.Button):
        v_id, error_msg = yt_api.find_video(search_keyword['사볼(일반)'])
        user = self.ctx.message.author

        if v_id == None:
            await interaction.response.edit_message(content=error_msg)
        else:
            progress_time, error_msg = yt_api.time_check(v_id)

            if progress_time == None:
                await interaction.response.edit_message(content=error_msg)
            else:
                error_msg = db_api.add_log(user.name, v_id, progress_time, '사볼 (일반기체)')

                if error_msg != None:
                    await interaction.response.edit_message(content=error_msg)
                else:
                    await interaction.response.edit_message(content=f'[OK] **사볼 (일반기체)** 기록되었습니다. 영상 내 시작 시간 : {progress_time}')
                    
        self.clear_items()
    
    @discord.ui.button(label='사볼(발키리)', style=discord.ButtonStyle.blurple)
    async def menu2(self, interaction:discord.Interaction, button:discord.ui.Button):
        v_id, error_msg = yt_api.find_video(search_keyword['사볼(발키리)'])
        user = self.ctx.message.author

        if v_id == None:
            await interaction.response.edit_message(content=error_msg)
        else:
            progress_time, error_msg = yt_api.time_check(v_id)

            if progress_time == None:
                await interaction.response.edit_message(content=error_msg)
            else:
                error_msg = db_api.add_log(user.name, v_id, progress_time, '사볼 (발키리기체)')

                if error_msg != None:
                    await interaction.response.edit_message(content=error_msg)
                else:
                    await interaction.response.edit_message(content=f'[OK] **사볼 (발키리기체)** 기록되었습니다. 영상 내 시작 시간 : {progress_time}')

        self.clear_items()
    
    @discord.ui.button(label='츄니즘', style=discord.ButtonStyle.blurple)
    async def menu3(self, interaction:discord.Interaction, button:discord.ui.Button):
        v_id, error_msg = yt_api.find_video(search_keyword['츄니즘'])
        user = self.ctx.message.author

        if v_id == None:
            await interaction.response.edit_message(content=error_msg)
        else:
            progress_time, error_msg = yt_api.time_check(v_id)

            if progress_time == None:
                await interaction.response.edit_message(content=error_msg)
            else:
                error_msg = db_api.add_log(user.name, v_id, progress_time, '츄니즘')

                if error_msg != None:
                    await interaction.response.edit_message(content=error_msg)
                else:
                    await interaction.response.edit_message(content=f'[OK] **츄니즘** 기록되었습니다. 영상 내 시작 시간 : {progress_time}')

        self.clear_items()

    @discord.ui.button(label='마이마이', style=discord.ButtonStyle.blurple)
    async def menu4(self, interaction:discord.Interaction, button:discord.ui.Button):
        v_id, error_msg = yt_api.find_video(search_keyword['마이마이'])
        user = self.ctx.message.author

        if v_id == None:
            await interaction.response.edit_message(content=error_msg)
        else:
            progress_time, error_msg = yt_api.time_check(v_id)
        
            if progress_time == None:
                await interaction.response.edit_message(content=error_msg)
            else:
                error_msg = db_api.add_log(user.name, v_id, progress_time, '마이마이')

                if error_msg != None:
                    await interaction.response.edit_message(content=error_msg)
                else:
                    await interaction.response.edit_message(content=f'[OK] **마이마이** 기록되었습니다. 영상 내 시작 시간 : {progress_time}')

        self.clear_items()


# 인사 명령어
@app.command()
async def hello(ctx):
    await ctx.reply('ㅎㅇ')


# 자동 체크 명령어
@app.command(aliases=['오토', '자동'])
async def auto(ctx):
    view = Menu(ctx)
    await ctx.reply('체크하고자 하는 기기를 골라주세요.',view=view)


# 수동 체크 명령어
@app.command(aliases=['수동'])
async def check(ctx, url):
    v_id, error_msg = yt_api.url_parse(url)
    user = ctx.message.author

    if v_id == None:
        await ctx.reply(error_msg)
    else:
        progress_time, error_msg = yt_api.time_check(v_id)

        if progress_time == None:
            await ctx.reply(error_msg)
        else:
            error_msg = db_api.add_log(user.name, v_id, progress_time, '수동 기록됨')

            if error_msg != None:
                await ctx.reply(error_msg)
            else:
                await ctx.reply(f'[OK] 기록되었습니다. 영상 내 시작 시간 : {progress_time}')


app.run(BOT_KEY)