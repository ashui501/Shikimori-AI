

from nandha import db

db = db['chats']

def set_chat_mode(chat_id: int, mode):
     chat = {'chat_id': chat_id}
     db.update_one(chat,
            {'$set': {'chat': mode}}, upsert=True
                  )
     return True

def get_chats():
    chat_ids = [ chat['chat_id'] for chat in db.find() ]
    if chat_ids is None:
        return []
    else:
        return chat_ids
   
              
def get_chat_mode(chat_id: int):
      chat = {'chat_id': chat_id}
      if not db.find_one(chat):
          set_chat_mode(chat_id, False)
      chat = db.find_one(chat)
      return chat['chat']
      
           

          
  
    
