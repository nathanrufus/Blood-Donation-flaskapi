import React from "react";
import Navbar from "./componenets/Navbar/Navbar";
import Home from "./componenets/Home/Home";
import List from "./componenets/List/List";
import Login from "./componenets/Login/Login";
import{Route,Routes}from 'react-router-dom'

function App() {
  return <div>
    <Navbar/>
    {/* <Login/> */}
    <Routes>
      <Route path="/" element={<Home/>}/>
      <Route path="/list" element={<List/>}/>
    </Routes>
  </div>;
}

export default App;
