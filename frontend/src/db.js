import Dexie from 'dexie';

export const db = new Dexie("ChatDB");
db.version(1).stores({
  chats: "++id,messages"
});