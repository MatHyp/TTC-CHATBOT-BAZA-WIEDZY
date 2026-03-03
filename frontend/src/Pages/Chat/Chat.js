import InputText from "./../../modules/Text-Input/Text-Input.js";
import style from "./chat.module.css";
import {UserMes , AiMes} from "../../modules/Messages/Messages";
import { useState, useEffect, useId } from "react";
import {AI} from "../../modules/API-Prompt/POST.js"
function Chat({className}) {
const [data, setData] = useState()
const [loading, setLoading] = useState(true)
const [messages, setMessages] = useState([
  {
    userText: "Cześć, AI!",
    aiResponse:"",  
    date: new Date().getTime()
  },
    {
    userText: "Cześć, AI!",
    aiResponse: "hello",  
    date: new Date().getTime()
  }
]);

  useEffect(() => {
    const fetchData = async () => {
		if(messages[messages.length - 1].userText!=""){
      try {
        const result = await AI(messages[messages.length - 1]?.userText);
        setData(result);
      } catch (err) {
        console.log(err.message);
      } finally {
        setLoading(false);
      }
    };}

    fetchData();
  }, [messages]); 
  
const sortedMessages = [...messages].sort((a, b) => a.date - b.date);	
const id = useId()
const SendMess = (text) => {
  if (!text.trim()) return; // ignoruj puste wiadomości
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
