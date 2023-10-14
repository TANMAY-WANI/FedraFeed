import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import PgOne from './Pages/PgOne'
const App = () => (
  <Router>
    <Routes>
      <Route path='/' element={<PgOne/>}/>
      {/* <Route exact path='/Home' element={<PgTwo/>}/> */}
    </Routes>
  </Router>

)

export default App