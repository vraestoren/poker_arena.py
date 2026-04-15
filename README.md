# <img src="https://play-lh.googleusercontent.com/SJwgFdT5PABc2SQyiN5oB7bndxFTJ6oq5J5rfXoLqm6kkhB13jZXe6N66unpzgcTBo2B=w240-h480-rw" width="28" style="vertical-align:middle;" /> poker_arena.py

> Mobile-API for [Poker Arena](https://adrminipoker_arenas.mail.ru) a mobile poker game by Mail.ru.

## Quick Start

```python
from poker_arena import PokerArena

poker_arena = PokerArena()
poker_arena.login(email="you@example.com", password="secret")
```

## Usage

### Authentication

```python
# Login with email and password
poker_arena.login(email="you@example.com", password="secret")

# Login with existing token
poker_arena.login_with_token("your_token")

# Register a new account
poker_arena.register(email="you@example.com", password="secret", nickname="Hero")
```

### Player

```python
poker_arena.get_user_info(user_id=123)
poker_arena.get_user_achievements(user_id=123)
poker_arena.get_top_players(count=100, type="all")
```

### Profile

```python
poker_arena.edit_profile(nickname="NewName")
poker_arena.edit_profile(picture="https://example.com/avatar.jpg")
```

### Rooms & Tournaments

```python
poker_arena.get_room_list()
poker_arena.get_tournament_players(type=1)
```

### HiLo Mini-poker_arena

```python
# Get current poker_arena state
poker_arena.get_state()

# Play a round
poker_arena.play_hilo_mobile(card="7H", choice="HI")
poker_arena.play_hilo_mobile(card="3D", choice="LO")

# Pay with HiLo coins
poker_arena.play_hilo_mobile(card="7H", choice="HI", pay_with_hilocs=1)
```

> `choice` must be `"HI"` (higher) or `"LO"` (lower).

### Gifts

```python
poker_arena.get_gifts_list()
```

## API Reference

| Method | Description |
|---|---|
| `login(email, password)` | Login with email and password |
| `login_with_token(token)` | Login with an existing token |
| `register(email, password, nickname)` | Register a new account |
| `get_user_info(user_id)` | Get a player's profile |
| `get_user_achievements(user_id)` | Get a player's achievements |
| `edit_profile(nickname, picture)` | Edit your profile |
| `get_top_players(count, type)` | Get the leaderboard |
| `get_room_list()` | Get available poker rooms |
| `get_tournament_players(type)` | Get tournament standings |
| `get_state()` | Get current HiLo poker_arena state |
| `play_hilo_mobile(card, choice)` | Play a HiLo round |
| `get_gifts_list()` | Get available gifts |
