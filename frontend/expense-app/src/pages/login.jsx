import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

import { LoginAuth } from '../api/login-api';
import './login.css'
import Navbar from "../components/Navbar";

export default function Login() {
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [error, setError] = useState("");
    const navigate = useNavigate();

    useEffect(() => {
        const msg = sessionStorage.getItem("authError");
        
        if (msg){
            setError(msg);
            sessionStorage.removeItem("authError");
        }
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError("");
        try{
            const response = await LoginAuth(username,password)

            if (response?.access_token){
                navigate("/transactions");
            }
            
        } catch (err) {
            if (err.response?.status === 404){
                setError("user not found, pls register to login");
            } else if (err.response?.status === 401){
                setError(err.response?.data.detail);
            }else if((username === "") || (password === "")){
                setError("Enter all fields");
            }else {
                setError("Something went wrong");
            }
        }
    }

    return (
        <>

            <div className="user-form">
                <form onSubmit={handleSubmit}>
                    <label >Username: 
                        <input 
                            type="email"
                            placeholder="Enter Email"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                        />
                    </label>
                    <label>Password: 
                        <input 
                            type="password"
                            placeholder="Password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                    </label>
                    {error && <div style={{backgroundColor:"maroon",color: "white"}}>{error}</div>}
                    <label>
                        <input type="checkbox" /><span>Remember me</span>
                    </label>
                    <button type="submit" >SignIn</button>
                    <button type="submit" onClick={()=> navigate("/register")}>Register</button>
                </form>
            </div>
        </>

    );
}