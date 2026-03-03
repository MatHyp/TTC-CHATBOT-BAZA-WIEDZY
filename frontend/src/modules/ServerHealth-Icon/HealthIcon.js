import style from "./HealthIcon.module.css";
import axios from 'axios';
import {useState, useEffect} from 'react';
function HealthIcon({ForceRefresh}) {



const [data,setData]=useState();
const [loading,setLoading]=useState(true);
useEffect(()=>
{
	ApiTest();
},[]);
const ApiTest=()=>
{
axios.get(
  `https://${process.env.REACT_APP_BASE_URL}/health`,
  {
    headers: {
      "X-API-Key": process.env.REACT_APP_API_KEY
    }
  }
)
	
	
	
	
            .then((response) => {
                setData(0);
                setLoading(false);
            })
            .catch((err) => {
                setData(err.message);
                setLoading(false);
            });
    
}
  return (
		<div className={`${style.StatusIco} ${loading ? style.loading : data === 0 ? style.online: style.offline}`}>
			
		
		</div>
  );
}

export default HealthIcon;