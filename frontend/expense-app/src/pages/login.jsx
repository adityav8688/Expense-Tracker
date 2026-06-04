import { useState } from "react";
import axios from "axios";
import './login.css'

function loginReq(username, password){
    window.confirm(`do you want to set username to ${username}`)
}

export default function Login() {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const handleSubmit = (e) => {
        loginReq(username,password)
    }

    return (
        <div className="login-form">
            <form onSubmit={handleSubmit}>
                <label >Username: 
                    <input 
                        type="email"
                        placeholder="Enter email"
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