

import style from "./Text-Input.module.css";
import { useState } from "react";
function TextInput() {
	
  const [searchText, setSearchText] = useState("");
	
	
  const handleChangeSearch = (e) => {
		setSearchText(e.target.value);
  };
	
	
	
	
  return (
		<div>
			<form>
					
        <input
        
          type="text"
          placeholder="Search"
          onChange={handleChangeSearch}
          value={searchText}
        />
			
			</form>
		
		</div>
		
  );
}

export default TextInput;
