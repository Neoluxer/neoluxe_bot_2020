import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = '1204797421:AAGTUUbHkRjJDoQx3Flf737aMC_z-06PWjk'

admins = [
    os.getenv("ADMIN_ID"),
]

ip = os.getenv("ip")

SCHETCHIK_PATH='C:\\Users\\neoluxe\\PycharmProjects\\InvoiceAiogram\\Invoice_bot\\BIN\\sch.bin'

PICTURE_PATH = 'C:\\Users\\neoluxe\\PycharmProjects\\InvoiceAiogram\\Invoice_bot\\PICTURES\\' # Тут лежат росписи, печать, логотип

EXEL_PATH = 'C:\\Users\\neoluxe\\PycharmProjects\\InvoiceAiogram\\Invoice_bot\\XLS\\' # Тут лежать заготовки документов

STAMP = 'C:\\Users\\neoluxe\\PycharmProjects\\InvoiceAiogram\\Invoice_bot\\PICTURES\\stamp_neoluxe.png'

AUTOGRAPH ='C:\\Users\\neoluxe\\PycharmProjects\\InvoiceAiogram\\Invoice_bot\\PICTURES\\autograph.png'

AUTOGRAPH2 ='C:\\Users\\neoluxe\\PycharmProjects\\InvoiceAiogram\\Invoice_bot\\PICTURES\\autograph2.png'

LOGO = 'C:\\Users\\neoluxe\\PycharmProjects\\InvoiceAiogram\\Invoice_bot\\PICTURES\\logo.png'

YesDict =['Yes','yes','Y','y','1','Д','д','Да','да','True','true']