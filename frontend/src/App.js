import './App.css';
import {Routes, Route, Router} from "react-router-dom";
import Dashboard from './pages/Dashboard';
import Authentication from './pages/Authentication';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={< Dashboard />}/>
                <Route path="/login" element={< Authentication />}/>
            </Routes>
        </Router>
    );
}

export default App;
