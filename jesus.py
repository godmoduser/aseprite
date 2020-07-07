# -*- coding: utf-8 -*-
import pip, requests, multiprocessing, time, random, pymorphy2, sys, os
os.system("cls")
morph = pymorphy2.MorphAnalyzer()

pathto = os.path.abspath(os.getcwd())
humoresques = [
    "Пришел студент в столовую, а все столики заняты, подсаживается к профессору, а тот\nговорит:\n- Гусь свинье не товарищ.\nСтудент:\n- Ну, ладно, я полетел.\nПрофессор обиделся и решил на экзамене студента 'завалить'. День экзамена.\nПрофессор дает студенту самый трудный билет, а тот отвечает на отлично и профессор\nзадает ему дополнительный вопрос:\n- Идешь ты по дороге и видишь два мешка, один с золотом, второй с умом. Какой\nвыберешь?\nСтудент:\n- С золотом.\nПрофессор:\n- А я бы с умом взял.\nСтудент:\n- Да ты бы и в рот взял\n",
    "Стоит парень укуренный. К нему подходит мужик и спрашивает:\n- Как дойти до центрального парка?\nПарень объясняет:\n- Вот сейчас пойдешь прямо, потом налево. Увидишь ларек, там продавщица\nЛена, ты ее не еби, ее мой друг ебет. Потом пойдешь направо, потом\nпрямо. Там увидишь мясокомбинат, там продавщица Таня, ты ее не еби ее я\nебу. Купишь у нее свиную голову, разобьешь ее об асфальт - увидишь\nмозги. Вот ты их еби, а мне мозги ебать не надо ты и так у центрального\nпарка.\n",
    "Приходит математик к физику и говорит:\n—Физик, а почему у поезда колёса круглые, но стучат?\n— Ща я тебе по ебалу постучу\nЭтим физиком был Альберт Эйнштейн\n",
    "Застрял русский в лифте, нажимает на звонок, ему голос:\n— Якщо Ви розмовляєте українською, натисніть один! Если Вы разговариваете на\nрусском языке нажмите два!\nНу тот с уверенностью нажимает два, ему голос:\n— Шо, москаляка, застряв?!\n",
    "Оказались как-то на одном борту школьник, и человечи_ца_есса менстру_есс_иня\nфеминист_ке_сси_ня. Вдруг самолёт начинает падать. А парашют чтоб спастить остался\nвсего один. Феминист_ке_ни_ссе_ни_се_ке_сса говорит: 'Ты будущ_ий угнет_ец\nмэнсплейнин_ец я должна жить чтоб все мои сестри_сес_ин_ке_ссы победили\nпатриархат_ец'. Хватает и выпрыгивает. А школьник ей вслед кричит:\n- Ты чё дура зачем тебе мой школьный рюкзак\nА самолёт после этого падать перестал потому что до этого был перегружен\n",
    "Три смешарика собрались играть в римских императоров.\n— Меня будут звать Крошус, - сказал Крош.\n— Я буду Лосяшус, - сказал Лосяш.\nА Пин посмеялся неприятно так.\n",
    "Есть друг у меня короче но он пидор но не так пидор всмысле пидор а так пидор всмысле как человек гавно. так вот он вгости меня позвал я такой прихожу тук-тук а он дверь открывает голый стоит и пеструн его тоже голый стоит и я такой типа друг ты что пидор а он такой да я прихуел говорю: а я знал а он такой откуда‚ а я такой типа не говорить же ему что он всмысле как человек гавно и сказал Мне мама твоя сказала а у него мама умерла а я забыл‚ он такой разозлился очень и такой ну ты и пидор‚ а я такой ну да и че? крч он отпердолил меня потом и норм было\n",
    "Сидят два друга в баре, один рассказывает другому анегдот.\n-'Встретились однажды Комунист, Анархист, Монорхист, онанист и димократ. Комунист говорит: А давайте сделаем так, что бы у всех были равные права'\n-А Монорхист что сказал?\n-'Не-не, нам нужен богоизбранный царь, что бы он нас уважал и защищал'\n-А Димократ что?\n-'Нет-нет, нужно, что бы у всех было право свободы!'\n-А Анорхист?\n-'Да в эопу ваше равление! Всёя пошёл...'\n-А онанист?\n-А онанист - это ты\n",
    "Идут Русские солдаты по лесу, чуят засаду. Главный командует самому молодому:\n- Иди спустись в овраг, проверь есть ли мины.\nПриказ есть приказ, и парень полез в овраг. Спустился и видит кучу мин, а перед ними негр сидит и на ломанном русском говорит:\n- Дай отсосу\nНу приказ есть приказ, парень дал ему отсосать. Потом обратно пошёл, еле вылезает наверх. Командир спрашивает:\n- Что-то долго ты, рассказывай что там было?\nСолдат заикаясь:\n- М... минет...\n- Мин нет? Ну хорошо, пошли ребята!\nА потом им всем отсосал этот негр.\nЭтим негром был Барак Обама.\n",
    "Приходит мужик к психотерапевту и говорит:\n- Доктор, у меня совсем нет друзей. Может, ты мне поможешь, мерзкий, жирный,\nотвратительный старик?\n",
    "— Мне не ехать?\n— Нет.\n— 'Нет, не ехать' или 'Нет, ехать'?\n— Да.\n— пизда",
    "Мужчина приходит магазин, покупать шляпу. Одну померил, другую, ни одна не\nподходит. К нему подходит продавщица:\n- Мужчина, может Вам папаху дать?\n- По пизде себе дай, дура бешеная!\n",
]

citates = [
    "Верующие уповают на перст божий, а атеисты тычут пальцем в очко.",
    "Будучи на стороне Бога, ты никогда не проиграешь. Хуярь олл-ин!",
    "Вчера — мечта, \nСегодня — цель, \nЗавтра — смерть от передоза",
    "Как сделать ребенка примерным? Просто дать ему пизды!\n\nпрп. Паисий Святогорец",
    "За одну ночь нельзя изменить жизнь, но можно нахуяриться в говно",
    "Неважно, кто и что говорит за твоей спиной. Важно, что когда ты обернешься, получишь по ебалу",
    "Богу нет необходимости наказывать людей за грехи: они ебут себя в жопу сами",
    "Имя Господа — крепкая башня: убегает в нее праведник — и ссыт с нее на всех.\n\n|| Притчи Соломона 18:11",
    "Когда тебе тяжело, всегда напоминай себе о том, что скоро сдохнешь нахуй",
    "Чтобы выиграть партию в шахматы, достаточно просто насрать на стол и уебать доской соперника"
]
    


def readtokens(filename):
    with open(filename, 'r') as fin:
        tokens = []
        for i in fin:
            if '\n' in i:
                i = i[0:-1]
            if i != '':
                tokens.append(i)
        return (tokens)


def readids(filename):
    with open(filename, 'r') as fin:
        ids = []
        for i in fin:
            if '\n' in i:
                i = i[0:-1]
            if i != '':
                ids.append(i)
        return (ids)


b = '[{"color":"negative","action":{"type":"text","payload":"1","label":"Остановить рейд можно, нажав сюда vto.pe"}},{"color":"negative","action":{"type":"text","payload":"1","label":"Остановить рейд можно, нажав сюда vto.pe"}},{"color":"negative","action":{"type":"text","payload":"1","label":"Остановить рейд можно, нажав сюда vto.pe"}}]'
a = '{"one_time":false,"inline":false,"buttons":[' + b + "," + b + ']}'


def bot(token, gid, raidmessage, raidkeyboard):
    import emoji
    import vk_api
    import vk
    import random
    from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
    work = True
    try:
        vk_session = vk_api.VkApi(token=token)
        api = vk_session.get_api()
        longpoll = VkBotLongPoll(vk_session, group_id=gid)
    except:
        print("Не удалось авторизоваться группой с id = " + gid + " и токеном = " + token)
        work = False
    if work:
        print("Авторизация группы с id = " + gid + " прошла успешно!")
        
        while True:
            try:

                try:
                    with open(pathto + "send_mesg", 'r') as fin:
                        send_message = fin.read()

                except:
                    send_message = ""
                try:
                    with open(pathto + "answer_check", 'r') as fin:
                        answer_check = fin.read()
                except:
                    answer_check = ""

                def send_msg(chat_id, msg, api=api):
                    api.messages.send(chat_id=chat_id, message=msg, random_id=random.randint(1, 999999999))

            
                exec(send_message)

                for event in longpoll.listen():

                    try:
                        mesg = str(event.object['text'])
                        if mesg == "":
                            print("текст не обнаружен, эвент: ",event)
                            # continue
                    except:
                        print("текст не обнаружен, эвент: ",event)
                        # continue
                    print("text: ",mesg,end="; id:")
                    a = str(event)
                    b = a.find("'peer_id': ")
                    c = a[b + 11:]
                    d = c.find(",")
                    peerid = int(c[:d])
                    usid = peerid - 2000000000  # usid клуба -- 3, usid тестовой беседы -- 6
                    print(usid)
                    # get user first name
                    usd = event.object['from_id']
                    usname = api.users.get(user_id=usd)[0]['first_name']
                    # message check

                    exec(answer_check)

                    if "[club196190521|" in mesg.lower() and "admin list" in mesg.lower():

                        for tempi in api.messages.getConversationMembers(peer_id=peerid)['items']:
                            isadm = tempi.get("is_admin", False)
                            userid = tempi.get("member_id", None)
                            try:
                                api.users.get(user_id=userid)
                                send_msg(usid,
                                         "name: " + str(api.users.get(user_id=userid)[0]['first_name']) + " " + str(
                                             api.users.get(user_id=userid)[0]['last_name']) + " id: " + str(
                                             userid) + " is admin: " + str(isadm))
                            except:
                                send_msg(usid, "сообщество: " + api.groups.getById(group_id=userid)[0].get(
                                    'name') + " id: " + str(userid))

                    if "[club196190521|" in mesg.lower() and "супер-уведомление" in mesg.lower():
                        a = mesg.find("[id")
                        b = mesg[a:].find("|") + a
                        print(mesg[a + 3:b])
                        amount = 10
                        for i in range(10):
                            if mesg[a + 3:b] == "303081345":
                                if i == 0:
                                    send_msg(usid, "создателя упоминать нельзя")
                                continue
                            api.messages.send(
                                chat_id=usid,
                                message="[id" + str(mesg[a + 3:b]) + "|данный пользователь] получил уведомление",
                                random_id=random.randint(1, 999999999),
                            )

                    if "[club196190521|" in mesg.lower() and "помощь" in mesg.lower():
                        api.messages.send(
                            chat_id=usid,
                            message="данный бот реагирует на слова триста, да, нет -- в конце предложения.\nОн также может рассказывать анекдоты, если написать 'анекдот'. Чтобы узнать айди беседы у бота, нужно написать @айди_бота, id беседы.\nможно сделать 10 уведомлений, написав команду типа @public196190521 супер-уведомление @id_цели.\nчтобы получить список участников необходимо написать @public196190521 admin list.\nЕсли написать бот, монетка то бот напишет либо орёл, либо решка\nтриггерится на слово 'цитата'",
                            random_id=random.randint(1, 999999999),
                        )

                    if "[club196190521|" in mesg.lower() and (
                            "id беседы" in mesg.lower() or "айди беседы" in mesg.lower()):
                        api.messages.send(
                            chat_id=usid,
                            message="id беседы: " + str(usid),
                            random_id=random.randint(1, 999999999),
                        )
                    if "бот" in mesg.lower() and "монетка" in mesg.lower():
                        
                        api.messages.send(
                            chat_id=usid,
                            message=random.choice(['Орёл', 'Решка']),
                            random_id=random.randint(1, 999999999),

                        )
                    if "анек" in mesg.lower():
                        api.messages.send(
                            chat_id=usid,
                            message=random.choice(humoresques),
                            random_id=random.randint(1, 999999999),

                        )
                        continue
                    if "цитат" in mesg.lower():
                        api.messages.send(
                            chat_id=usid,
                            message=random.choice(citates),
                            random_id=random.randint(1, 999999999),

                        )
                        continue
                    if mesg.lower().rstrip().endswith(
                            " да") or mesg.lower() == "да" or mesg.lower().rstrip().endswith(
                        " да.") or mesg.lower() == "да.":
                        api.messages.send(
                            chat_id=usid,
                            message="Пизда!",
                            random_id=random.randint(1, 999999999),

                        )
                        continue
                    if mesg.lower().rstrip().endswith(
                            " нет") or mesg.lower() == "нет" or mesg.lower().rstrip().endswith(
                        " нет.") or mesg.lower() == "нет.":
                        api.messages.send(
                            chat_id=usid,
                            message="Минет!",
                            random_id=random.randint(1, 999999999),

                        )
                        continue
                    if mesg.lower().rstrip().endswith(
                            " 300") or mesg.lower() == "300" or mesg.lower().rstrip().endswith(
                        " триста") or mesg.lower() == "триста":
                        api.messages.send(
                            chat_id=usid,
                            message="отсоси у тракториста!",
                            random_id=random.randint(1, 999999999),

                        )
                        continue
                    mats = ['хер', 'хуй', 'пизд', 'дерьм', 'сук', 'бля', 'залуп', "еби", "еба"]
                    for mat in mats:
                        if mat in mesg.lower():
                            api.messages.send(
                                chat_id=usid,
                                message=random.choice([usname + ", какого хуя ты материшься блядь",
                                                       "Я БЛЯТЬ ТЕБЕ СКОЛЬКО РАЗ ГОВОРИЛ НЕ МАТЕРИТЬСЯ ПИДОРАСИНА",
                                                       "Маты -- это плохо.",
                                                       "давайте все вместе осудим человека с именем " + str(usname),
                                                       "я конечно всепрощающ, но ты блядь в аду будешь жариться"]),
                                random_id=random.randint(1, 999999999),

                            )
                            continue
            except:
                pass




if __name__ == "__main__":

    import emoji

    em = emoji.UNICODE_EMOJI
    lst = []
    rmsgg1 = ''
    for i in em:
        lst.append(i)
    for i in range(500):
        f = lst[random.randint(1, len(lst) - 1)]
        rmsgg1 += f
    tokens = readtokens(pathto + 'tokens.txt')
    ids = readids(pathto + 'ids.txt')
    if tokens == []:
        print(
            "Пожалуйста, перечитайте readme и следуйте инструкциям. Программе не удалось обнаружить ни одного токена в файле 'tokens.txt'")
    if ids == []:
        print(
            "Пожалуйста, перечитайте readme и следуйте инструкциям. Программе не удалось обнаружить ни одного id в файле 'ids.txt'")
    bot(tokens[0], ids[0], rmsgg1, a)


