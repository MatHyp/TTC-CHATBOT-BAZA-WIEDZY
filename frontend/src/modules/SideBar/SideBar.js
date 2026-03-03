import style from "./SideBar.module.css";
import Burger from "../Burger-icon/Burger.js";
import HealthIcon from "../ServerHealth-Icon/HealthIcon.js";
import { Link, NavLink } from "react-router-dom";
import { useState } from "react";
function SideBar({className}) {
  const [showPanel, setShowPanel] = useState(true);
  let showTopBurger
  let showInsideBurger
	showTopBurger = showPanel
	showInsideBurger = !showPanel
   
	const changeState = () => {
	  setShowPanel(prev => !prev);
	   console.log(showPanel)
	};
	
	
	
	
		  return (
			<>
					<Burger DoAfterClick={changeState}   showBurger={showTopBurger} classCSS={style.BurgerMenu}/>
				<div className={`${className} ${showPanel  ? style.sideBarLocal : style.sideBarLocalDezactive }`} >
					<div className={style.Title}>
						<h1>TTC Docktor</h1>
						<div><Burger DoAfterClick={changeState}  showBurger={showInsideBurger} classCSS={style.BurgerAbsolute}/></div>
					</div>
						<ul>
						  <li className={style.MenuItem}>
							<NavLink 
							  to="/" 
							  className={({ isActive }) =>`${style.MenuLink} ${isActive ? style.MenuItemActive : ""}`}
							  inert={!showPanel}>
							  Home
							</NavLink>
						  </li>

						  <li className={style.MenuItem}>
							<NavLink 
							  to="/login" 
							  className={({ isActive }) => `${style.MenuLink} ${isActive ? style.MenuItemActive : ""}`}
							  inert={!showPanel}>
							  Login
							</NavLink>
						  </li>

						  <li className={style.MenuItem}>
							<NavLink 
							  to="/API" 
							  className={({ isActive }) => `${style.MenuLink} ${isActive ? style.MenuItemActive : ""}`}
							  inert={!showPanel}>
							  Api Info
							</NavLink>
						  </li>
						</ul>
						<div className={`${!showPanel ? style.DisplayNone : ""} `}>
					<HealthIcon /></div>
				</div>
		  </>);
}

export default SideBar;
