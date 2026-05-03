import requests
from bs4 import BeautifulSoup

def get_df_status():
    #olc_case_no = 'H005-2504-2381594'
    case_no = 'H005-2505-2460398'
    passport_no = "C1120213"

    url = "https://www.dataflowstatus.com/applicationstatus/validate_report"
    data = {'barcode': case_no, "passportno": passport_no}

    x = requests.post(url, data = data)

    soup = BeautifulSoup(x.content, 'html.parser')

    box = soup.find("div",{"class":"status-main-content"})

    message = "Case No. : " + case_no + "\nPassport No. : " + passport_no + "\n\n" + box.text.replace("\n\n","").replace("                                                    ","")

    return message[:4096]