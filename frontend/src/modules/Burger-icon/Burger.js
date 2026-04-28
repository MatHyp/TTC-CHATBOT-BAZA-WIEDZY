
import style from "./Burger.module.css";

function Burger({ DoAfterClick, showBurger ,classCSS }) {
  return (
    <div
      className={`${style.Burger} ${showBurger && style.ItemDisplayNone} ${classCSS}`}
      onClick={DoAfterClick}
    >
      <div className={style.Burgerline}></div>
      <div className={style.Burgerline}></div>
      <div className={style.Burgerline}></div>
    </div>
  );
}

export default Burger;