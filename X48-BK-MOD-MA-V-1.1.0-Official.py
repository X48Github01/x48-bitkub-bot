# ! =========== Import Zone ============
import os
import logging
from bitkub import Bitkub
from line_notify import LineNotify
import mplfinance as mplf
from configparser import ConfigParser
import time
import random
import pandas as pd
pd.set_option('display.max_rows', None)
import pandas_ta as ta
import warnings
warnings.filterwarnings('ignore')
import requests
import colorama
from colorama import Fore, Back, Style, init
init()

# ! ================ Version Of Bot ==================
version = f'⭐X48-BitKub-BOT-MA-TYPE-MOD⭐\n[Version] 1.1.0\n[Build] 20-01-2023\n[Original Source] By Varbara\n\n🧬[Mod] By X4815162342🧬'

# ! ================ API Host Of Bitkub ===============
API_HOST = 'https://api.bitkub.com'

# ! ================ Prepare Config Setting =================
dbconf = ConfigParser()
dbconf.read_file(open('config.ini'))

API_KEY = dbconf.get('CONFIG', 'API_KEY')
API_SECRET = dbconf.get('CONFIG', 'API_SECRET')
LINE_TOKEN = dbconf.get('CONFIG', 'LINE_TOKEN')
Account_Name = dbconf.get('CONFIG', 'ACCOUNT_NAME')

Symbol = dbconf.get('SETTING', 'SYMBOL').split(",")
cost = dbconf.get('SETTING', 'COST').split(",")
TFi = dbconf.get('SETTING', 'TF').split(",")
FASTTYPEi = dbconf.get('SETTING', 'FAST_TYPE').split(",")
FASTEMAi = dbconf.get('SETTING', 'FAST_MA').split(",")
MIDTYPEi = dbconf.get('SETTING', 'MID_TYPE').split(",")
MIDEMAi = dbconf.get('SETTING', 'MID_MA').split(",")
SLOWTYPEi = dbconf.get('SETTING', 'SLOW_TYPE').split(",")
SLOWEMAi = dbconf.get('SETTING', 'SLOW_MA').split(",")

TP_Mode = dbconf.get('TPSL', 'TP_MODE')
SL_Mode = dbconf.get('TPSL', 'SL_MODE')
TP_Percenti = dbconf.get('TPSL', 'TP_PERCENT').split(",")
SL_Percenti = dbconf.get('TPSL', 'SL_PERCENT').split(",")

PNL_Mode = dbconf.get('PNL', 'PNL_MODE')
TP_PNLi = dbconf.get('PNL', 'TP_PNL').split(",")
SL_PNLi = dbconf.get('PNL', 'SL_PNL').split(",")

mode_trade = dbconf.get('OPTION', 'MODE_TRADE')
Bar_Look = dbconf.get('OPTION', 'BAR_LOOK')
looptimeframe = dbconf.get("OPTION","TIME_LOOP_CHECK")
double_check = dbconf.get("OPTION","DOUBLE_CHECK")

# ! ============== Loop TimeFrame Type ===================
if  looptimeframe == '1s':
	looptimeframe_value = 0.018
	looptimeframe_values = 1
if  looptimeframe == '5s':
	looptimeframe_value = 0.085
	looptimeframe_values = 5
if  looptimeframe == '10s':
	looptimeframe_value = 0.17
	looptimeframe_values = 10
if  looptimeframe == '15s':
	looptimeframe_value = 0.25
	looptimeframe_values = 15
if  looptimeframe == '30s':
	looptimeframe_value = 0.5
	looptimeframe_values = 30
if  looptimeframe == '1m':
	looptimeframe_value = 1
	looptimeframe_values = 1
if  looptimeframe == '15m':
	looptimeframe_value = 15
	looptimeframe_values = 15
if  looptimeframe == '30m':
	looptimeframe_value = 30
	looptimeframe_values = 30
if  looptimeframe == '1h':
	looptimeframe_value = 60
	looptimeframe_values = 1
if  looptimeframe == '4h':
	looptimeframe_values = 4
	looptimeframe_value = 240
if  looptimeframe == '1d':
	looptimeframe_value = 1440
	looptimeframe_values = 1
if looptimeframe_value < 60:
	looptimeframe_type = 'นาที'
if looptimeframe_value >=60 and looptimeframe_value <1440 :
	looptimeframe_type = 'ชั่วโมง'
if looptimeframe_value == 1440:
	looptimeframe_type = 'วัน'

# ! ============== Make Important Variable To Float, Int, Str ===============
Bar_Look = int(Bar_Look)
text_side = 0
result = 0
TP_Calculate = 0
SL_Calculate = 0
TP_Divine = 0
SL_Divine = 0
pnl_cal = 0
pnl_cal_text = 'null'
now_cal = 0
entry_cal = 0
history_entry = 0
history_bk = 0
history_rate = 0
add_plus = 0
pnl_percent_change = 0
pnl_percent_change_text = 'null'

# ! ============== Line Notify Setting ==================
notify = LineNotify(LINE_TOKEN)

# ! ============= Print Welcome To CMD ==============
print(Fore.MAGENTA, Style.BRIGHT + 'Hi ! Master')
print(Style.RESET_ALL)
print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + 'Welcome To Auto Trade System On BITKUB SPOT')
print(Style.RESET_ALL)
print(Fore.LIGHTGREEN_EX, Style.BRIGHT, Back.BLUE + 'Mod By X4815162342')
print(Style.RESET_ALL)
print(Fore.LIGHTWHITE_EX, Style.BRIGHT + 'Tips')
print(Style.RESET_ALL)
print(Fore.LIGHTWHITE_EX, Style.BRIGHT + '5 MA TYPE CROSS')
print(Style.RESET_ALL)
print(Fore.LIGHTWHITE_EX, Style.BRIGHT + '1. EMA   2. SMA  3. HWA  4. RMA  5. WMA')
print(Style.RESET_ALL)
print(Fore.RED, Style.BRIGHT + 'Before Use Me, Dont Forget Backtest The Strategy MA Type Cross For Best Of Profit and Low Drawdown % ^^')
print(Style.RESET_ALL)
print(Fore.CYAN, Style.BRIGHT + 'Master !! You Can Try Backtest Your Stategy Here >> https://www.tradingview.com/v/DAD06s8m/')
print(Style.RESET_ALL)
xmr_donte = f'Donate For My Coffee\nXMR Address : 89Emmdegk7deMqR3iFDcwZGw8GtRwGPWAVzZbp6zdRm94eJ4j5bGWwnYozRAvw7y2EDoNbNWvZuGjL3h9v9v9TZWVZ5We1E'
print(Fore.LIGHTWHITE_EX, Style.BRIGHT + f'Donate For My Coffee\nXMR Address : 89Emmdegk7deMqR3iFDcwZGw8GtRwGPWAVzZbp6zdRm94eJ4j5bGWwnYozRAvw7y2EDoNbNWvZuGjL3h9v9v9TZWVZ5We1E' + Style.RESET_ALL)
print(Fore.LIGHTWHITE_EX, Style.BRIGHT + f'Donate For My Coffee\nDOGE Address : DAwnrjUBkucJTVJJghQSDcmBvZyciAP4Be' + Style.RESET_ALL)
print(Fore.LIGHTWHITE_EX, Style.BRIGHT + f'Donate For My Coffee\nCardano(ADA) Address : DdzFFzCqrhtCtT8xEpsuFZE3uxFX715Y3niUmbmie8eEP3cfrCnrkQjsvGNaJTLy26rySKwtdCzVJjGzZ8ztK31WTM5HreUbQpUfDR9U' + Style.RESET_ALL)
print(Fore.LIGHTWHITE_EX, Style.BRIGHT + f'Donate For My Coffee\nBitcoin(BTC) Address : 1Cq4Jpn6TZihRRX3Bo4XYF7xWMhR8fmDWy' + Style.RESET_ALL)
promptpay_donate = 'Buy Me a Coffee : PromptPay : 095-518-8528'
print(Fore.LIGHTYELLOW_EX, Style.BRIGHT + promptpay_donate + Style.RESET_ALL)
print(Fore.LIGHTGREEN_EX, Style.BRIGHT + 'Thanks For Support' + Style.RESET_ALL)
print('---------------------------------------------------------------------------------')
print('██   ██ ██   ██  █████   ██ ███████  ██  ██████  ██████  ██████  ██   ██ ██████ ')
print(' ██ ██  ██   ██ ██   ██ ███ ██      ███ ██            ██      ██ ██   ██      ██')
print('  ███   ███████  █████   ██ ███████  ██ ███████   █████   █████  ███████  █████ ')
print(' ██ ██       ██ ██   ██  ██      ██  ██ ██    ██ ██           ██      ██ ██     ')
print('██   ██      ██  █████   ██ ███████  ██  ██████  ███████ ██████       ██ ███████')
print('---------------------------------------------------------------------------------')
print(Fore.GREEN, Style.BRIGHT + '')
print('██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗ ')
print('██╔══██╗██║╚══██╔══╝██║ ██╔╝██║   ██║██╔══██╗')
print('██████╔╝██║   ██║   █████╔╝ ██║   ██║██████╔╝')
print('██╔══██╗██║   ██║   ██╔═██╗ ██║   ██║██╔══██╗')
print('██████╔╝██║   ██║   ██║  ██╗╚██████╔╝██████╔╝')
print('╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ')
print(Style.RESET_ALL + '')
print('---------------------------------------------------------------------------------')
print(Fore.BLUE, Style.BRIGHT + 'If You Found Some Bug Please Contact My Developer Master >> Here Line ID : x4815x')
print(Style.RESET_ALL)
print(Fore.LIGHTGREEN_EX + 'Master !! Please Wait For New TimeLoop By TimeFrame Setting <3 ^^')
print(Style.RESET_ALL)
print(Fore.GREEN, Style.BRIGHT + f'Account Name : ' + Style.RESET_ALL , Fore.LIGHTCYAN_EX + f'{Account_Name}' + Style.RESET_ALL)
print(Fore.GREEN, Style.BRIGHT + f'Time Loop Check : ' + Style.RESET_ALL , Fore.LIGHTCYAN_EX + f'{looptimeframe}' + Style.RESET_ALL)
print(Style.RESET_ALL)

list_trade = f'AAVE | ABT | ADA | ALPHA | BAL | BAND | BAT | BCH | BNB | BTC | COMP | CRV | CTXC | CVC | DOGE | DOT | ENJ | ETH | GALA | GLM | GRT | IOST | JFIN | KNC | KSM | KUB | LINK | MANA | MKR | NEAR | OMG | OP | POW | SCRT | SIX | SNT | SOL | SUSHI | UNI | WAN | XLM | XRP | YFI | ZIL | ZRX'

# ! ============== Welcome Notify Setting =================
welcome = f'\n💖💖สวัสดีค่ะนายท่าน ยินดีต้อนรับเข้าสู่\n\n{version}\n\n💎วิธีให้ BOT จับคู่เหรียญทำตามนี้ค่ะ💎\n❓เนื่องจาก Bitkub ต้องเปิดประวัติการทำธุรกรรมก่อน ถึงจะดึงประวัติได้\nแนะนำให้กดซื้อ/ขาย ผ่าน APP Bitkub ด้วยราคาขั้นต่ำ 20บ. ก่อน สำหรับทุกคู่เหรียญที่จะให้ BOT เทรด\n‼️‼️หากไม่มีประวัติ BOT จะ Error ไม่สามารถเทรดคู่เหรียญนั้นๆได้ค่ะ'
mes4 = f'\n💕คู่มือการใช้งาน💕\n😘MA TYPE CROSS ทั้ง 5 ประเภทดังนี้ค่ะ\n ➖EMA➖\n ➖SMA➖\n ➖HWA➖\n ➖RMA➖\n ➖WMA➖\n🚨อย่าลืม Backtest ก่อนใช้งานนะคะ🚨\nเพื่อผลลัพธ์ที่ดีที่สุดค่ะ\n🛎️สามารถ Backtest ได้ที่นี่เลยค่ะ ⏬⏬⏬\nhttps://www.tradingview.com/v/DAD06s8m/\nหากพบปัญหา แจ้งเข้ามาได้ที่นี่ค่ะ Line ID : x4815x\n🍵สนับสนุนค่ากาแฟ ได้ที่นี่ค่ะ : พร้อมเพย์ 095-518-8528'
mesconfig = f'\n💞การตั้งค่าเบื้องต้นค่ะ💞\n\n👑คู่เหรียญที่เทรด👑\n{Symbol}\n\n📌OPTION📌\nTRADE : {mode_trade}\nแท่งเทียนย้อนหลัง : {Bar_Look} แท่ง\nระบบทำงานทุกๆ : {looptimeframe_values} {looptimeframe_type}\nDouble Check : {double_check}\nTake Profit (%) Mode : {TP_Mode}\nStop Loss (%) Mode : {SL_Mode}\nTP/SL by PNL MODE : {PNL_Mode}'
meserror = f'\n💉💉โปรแกรมนี้เป็นโปรแกรมที่จัดทำขึ้นให้เพื่อนๆพี่ๆน้องๆ ใช้งานฟรี\n\n>>ขอความกรุณาโปรดอย่านำไปขาย<<\n\nหากผู้พัฒนาพบเห็นการขายบอทนี้ จะไม่ Update และปรับปรุงพัฒนาให้ใช้งานฟรีอีกต่อไป'
messdonation = f'\n📣💰หากอยากเลี้ยงกาแฟ หรือ สนับสนุนผู้พัฒนาและน้องแสนเหนื่อย สามารถทำได้ดังช่องทางต่อไปนี้เลยค่ะ\n\n📱พร้อมเพย์ : 095-518-8528\n💲Bitcoin(BTC) address : 1Cq4Jpn6TZihRRX3Bo4XYF7xWMhR8fmDWy\n🐕‍🦺DogeCoin(Doge) address : DAwnrjUBkucJTVJJghQSDcmBvZyciAP4Be'
notify.send(welcome)
notify.send(mes4)
notify.send(mesconfig)
notify.send(meserror)
notify.send(messdonation)

# ! ============== Bitkub API Setting ===============
bitkub = Bitkub()
bitkub.set_api_key(API_KEY)
bitkub.set_api_secret(API_SECRET)
bitkub.servertime()

# ! ============= mplfinance for plot LinePic Setting ==============
def LinePic(symbol, df, TF, FASTTYPE, MIDTYPE, SLOWTYPE, FASTEMA, MIDEMA, SLOWEMA, text_side, bathcoin, amount):
	try:
		data = df.tail(Bar_Look)
		df["rsiup"] = 70
		df["rsidown"] = 30
		rsi_tail = df["rsi"].tail(Bar_Look)
		rsiup = df["rsiup"].tail(Bar_Look)
		rsidown = df["rsidown"].tail(Bar_Look)

		rsiupplot = mplf.make_addplot(rsiup, ylim=(10, 90), linestyle = "--", color = "red", panel = 1)
		rsidownplot = mplf.make_addplot(rsidown, ylim = (10, 90), linestyle = "--", color = "red", panel = 1)

		RSIplot = mplf.make_addplot(rsi_tail, ylim = (10,90), color = "yellow", fill_between = dict(y1 = 30, y2 = 69, color = "#6C0065"), panel = 1, ylabel = f'\n\nRSI', linewidths = 1)

		MACD = df["MACD"].tail(Bar_Look)
		MACDs = df["MACDs"].tail(Bar_Look)
		colors = ['#4BEA00' if h >= 0 else '#FF3737' for h in MACD]
		MACDplot = mplf.make_addplot(MACD, type='bar', color=colors, panel=2, ylabel=f'\n\n\nMACD')
		MACDsplot = mplf.make_addplot(MACDs, color="white", panel=2, linewidths=1)

		fast = df["EMAfast"].tail(Bar_Look)
		fastplot = mplf.make_addplot(fast, secondary_y = False, color='yellow')

		mid = df["EMAmid"].tail(Bar_Look)
		midplot = mplf.make_addplot(mid,secondary_y=False,color='#2FE3FF')

		slow = df["EMAslow"].tail(Bar_Look)
		slowplot = mplf.make_addplot(slow,secondary_y=False,color='#FF61F5')
		amount = str(amount)
		if text_side =='SELL':
			minititile_detail = f'\n\n{symbol} | {TF} | {FASTTYPE} x {MIDTYPE} x {SLOWTYPE} | {FASTEMA} x {MIDEMA} x {SLOWEMA}\nSignal : {text_side} | Order Size : {bathcoin} ฿'
		if text_side =='BUY':
			minititile_detail = f'\n\n{symbol} | {TF} | {FASTTYPE} x {MIDTYPE} x {SLOWTYPE} | {FASTEMA} x {MIDEMA} x {SLOWEMA}\nSignal : {text_side} | Order Size : {bathcoin} ฿'
		mc = mplf.make_marketcolors(up='#00CA19',down='#FF1F1F',inherit=True)
		s  = mplf.make_mpf_style(base_mpf_style='nightclouds',marketcolors=mc)
		mplf.plot(data, figratio = (16, 9), type = 'candle', title = f'Bitkub\n{minititile_detail}', tight_layout = False, addplot = [fastplot, midplot, slowplot, rsiupplot, rsidownplot, RSIplot, MACDplot, MACDsplot], style = s,  panel_ratios=(6, 3, 2), savefig = 'order.png')
		notify.send("Order : "+symbol,image_path ='./order.png')
	except Exception as Error:
		print(Fore.WHITE, Back.RED + f'[LinePicture Error] -LinePic Def Error {Error}' + Style.RESET_ALL)
		mess_error = f'\n📣📣ตรวจพบ Error ใน LinePic Def ค่ะนายท่าน 📣📣\n\n{Error}'
		notify.send(mess_error)
		pass
	return


def trade(symbol, df, EMAfast, EMAmid, EMAslow, order, TF, FASTEMA, MIDEMA, SLOWEMA, FASTTYPE, MIDTYPE, SLOWTYPE, TP_Mode, SL_Mode, TP_Percent, SL_Percent, PNL_Mode, TP_PNL, SL_PNL):
	wall = bitkub.wallet()
	res = 'result'
	t = 'THB'
	amtwall = (wall[res][t])  #เงินในกระเป๋า
	BKcoin=t+ '_'+symbol
	Symbol_Show = symbol + '/' + t
	last=bitkub.ticker(BKcoin)[BKcoin]['last'] #ราคาเหรียญปัจจุบัน
	#print(amtwall)
	#amount = 0
	if order[0]=='!' :
		amount = (float(amtwall) * (float(order[1:len(order)])/ 100))
	elif order[0]=='@' :
		amount = (float(order[1:len(order)]))*float(last)
	else:
		amount = float(order)
	last = float(last)
	amtcoin = float(wall[res][symbol])
	amtcoin = float(amtcoin)
	bathcoin = float(last * amtcoin)
	bathcoin = int(bathcoin)
	try :
		if bathcoin < 11 and amtwall >= amount and EMAfast.iloc[-3]<EMAslow.iloc[-3] and EMAfast.iloc[-2]>=EMAslow.iloc[-2]:
			print(Fore.WHITE, Back.LIGHTGREEN_EX, Style.BRIGHT + f'MA Cross Up ==BUY==' + Style.RESET_ALL + '\n===============')
			text_side = 'BUY'
			pbuy = bitkub.place_bid(sym=BKcoin, amt=amount, rat=last, typ='market')
			wall = bitkub.wallet()
			res = 'result'
			t = 'THB'
			amtwall = (wall[res][t])
			LinePic(symbol, df, TF, FASTTYPE, MIDTYPE, SLOWTYPE, FASTEMA, MIDEMA, SLOWEMA, text_side, amount, bathcoin)
			mess_buy = f'\n💕นายท่านจ๋า หนูพบสัญญาณเข้าซื้อค่ะ\n\n💎 {Symbol_Show} 💎\n💱สถานะ : เข้าซื้อ ⬆️↗️\n💵ราคา : {round(last,5)} บาท\n🔢จำนวน : {round(amount,2)} บาท / {round(amount/last,5)} เหรียญ\n🕛TimeFrame : {TF}\n📊MA Type : {FASTTYPE} x {MIDTYPE} x {SLOWTYPE}\n🔎MA Value : {FASTEMA} x {MIDEMA} x {SLOWEMA}\n\n💰ยอดเงินคงเหลือ : {amtwall} บาท\n\n📌Account : {Account_Name}'
			notify.send(mess_buy, sticker_id=51626495, package_id=11538)
			if TP_Mode == 'ON':
				TP_Divine = float(TP_Percent/100)
				TP_Calculate = round(last+(last*TP_Divine),2)
				mess_tp = f'\n📈รายละเอียดการ TP ค่ะนายท่าน📈\n\n💎 {Symbol_Show} 💎\n🔝💹 TP % : {TP_Percent} % ⬆️↗️\n📍ราคาเข้าซื้อ : {last} บาท\n💲ราคา TP : {TP_Calculate} บาท\n\n✅น้องแสนเหนื่อยได้รับคำสั่ง TakeProfit เรียบร้อยค่ะ✅'
				notify.send(mess_tp)
				print(f'Notify TP_Mode = ON | TP% : {TP_Percent}% | Price TP Target : {TP_Calculate} THB')
			if SL_Mode == 'ON':
				SL_Divine = float(SL_Percent/100)
				SL_Calculate = round(last-(last*SL_Divine),2)
				mess_sl = f'\n📉รายละเอียดการ SL ค่ะนายท่าน📉\n\n💎 {Symbol_Show} 💎\n🔻↘️ SL % : {SL_Percent} % ⬇️↘️\n📍ราคาเข้าซื้อ : {last} บาท\n💲ราคา SL : {SL_Calculate} บาท\n\n✅น้องแสนเหนื่อยได้รับคำสั่ง StopLoss เรียบร้อยค่ะ✅'
				notify.send(mess_sl)
				print(f'Notify SL_Mode = ON | SL% : {SL_Percent}% | Price SL Target : {SL_Calculate} THB')
			if PNL_Mode == 'ON':
				mess_pnl = f'\n🏧รายละเอียดการ TP/SL by PNL ค่ะนายท่าน🏧\n\n💎 {Symbol_Show} 💎\n🔢จำนวนเงินเข้าซื้อ : {round(amount,2)} บาท\n🔝💹 TP by PNL(กำไร) : +{TP_PNL} บาท\n🔻↘️ SL by PNL(ขาดทุน) : -{SL_PNL} บาท\n\n✅น้องแสนเหนื่อยได้รับคำสั่ง TP/SL by PNL เรียบร้อยค่ะ✅\nหากราคา กำไร/ขาดทุน ถึงที่กำหนด ระบบจะทำการขายให้อัตโนมัติค่ะ 😘'
				notify.send(mess_pnl)
				print(f'Notify PNL_Mode = ON | TP by PNL : +{TP_PNL} THB | SL by PNL : -{SL_PNL} THB')

		if bathcoin >= 11 and EMAfast.iloc[-3]>EMAmid.iloc[-3] and EMAfast.iloc[-2]<EMAmid.iloc[-2]:
			print(Fore.WHITE, Back.LIGHTRED_EX, Style.BRIGHT + f'MA Cross Down ==SELL==' + Style.RESET_ALL + '\n===============')
			wall = bitkub.wallet()
			res = 'result'
			t = 'THB'
			amtwall = (wall[res][t])  #เงินในกระเป๋า
			BKcoin= t+ '_'+symbol
			Symbol_Show = symbol + '/' + t
			last = bitkub.ticker(BKcoin)[BKcoin]['last'] #ราคาเหรียญปัจจุบัน
			last = float(last)
			amtcoin = float(wall[res][symbol])
			amtcoin = float(amtcoin)
			bathcoin = float(last * amtcoin)
			bathcoin = int(bathcoin)
			text_side = 'SELL'
			psell = bitkub.place_ask_by_fiat(sym=BKcoin, amt=bathcoin, rat=last, typ='market')
			time.sleep(1)
			LinePic(symbol, df, TF, FASTTYPE, MIDTYPE, SLOWTYPE, FASTEMA, MIDEMA, SLOWEMA, text_side, bathcoin, amount)
			mess_sell = f'\n💕นายท่านจ๋า หนูพบสัญญาณขายค่ะ\n\n💎 {Symbol_Show} 💎\n💱สถานะ : ขาย ⬇️↘️\n💵ราคา : {round(last,5)} บาท\n🔢จำนวน : {round(amtcoin,5)} เหรียญ / {round(bathcoin,2)} บาท\n🕛TimeFrame : {TF}\n📊MA Type : {FASTTYPE} x {MIDTYPE} x {SLOWTYPE}\n🔎MA Value : {FASTEMA} x {MIDEMA} x {SLOWEMA}\n\n💰ยอดเงินคงเหลือ : {amtwall} บาท\n\n📌Account : {Account_Name}'
			notify.send(mess_sell, sticker_id=51626509, package_id=11538)
			time.sleep(1)
			#if bathcoin >= 11:
			#    time.sleep(1)
			#    wall = bitkub.wallet()
			#    res = 'result'
			#    t = 'THB'
			#    amtwall = (wall[res][t])  #เงินในกระเป๋า
			#    BKcoin=t+ '_'+symbol
			#    Symbol_Show = symbol + '/' + t
			#    last = bitkub.ticker(BKcoin)[BKcoin]['last'] #ราคาเหรียญปัจจุบัน
			#    last = int(last)
			#    amtcoin = float(wall[res][symbol])
			#    amtcoin = round(amtcoin,8)
			#    bathcoin = int(last * amtcoin)
			#    psell = bitkub.place_ask_by_fiat(sym=BKcoin, amt=bathcoin, rat=last, typ='market')
			#    mess_sell2 = f'\n🚨นายท่านจ๋าหนูตรวจพบ สัญญาณก่อนหน้านี้ขายไม่หมดค่ะ\n\n✅หนูได้ทำการขายเศษเหรียญที่เหลือเรียบร้อยแล้ว✅\n\n💎 {Symbol_Show} 💎\n💵ราคา : {round(last,5)} บาท\n🔢จำนวน : {round(amtcoin,5)} เหรียญ / {round(bathcoin,2)} บาท\n\n💰ยอดเงินคงเหลือ : {amtwall} บาท\n\n📌Account : {Account_Name}'
			#    notify.send(mess_sell2, sticker_id=51626518, package_id=11538)
			#    time.sleep(1)


	except Exception as Error:
		print(Fore.WHITE, Back.RED + f'[Cross Calculate Error] - Trade Def Error {Error}' + Style.RESET_ALL)
		mess_error = f'\n📣📣ตรวจพบ Error ใน Trade Def When Cross Calculation ค่ะนายท่าน 📣📣\n\n{BKcoin}\n{Error}'
		notify.send(mess_error)
		pass

	if bathcoin < 11:
		print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + f'{Symbol_Show} | {order} ฿ | TimeFrame : {TF} | MA Type : {FASTTYPE} x {MIDTYPE} x {SLOWTYPE} | MA Value : {FASTEMA} x {MIDEMA} x {SLOWEMA}' + Style.RESET_ALL)
		print(Style.RESET_ALL)
		print(Fore.LIGHTGREEN_EX, Style.BRIGHT, Back.BLUE + 'Status : Waiting For >>Buy<< Signal By MA Type Cross ...' + Style.RESET_ALL + '\n================================')
	if bathcoin >= 11:
		print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + f'{Symbol_Show} | {round(bathcoin, 2)} ฿ | TimeFrame : {TF} | MA Type : {FASTTYPE} x {MIDTYPE} x {SLOWTYPE} | MA Value : {FASTEMA} x {MIDEMA} x {SLOWEMA}' + Style.RESET_ALL)
		print(Style.RESET_ALL)
		print(Fore.LIGHTWHITE_EX, Style.BRIGHT, Back.GREEN + 'Status : Waiting For >>Sell<< Signal By MA Type Cross ...' + Style.RESET_ALL + '\n================================')
		try:
			if TP_Mode == 'ON':
				history_bk = bitkub.my_open_history(sym=BKcoin)[res]
				history_rate = []
				for i in history_bk:
					if i ['side']=='buy':
						if 'rate' in i:
							history_rate.append(i['rate'])
				#print(f'Last Price Entry : {history_rate[0]}')
				history_entry = float(history_rate[0])
				entry_cal = round(history_entry*amtcoin,2)
				now_cal = round(last*amtcoin,2)
				pnl_cal = round(now_cal-entry_cal,2)
				TP_Divine = float(TP_Percent/100)
				TP_Calculate = round(history_entry+(history_entry*TP_Divine),2)
				pnl_percent_change = round(((now_cal-entry_cal)/entry_cal)*100,2)
				if pnl_cal > 0:
					add_plus = str('+')
					pnl_cal_text = str(add_plus) + str(pnl_cal) + " " + t
					pnl_percent_change_text = str(add_plus) + str(pnl_percent_change)
				elif pnl_cal < 0:
					pnl_cal_text = str(pnl_cal) + " " + t
					pnl_percent_change_text = str(pnl_percent_change)
				if last > TP_Calculate:
					text_side = 'SELL'
					psell = bitkub.place_ask_by_fiat(sym=BKcoin, amt=bathcoin, rat=last, typ='market')
					time.sleep(1)
					LinePic(symbol, df, TF, FASTTYPE, MIDTYPE, SLOWTYPE, FASTEMA, MIDEMA, SLOWEMA, text_side, bathcoin, amount)
					mess_sell = f'\n💕นายท่านจ๋า ยินดีด้วยถึงเวลา TP ค่าาาาา💕\n\n💎 {Symbol_Show} 💎\n💱สถานะ : Take Profit 🤑🤑\n💵ราคา : {round(last,5)} บาท\n🔢จำนวน : {round(amtcoin,5)} เหรียญ / {round(bathcoin,2)} บาท\n🕛TimeFrame : {TF}\n\n💵💰Profit PNL : {pnl_cal_text}\nPrice Now : {now_cal} บาท\nPrice TP : {TP_Calculate} บาท\n\n📌Account : {Account_Name}'
					notify.send(mess_sell, sticker_id=51626509, package_id=11538)
					print(f'History Entry Price: {str(history_entry)} | History Baht Entry Pay : {str(entry_cal)} ฿ | Now Baht Calculate : {str(now_cal)} | PNL by THB : {str(pnl_cal_text)} | PNL by % : {str(pnl_percent_change_text)}%\nTP Calculate : {TP_Calculate} THB')
					time.sleep(1)
			if SL_Mode == 'ON':
				history_bk = bitkub.my_open_history(sym=BKcoin)[res]
				history_rate = []
				for i in history_bk:
					if i ['side']=='buy':
						if 'rate' in i:
							history_rate.append(i['rate'])
				#print(f'Last Price Entry : {history_rate[0]}')
				history_entry = float(history_rate[0])
				entry_cal = round(history_entry*amtcoin,2)
				now_cal = round(last*amtcoin,2)
				pnl_cal = round(now_cal-entry_cal,2)
				SL_Divine = float(SL_Percent/100)
				SL_Calculate = round(history_entry-(history_entry*SL_Divine),2)
				pnl_percent_change = round(((now_cal-entry_cal)/entry_cal)*100,2)
				if pnl_cal > 0:
					add_plus = str('+')
					pnl_cal_text = str(add_plus) + str(pnl_cal) + " " + t
					pnl_percent_change_text = str(add_plus) + str(pnl_percent_change)
				elif pnl_cal < 0:
					pnl_cal_text = str(pnl_cal) + " " + t
					pnl_percent_change_text = str(pnl_percent_change)
				if last < SL_Calculate:
					text_side = 'SELL'
					psell = bitkub.place_ask_by_fiat(sym=BKcoin, amt=bathcoin, rat=last, typ='market')
					time.sleep(1)
					LinePic(symbol, df, TF, FASTTYPE, MIDTYPE, SLOWTYPE, FASTEMA, MIDEMA, SLOWEMA, text_side, bathcoin, amount)
					mess_sell = f'\n💕นายท่านจ๋า นี่คือช่วงเวลา SL เพื่อให้พอร์ตดำเนินต่อไปค่ะ💕\nเสียได้ แต่ไม่ล้างพอร์ต ไม่ดอย แน่นอนค่ะ ฮึบๆ 🥰🥰ต้องมีผิดทางบ้าง ไม่มีระบบไหน ถูกต้อง 100% แน่นอนค่ะในโลกนี้🥲🥲\nน้องแสนเหนื่อยเป็นกำลังใจให้นายท่านเสมอค่าาา ♥️♥️\n\n💎 {Symbol_Show} 💎\n💱สถานะ : Stop Loss 😅😅\n💵ราคา : {round(last,5)} บาท\n🔢จำนวน : {round(amtcoin,5)} เหรียญ / {round(bathcoin,2)} บาท\n🕛TimeFrame : {TF}\n\n💵💰Profit PNL : {pnl_cal_text}\nPrice Now : {now_cal} บาท\nPrice SL : {SL_Calculate}\n\n📌Account : {Account_Name}'
					notify.send(mess_sell, sticker_id=51626509, package_id=11538)
					print(f'History Entry Price: {str(history_entry)} | History Baht Entry Pay : {str(entry_cal)} ฿ | Now Baht Calculate : {str(now_cal)} | PNL by THB : {str(pnl_cal_text)} | PNL by % : {str(pnl_percent_change_text)}%\nSL Calculate : {SL_Calculate} THB')
					time.sleep(1)
			if PNL_Mode == 'ON':
				history_bk = bitkub.my_open_history(sym=BKcoin)[res]
				history_rate = []
				for i in history_bk:
					if i ['side']=='buy':
						if 'rate' in i:
							history_rate.append(i['rate'])
				#print(f'Last Price Entry : {history_rate[0]}')
				history_entry = float(history_rate[0])
				entry_cal = round(history_entry*amtcoin,2)
				now_cal = round(last*amtcoin,2)
				pnl_cal = round(now_cal-entry_cal,2)
				SL_PNL = (SL_PNL*-1)
				if pnl_cal > TP_PNL:
					text_side = 'SELL'
					psell = bitkub.place_ask_by_fiat(sym=BKcoin, amt=bathcoin, rat=last, typ='market')
					time.sleep(1)
					LinePic(symbol, df, TF, FASTTYPE, MIDTYPE, SLOWTYPE, FASTEMA, MIDEMA, SLOWEMA, text_side, bathcoin, amount)
					mess_sell = f'\n💕นายท่านจ๋า ยินดีด้วยถึงเวลา TP by PNL ค่าาาาา💕\n\n💎 {Symbol_Show} 💎\n💱สถานะ : Take Profit by PNL🤑🤑\n💵ราคา : {round(last,5)} บาท\n🔢จำนวน : {round(amtcoin,5)} เหรียญ / {round(bathcoin,2)} บาท\n🕛TimeFrame : {TF}\n\n💵💰Profit by PNL : +{pnl_cal} บาท\nPNL Target : +{TP_PNL} บาท\n\n📌Account : {Account_Name}'
					notify.send(mess_sell, sticker_id=51626509, package_id=11538)
					print(f'History Entry Price: {str(history_entry)} | History Baht Entry Pay : {str(entry_cal)} ฿ | Now Baht Calculate : {str(now_cal)} | PNL by THB : {str(pnl_cal_text)} | PNL by % : {str(pnl_percent_change_text)}% | PNL TP : {TP_PNL} THB | PNL SL : {SL_PNL} THB')
					time.sleep(1)
				elif pnl_cal < SL_PNL:
					text_side = 'SELL'
					psell = bitkub.place_ask_by_fiat(sym=BKcoin, amt=bathcoin, rat=last, typ='market')
					time.sleep(1)
					LinePic(symbol, df, TF, FASTTYPE, MIDTYPE, SLOWTYPE, FASTEMA, MIDEMA, SLOWEMA, text_side, bathcoin, amount)
					mess_sell = f'\n💕นายท่านจ๋า นี่คือช่วงเวลา SL by PNL เพื่อให้พอร์ตดำเนินต่อไปค่ะ💕\nเสียได้ แต่ไม่ล้างพอร์ต ไม่ดอย แน่นอนค่ะ ฮึบๆ 🥰🥰ต้องมีผิดทางบ้าง ไม่มีระบบไหน ถูกต้อง 100% แน่นอนค่ะในโลกนี้🥲🥲\nน้องแสนเหนื่อยเป็นกำลังใจให้นายท่านเสมอค่าาา ♥️♥️\n\n💎 {Symbol_Show} 💎\n💱สถานะ : Stop Loss by PNL😅😅\n💵ราคา : {round(last,5)} บาท\n🔢จำนวน : {round(amtcoin,5)} เหรียญ / {round(bathcoin,2)} บาท\n🕛TimeFrame : {TF}\n\n💵💰Loss PNL : {pnl_cal} บาท\nPNL SL Target : {SL_PNL} บาท\n\n📌Account : {Account_Name}'
					notify.send(mess_sell, sticker_id=51626509, package_id=11538)
					print(f'History Entry Price: {str(history_entry)} | History Baht Entry Pay : {str(entry_cal)} ฿ | Now Baht Calculate : {str(now_cal)} | PNL by THB : {str(pnl_cal_text)} | PNL by % : {str(pnl_percent_change_text)}% | PNL TP : {TP_PNL} THB | PNL SL : {SL_PNL} THB')
					time.sleep(1)
		except Exception as Error:
			print(f'Error In Trade Def : {Error}')
			mess_error = f'\n📣📣ตรวจพบ Error ใน Trade Def ค่ะนายท่าน 📣📣\n\n{BKcoin}\n{Error}'
			notify.send(mess_error)
			pass
	return

def indicator(symbol, TF, FASTEMA, MIDEMA, SLOWEMA, FASTTYPE, MIDTYPE, SLOWTYPE):
	response = requests.get(API_HOST + '/api/servertime')
	ts = int(response.text)
	COIN_TV = symbol+'_THB'
	### ระยะเวลาที่ต้องการดึงข้อมูลย้อนหลัง หน่วยวินาที
	tc = ts - 86400000
	TF_Value = '1d'
	if TF=='15m' or TF=='15':
		tc = ts - 910000
		TF_Value = 15
	if TF=='30m' or TF=='30':
		tc = ts - 1810000
		TF_Value = 30
	if TF=='1h' or TF=='60':
		tc = ts - 3610000
		TF_Value = 60
	if TF=='4h' or TF=='240':
		tc = ts - 14410000
		TF_Value = 240
	if TF=='1d' or TF=='1D':
		tc = ts - 86400000
		TF_Value = '1D'
	if TF == '1m' or TF=='1':
		tc = ts - 60000
		TF_Value = 1
		#print(Fore.YELLOW, Back.RED, Style.BRIGHT + f'TF Cant Less Than 15m\nAuto Fix TF Minimum = 15m\nPlease Check Config Setting and Fix This Error' + Style.RESET_ALL)
		#mess_tf_error = f'\n📢📢แจ้งนายท่าน🚨🚨\nตรวจพบการตั้งค่า TF ผิดพลาด\n\n⛔⛔ไม่สามารถตั้ง TF น้อยกว่า 15 นาทีได้⛔⛔\n\nหนูจะทำการ Set Auto TF ที่ 15m ให้อัตโนมัติก่อนค่ะ\n\nโปรดตรวจสอบและแก้ไข Config ใหม่อีกครั้ง💕💕'
		#notify.send(mess_tf_error, sticker_id=51626516, package_id=11538)
	SYMBOL = COIN_TV
	RESULOTION = TF_Value
	TIME_FROM = (str(tc))  #Timestamp of the starting time
	TIME_TO = (str(ts))   #Timestamp of the ending time
	response = requests.get(API_HOST+f'/tradingview/history?symbol={SYMBOL}&resolution={RESULOTION}&from={TIME_FROM}&to={TIME_TO}')
	result = response.json()
	df = pd.DataFrame(result)
	df = df.rename(columns={'c':'Close','h':'High','l':'Low','o':'Open','s':'Stat','t':'Date','v':'Volume'})
	df['Date'] = pd.to_datetime(df['Date'], unit='s', utc=True).map(lambda x: x.tz_convert('Asia/Bangkok'))
	df = df.set_index('Date')
	#print(df)
	# ! ============= Value of Indicator Setting ==================
	try:
		df["rsi"] = ta.rsi(df["Close"],14)
		rsi = df["rsi"]
		datamacd = ta.macd(df["Close"], 12, 26, 9)
		df["MACD"] = datamacd["MACD_12_26_9"]
		df["MACDs"] = datamacd["MACDs_12_26_9"]
		# ! ========== FAST MA TYPE ============
		if FASTTYPE == 'EMA':
			df['EMAfast'] = ta.ema(df['Close'], int(FASTEMA))
		if FASTTYPE == 'SMA':
			df['EMAfast'] = ta.sma(df['Close'], int(FASTEMA))
		if FASTTYPE == 'WMA':
			df['EMAfast'] = ta.wma(df['Close'], int(FASTEMA))
		if FASTTYPE == 'HMA':
			df['EMAfast'] = ta.hma(df['Close'], int(FASTEMA))
		if FASTTYPE == 'RMA':
			df['EMAfast'] = ta.rma(df['Close'], int(FASTEMA))
		# ! ========== MID MA TYPE ============
		if MIDTYPE == 'EMA':
			df['EMAmid'] = ta.ema(df['Close'], int(MIDEMA))
		if MIDTYPE == 'SMA':
			df['EMAmid'] = ta.sma(df['Close'], int(MIDEMA))
		if MIDTYPE == 'WMA':
			df['EMAmid'] = ta.wma(df['Close'], int(MIDEMA))
		if MIDTYPE == 'HMA':
			df['EMAmid'] = ta.hma(df['Close'], int(MIDEMA))
		if MIDTYPE == 'RMA':
			df['EMAmid'] = ta.rma(df['Close'], int(MIDEMA))
		# ! ========== SLOW MA TYPE ===========
		if SLOWTYPE == 'EMA':
			df['EMAslow'] = ta.ema(df['Close'], int(SLOWEMA))
		if SLOWTYPE == 'SMA':
			df['EMAslow'] = ta.sma(df['Close'], int(SLOWEMA))
		if SLOWTYPE == 'WMA':
			df['EMAslow'] = ta.wma(df['Close'], int(SLOWEMA))
		if SLOWTYPE == 'HMA':
			df['EMAslow'] = ta.hma(df['Close'], int(SLOWEMA))
		if SLOWTYPE == 'RMA':
			df['EMAslow'] = ta.rma(df['Close'], int(SLOWEMA))
		# ! ========== After Def. MA Type =============
		EMAfast = df['EMAfast']
		EMAmid = df['EMAmid']
		EMAslow = df['EMAslow']
	except Exception as Error:
		rsi = 0
		adx = 0
		datamacd = ta.macd(df["Close"], 1, 1, 9)
		df['EMAfast'] = ta.ema(df['Close'], int(0))
		df['EMAmid'] = ta.ema(df['Close'], int(0))
		df['EMAslow'] = ta.ema(df['Close'], int(0))
		EMAfast = df['EMAfast']
		EMAmid = df['EMAmid']
		EMAslow = df['EMAslow']
		pass

	return EMAfast, EMAmid, EMAslow, df

LineNotice = False

def main():
	global LineNotice
	seconds = time.time()
	local_time = time.ctime(seconds)
	wall = bitkub.wallet()
	res = 'result'
	t = 'THB'
	for i in range(len(Symbol)):
		try:
			symbol = Symbol[i]
			order = cost[i]
			TF = TFi[i]
			FASTTYPE = FASTTYPEi[i]
			FASTEMA = FASTEMAi[i]
			MIDTYPE = MIDTYPEi[i]
			MIDEMA = MIDEMAi[i]
			SLOWTYPE = SLOWTYPEi[i]
			SLOWEMA = SLOWEMAi[i]
			TP_Percent = float(TP_Percenti[i])
			SL_Percent = float(SL_Percenti[i])
			TP_PNL = float(TP_PNLi[i])
			SL_PNL = float(SL_PNLi[i])
			amtwall = (wall[res][t])
			EMAfast, EMAmid, EMAslow, df = indicator(symbol, TF, FASTEMA, MIDEMA, SLOWEMA, FASTTYPE, MIDTYPE, SLOWTYPE)
			#EMAfasts = round(EMAfast.iloc[-2],5)
			#EMAmids = round(EMAmid.iloc[-2],5)
			#EMAslows = round(EMAslow.iloc[-2],5)
			#print(f'{symbol}')
			if mode_trade == 'ON':
				trade(symbol, df, EMAfast, EMAmid, EMAslow, order, TF, FASTEMA, MIDEMA, SLOWEMA, FASTTYPE, MIDTYPE, SLOWTYPE, TP_Mode, SL_Mode, TP_Percent, SL_Percent, PNL_Mode, TP_PNL, SL_PNL)
			if str(local_time[14:-9]) == '0' and not LineNotice:
				sticker_time = [16581272, 16581275, 16581279, 16581289, 16581285]
				stickertime = random.choice(sticker_time)
				mes=f'\n⏰⏰แจ้งเตือนทุก 1 ชั่วโมงค่ะนายท่าน\n\n{version}\n\n⭐Status : ระบบทำงานปกติค่ะ\n\n💰ยอดเงินคงเหลือ : {amtwall} บาท\n\nAccount : {Account_Name}'
				notify.send(mes, sticker_id=stickertime, package_id=8522)
				LineNotice = True
				# ! ============= Print Welcome To CMD ==============
				print(Fore.MAGENTA, Style.BRIGHT + 'Hi ! Master')
				print(Style.RESET_ALL)
				print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + 'Welcome To Auto Trade System On BITKUB SPOT')
				print(Style.RESET_ALL)
				print(Fore.LIGHTGREEN_EX, Style.BRIGHT, Back.BLUE + 'Mod By X4815162342')
				print(Style.RESET_ALL)
				print(Fore.LIGHTWHITE_EX, Style.BRIGHT + 'Tips')
				print(Style.RESET_ALL)
				print(Fore.LIGHTWHITE_EX, Style.BRIGHT + '5 MA TYPE CROSS')
				print(Style.RESET_ALL)
				print(Fore.LIGHTWHITE_EX, Style.BRIGHT + '1. EMA   2. SMA  3. HWA  4. RMA  5. WMA')
				print(Style.RESET_ALL)
				print(Fore.RED, Style.BRIGHT + 'Before Use Me, Dont Forget Backtest The Strategy MA Type Cross For Best Of Profit and Low Drawdown % ^^')
				print(Style.RESET_ALL)
				print(Fore.CYAN, Style.BRIGHT + 'Master !! You Can Try Backtest Your Stategy Here >> https://www.tradingview.com/v/DAD06s8m/')
				print(Style.RESET_ALL)
				xmr_donte = f'Donate For My Coffee\nXMR Address : 89Emmdegk7deMqR3iFDcwZGw8GtRwGPWAVzZbp6zdRm94eJ4j5bGWwnYozRAvw7y2EDoNbNWvZuGjL3h9v9v9TZWVZ5We1E'
				print(Fore.LIGHTWHITE_EX, Style.BRIGHT + f'Donate For My Coffee\nXMR Address : 89Emmdegk7deMqR3iFDcwZGw8GtRwGPWAVzZbp6zdRm94eJ4j5bGWwnYozRAvw7y2EDoNbNWvZuGjL3h9v9v9TZWVZ5We1E' + Style.RESET_ALL)
				promptpay_donate = 'Buy Me a Coffee : PromptPay : 095-518-8528'
				print(Fore.LIGHTYELLOW_EX, Style.BRIGHT + promptpay_donate + Style.RESET_ALL)
				print(Fore.LIGHTGREEN_EX, Style.BRIGHT + 'Thanks For Support' + Style.RESET_ALL)
				print('---------------------------------------------------------------------------------')
				print('██   ██ ██   ██  █████   ██ ███████  ██  ██████  ██████  ██████  ██   ██ ██████ ')
				print(' ██ ██  ██   ██ ██   ██ ███ ██      ███ ██            ██      ██ ██   ██      ██')
				print('  ███   ███████  █████   ██ ███████  ██ ███████   █████   █████  ███████  █████ ')
				print(' ██ ██       ██ ██   ██  ██      ██  ██ ██    ██ ██           ██      ██ ██     ')
				print('██   ██      ██  █████   ██ ███████  ██  ██████  ███████ ██████       ██ ███████')
				print('---------------------------------------------------------------------------------')
				print(Fore.GREEN, Style.BRIGHT + '')
				print('██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗ ')
				print('██╔══██╗██║╚══██╔══╝██║ ██╔╝██║   ██║██╔══██╗')
				print('██████╔╝██║   ██║   █████╔╝ ██║   ██║██████╔╝')
				print('██╔══██╗██║   ██║   ██╔═██╗ ██║   ██║██╔══██╗')
				print('██████╔╝██║   ██║   ██║  ██╗╚██████╔╝██████╔╝')
				print('╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ')
				print(Style.RESET_ALL + '')
				print('---------------------------------------------------------------------------------')
				print(Fore.BLUE, Style.BRIGHT + 'If You Found Some Bug Please Contact My Developer Master >> Here Line ID : x4815x')
				print(Style.RESET_ALL)
				print(Fore.LIGHTGREEN_EX + 'Master !! Please Wait For New TimeLoop By TimeFrame Setting <3 ^^')
				print(Style.RESET_ALL)
				print(Fore.GREEN, Style.BRIGHT + f'Account Name : ' + Style.RESET_ALL , Fore.LIGHTCYAN_EX + f'{Account_Name}' + Style.RESET_ALL)
				print(Fore.GREEN, Style.BRIGHT + f'Time Loop Check : ' + Style.RESET_ALL , Fore.LIGHTCYAN_EX + f'{looptimeframe}' + Style.RESET_ALL)
				print(Style.RESET_ALL)
			if str(local_time[14:-9]) == '3':
				LineNotice = False
		except Exception as Error:
			print(Fore.WHITE, Back.RED + f'MAIN ERROR SYMBOL FOR WALLET CHECK : {symbol} Please Check Config Setting {Error}' + Style.RESET_ALL)
			notify.send(f'\n🚨🚨ตรวจพบ SYMBOL ERROR ค่าาานายท่านนนน\n\nAsset : {symbol}\n🆘MAIN LOOP ERROR🆘\n{Error}\n\n📢โปรดตรวจสอบคู่เหรียญอีกครั้ง บางเหรียญไม่สามารถใช้ BOT TRADE ได้ค่ะ')
			continue
	return

def text_logo():
	print(Style.RESET_ALL)
	print(Fore.LIGHTGREEN_EX, Style.BRIGHT, Back.BLUE + 'Mod By X4815162342')
	print(Style.RESET_ALL)
	print(Fore.LIGHTWHITE_EX, Style.BRIGHT + 'Tips')
	print(Style.RESET_ALL)
	print(Fore.LIGHTWHITE_EX, Style.BRIGHT + '5 MA TYPE CROSS')
	print(Style.RESET_ALL)
	print(Fore.LIGHTWHITE_EX, Style.BRIGHT + '1. EMA   2. SMA  3. HWA  4. RMA  5. WMA')
	print(Style.RESET_ALL)
	print(Fore.RED, Style.BRIGHT + 'Before Use Me, Dont Forget Backtest The Strategy MA Type Cross For Best Of Profit and Low Drawdown % ^^')
	print(Style.RESET_ALL)
	print(Fore.CYAN, Style.BRIGHT + 'Master !! You Can Try Backtest Your Stategy Here >> https://www.tradingview.com/v/DAD06s8m/')
	print(Style.RESET_ALL)
	xmr_donte = f'Donate For My Coffee\nXMR Address : 89Emmdegk7deMqR3iFDcwZGw8GtRwGPWAVzZbp6zdRm94eJ4j5bGWwnYozRAvw7y2EDoNbNWvZuGjL3h9v9v9TZWVZ5We1E'
	print(Fore.LIGHTWHITE_EX, Style.BRIGHT + f'Donate For My Coffee\nXMR Address : 89Emmdegk7deMqR3iFDcwZGw8GtRwGPWAVzZbp6zdRm94eJ4j5bGWwnYozRAvw7y2EDoNbNWvZuGjL3h9v9v9TZWVZ5We1E' + Style.RESET_ALL)
	promptpay_donate = 'Buy Me a Coffee : PromptPay : 095-518-8528'
	print(Fore.LIGHTYELLOW_EX, Style.BRIGHT + promptpay_donate + Style.RESET_ALL)
	print(Fore.LIGHTGREEN_EX, Style.BRIGHT + 'Thanks For Support' + Style.RESET_ALL)
	print('---------------------------------------------------------------------------------')
	print('██   ██ ██   ██  █████   ██ ███████  ██  ██████  ██████  ██████  ██   ██ ██████ ')
	print(' ██ ██  ██   ██ ██   ██ ███ ██      ███ ██            ██      ██ ██   ██      ██')
	print('  ███   ███████  █████   ██ ███████  ██ ███████   █████   █████  ███████  █████ ')
	print(' ██ ██       ██ ██   ██  ██      ██  ██ ██    ██ ██           ██      ██ ██     ')
	print('██   ██      ██  █████   ██ ███████  ██  ██████  ███████ ██████       ██ ███████')
	print('---------------------------------------------------------------------------------')
	print(Fore.GREEN, Style.BRIGHT + '')
	print('██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗ ')
	print('██╔══██╗██║╚══██╔══╝██║ ██╔╝██║   ██║██╔══██╗')
	print('██████╔╝██║   ██║   █████╔╝ ██║   ██║██████╔╝')
	print('██╔══██╗██║   ██║   ██╔═██╗ ██║   ██║██╔══██╗')
	print('██████╔╝██║   ██║   ██║  ██╗╚██████╔╝██████╔╝')
	print('╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ')
	print(Style.RESET_ALL + '')
	print('---------------------------------------------------------------------------------')
	print(Fore.BLUE, Style.BRIGHT + 'If You Found Some Bug Please Contact My Developer Master >> Here Line ID : x4815x')
	print(Style.RESET_ALL)
	print(Fore.LIGHTGREEN_EX + 'Master !! Please Wait For New TimeLoop By TimeFrame Setting <3 ^^')
	print(Style.RESET_ALL)
	print(Fore.GREEN, Style.BRIGHT + f'Account Name : ' + Style.RESET_ALL , Fore.LIGHTCYAN_EX + f'{Account_Name}' + Style.RESET_ALL)
	print(Fore.GREEN, Style.BRIGHT + f'Time Loop Check : ' + Style.RESET_ALL , Fore.LIGHTCYAN_EX + f'{looptimeframe}' + Style.RESET_ALL)
	print(Style.RESET_ALL)
	return

main()
text_logo()

if __name__ == "__main__":
	while True:
		#print(f'{version}\n===============')
		seconds = time.time()
		local_time = time.ctime(seconds)
		time.sleep(1)
		# ! ============ Every 15 Minute Notify Balance =================
		if (str(local_time[14:-5]) == '00:00' or str(local_time[14:-5]) == '15:00' or str(local_time[14:-5]) == '30:00' or str(local_time[14:-5]) == '45:00') :
			# ! ======== Every 15 Minute =========
			if looptimeframe == '15m':
				main()
				text_logo()
				time.sleep(1)
				if double_check == 'ON':
					print(Fore.YELLOW, Back.MAGENTA, Style.BRIGHT + f'=============== Next >> Double Check. Please Wait=============\n' + Style.RESET_ALL)
					main()
					text_logo()
		if (str(local_time[14:-5]) == '00:00' or str(local_time[14:-5]) == '30:00') :
			# ! ============ Every 30 Minute Notify Balance =================
			if looptimeframe == '30m':
				main()
				text_logo()
				time.sleep(1)
				if double_check == 'ON':
					print(Fore.YELLOW, Back.MAGENTA, Style.BRIGHT + f'=============== Next >> Double Check. Please Wait=============\n' + Style.RESET_ALL)
					main()
					text_logo()
			if (str(local_time[14:-5]) == '00:00') :
				# ! ============ Every 60 Minute Notify Balance =================
				if looptimeframe == '1h':
					main()
					text_logo()
					time.sleep(1)
					if double_check == 'ON':
						print(Fore.YELLOW, Back.MAGENTA, Style.BRIGHT + f'=============== Next >> Double Check. Please Wait=============\n' + Style.RESET_ALL)
						main()
						text_logo()
		# ! ============ Every 4 Hour Notify Balance =================
		if (str(local_time[11:-5]) == '00:00:00' or str(local_time[11:-5]) == '04:00:00' or str(local_time[11:-5]) == '08:00:00' or str(local_time[11:-5]) == '12:00:00' or str(local_time[11:-5]) == '16:00:00' or str(local_time[11:-5]) == '20:00:00') :
			# posix is os name for linux or mac
			if(os.name == 'posix'):
				os.system('clear')
				text_logo()
			# else screen will be cleared for windows
			else:
				os.system('cls')
				text_logo()
			if looptimeframe == '4h':
				main()
				text_logo()
				time.sleep(1)
				if double_check == 'ON':
					print(Fore.YELLOW, Back.MAGENTA, Style.BRIGHT + f'=============== Next >> Double Check. Please Wait=============\n' + Style.RESET_ALL)
					main()
					text_logo()
		# ! ============ Every 1 Day Notify Balance =================
		if (str(local_time[11:-5]) == '00:00:00') :
			if looptimeframe == '1d':
				main()
				text_logo()
				time.sleep(1)
				if double_check == 'ON':
					print(Fore.YELLOW, Back.MAGENTA, Style.BRIGHT + f'=============== Next >> Double Check. Please Wait=============\n' + Style.RESET_ALL)
					main()
					text_logo()
		# ! ============ Every 1 Minute Loop =================
		if (str(local_time[15:-5]) == '0:00' or str(local_time[15:-5]) == '1:00' or str(local_time[15:-5]) == '2:00' or str(local_time[15:-5]) == '3:00' or str(local_time[15:-5]) == '4:00' or str(local_time[15:-5]) == '5:00' or str(local_time[15:-5]) == '6:00' or str(local_time[15:-5]) == '7:00' or str(local_time[15:-5]) == '8:00' or str(local_time[15:-5]) == '9:00') :
			if looptimeframe == '1m':
				main()
				text_logo()
				time.sleep(1)
				if double_check == 'ON':
					print(Fore.YELLOW, Back.MAGENTA, Style.BRIGHT + f'=============== Next >> Double Check. Please Wait=============\n' + Style.RESET_ALL)
					main()
					text_logo()
		time.sleep(1)
