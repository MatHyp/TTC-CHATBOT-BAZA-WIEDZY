import InputText from "./../../modules/Text-Input/Text-Input.js";
import style from "./chat.module.css";
import {UserMes , AiMes} from "../../modules/Messages/Messages";
import { useState } from "react";
function Chat({className}) {
const [messages, setMessages] = useState([
  {
    userText: "Cześć, AI!",
    aiResponse: "hello",  
    date: new Date().getTime()
  },
    {
    userText: "Cześć, AI!",
    aiResponse: "hello",  
    date: new Date().getTime()
  }
]);
const sortedMessages = [...messages].sort((a, b) => a.date - b.date);	
	
const SendMess = (text) => {
  if (!text.trim()) return; // ignoruj puste wiadomości

  const newMessage = {
    userText: text,        // tekst od użytkownika
    aiResponse: "",        // póki co pusty
    date: Date.now()       // aktualny timestamp
  };

  // dodajemy do stanu
  setMessages(prevMessages => [...prevMessages, newMessage]);
};
  return (
    <div className={className}>
      <div className={style.chatBox}>
		  {/*Wyswietla Prompty i odpowiedzi z messages(6 linijka obecnie)*/}
		{sortedMessages.map((msg, index) => (
		  <> 
			<UserMes key={`user-${index}`} Text={msg.userText} />
			{msg.aiResponse && <AiMes key={`ai-${index}`} Text={msg.aiResponse} />}
		  </>
		))}
      </div>

      <div className={style.promptInput} >
        <InputText SendPrompt={SendMess} />
      </div>
    </div>
  );
}

export default Chat;
