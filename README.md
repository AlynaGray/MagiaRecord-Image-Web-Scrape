# Magia Record Image_Web Scrape

This is a semi-manual scrape of Magia Record's `magica/resource/image_web` directory for archival. The pattens for scraping are manually constructed by looking at the JS files and patterns in already archived assets in [puella-historia](https://gitlab.com/puella-care/puella-historia) and [bella_donna](https://github.com/LiviaMedeiros/bella_donna).

Although EoS has already occurred, the asset servers are still online. I guess the servers will stay up while the archive app is sitll available to download, which is until October 14, 2024.

Only `scrape_memora.py` and `scrape_tower_buttons.py` were run before EoS. The servers remained up after, but I'm noting this just in case the assets changed after EoS.

Note: Some of the excerpts have their single and double quotes modified to match. Not sure why they don't match in the original.

## scrape_memora.py

Based on [this line](https://github.com/LiviaMedeiros/bella_donna/blob/a5809ede9c8a62442049e96865e8d2b9242033de/magica/js/view/memoria/MemoriaComposeTopUseMaterialView.js#L72)

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

## Remaining lines
Lines referencing image_web files that don't have a scraper built from them yet. The scraper may not work yet, and this list might not be comprehensive

### Unknown formats
Can't find examples of these assets in existing archives.

```
event/dailytower/EventDailyTowerTop.js:              e = b.doc.createElement("img"), e.className = "charaImg", e.src = "/magica/resource/image_web/event/dailytower/" + d.eventId + "/chara/chara_" + a.charaId + ".png", f.el.querySelector(".firstView").appendChild(e), f.el.querySelector(".questTitle").textContent = a.charaTitle
regularEvent/groupBattle/RegularEventGroupBattleSelectUnion.js:        content: "<div id='unionImg'><img src='/magica/resource/image_web/regularEvent/groupBattle/union_logo_0" + c.charaUnionList[this.unionIndex].unionId + ".png'/></div>",
```

### Deferred

Put off due to difficulty
```
event/accomplish/EventAccomplishDeck.js:            f.style.cssText = "background:url('/magica/resource/image_web/common/icon/event/icon_" + l + "_f.png') left top no-repeat; background-size:26px 26px;";
formation/DeckFormation.js:            l.style.cssText = "background:url('/magica/resource/image_web/common/icon/event/icon_" + g + "_f.png') left top no-repeat; background-size:26px 26px;";
quest/EventQuest.js:              c.specialQuestObj.useItemImagePath = "/magica/resource/image_web/item/" + (-1 < f.indexOf("EVENT_") ? "event/" : "main/") + f.toLowerCase() + ".png";
```

### To be investigated
```
quest/puellaHistoria/lastBattle/QuestResultMainBoss.js:          10 > g && (a.doc.getElementById("count").getElementsByClassName("damageNumImg")[f].dataset.num = g, a.doc.getElementById("count").getElementsByClassName("damageNumImg")[f].src = "/magica/resource/image_web/page/quest/puellaHistoria_lastBattle/result/_number/b_num_" + Number(g) + ".png")
campaign/quiz/CampaignQuizTop.js:          a.doc.getElementById("firstClearImg").innerHTML = '<img src="/magica/resource/image_web/item/' + e + "/" + l + '.png">';
campaign/quiz/CampaignQuizTop.js:          a.doc.getElementById("completeClearImg").innerHTML = '<img src="/magica/resource/image_web/item/' + c + "/" + g + '.png">';
view/mission/MissionTopView.js:        c = "/magica/resource/image_web/page/mission/doppelMission/" + f + "01/banner.png";
view/mission/MissionTopView.js:        var c = "/magica/resource/image_web/page/mission/panelMission/" + a.panelMissionList[d].id + "/banner.png",
view/quest/QuestChapterListPartsView.js:        var a = "url(" + ("/magica/resource/image_web/page/quest/main/titleBg/bg_chapter_" + ("HARD" == b.mainQuestMode ? "challenge_" + this.model.chapterId : this.model.chapterId) + ".png") + ") left center no-repeat";
view/quest/QuestResultView.js:            e.src = "/magica/resource/image_web/common/treasure/" + b + "_close.png";
view/quest/QuestResultView.js:              e.src = "/magica/resource/image_web/common/treasure/" + b + "_open.png";
view/quest/QuestResultView.js:            b.src = "/magica/resource/image_web/common/treasure/event/" + a + "_close.png";
view/quest/QuestResultView.js:              b.src = "/magica/resource/image_web/common/treasure/event/" + a + "_open.png";
view/item/ItemImgPartsView.js:      this.model.imagePath && (this.model.imagePath = this.model.nativeimgkey ? "resource/image_native/" + this.model.imagePath + ".png" : "/magica/resource/image_web/" + this.model.imagePath + ".png");
view/gacha/GachaBtnView.js:            -1 !== b.selectablePieceIdList.indexOf(a.pieceId) && (g += "<img src='/magica/resource/image_web/memoria/memoria_" + a.pieceId + "_s.png' width='80'>")
view/shop/ShopTopPartsView.js:          content: "<img class='detailImg' src='/magica/resource/image_web/page/shop/detail/" + this.model.genericId.toLowerCase() + ".png'>",
view/user/GlobalMenuView.js:          l.src = resDir + "/magica/resource/image_web/common/number/" + d[e] + ".png";
view/user/GlobalMenuView.js:            a = "/magica/resource/image_web/page/quest/puellaHistoria_lastBattle/event/" + this.model.toJSON().eventId + "/event_pop.png";
view/user/GlobalMenuView.js:            a = "/magica/resource/image_web/event/" + x[this.model.get("eventType")] + "/" + this.model.toJSON().eventId + "/event_pop.png"
view/user/GlobalMenuView.js:        else this.model.get("regularEventType") ? (this.eventType = this.model.get("regularEventType"), a = "/magica/resource/image_web/common/global/event_pop.png", "ARENARANKMATCH" == this.eventType && (a = "/magica/resource/image_web/event/arenaRankMatch/common/event_pop.png")) : a = "/magica/resource/image_web/regularEvent/groupBattle/common2/event_pop.png";
patrol/PatrolResult.js:            f.src = "/magica/resource/image_web/common/treasure/" + c + "_close.png";
patrol/PatrolResult.js:              d.src = "/magica/resource/image_web/common/treasure/" + c + "_open.png";
patrol/PatrolResult.js:            c.src = "/magica/resource/image_web/common/treasure/event/" + a + "_close.png";
patrol/PatrolResult.js:              c.src = "/magica/resource/image_web/common/treasure/event/" + a + "_open.png";
patrol/PatrolLumpResult.js:            c.src = "/magica/resource/image_web/common/treasure/" + b + "_close.png";
patrol/PatrolLumpResult.js:              d.src = "/magica/resource/image_web/common/treasure/" + b + "_open.png";
patrol/PatrolLumpResult.js:            b.src = "/magica/resource/image_web/common/treasure/event/" + a + "_close.png";
patrol/PatrolLumpResult.js:              b.src = "/magica/resource/image_web/common/treasure/event/" + a + "_open.png";
_common/backboneCommon.js:          d.bgImgPath = "url(/magica/resource/image_web/campaign/drop_up/" + d.campaignId + "/global_icon.png) left top no-repeat";
_common/backboneCommon.js:    return "/magica/resource/image_web/common/icon/" + (c ? b + ".png" : b + "_f.png")
```
