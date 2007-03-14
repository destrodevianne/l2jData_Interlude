# To Lead and to be led - v0.1 by DrLecter
import sys
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

#CONFIG
DEBUG=1
#ITEMS 
BLOOD,LEG = 8062,8063
#NPCS
PINTER = 30298
#MOBS and DROPS
DROPLIST={20919:[BLOOD,90,10,1,0],
          20920:[BLOOD,90,10,1,0],
          20921:[BLOOD,90,10,1,0],
          20927:[LEG,100,8,7,1]
          }

 
class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self,event,st) :
   htmltext = event
   if event == "30517-02.htm" :
     st.set("cond","1")
     st.setState(PROGRESS)
     st.playSound("ItemSound.quest_accept")
   elif event == "30517-05a.htm" :
     if st.getQuestItemsCount(BLOOD) >= 10 :
         st.takeItems(BLOOD,-1)
         st.set("cond","3");
         st.set("settype","1")
         st.playSound("ItemSound.quest_middle")
     else:
         htmltext = "Incorrect item count"
   elif event == "30517-05b.htm" :
     if st.getQuestItemsCount(BLOOD) >= 10 :
         st.takeItems(BLOOD,-1)
         st.set("cond","4")
         st.set("settype","2")
         st.playSound("ItemSound.quest_middle")
     else:
         htmltext = "Incorrect item count"
   elif event == "30517-05c.htm" :
     if st.getQuestItemsCount(BLOOD) >= 10 :
         st.takeItems(BLOOD,-1)
         st.set("cond","5");
         st.set("settype","3")
         st.playSound("ItemSound.quest_middle") 
     else:
         htmltext = "Incorrect item count"
   elif event == "30517-09.htm" :
     cm_apprentice = st.getPlayer().getClan().getClanMember(st.getPlayer().getApprentice())
     if cm_apprentice.isOnline():
        apprentice = cm_apprentice.getPlayerInstance()
        if apprentice :
           ap_quest=apprentice.getQuestState("118_ToLeadAndBeLed")
           if ap_quest <> None :
              ap_cond=ap_quest.getInt("cond")
              if  ap_cond == 3 :
                 crystals=922
              elif ap_cond in [4,5] :
                 crystals=771
              if st.getQuestItemsCount(1458) >= crystals:
                 st.takeItems(1458,crystals)
                 ap_quest.set("cond","6")
                 st.playSound("ItemSound.quest_middle")
                 ap_quest.playSound("ItemSound.quest_middle")
                 htmltext = "30517-10.htm"
     st.exitQuest(1)
   return htmltext 

 def onTalk (Self,npc,st):
   npcId = npc.getNpcId()
   htmltext = "<html><head><body>I have nothing to say to you</body></html>"
   id = st.getState()
   cond = st.getInt("cond") 
   if id==COMPLETED:
     htmltext = "<html><head><body>This quest have already been completed.</body></html>" 
   elif st.getPlayer().getClan() == None :
     htmltext = "30517-00.htm"
     st.exitQuest(1)
   elif st.getPlayer().getPledgeType() == -1 :
     if st.getPlayer().getLevel() < 19 or not st.getPlayer().getSponsor() :
       htmltext = "30517-00.htm"
       st.exitQuest(1)
     else :
       if id == CREATED :
         htmltext = "30517-01.htm"
       elif cond == 1 :
         htmltext = "30517-03.htm" 
       elif cond == 2 :
         htmltext = "30517-04.htm"
       elif cond == 3 :
         htmltext = "30517-05d.htm"
       elif cond == 4 :
         htmltext = "30517-05e.htm"
       elif cond == 5 :
         htmltext = "30517-05f.htm"
       elif cond == 6 :
         htmltext = "30517-06.htm"
         st.set("cond", "7")
       elif cond == 7 :
         htmltext = "30517-07.htm"
       elif cond == 8 and st.getQuestItemsCount(LEG)==8 :
         settype = st.getInt("settype")
         htmltext = "30517-08.htm"
         st.takeItems(LEG,-1)
         if settype == 1 :
            set = range(7851,7854) #heavy
         elif settype == 2 :
            set = range(7854,7857) #light
         elif settype == 3 :
            set = range(7857,7860) #robe
         for item in [7850]+set:
            st.giveItems(item,1)
         st.unset("cond")
         st.unset("settype")
         st.setState(COMPLETED) 
         st.playSound("ItemSound.quest_finish")
   elif st.getPlayer().getApprentice() :
     cm_apprentice = st.getPlayer().getClan().getClanMember(st.getPlayer().getApprentice())
     if cm_apprentice.isOnline():
        apprentice = cm_apprentice.getPlayerInstance()
        if apprentice :
           ap_quest=apprentice.getQuestState("118_ToLeadAndBeLed")
           if ap_quest <> None :
              ap_cond=ap_quest.getInt("cond")
              if ap_cond == 3 :
                 htmltext = "30517-09a.htm"
              elif ap_cond == 4 :
                 htmltext = "30517-09b.htm"
              elif ap_cond == 5 :
                 htmltext = "30517-09c.htm"
              else :
                 if DEBUG : htmltext = "30517-FF.htm"
                 st.exitQuest(1)
           else :
             if DEBUG: htmltext = "30517-FE.htm"
             st.exitQuest(1)
        else :
          if DEBUG: htmltext = "30517-FD.htm"
          st.exitQuest(1)
     else :
       if DEBUG:htmltext = "30517-FC.htm"
       st.exitQuest(1)
   else :
     if DEBUG:htmltext = "30517-FB.htm"
     st.exitQuest(1)
   return htmltext

 def onKill (Self,npc,st):
    sponsor = st.getPlayer().getSponsor()
    if not sponsor:
      st.exitQuest(1)
      return
    item,chance,max,cond,check = DROPLIST[npc.getNpcId()]
    count,enabled=st.getQuestItemsCount(item),True
    if check :
       enabled=False
       cm_sponsor = st.getPlayer().getClan().getClanMember(st.getPlayer().getSponsor())
       if cm_sponsor.isOnline():
          sponsor = cm_sponsor.getPlayerInstance()
          if sponsor :
            if st.getPlayer().isInsideRadius(sponsor, 1100, 1, 0) :
               enabled=True
    if st.getInt("cond") == cond and count < max and st.getRandom(100) < chance and enabled :
       st.giveItems(item,1)
       if count == max-1:
          st.set("cond",str(cond+1))
          st.playSound("ItemSound.quest_middle")
       else :
          st.playSound("ItemSound.quest_itemget")
    return
     

QUEST     = Quest(118,"118_ToLeadAndBeLed","To Lead And Be Led") 
CREATED   = State('Start',     QUEST) 
PROGRESS  = State('Progress',   QUEST) 
COMPLETED = State('Completed', QUEST) 

QUEST.setInitialState(CREATED)
QUEST.addStartNpc(PINTER) 

CREATED.addTalkId(PINTER)
PROGRESS.addTalkId(PINTER)

for mob in DROPLIST.keys():
    PROGRESS.addKillId(mob)

PROGRESS.addQuestDrop(PINTER,BLOOD,1)
PROGRESS.addQuestDrop(PINTER,LEG,1)

print "importing quests: 118: To Lead And Be Led"