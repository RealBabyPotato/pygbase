import pygame.mouse

from .events import EventManager


class InputManager:
	# Mouse
	mouse_down: list[bool, bool, bool] = [False, False, False]
	mouse_up: list[bool, bool, bool] = [False, False, False]
	mouse_pressed: tuple[bool, bool, bool] = (False, False, False)

	scroll: pygame.Vector2 = pygame.Vector2()

	# Keyboard
	keys_down = [False] * 512
	keys_pressed = [False] * 512
	keys_up = [False] * 512

	mods = 0

	@classmethod
	def reset(cls):
		cls.mouse_down[:] = [False, False, False]
		cls.mouse_up[:] = [False, False, False]
		cls.mouse_pressed = pygame.mouse.get_pressed(3)

		cls.scroll.update(0)

		cls.keys_down[:] = [False] * 512
		cls.keys_up[:] = [False] * 512
		cls.keys_pressed = pygame.key.get_pressed()

		cls.mods = pygame.key.get_mods()

	@classmethod
	def register_handlers(cls):
		EventManager.add_handler("all", pygame.KEYDOWN, cls._keydown_handler)
		EventManager.add_handler("all", pygame.KEYUP, cls._keyup_handler)
		EventManager.add_handler("all", pygame.MOUSEBUTTONDOWN, cls._mouse_down_handler)
		EventManager.add_handler("all", pygame.MOUSEBUTTONUP, cls._mouse_up_handler)
		EventManager.add_handler("all", pygame.MOUSEWHEEL, cls._mouse_wheel_handler)

	@classmethod
	def _keydown_handler(cls, event: pygame.event.Event):
		if event.key <= 512:
			cls.keys_down[event.key] = True

	@classmethod
	def _keyup_handler(cls, event: pygame.event.Event):
		if event.key <= 512:
			cls.keys_up[event.key] = True

	@classmethod
	def _mouse_down_handler(cls, event: pygame.event.Event):
		button = event.button - 1
		if button <= 2:
			cls.mouse_down[button] = True

	@classmethod
	def _mouse_up_handler(cls, event: pygame.event.Event):
		button = event.button - 1
		if button <= 2:
			cls.mouse_up[button] = True

	@classmethod
	def _mouse_wheel_handler(cls, event: pygame.event.Event):
		wheel_x = event.precise_x
		wheel_y = event.precise_y

		cls.scroll.x = wheel_x
		cls.scroll.y = wheel_y
