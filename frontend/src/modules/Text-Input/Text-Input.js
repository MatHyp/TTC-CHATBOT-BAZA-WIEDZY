import style from "./Text-Input.module.css";
import { useState } from "react";
function TextInput(props) {
		
	const [searchText, setSearchText] = useState("");
		
		
	const handleChangeSearch = (e) => {
			setSearchText(e.target.value);
	};
	  
	const handleSend = () => {
	  if (!searchText.trim()) return;
	  props.SendPrompt(searchText);
	  setSearchText("");
	};
	const handleKeyDown = (e) => {
	  if (e.key === "Enter" && !e.shiftKey) {
		e.preventDefault(); // prevent newline
		handleSend();       // use state directly
	  }
	};
		
	  return (
			<div>
				<form>
						
				<textarea
				  className={style.textInput}
				  id="UserInput"
				  placeholder="Search"
				  value={searchText}
				  onChange={handleChangeSearch}
				  onKeyDown={handleKeyDown}  // must be here
				/>
				<button type="button" disabled={!props.EnableSend} onKeyDown={handleKeyDown} onClick={handleSend}className={style.SendPrompt}><i className="icon-paper-plane"></i></button>
				
				</form>
			
			</div>
			
	  );
}

export default TextInput;
