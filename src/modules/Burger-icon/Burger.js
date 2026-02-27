import style from "./Burger.module.css";
import { useState } from "react";
function Burger({DoAfterClick}) {
	
	const [BurgerCliked, setBurgerCliked] = useState(false);
const DoAfterClickLocal=()=>
{
	setBurgerCliked(!BurgerCliked);
	DoAfterClick();
};
  return (
	<div className={`${style.Burger} ${BurgerCliked && style.BurgerCliked}`}onClick={DoAfterClickLocal}>
		<div className={style.Burgerline}></div>
		<div className={style.Burgerline}></div>
		<div className={style.Burgerline}></div>
	</div>
  );
}

export default Burger;
