import style from "./SideBar.module.css";
import Burger from "../Burger-icon/Burger.js";
import { useState } from "react";
function SideBar({className}) {
	
	const [ShowPanel, setShowPanel] = useState(false);
const changeState = () => {
  setShowPanel(prev => !prev);
};
  return (
	<>
		
		<div className={`${className} ${ShowPanel  ? style.sideBarLocal : style.sideBarLocalDezactive }`} >
		<div className={style.Title}>
			<h1>TTC Docktor</h1>
			<Burger DoAfterClick={changeState}/>
		</div>
			<ul>
				<li className={`${style.MenuItemActive} `} inerd={ShowPanel}>Home</li>
				<li className={style.MenuItem}>Login</li>
				<li className={style.MenuItem}>Api Info</li>
			</ul>
			
	    </div>
  </>);
}

export default SideBar;
