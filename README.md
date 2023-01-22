# x48-bitkub-bot
วิธีใช้งานเบื้องต้น

[CONFIG]
API_KEY = ใส่ API KEY ของคุณ
API_SECRET = ใส่ API SECRET ของคุณ
LINE_TOKEN = ใส่ LINE TOKEN เพื่อรับการแจ้งเตือน
ACCOUNT_NAME = ใส่ชื่อบัญชีอะไรก็ได้ เช่น BK-TEST-WALLET

[SETTING]
SYMBOL = BTC,ETH,ADA,XLM,XRP,DOGE
COST = 20,20,20,20,20,20
TF = สามารถเลือก TF ได้ 6 รูปแบบ ได้แก่ : 1m,15m,30m,1h,4h,1d (ใส่ , คั่นแยก TF ได้)
FAST_TYPE = EMA,EMA,SMA,EMA,HMA,WMA (MA TYPE 5 รูปแบบ ได้แก่ EMA, SMA, WMA, HMA, RMA)
FAST_MA = 2,2,78,2,2,2
MID_TYPE = EMA,EMA,RMA,RMA,HMA,WMA (MA TYPE 5 รูปแบบ ได้แก่ EMA, SMA, WMA, HMA, RMA)
MID_MA = 4,4,80,4,4,4
SLOW_TYPE = EMA,EMA,RMA,RMA,HMA,WMA (MA TYPE 5 รูปแบบ ได้แก่ EMA, SMA, WMA, HMA, RMA)
SLOW_MA = 4,4,80,4,4,4

[TPSL]
TP_MODE = ON [ON/OFF หาก OFF จะไม่คำนวณ TP Price รอเส้นตัดอย่างเดียว]
SL_MODE = ON [ON/OFF หาก OFF จะไม่คำนวณ SL Price รอเส้นตัดอย่างเดียว]
TP_PERCENT = 138.2,138.2,138.2,138.2,138.2,138.2 [ใส่เป็น % TP]
SL_PERCENT = 25,25,25,25,25,25 [ใส่เป็น % SL]

[PNL]
PNL_MODE = ON [ON/OFF หาก OFF จะไม่คำนวณ PNL รอเส้นตัดอย่างเดียว]
TP_PNL = 20,20,20,20,20,20 [ใส่เป็นกำไร เช่น กำไร 20 บาท จะขายเหรียญนั้นทิ้ง]
SL_PNL = 10,10,10,10,10,10 [ใส่เป็นขาดทุน เช่น ขาดทุน 10 บาท จะขายเหรียญนั้นทิ้ง]


[OPTION]
MODE_TRADE = ON/OFF [หาก OFF จะส่งเฉพาะแจ้งเตือนไลน์ สัญญาณเข้าซื้อ/ขาย | หาก ON จะทำการ Trade + ส่งแจ้งเตือน]
BAR_LOOK = 100 [จำนวนแท่งในการมองย้อนของ BOT ใช้ 50-150 กำลังดี ไม่ควรเกินนี้]
TIME_LOOP_CHECK = 1m [BOT จะทำงานตามช่วงเวลา นาฬิกาโลก ได้แก้ 1m, 15m, 30m, 1h, 4h, 1d เลือกได้ 1 ช่วงเวลา 15 นาทีกำลังดี]
DOUBLE_CHECK = ON [BOT จะทำการ LOOP เพิ่มอีก 1 รอบ เพื่อตรวจสอบสัญญาณอีกครั้ง]
