import vk_api, random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
vk = vk_api.VkApi(token'')
vk._auth_token()
snd = vk.get_api()
longpoll = VkBotLongPoll(vk,188426283)
stages = ["1 stage", "2 stage"]
s = -1
items = []
def say(msg, id):
	snd.messages.send(peer_id = id, message = msg,random_id =random.randint(0, 2147483647))
while True:
	for event in longpoll.listen():
		if event.type == VkBotEventType.MESSAGE_NEW:
			if s == -1:
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
							say("Для следующей страницы введите '\!r\'. Осталось: "+ str(len(items)),event.object.peer_id)
							continue
						say("Режим просмотра уже запущен. Для дальнейших действий напишите \'!r\'. Осталось: " + str(len(items)),event.object.peer_id)
						
						
			elif s >= 0:
				if  event.object.text.lower() == "!r":
					if event.object.from_id in items:
						items.pop(items.index(event.object.from_id))
						if len(items) == 0:
							s = s + 1
							if s > len(stages)-1:
								say("Режим просмотра отключен. Спасибо за прочтение. ", event.object.peer_id)
								s = -1
								continue
							else:
								say(stages[s],event.object.peer_id)
								items = []
								for id in snd.messages.getConversationMembers(peer_id=event.object.peer_id)["items"]:
									if id["member_id"] > 0:
										items.append(id["member_id"])
								say("Для следующей страницы введите '\!r\'. Осталось: "+ str(len(items)),event.object.peer_id)
								continue
						say("Для следующей страницы введите '\!r\'. Осталось: "+ str(len(items)),event.object.peer_id)

				
