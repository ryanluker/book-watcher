### Book Watcher
- Holds playwright scripts for keeping track of the following book lists

#### Kobo
- ~Playwright script automates watching for book deals as kobo does not provide this feature~
- ~Book deal notifying is restricted to just books within the wishlist~

#### ORL
- Library book holds where I am notified when I get to the #1 position
- This allows me to choose to "pause" the hold if I already have a book on the go

### Config
Set the following config values (create a local `config.ini`)
```ini
[orl]
username=***
password=***
```

### Running
`uv run watcher.py`

```
The Long Way to A Small, Angry Planet
In transit
#1 on 3 copies

Artificial Condition
Not ready
#2 on 6 copies

The Moon Is A Harsh Mistress
Not ready
#2 on 1 copies

Incorruptible : Why Good Companies Go Bad And How Great Companies Stay Great
Not ready
#5 on 2 copies

The Well of Ascension
Not ready
#6 on 4 copies

A Psalm for the Wild-built
Not ready
#9 on 7 copies

The Tainted Cup
Paused
```
