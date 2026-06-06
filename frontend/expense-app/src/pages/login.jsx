import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

import { LoginAuth } from '../api/login-api';
import './login.css'

function loginReq(username, password){
    window.confirm(`do you want to set username to ${username}`)
}

export default function Login() {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault()
        let response = await LoginAuth(username,password)

        if (response?.access_token){
            navigate("/transactions");
        }
    }

    return (
        <div className="login-form">
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
                <button type="submit">Login</button>
            </form>
        </div>
    );
}