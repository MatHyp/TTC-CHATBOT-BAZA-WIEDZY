

import style from "./Text-Input.module.css";
import { useState } from "react";
function TextInput(props) {
	
  const [searchText, setSearchText] = useState("");
	
	
  const handleChangeSearch = (e) => {
		setSearchText(e.target.value);
  };
	
  const handleSend = (e) => {
    e.preventDefault(); // blokuje submit
    if (!searchText.trim()) return;
    props.SendPrompt(searchText); // wywołanie funkcji w Chat.js
    setSearchText("");            // czyszczenie inputa
  };
	
	
  return (
		<div>
			<form>
					
        <input className={style.textInput}
        
          type="text"
          placeholder="Search"
          onChange={handleChangeSearch}
          value={searchText}
        />
		<button onClick={handleSend}className={style.SendPrompt}><i className="icon-paper-plane"></i></button>
			
			</form>
		
		</div>
		
  );
}

export default TextInput;
