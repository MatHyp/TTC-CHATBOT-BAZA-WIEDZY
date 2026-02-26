import style from "./SideBar.module.css";
import { useState } from "react";
function SideBar({className}) {
	
	const [ShowPanel, setShowPanel] = useState(false);
const changeState = () => {
  setShowPanel(prev => !prev);
};
  return (
	<>
<button onClick={changeState}>test</button>
		<div className={`${className} ${ShowPanel  ? style.sideBarLocal : style.sideBarLocalDezactive }`} >

		</div>
  </>);
}

export default SideBar;
