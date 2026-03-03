import InputText from "./../../modules/Text-Input/Text-Input.js";
import style from "./chat.module.css";
import {UserMes , AiMes} from "../../modules/Messages/Messages";
import { useState, useEffect, useId } from "react";
import {AI} from "../../modules/API-Prompt/POST.js"
function Chat({className}) {
const [data, setData] = useState()
const [loading, setLoading] = useState(true)
const [messages, setMessages] = useState([]);



 
  
const sortedMessages = [...messages].sort((a, b) => a.date - b.date);	
const id = useId()
const SendMess = async (text) => {
  if (!text.trim()) return;

  const newMessage = {
    userText: text,
    aiResponse: "",
    date: Date.now()
  };

  // najpierw dodaj wiadomość użytkownika
  setMessages(function(prevMessages) {
    return [...prevMessages, newMessage];
  });

  try {
    setLoading(true);

    const result = await AI(text);

    // teraz ustaw odpowiedź AI do OSTATNIEJ wiadomości
	
	
	setMessages(function(prevMessages) {
	  var newMessages = [...prevMessages];
	  var lastIndex = newMessages.length - 1;
	  newMessages[lastIndex] = {
		...newMessages[lastIndex],
		aiResponse: result.response
	  };
	  return newMessages;
	});
	
	

  } catch (err) {
    console.log(err.message);
  } finally {
    setLoading(false);
  }
};


  return (
    <div className={className}>
      <div  className={style.chatBox}>
		  {/*Wyswietla Prompty i odpowiedzi z messages(6 linijka obecnie)*/}
		{sortedMessages.map((msg, index) => (
		  <> 
			<UserMes mesDate={msg.date} key={id} Text={msg.userText} />
			{msg.aiResponse && <AiMes kkey={id}  Text={msg.aiResponse} />}
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
