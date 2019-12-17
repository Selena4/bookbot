import vk_api, codecs, random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import os
vk = vk_api.VkApi(token='')
vk._auth_token()
snd = vk.get_api()
longpoll = VkBotLongPoll(vk,188426283)
stages =  []
txt = 'book.txt'
doc = os.listdir('pages/')
for i in range(1,len(doc)+1):
        file = codecs.open("pages/page" + str(i) + ".txt", "r", "utf_8_sig" )
        stages.append(file.read())
        file.close()
print('[info] bot started.')
s = 0
items = []
def say(msg, id):
        if len(msg) > 4000:
                snd.messages.send(peer_id = id, message = msg[:4000],random_id =random.randint(0, 2147483647))
                snd.messages.send(peer_id = id, message = msg[4000:],random_id =random.randint(0, 2147483647))
        else:
                snd.messages.send(peer_id = id, message = msg,random_id =random.randint(0, 2147483647))
while True:
	for event in longpoll.listen():
		if event.type == VkBotEventType.MESSAGE_NEW:
			if event.object.text.lower() == "!p":
				msg = ""
				for i in items:
					msg = msg + "@id" + str(i) +", "
				say(msg,event.object.peer_id)
			if s == 0:
				admins = []
				for id in snd.messages.getConversationMembers(peer_id=event.object.peer_id)["items"]:
					if "is_admin" in id.keys() and id["member_id"] > 0:
						admins.append(id["member_id"])
				if event.object.text.lower() == "!s" and event.object.from_id in admins:
					items = []
					for id in snd.messages.getConversationMembers(peer_id=event.object.peer_id)["items"]:
						if id["member_id"] > 0:
							items.append(id["member_id"])
					say("Режим просмотра был запущен. Для дальнейших действий напишите \'!r\'. Осталось: " + str(len(items)),event.object.peer_id)
				if  event.object.text.lower() == "!r":
					if len(items) == 0:
						say("Режим промотра не был запущен",event.object.peer_id)
					elif event.object.from_id in items:
						items.pop(items.index(event.object.from_id))
						if len(items) == 0:
							s = s + 1
							say(stages[s],event.object.peer_id)
							items = []
							for id in snd.messages.getConversationMembers(peer_id=event.object.peer_id)["items"]:
								if id["member_id"] > 0:
									items.append(id["member_id"])
							say("Для следующей страницы введите \'!r\'. Осталось: "+ str(len(items)),event.object.peer_id)
							continue
						say("Режим просмотра уже запущен. Для дальнейших действий напишите \'!r\'. Осталось: " + str(len(items)),event.object.peer_id)
						
						
			elif s >= 1:
				if  event.object.text.lower() == "!r":
					if event.object.from_id in items:
						items.pop(items.index(event.object.from_id))
						if len(items) == 0:
							s = s + 1
							if s > len(stages)-1:
								say("Режим просмотра отключен. Спасибо за прочтение. ", event.object.peer_id)
								s = 0
								continue
							else:
								say(stages[s],event.object.peer_id)
								items = []
								for id in snd.messages.getConversationMembers(peer_id=event.object.peer_id)["items"]:
									if id["member_id"] > 0:
										items.append(id["member_id"])
								say("Для следующей страницы введите \'!r\'. Осталось: "+ str(len(items)),event.object.peer_id)
								continue
						say("Для следующей страницы введите \'!r\'. Осталось: "+ str(len(items)),event.object.peer_id)

				

