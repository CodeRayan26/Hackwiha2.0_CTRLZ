
import './App.css'
import './Pages/Sign-up'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Signup from './Pages/Sign-up'
import Login from './Pages/Log-in'
import Landing from './Pages/Landing'
import MainPage from './Pages/MainPage'


function App() {
  return(
    <Router>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/Sign-up" element={<Signup />} />
        <Route path="/Log-in" element={<Login />} />
        <Route path="/MainPage" element={<MainPage />} />

      </Routes>
    </Router>
  )
}

export default App
