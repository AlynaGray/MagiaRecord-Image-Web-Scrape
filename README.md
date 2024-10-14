# Magia Record Image_Web Scrape

This is a semi-manual scrape of Magia Record's `magica/resource/image_web` directory for archival. The pattens for scraping are manually constructed by looking at the JS files and patterns in already archived assets in [puella-historia](https://gitlab.com/puella-care/puella-historia) and [bella_donna](https://github.com/LiviaMedeiros/bella_donna).

Although EoS has already occurred, the asset servers are still online. I guess the servers will stay up while the archive app is sitll available to download, which is until October 14, 2024.

Only `scrape_memora.py` and `scrape_tower_buttons.py` were run before EoS. The servers remained up after, but I'm noting this just in case the assets changed after EoS.

Note: Some of the excerpts have their single and double quotes modified to match. Not sure why they don't match in the original.

## scrape_memora.py

Based on [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/view/memoria/MemoriaComposeTopUseMaterialView.js#L72), [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/event/EventWitch/parts/ExchangeMemoria.js#L47), and [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/view/gacha/GachaBtnView.js#L90)

```js
"/magica/resource/image_web/memoria/memoria_" + b.pieceId + "_s.png"
```

## scrape_tower_buttons.py

Based on [these lines](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/event/tower/EventTowerTop.js#L160)

```js
"/magica/resource/image_web/event/tower/' + z + "/tab_" + d + '_on.png"
"/magica/resource/image_web/event/tower/' + z + "/tab_" + a + '_off.png"
```

## scrape_tower_chara.py

:warning:**Does not work**

Based on [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/event/tower/EventTowerTop.js#L266)

```js
"/magica/resource/image_web/event/tower/" + g.eventId + "/chara/chara_" + a.charaId + ".png"
```

I can't figure out the format for `a.charaId` because I haven't found any examples of this asset in the archives.

## scrape_memoria_thumb.py

Based on [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/event/dailytower/EventDailyTowerTop.js#L675C1-L675C298)

```js
"/magica/resource/image_web/event/dailytower/common/" + ("memoria_thumb_s" + a.pieceRank + "_" + ("SKILL" == a.pieceType ? 1 : 2)).toLowerCase() + ".png'";
```

## scrape_reward_list.py

Based on [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/event/accomplish/EventAccomplishTop.js#L99)

```js
"/magica/resource/image_web/event/accomplish/" + c.eventId + "/reward_list.png"
```

## scrape_alina_memoria_thumb.py

Based on [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/event/EventWitch/parts/ExchangeMemoria.js#L45)

```
"/magica/resource/image_web/event/eventWitch/common/alina_request/memoria_thumb_s4_" + b + ".png"
```

## scrape_event_quest_tab.py

Based on [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/quest/QuestUtil.js#L277)

```js
"/magica/resource/image_web/event/" + x[d.eventType] + "/" + d.eventId + "/tab_limited_quest_s.png"
```

Note: Some of the training events don't have a tab image on the server at the time of scraping.

## scrape_puella_historia_damage_num.py

Based on [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/quest/puellaHistoria/lastBattle/QuestResultMainBoss.js#L99C1-L99C298)

```js
"/magica/resource/image_web/page/quest/puellaHistoria_lastBattle/result/_number/b_num_" + Number(g) + ".png"
```

## scrape_doppel_mission_banner.py

Based on [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/view/mission/MissionTopView.js#L218)

```js
"/magica/resource/image_web/page/mission/doppelMission/" + f + "01/banner.png"
```

## scrape_stamp_mission_banner.py

Based on [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/view/mission/MissionTopView.js#L250)

```js
"/magica/resource/image_web/page/mission/panelMission/" + a.panelMissionList[d].id + "/banner.png"
```

## scrape_quest_chapter_bg.py

Based on [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/view/quest/QuestChapterListPartsView.js#L33C1-L33C221)

```js
"/magica/resource/image_web/page/quest/main/titleBg/bg_chapter_" + ("HARD" == b.mainQuestMode ? "challenge_" + this.model.chapterId : this.model.chapterId) + ".png"
```

## scrape_treasure.py

Based on [these lines](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/view/quest/QuestResultView.js#L423), [these lines](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/patrol/PatrolResult.js#L118), and [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/template/event/accomplish/EventAccomplishTop.html#L263)

```js
"/magica/resource/image_web/common/treasure/" + b + "_close.png"
"/magica/resource/image_web/common/treasure/" + b + "_open.png"
```
```html
/magica/resource/image_web/common/treasure/<%="<%= model.chestColor.toLowerCase() %\>"%>.png
```

## scrape_number.py
Based on [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/view/user/GlobalMenuView.js#L125C1-L125C88) and [these lines](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/css/gacha/GachaResult.css#L1057C1-L1057C92)

```js
"/magica/resource/image_web/common/number/" + d[e] + ".png"
```
```css
"/magica/resource/image_web/common/number/num_0.png"
```

## scrape_puella_historia_pop.py

Based on [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/view/user/GlobalMenuView.js#L933)

```js
"/magica/resource/image_web/page/quest/puellaHistoria_lastBattle/event/" + this.model.toJSON().eventId + "/event_pop.png"
```

## scrape_event_pop.py

Based on [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/view/user/GlobalMenuView.js#L942)

```js
"/magica/resource/image_web/event/" + x[this.model.get("eventType")] + "/" + this.model.toJSON().eventId + "/event_pop.png"
```

## scrape_specific_event_pop.py

Based on [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/view/user/GlobalMenuView.js#L936), [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/view/user/GlobalMenuView.js#L944), [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/template/top/__TopPage.html#L6C91-L6C97), [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/css/quest/PuellaHistoriaTop.css#L94), [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/css/_common/common.css#L9224), and [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/css/_common/common.css#L9321)

## scrape_drop_up_campaign_icon.py

Based on [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/_common/backboneCommon.js#L441)

```js
"/magica/resource/image_web/campaign/drop_up/" + d.campaignId + "/global_icon.png"
```

## scrape_kimochi_stone.py

Pattern identified through inspection of existing archives.

## scrape_story_collection_title.py

Based on [this file](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/template/collection/StoryCollection.html)

```html
"/magica/resource/image_web/page/quest/puellaHistoria_lastBattle/event/1198/story_collection_title.png"
"/magica/resource/image_web/event/<%='<%= model.questType.toLowerCase() %\>'%>/<%='<%= model.eventId %\>'%>/story_collection_title.png"
"/magica/resource/image_web/<%='<%= eventKind %\>'%>/<%='<%= eventDir %\>'%>/<%='<%= eventId %\>'%>/story_collection_title.png"
"/magica/resource/image_web/event/<%='<%= model.eventType.toLowerCase() %\>'%>/<%='<%= model.eventId %\>'%>/story_collection_title.png"
"/magica/resource/image_web/event/eventWitch/<%='<%= model.eventId %\>'%>/story_collection_title.png"
"/magica/resource/image_web/campaign/story/<%='<%= model.campaignId %\>'%>/story_collection_title.png"
```

## scrape_event_navi_01.py

Based on existing archive patterns and game knowledge. Only scrapes `navi_01.png`. Plan to use these locations to scrape the rest.

## scrape_rest_of_event_navi.py

Based on search for `navi_0` and `navi_1` in `bella_donna` and existing archives. Must be run after `scrape_event_navi_01.py`. It checks for more `navi_01.png` in existing directories, and then tries to download the rest of the `navi` files in the directories that already have `navi_01.png`.

## scrape_all_specific_paths.py

Search through text files in `bella_donna`, `puella-historia`, and `MITaMa` for full paths and download them. Interestingly, there were some full paths that weren't in the server e.g. `/magica/resource/image_web/regularEvent/senmetsu/common/bg_map_enemy.png` and `magica/resource/image_web/item/main/cure_ap_10.png`. I guess they're unimplemented features or things that were changed or removed during development.

## scrape_announce_common.py

Based on inspection of `MITaMa`. I didn't find any reference to it in the code.

## scrape_banner_announce.py

Based on inspection of `MITaMa` and `puella-historia`. I only found full path references to these files, and not generic templates, in the code.

## scrape_announce_2.py

Based on inspection of `MITaMa`. Searches for patterns like `magica/resource/image_web/announce/announce_230117.png`.

## scrape_announce_campaign_bare.py

Scrape files like `magica/resource/image_web/announce/announce_campaign_10381.png` without suffixes.

## scrape_announce_campaign_with_1.py

Scrape files like `magica/resource/image_web/announce/announce_campaign_10381_1.png` with the `_1` suffix.

## scrape_announce_event_bare.py

Scrape files like `magica/resource/image_web/announce/announce_event_11473.png` without suffixes.

## scrape_announce_event_with_a.py

Scrape files like `magica/resource/image_web/announce/announce_event_11454_a.png` with the `_a` suffix.

## scrape_announce_event_with_1.py

Scrape files like `magica/resource/image_web/announce/announce_event_10631_1.png` with the `_1` suffix.

## scrape_announce_memoria.py

Scrape files like `magica/resource/image_web/announce/announce_memoria_1016.png`

## Remaining lines
Lines referencing image_web files that don't have a scraper built from them yet. The scraper may not work yet, and this list might not be comprehensive

### Unknown formats
Can't find examples of these assets in existing archives.

```
event/dailytower/EventDailyTowerTop.js:              e = b.doc.createElement("img"), e.className = "charaImg", e.src = "/magica/resource/image_web/event/dailytower/" + d.eventId + "/chara/chara_" + a.charaId + ".png", f.el.querySelector(".firstView").appendChild(e), f.el.querySelector(".questTitle").textContent = a.charaTitle
regularEvent/groupBattle/RegularEventGroupBattleSelectUnion.js:        content: "<div id='unionImg'><img src='/magica/resource/image_web/regularEvent/groupBattle/union_logo_0" + c.charaUnionList[this.unionIndex].unionId + ".png'/></div>",
```

### Deferred

Put off due to difficulty.

Related to generating event related identifiers:
```
event/accomplish/EventAccomplishDeck.js:            f.style.cssText = "background:url('/magica/resource/image_web/common/icon/event/icon_" + l + "_f.png') left top no-repeat; background-size:26px 26px;";
formation/DeckFormation.js:            l.style.cssText = "background:url('/magica/resource/image_web/common/icon/event/icon_" + g + "_f.png') left top no-repeat; background-size:26px 26px;";
quest/EventQuest.js:              c.specialQuestObj.useItemImagePath = "/magica/resource/image_web/item/" + (-1 < f.indexOf("EVENT_") ? "event/" : "main/") + f.toLowerCase() + ".png";
campaign/quiz/CampaignQuizTop.js:          a.doc.getElementById("firstClearImg").innerHTML = '<img src="/magica/resource/image_web/item/' + e + "/" + l + '.png">';
campaign/quiz/CampaignQuizTop.js:          a.doc.getElementById("completeClearImg").innerHTML = '<img src="/magica/resource/image_web/item/' + c + "/" + g + '.png">';
view/quest/QuestResultView.js:            b.src = "/magica/resource/image_web/common/treasure/event/" + a + "_close.png";
view/quest/QuestResultView.js:              b.src = "/magica/resource/image_web/common/treasure/event/" + a + "_open.png";
patrol/PatrolResult.js:            c.src = "/magica/resource/image_web/common/treasure/event/" + a + "_close.png";
patrol/PatrolResult.js:              c.src = "/magica/resource/image_web/common/treasure/event/" + a + "_open.png";
patrol/PatrolLumpResult.js:            b.src = "/magica/resource/image_web/common/treasure/event/" + a + "_close.png";
patrol/PatrolLumpResult.js:              b.src = "/magica/resource/image_web/common/treasure/event/" + a + "_open.png";
```

Very generic:
```
view/item/ItemImgPartsView.js:      this.model.imagePath && (this.model.imagePath = this.model.nativeimgkey ? "resource/image_native/" + this.model.imagePath + ".png" : "/magica/resource/image_web/" + this.model.imagePath + ".png");
```

No clear pattern in identifier:
```
view/shop/ShopTopPartsView.js:          content: "<img class='detailImg' src='/magica/resource/image_web/page/shop/detail/" + this.model.genericId.toLowerCase() + ".png'>",
_common/backboneCommon.js:    return "/magica/resource/image_web/common/icon/" + (c ? b + ".png" : b + "_f.png")
```

### To be investigated
```
```
