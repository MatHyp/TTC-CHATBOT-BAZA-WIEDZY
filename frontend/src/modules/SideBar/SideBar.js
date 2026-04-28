import style from "./SideBar.module.css";
import Burger from "../Burger-icon/Burger.js";
import HealthIcon from "../ServerHealth-Icon/HealthIcon.js";
import { Link, NavLink } from "react-router-dom";
import { useState, useEffect } from "react";
import { db } from "../../db.js";
import { useLiveQuery } from "dexie-react-hooks";
function SideBar({className}) {
  const [showPanel, setShowPanel] = useState(true);
 const chats = useLiveQuery(() => db.chats.toArray(), []) || [];
   
	const changeState = () => {
	  setShowPanel(prev => !prev);
	   console.log(showPanel)
	};
	

	
	
		  return (
			<>
					<Burger DoAfterClick={changeState}  showBurger={false} classCSS={showPanel==true ? style.BurgerAbsolute : style.BurgerMenu}/>
				<div className={`${className} ${showPanel  ? style.sideBarLocal : style.sideBarLocalDezactive }`} >
					<div className={style.Title}>
						<h1>Chat TTC</h1>
						
					</div>
						<ul>
						  <li className={style.MenuItem}>
							<NavLink 
							  to="/c/" 
							  className={({ isActive }) =>`${style.MenuLink} ${isActive ? style.MenuItemActive : ""}`}
							  inert={!showPanel}>
							  New Chat
							</NavLink>
						  </li>
							
						  <li className={style.MenuItem}>
						  
						  </li>
		
						</ul>
										  <div className={style.chatsCointainer}>
						  
							{chats.slice().reverse().map((chat, index) => (
							<NavLink to={`/c/${chat.id}`} className={({ isActive }) =>`${style.MenuLink} ${style.MenuItemActive} ${style.userChat}`} inert={!showPanel}>
										<li key={index}>
											{chat.messages[0].userText}
										</li>
								  
									</NavLink>
							))}
							</div>
						<div className={`${!showPanel ? style.DisplayNone : ""} `}>
					<HealthIcon /></div>
				</div>
		  </>);
}

export default SideBar;
