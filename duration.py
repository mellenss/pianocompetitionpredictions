import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

urls=['https://musescore.com/user/31759/scores/6699541',
 'https://musescore.com/user/40171282/scores/21637255',
 'https://musescore.com/user/49355771/scores/8188694',
 'https://musescore.com/user/47402189/scores/9018602',
 'https://musescore.com/user/19710/scores/5209742',
 'https://musescore.com/user/29926531/scores/5674977',
 'https://musescore.com/user/1839111/scores/2002831',
 'https://musescore.com/user/34104354/scores/6747206',
 'https://musescore.com/user/27069094/scores/21641986',
 'https://musescore.com/user/7839731/scores/4865717',
 'https://musescore.com/user/20331431/scores/5824861',
 'https://musescore.com/user/19710/scores/149954',
 'https://musescore.com/user/19710/scores/106022',
 'https://musescore.com/user/1945976/scores/5894874',
 'https://musescore.com/user/30704984/scores/6265187',
 'https://musescore.com/user/39593079/scores/18640222',
 'https://musescore.com/user/6053266/scores/6115529',
 'https://musescore.com/user/2749876/scores/5215854',
 'https://musescore.com/user/2749876/scores/5971806',
 'https://musescore.com/user/34104354/scores/6747206',
 'https://musescore.com/user/36713561/scores/7049328',
 'https://musescore.com/user/2749876/scores/11975431',
 'https://musescore.com/user/24069/scores/768926',
 'https://musescore.com/user/33685231/scores/10241464',
 'https://musescore.com/user/24069/scores/1116201',
 'https://musescore.com/user/46963286/scores/10048660',
 'https://musescore.com/user/4385496/scores/6995114',
 'https://musescore.com/user/39593079/scores/18640222',
 'https://musescore.com/user/24069/scores/1116201',
 'https://musescore.com/user/38573602/scores/6810592',
 'https://musescore.com/user/19710/scores/254071',
 'https://musescore.com/user/19710/scores/4801031',
 'https://musescore.com/user/94336705/scores/23509777',
 'https://musescore.com/user/11239551/scores/6377941',
 'https://musescore.com/user/28722347/scores/11545093',
 'https://musescore.com/user/19854161/scores/6232707',
 'https://musescore.com/user/19710/scores/254071',
 'https://musescore.com/user/2749876/scores/2603291',
 'https://musescore.com/user/39593079/scores/18640222',
 'https://musescore.com/user/3990006/scores/1616291',
 'https://musescore.com/user/2749876/scores/2603291',
 'https://musescore.com/user/31789257/scores/15950638',
 'https://musescore.com/user/47420939/scores/8099223',
 'https://musescore.com/user/3177366/scores/2182146',
 'https://musescore.com/user/19710/scores/77075',
 'https://musescore.com/user/27095571/scores/4898485',
 'https://musescore.com/user/33306646/scores/6541491',
 'https://musescore.com/user/19710/scores/77075',
 'https://musescore.com/user/32472836/scores/5616665',
 'https://musescore.com/user/39593079/scores/17897299',
 'https://musescore.com/user/19710/scores/658031',
 'https://musescore.com/user/31712176/scores/6173852',
 'https://musescore.com/user/31390628/scores/6543316',
 'https://musescore.com/user/19710/scores/254071',
 'https://musescore.com/user/47420939/scores/8099223',
 'https://musescore.com/user/28614883/scores/6299687',
 'https://musescore.com/user/33144689/scores/8753655',
 'https://musescore.com/user/28722347/scores/11545093',
 'https://musescore.com/user/6053266/scores/6160321',
 'https://musescore.com/user/27683639/scores/8768529',
 'https://musescore.com/user/6128801/scores/5830787',
 'https://musescore.com/user/29386707/scores/5631285',
 'https://musescore.com/user/31390628/scores/6543316',
 'https://musescore.com/user/2749876/scores/5971806',
 'https://musescore.com/user/19854161/scores/6232707',
 'https://musescore.com/user/33144689/scores/8591183',
 'https://musescore.com/user/39593079/scores/18293536',
 'https://musescore.com/user/33306646/scores/6541491',
 'https://musescore.com/user/24069/scores/768926',
 'https://musescore.com/user/27371958/scores/12228457',
 'https://musescore.com/user/2585196/scores/890041',
 'https://musescore.com/user/30432972/scores/5444607',
 'https://musescore.com/user/202809/scores/8608955',
 'https://musescore.com/user/38235231/scores/5003370',
 'https://musescore.com/user/33685231/scores/12966424',
 'https://musescore.com/user/2749876/scores/5215854',
 'https://musescore.com/user/615091/scores/5486916',
 'https://musescore.com/user/19710/scores/760356',
 'https://musescore.com/user/30275987/scores/7400966',
 'https://musescore.com/user/202809/scores/15041581',
 'https://musescore.com/user/24069/scores/1116201',
 'https://musescore.com/user/19710/scores/5209742',
 'https://musescore.com/user/37403731/scores/8697717',
 'https://musescore.com/user/202809/scores/9428485',
 'https://musescore.com/user/30992975/scores/9400321',
 'https://musescore.com/user/10136086/scores/12403834',
 'https://musescore.com/user/39593079/scores/18640222',
 'https://musescore.com/user/47469701/scores/9515089',
 'https://musescore.com/user/9836/scores/48072',
 'https://musescore.com/user/39593079/scores/16633900',
 'https://musescore.com/user/56286572/scores/16768039',
 'https://musescore.com/user/19710/scores/77075',
 'https://musescore.com/user/6725176/scores/2698796',
 'https://musescore.com/user/44543999/scores/12984574',
 'https://musescore.com/user/33306646/scores/6541491',
 'https://musescore.com/user/33306646/scores/6110403',
 'https://musescore.com/user/33306646/scores/6338294',
 'https://musescore.com/user/34745720/scores/6189405',
 'https://musescore.com/user/1945976/scores/5894874',
 'https://musescore.com/user/34104354/scores/6716159',
 'https://musescore.com/user/1945976/scores/5894874',
 'https://musescore.com/user/33306646/scores/6036358',
 'https://musescore.com/user/26830520/scores/13069894',
 'https://musescore.com/user/6053266/scores/6160321',
 'https://musescore.com/user/1945976/scores/5894874',
 'https://musescore.com/user/2749876/scores/5971806',
 'https://musescore.com/user/38573602/scores/6810592',
 'https://musescore.com/user/31759/scores/5835997',
 'https://musescore.com/user/3990006/scores/1616291',
 'https://musescore.com/user/1945976/scores/5894874',
 'https://musescore.com/user/3990006/scores/1616291',
 'https://musescore.com/user/34745720/scores/6189405',
 'https://musescore.com/user/19710/scores/760356',
 'https://musescore.com/user/34296022/scores/6307244',
 'https://musescore.com/user/46963286/scores/10048660',
 'https://musescore.com/user/8066/scores/1321656',
 'https://musescore.com/user/2749876/scores/11975431',
 'https://musescore.com/user/33306646/scores/6224476',
 'https://musescore.com/user/19710/scores/117330',
 'https://musescore.com/user/24069/scores/1116201',
 'https://musescore.com/user/26830520/scores/5460395',
 'https://musescore.com/user/2749876/scores/3433406',
 'https://musescore.com/user/19710/scores/77075',
 'https://musescore.com/user/19710/scores/105738',
 'https://musescore.com/user/19710/scores/254071',
 'https://musescore.com/user/19710/scores/321601',
 'https://musescore.com/user/108151/scores/1131666',
 'https://musescore.com/user/20208436/scores/6478611',
 'https://musescore.com/user/19710/scores/106022',
 'https://musescore.com/user/38617044/scores/6817048',
 'https://musescore.com/user/40076328/scores/9061349',
 'https://musescore.com/user/33306646/scores/5820504',
 'https://musescore.com/user/33306646/scores/5815407',
 'https://musescore.com/user/33306646/scores/6198821',
 'https://musescore.com/user/19710/scores/1040681',
 'https://musescore.com/user/5963031/scores/4978424',
 'https://musescore.com/user/19710/scores/210606',
 'https://musescore.com/user/101036/scores/7488107',
 'https://musescore.com/user/38617044/scores/6817048',
 'https://musescore.com/user/19710/scores/760356',
 'https://musescore.com/user/19854161/scores/6730566',
 'https://musescore.com/user/1397281/scores/3244316',
 'https://musescore.com/user/34104354/scores/6325410',
 'https://musescore.com/user/2749876/scores/4408941',
 'https://musescore.com/user/47420939/scores/8099223',
 'https://musescore.com/user/35931919/scores/6478760',
 'https://musescore.com/user/12384271/scores/5160847',
 'https://musescore.com/user/19710/scores/1559631',
 'https://musescore.com/user/19710/scores/77075',
 'https://musescore.com/user/4454/scores/30943',
 'https://musescore.com/user/19710/scores/1040681',
 'https://musescore.com/user/1839111/scores/2068076',
 'https://musescore.com/user/19710/scores/105738',
 'https://musescore.com/user/37114622/scores/7079825',
 'https://musescore.com/user/1945976/scores/5894874',
 'https://musescore.com/user/28722347/scores/11545093',
 'https://musescore.com/user/5963031/scores/4978424']

durations = []


options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = uc.Chrome(options=options)

def get_duration(url):
    try:
        print(f"Processing URL: {url}") 
        driver.get(url)
        duration_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="scoreInfo"]/div[2]/table/tbody/tr[6]/td/div'))
        )
        duration = duration_element.text  
        durations.append(duration)
        time.sleep(1)
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        durations.append(None)

for url in urls:
    get_duration(url)

driver.quit()
print(durations)


