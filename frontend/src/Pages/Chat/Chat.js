import InputText from "./../../modules/Text-Input/Text-Input.js";
import style from "./chat.module.css";
import {UserMes , AiMes} from "../../modules/Messages/Messages";
import { useState, useEffect, useId } from "react";
import {AI} from "../../modules/API-Prompt/POST.js"
import { db } from "../../db.js";
import { useParams, useNavigate  } from 'react-router-dom'



function Chat({className}) {
	const {id}= useParams()
	
		
	const [data, setData] = useState()
	const [loading, setLoading] = useState(true)
	const [chatId, setChatId] = useState(null);

	const [messages, setMessages] = useState([]);
	const navigate = useNavigate();
		useEffect(() => {
		  async function saveChat() {
			if (!messages.length	) return;
			if (!chatId) {
			  const id = await db.chats.add({
				messages
			  });
			  setChatId(id);
			  navigate(`/c/${id}`, { replace: true });
			} 
			else {
			  await db.chats.update(chatId, {
				messages
			  });
			}
		  }
		  saveChat();
		}, [messages]);
useEffect(() => {
  const loadChat = async () => {
    if (id == null) {
      // nowy czat, pusty
	  
      setMessages([]);
      setChatId(null);
      setLoading(false);
      return;
    }
	

    // wczytanie istniejącego chatu z DB
    const chat = await db.chats.get(Number(id));
    if (chat) {
      setMessages(chat.messages || []);
      setChatId(Number(id));
    }
    setLoading(false);
  };

  loadChat();
}, [id]);
	const sortedMessages = [...messages].sort((a, b) => a.date - b.date);	
	
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
			  {/*Wyswietla Prompty i odpowiedzi z messages*/}
			{sortedMessages.map((msg, index) => (
			  <div className={style.test}  key={msg.date}> 
				<UserMes mesDate={msg.date}  Text={msg.userText} AiText={msg.aiResponse} />
				{msg.aiResponse && <AiMes   Text={msg.aiResponse} />}
			  </div>
			))}
		  </div>

		  <div className={style.promptInput} >
			<InputText SendPrompt={SendMess} EnableSend={messages[messages.length - 1]?.aiResponse=="" ?  false : true} />
		  </div>
		</div>
	  );
	}

export default Chat;
