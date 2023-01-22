# **X48-BITKUB-BOT**

## **How To - วิธีใช้งานเบื้องต้น**

-   **ก่อนใช้งาน BOT ต้องเปิดประวัติธุรกรรมของเหรียญที่ต้องการให้ BOT ซื้อขายก่อน**
    -   เช่น
        -   หากยังไม่เคยซื้อขายเหรียญ DOGE / BOT จะไม่สามารถซื้อขายได้ เนื่องจากไม่มีประวัติให้ดึงข้อมูล
        -   ให้ทำการเปิดธุรกรรมก่อน เช่น ซื้อมา/ขายไป 20 บาท
        -   ทำการ ซื้อ/ขาย ขั้นต่ำให้ครบทุกเหรียญที่ต้องการ BOT

### CONFIG ด้านล่างนี้ เป็นเพียงตัวอย่างและคำอธิบายเพียงเท่านั้น \\ ก่อนใช้งานโปรดศึกษาแต่ละเหรียญควรใช้เส้นประเภทไหน และใช้ค่าเท่าไร
    -- Tips --
    มือใหม่ EMA 12/26/26 [FAST/MID/SLOW] // CDC Action Zone
    TF : 4h / 1d
    COST : ขั้นต่ำอย่างน้อย 20 บาท
    -----------------------------------------------------
    ** BOT สามารถใช้เส้นตัดได้ 3 เส้น [FAST/MID/SLOW]
    หากอยากใช้แค่ 2 เส้นตัด [FAST/SLOW] ให้ใช้ค่า MID = SLOW
        เช่น
            FAST_MA = 12
            MID_MA = 26
            SLOW_MA = 26

### **[CONFIG]**
* **API_KEY** = *<ใส่ API KEY ของคุณ>*
* **API_SECRET** = *<ใส่ API SECRET ของคุณ>*
* **LINE_TOKEN** = *<ใส่ LINE TOKEN เพื่อรับการแจ้งเตือน>*
* **ACCOUNT_NAME** = *<ใส่ชื่อบัญชีอะไรก็ได้ เช่น BK-TEST-WALLET>*

### **[SETTING]** ข้อที่มี * ต้องใส่ให้ครบคู่ด้วย เช่น SYMBOL*, COST*
* **SYMBOL*** = BTC,ETH,ADA,XLM,XRP,DOGE
  * <ใส่ชื่อเหรียญที่ต้องการให้ BOT รับข้อมูลจาก BITKUB>
* **COST*** = 20,20,20,20,20,20
    - *<ใส่เป็นจำนวนเงินที่ต้องการให้ BOT เข้าซื้อ>*
* **TF*** = 1m, 15m, 30m, 1h, 4h, 1d
  *  *<สามารถเลือก TF ได้ 6 รูปแบบ>* ได้แก่ : 1m, 15m, 30m, 1h, 4h, 1d
* **FAST_TYPE*** = EMA,EMA,SMA,EMA,HMA,WMA
    - *<MA TYPE 5 รูปแบบ>* ได้แก่ : EMA, SMA, WMA, HMA, RMA
* **FAST_MA*** = 2,2,78,2,2,2
  * *<ค่าของเส้น MA FAST TYPE>*
* **MID_TYPE*** = EMA,EMA,RMA,RMA,HMA,WMA
  - *<MA TYPE 5 รูปแบบ>* ได้แก่ : EMA, SMA, WMA, HMA, RMA
* **MID_MA*** = 4,4,80,4,4,4
  * *<ค่าของเส้น MA MIDDLE TYPE>*
* **SLOW_TYPE*** = EMA,EMA,RMA,RMA,HMA,WMA
  - *<MA TYPE 5 รูปแบบ>* ได้แก่ : EMA, SMA, WMA, HMA, RMA
* **SLOW_MA*** = 4,4,80,4,4,4
  * *<ค่าของเส้น MA SLOW TYPE>*

### [TPSL] - คือโหมด TakeProfit & StopLoss แบบ %
* **TP_MODE** = ON
  * *[ON/OFF หาก OFF จะไม่คำนวณ TP Price รอเส้นตัดอย่างเดียว]*
* **SL_MODE** = ON
  * *[ON/OFF หาก OFF จะไม่คำนวณ SL Price รอเส้นตัดอย่างเดียว]*
* **TP_PERCENT*** = 138.2,138.2,138.2,138.2,138.2,138.2
  * *<ใส่เป็น % ที่ต้องการ TP / BOT จะคำนวณแปลง % เป็นราคาให้อัตโนมัติ>*
* **SL_PERCENT*** = 25,25,25,25,25,25 
  * *<ใส่เป็น % ที่ต้องการ SL / BOT จะคำนวณแปลง % เป็นราคาให้อัตโนมัติ>*

### [PNL] - คือโหมด TakeProfit & StopLoss แบบคำนวณจาก PNL (กำไร/ขาดทุน)
    สามารถใช้ร่วมกับ TPSL โหมดปกติได้
*   **PNL_MODE** = ON
    *   *[ON/OFF หาก OFF จะไม่คำนวณ PNL รอเส้นตัดอย่างเดียว]*
*   **TP_PNL*** = 20,20,20,20,20,20
    *   *<ใส่เป็นกำไร เช่น กำไร 20 บาท จะขายเหรียญที่ได้กำไรนั้นทิ้ง>*
*   **SL_PNL*** = 10,10,10,10,10,10 
    *   *<ใส่เป็นยอดเงินขาดทุน เช่น ขาดทุน 10 บาท จะขายเหรียญนั้นทิ้ง>*

            -- Tips --
            การตั้ง TP/SL by PNL ควรจะสอดคล้องกับ COST ราคาเข้าซื้อ
                เช่น
                    COST = 1000 บาท
                    TP_PNL = 500 บาท <หมายถึง หากกำไร +500 บาท จะขายเหรียญที่กำไรนั้น>
                    SL_PNL = 250 บาท <หมายถึง หากขาดทุน -250 บาท จะขายเหรียญที่ขาดทุนทิ้ง เพื่อไม่ให้ติดดอย ยอม StopLoss>

            ** คิดง่ายๆ Mode นี้ สำหรับผู้ที่ไม่ต้องการคำนวณ % คือ Fix ที่ยอดเงินแทน

### [OPTION] - การตั้งค่าส่วนเสริมของ BOT
* **MODE_TRADE** = ON
  * *[ON/OFF หาก OFF จะส่งเฉพาะแจ้งเตือนไลน์ สัญญาณเข้าซื้อ/ขาย | หาก ON จะทำการ Trade + ส่งแจ้งเตือน]*
* **BAR_LOOK** = 100
  * <มือใหม่ใส่ค่ามาตรฐานที่ 100 ไม่ต้องแก้ไข>
  * <จำนวนแท่งในการมองย้อนของ BOT ใช้ 50-150 กำลังดี ไม่ควรเกินนี้>
* **TIME_LOOP_CHECK** = 1m 
  * <BOT จะทำงานตามช่วงเวลา นาฬิกาโลก ได้แก้ 1m, 15m, 30m, 1h, 4h, 1d เลือกได้ 1 ช่วงเวลา 15 นาทีกำลังดี>
* **DOUBLE_CHECK** = ON
  * *[ON/OFF หาก ON : BOT จะทำการ LOOP เพิ่มอีก 1 รอบ เพื่อตรวจสอบสัญญาณอีกครั้ง]*

        -- Tips --
        - TIME_LOOP_CHECK ควรตั้งให้สอดคล้องกับ TF เช่น ให้ BOT เทรด TF 15m ควรตั้ง TIME_LOOP_CHECK ที่ขั้นต่ำ ที่ 15m เพื่อการทำงานที่สอดคล้องกัน
        - DOUBLE_CHECK จะทำให้ BOT ทำการตรวจเช็คซ้ำ 2 รอบ เผื่อกรณีเกิดการ ERROR ขึ้น
            ** BOT จะไม่เข้าซื้อซ้ำ หากเข้าซื้อไปแล้ว ไม่ต้องกลัวเบิ้ลไม้
