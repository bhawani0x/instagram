import './App.css';
import HomePage from './pages/home';
import { BrowserRouter as Router, Route, Routes} from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Router>
      <div>
        <Routes>
          {/* <Route path="/login" element={<LoginPage/>} />
          <Route path="/creategiveaway" element={<CreateGiveaway/>} /> */}
          <Route path="/" element={<HomePage/>} />
        </Routes>
      </div>
    </Router>
    </div>
  );
}

export default App;
