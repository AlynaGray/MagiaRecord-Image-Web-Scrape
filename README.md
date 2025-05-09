# Magia Record Image_Web Scrape

This is a semi-manual scrape of Magia Record's `magica/resource/image_web` directory for archival. The pattens for scraping are manually constructed by looking at the JS files and patterns in already archived assets in [puella-historia](https://gitlab.com/puella-care/puella-historia), [MITaMa](https://gitlab.com/puella-care/MITaMa), [bella_donna](https://github.com/LiviaMedeiros/bella_donna), and [uwasa](https://github.com/LiviaMedeiros/uwasa).

The assets scraped for this repo are stored in `magica/resource/image_web`. Other archives are included as submodules because some of the scripts use them.

After EoS, the asset servers remained online until November 29, 2024 JST (don't know exactly when it went down). Only `scrape_memora.py` and `scrape_tower_buttons.py` were run before EoS. It doesn't seem like the assets were changed or removed after EoS, although I didn't rigorously check.

**This archive is NOT comprehensive because the scraping was done manually and I didn't get around to every type of asset. For example, I didn't scrape any stickers. The other archives listed above may have assets that are not here.**

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

Search through text files in `bella_donna`, `puella-historia`, and `MITaMa` for full png paths and download them. Interestingly, there were some full paths that weren't in the server e.g. `/magica/resource/image_web/regularEvent/senmetsu/common/bg_map_enemy.png` and `magica/resource/image_web/item/main/cure_ap_10.png`. I guess they're unimplemented features or things that were changed or removed during development.

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

## scrape_announce_1.py

Scrape files like `magica/resource/image_web/announce/announce_266_1.png`

## scrape_event_currency.py

Based on [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/event/accomplish/EventAccomplishDeck.js#L590) and [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/formation/DeckFormation.js#L1731)

```js
"/magica/resource/image_web/common/icon/event/icon_" + l + "_f.png"
```

## scrape_event_currency_2.py

**Scrapes nothing.**

This didn't actually scrape anything and doesn't correspond to everything. I made this after misreading a filepath. I'm leaving this here for informational purposes to show that there's nothing with this pattern.

## scrape_event_currency_3.py

Handles event portion of [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/quest/EventQuest.js#L102)

**Does not handle stickers or chara assets**

```js
"/magica/resource/image_web/item/" + (-1 < f.indexOf("EVENT_") ? "event/" : "main/") + f.toLowerCase() + ".png"
```

## scrape_event_treasure.py

Based on [these lines](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/view/quest/QuestResultView.js#L439), [these lines](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/patrol/PatrolResult.js#L134), and [these lines](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/patrol/PatrolLumpResult.js#L148)

```js
"/magica/resource/image_web/common/treasure/event/" + a + "_close.png"
"/magica/resource/image_web/common/treasure/event/" + a + "_open.png"
```

## scrape_campaign_exchange.py

Handles campaign exchanges in main in [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/quest/EventQuest.js#L102)

```js
"/magica/resource/image_web/item/" + (-1 < f.indexOf("EVENT_") ? "event/" : "main/") + f.toLowerCase() + ".png"
```

## scrape announce

Because there are so many candidates for announcements like `magica/resource/image_web/announce/announce_2201072_a.png`, multiple scripts are made to allow for them to run in parallel.

Comprehensive scrapers:

### scrape_announce_3.py
### scrape_announce_4.py

Shorter scrapers used while the comphrehensive scrapers were running:

### scrape_announce_3_a1.py
### scrape_announce_3_a2.py
### scrape_announce_3_a3.py
### scrape_announce_3_a4.py
### scrape_announce_3_c1.py
### scrape_announce_3_c2.py
### scrape_announce_4_a1.py
### scrape_announce_4_a2.py
### scrape_announce_4_a3.py
### scrape_announce_4_a4.py
### scrape_announce_4_c1.py
### scrape_announce_4_c2.py

The comprehensive scrapers finshed after archive app download deadline of Oct 14 15:00 JST.

## scrape_weekly_banner.py

Based on inspecting [MagiRecoStatic](https://github.com/GrygrFlzr/MagiRecoStatic/tree/master/magica/resource/image_web/banner/common)

## scrape_chapter.py

Based on [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/template/quest/MainQuestBranch.html#L4) and [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/template/quest/MainQuestSingleRaid.html#L7)

```html
"/magica/resource/image_web/chapter/chapter_<%= chapterId %>_a.png"
"/magica/resource/image_web/chapter/chapter_<%= chapterId %>.png") le
```

## scrape_gacha_banner.py

Based on [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/template/present/GachaHistory.html#L43) and inspection of archivies.

```html
'/magica/resource/image_web/banner/gacha/gachabanner_<%="<%= gachaId %\>"%>_m.png'
```

## scrape_gacha_banner_2

Based on [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/template/present/GachaHistory.html#L36), [these lines](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/template/gacha/GachaTop.html#L9), and inspection of existing archives.

```html
'/magica/resource/image_web/gacha/' + model.gachaSchedule.imageBanner + '_s.png'
"/magica/resource/image_web/gacha/<%='<%= model.imageBanner ? model.imageBanner : "gacha_"+model.id+"_banner" %\>'%>_l.png"
"/magica/resource/image_web/gacha/<%='<%= model.viewParameterMap.IMAGE_DETAIL %\>'%>.png"
"/magica/resource/image_web/gacha/<%='<%= model.imageChara ? model.imageChara : "gacha_"+model.id+"card"
```

Scraper split into two parts for efficiency

### scrape_gacha_banner_2_first_pass.py
### scrape_gacha_banner_2_second_pass.py

Scraped after archive app download deadline of Oct 14 15:00 JST.

## scrape_uwasa_repo.py

Scrape the Uwasa repo for full paths.

Scraped after archive app download deadline of Oct 14 15:00 JST.

## scrape_title_grade.py

Based on [these lines](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/template/user/SetTitlePopup.html#L7) and inspection of existing archives.

```html
"/magica/resource/image_web/common/grade/<%= title.title.baseImage %>.png"
```

Scraped after archive app download deadline of Oct 14 15:00 JST.

## scrape_all_specific_jpg_paths.py

Search through text files in `bella_donna`, `puella-historia`, and `MITaMa` for full jpg paths and download them.

Scraped after archive app download deadline of Oct 14 15:00 JST.

## scrape_branch_event_chara.py

Based on inspection of existing archives. Scrapes files like `magica/resource/image_web/item/event/event_branch_1005_chara_3026.png`. Only checks files associated with branch events.

## scrape_all_event_chara.py

Extended version of `scrape_branch_event_chara.py`, just in case any events other than branch events had chara files in the same format. Did not find any.

## Remaining lines
Lines referencing image_web files that don't have a scraper built from them. The scraper may not work, and this list might not be comprehensive.

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
quest/EventQuest.js:              c.specialQuestObj.useItemImagePath = "/magica/resource/image_web/item/" + (-1 < f.indexOf("EVENT_") ? "event/" : "main/") + f.toLowerCase() + ".png";
campaign/quiz/CampaignQuizTop.js:          a.doc.getElementById("firstClearImg").innerHTML = '<img src="/magica/resource/image_web/item/' + e + "/" + l + '.png">';
campaign/quiz/CampaignQuizTop.js:          a.doc.getElementById("completeClearImg").innerHTML = '<img src="/magica/resource/image_web/item/' + c + "/" + g + '.png">';
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

### Not Investigated
Stuff I didn't get to before the servers went down.

- Stickers
- Announce Chara
- Magirepo
- Event chara assets
- Title text
```
```
