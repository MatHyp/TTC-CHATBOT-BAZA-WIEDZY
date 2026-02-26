import InputText from "./modules/Text-Input/Text-Input.js";
import style from "./chat.module.css";
import { useState } from "react";
function Chat({className}) {
	
	
	
	
	
  return (

		<div className={className}>
			<div className={style.response}>
			
			
			</div>
			<div className={style.promptInput}>
		
				<InputText/>
			</div>
		</div>
  );
}

export default Chat;
