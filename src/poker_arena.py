from time import time
from os import urandom
from hashlib import md5
from requests import Session

class PokerArena:
	def __init__(
			self,
			version: str = "2.4.82",
			language: str = "ru",
			game_id: int = 82) -> None:
		self.api = "https://adrminigames.mail.ru"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "Mozilla/5.0 (Android; U; ru-RU) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/33.0",
			"X-Flash-Version": "33,0,2,338"
		}
		self.token = None
		self.user_id = None
		self.version = version
		self.game_id = game_id
		self.language = language
		self.udid = self.generate_udid()
		self.extinit_poker()
	
	def _get(self, endpoint: str, params: dict = {}) -> dict:
		return self.session.get(
			f"{self.api}{endpoint}", params=params).json()

	def _post(self, endpoint: str, data: dict = None) -> dict:
		return self.session.post(
			f"{self.api}{endpoint}", data=data).json()

	def generate_udid(self) -> str:
		return md5((urandom(20))).hexdigest()
		
	def extinit_poker(self, token: str = None) -> dict:
		data = {
			"udid": self.udid,
			"ident": "poker",
			"lang": self.language,
			"version": self.version
		}
		data["_token_"] = token if token else None
		response = self._post("/extinit/poker", data=data)
		if "id" in response["user"]:
			self.user_id = response["user"]["id"]
			self.token = response["user"]["web_token"]
		return response
			
	def login(
			self,
			email: str,
			password: str) -> dict:
		data = {
			"login": email,
			"udid": self.udid,
			"lang": self.language,
			"socnet": 1,
			"password": password,
			"ident": "Poker",
			"version": self.version
		}
		response = self._post("/rest/auth", data=data)
		if "token" in response:
			self.token = response["token"]
			self.user_id = self.extinit_poker(self.token)["user"]["id"]
		return response

	def login_with_token(self, token: str) -> dict:
		self.token = token
		response = self.extinit_poker(self.token)
		if "game" in response:
			self.user_id = response["user"]["id"]
		return response

	def register(
			self,
			email: str,
			password: str,
			nickname: str) -> dict:
		data = {
			"ident": "Poker",
			"socnet": 1,
			"name": nickname,
			"_token_": self.token,
			"version": self.version,
			"password_confirm": password,
			"login": email,
			"lang": self.language,
			"password": password,
			"udid": self.udid,
			"pic": "https://minigames.imgsmail.ru/static/i/profile/avatars/mouse.jpg",
			"bonus": 1
		}
		return self._post("/rest/register", data=data)
	
	def get_room_list(self) -> dict:
		params = {
			"version": self.version
		}
		return self._get(
			"/game/Poker/roomlist", params)

	def udid_bind(self) -> dict:
		data = {
			"_token_": self.token,
			"uid": self.user_id,
			"udid": self.udid
		}
		return self._post(
			"/n/udid/bind", data=data)

	def get_state(self) -> dict:
		data = {
			"action": "state",
			"_token_": self.token,
			"game_id": self.game_id,
			"object": "hilo_mobile"
		}
		return self._post(
			"/index.php", data=data)

	def play_hilo_mobile(
			self,
			card: str,
			choice: str,
			pay_with_hilocs: int = None,
			user_hilo: str = None) -> dict:
		"""
		CHOICE:
			LO - LOW
			HI - HIGH
		"""
		data = {
			"action": "play",
			"game_id": self.game_id,
			"object": "hilo_mobile",
			"_token_": self.token,
			"card": card,
			"stacked_response": 1,
			"choice": choice
		}
		if user_hilo:
			data["user_hilo"] = user_hilo
		if pay_with_hilocs:
			data["pay_with_hilocs"] = pay_with_hilocs
			data["pay"] = 1
		return self._post(
			"/index.php", data=data)

	def get_user_info(self, user_id: int) -> dict:
		data = {
			"gifts": 100,
			"_token_": self.token,
			"nc": int(time() * 1000),
			"game": "Poker",
			"version": self.version
		}
		return self._post(
			f"/user/{user_id}/info", data=data)

	def get_user_achievements(self, user_id: int) -> dict:
		data = {
			"_token_": self.token,
			"nc": int(time() * 1000),
			"user": user_id,
			"game": "Poker",
			"version": self.version 
		}
		return self._post(
			"/achievement/get/user_achievement", data=data)

	def get_gifts_list(self) -> dict:
		params = {
			"_token_": self.token,
			"version": self.version
		}
		return self._get("/gift/list", params)

	def edit_profile(
			self,
			nickname: str = None,
			picture: str = None) -> dict:
		data = {
			"_token_": self.token,
			"version": self.version
		}
		if nickname:
			data["name"] = nickname
		if picture:
			data["pic"] = picture
		return self._post(
			"/profile/edit", data=data)

	def get_top_players(
			self,
			count: int = 100,
			type: str = "all") -> dict:
		data = {
			"_token_": self.token,
			"new": 1,
			"type": type,
			"count": count,
			"version": self.version
		}
		return self._post(
			"/game/Poker/top", data=data)

	def get_tournament_players(self, type: int = 1) -> dict:
		data = {
			"action": "state",
			"_token_": self.token,
			"game_id": self.game_id,
			"object": "tournament",
			"get_top": type
		}
		return self._post(
			"/index.php", data=data)
