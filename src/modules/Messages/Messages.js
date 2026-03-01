import style from "./Messages.module.css";

export  function UserMes(props) {
	
	
	
	
	
  return (

		<div className={`${style.Smes} ${style.mes}`}>
			<p>{props.Text}</p>
		</div>
  );
}
export  function AiMes(props) {
	
	
	
	
	
  return (

		<div className={`${style.Rmes} ${style.mes}`}>
			<p>{props.Text}</p>
		</div>
  );
}
