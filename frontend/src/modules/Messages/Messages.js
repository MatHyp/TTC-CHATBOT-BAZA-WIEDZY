import style from "./Messages.module.css";

export  function UserMes(props) {
	
	
		let date=new Date(props.mesDate);


const seconds = String(date.getSeconds()).padStart(2, '0');
const minutes = String(date.getMinutes()).padStart(2, '0');
const hours = String(date.getHours()).padStart(2, '0');
const day = String(date.getDate()).padStart(2, '0');
const month = String(date.getMonth() + 1).padStart(2, '0'); // month is 0-based
const year = date.getFullYear();
	const formatted = `${hours}:${minutes}:${seconds} ${day}/${month}/${year}`;
// Format: HH:MM:SS DD/MM/YYYY

// Output: "00:00:00 01/03/2023"
	
  return (

		<div className={`${style.Smes} ${style.mes} ${style.WFRespond}`}>
			<p>{props.Text}</p>
			<p className={style.mesDate}>{formatted}</p>
		</div>
  );
}
export  function AiMes(props) {
	




  return (

		<div className={`${style.Rmes} ${style.mes}`}>
			<p>{props.Text}</p>
		    <p className={style.mesDate}></p>

		</div>
  );
}
