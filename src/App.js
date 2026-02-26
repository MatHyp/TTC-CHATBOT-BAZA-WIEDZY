import logo from './logo.svg';
import './App.css';
import Chat  from './Chat.js';
import SideBar  from './modules/SideBar/SideBar.js';
import style from './main.module.css';

function App() {
  return (
		<div>
			<SideBar className={style.SideBar}/>
			<Chat className={style.Chat}/>
		</div>
  );
}

export default App;
