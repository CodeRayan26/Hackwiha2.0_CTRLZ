
import './App.css'
import './Pages/Sign-up'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Signup from './Pages/Sign-up'
import Login from './Pages/Log-in'

function App() {
  return(
    <Router>
      <Routes>
      <Route path="/" element={<Signup />} />
        <Route path="/Signup" element={<Signup />} />
        <Route path="/Login" element={<Login />} />
      </Routes>
    </Router>
  )
}

export default App
