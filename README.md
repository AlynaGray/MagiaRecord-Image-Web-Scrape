# Magia Record Image_Web Scrape

This is a semi-manual scrape of Magia Record's `magica/resource/image_web` directory for archival. The pattens for scraping are manually constructed by looking at the JS files and patterns in already archived assets in [puella-historia](https://gitlab.com/puella-care/puella-historia) and [bella_donna](https://github.com/LiviaMedeiros/bella_donna).

Although EoS has already occurred, the asset servers are still online. I guess the servers will stay up while the archive app is sitll available to download, which is until October 14, 2024.

## scrape_memora.py

Based on [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/view/memoria/MemoriaComposeTopUseMaterialView.js#L72)

```js
c.src = "/magica/resource/image_web/memoria/memoria_" + b.pieceId + "_s.png";
```

Scraped before EoS

## scrape_tower_buttons.py

Based on [these lines](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/event/tower/EventTowerTop.js#L160)

```js
h = 'url("/magica/resource/image_web/event/tower/' + z + "/tab_" + d + '_on.png") left top no-repeat',
z = 'url("/magica/resource/image_web/event/tower/' + z + "/tab_" + a + '_off.png") left top no-repeat';
```

Scraped before EoS

## scrape_tower_chara.py

**Does not work**

Based on [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/event/tower/EventTowerTop.js#L266)

```js
f = b.doc.createElement("img"), f.className = "charaImg", f.src = "/magica/resource/image_web/event/tower/" + g.eventId + "/chara/chara_" + a.charaId + ".png", e.el.querySelector(".firstView").appendChild(f), e.el.querySelector(".questTitle").textContent = a.charaTitle
```

I can't figure out the format for `a.charaId` because I haven't found any examples of this asset in the archives.
