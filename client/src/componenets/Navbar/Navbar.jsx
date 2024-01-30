import React from "react";
import { Link } from "react-router-dom";
import "./Navbar.css"


function Navbar() {
  return <div>
    <nav className="navbar">
        <h1>Blood Donation</h1>
        <Link to='/' className="list">Home</Link>
        <Link to='/list' className="list">List</Link>
        <span onClick={()=>{document.getElementById('login__container').scrollIntoView({behavior:'smooth'})}} className="login">Login</span>
    </nav>
  </div>;
}

export default Navbar;
