import Chat from './Pages/Chat/Chat';
import SideBar from './modules/SideBar/SideBar';
import { Routes, Route } from 'react-router-dom';
import style from './main.module.css';

function App() {
	console.log(process.env.REACT_APP_API_KEY)
  return (
    <div className={style.MainDiv}>
      <SideBar className={style.SideBar} />
        <Routes>
		  <Route path="/c/:id?" element={<div className={style.Chat}><Chat /></div>} />
		
          <Route path="/API" element={<div className={style.API}><h1>TU bedzie opisane API czy cos</h1></div>} />
          <Route path="/login" element={<div className={style.Login}><h1>TU bedzie logowanie wpisanie klucza czy czego</h1></div>} />
		  
		</Routes>
    </div>
  );
}

export default App;