import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import { CreateUser } from "../api/login-api";
import "./login.css";


export default function Register() {
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [res, setRes] = useState("");
    const [err, setError] = useState("");
    const navigate = useNavigate();
 
    const handleSubmit = async (e) => {
        e.preventDefault();
        setError("");
        setRes("");
        if (name.length <= 3){
            setError("name length must be greater than 3");
            return;
        }else if(password.length <= 3){
            setError("Password length must be greater than 3");
            return
        }
        
        try{
            const response = await CreateUser(name, email, password);

            if(response){
                setRes("Registered successfully.")
                setName("");
                setEmail("");
                setPassword("");
            }

        }catch (error){
            setError(error.response.data.detail);
            console.log("Error: ", error);
        }
    }

    return(
        <div className="user-form">
            <form onSubmit={handleSubmit}>
                <label>Name:
                    <input
                    type="text"
                    placeholder="Enter Name"
                    value={name}
                    onChange={(e)=>setName(e.target.value)}
                    />
                </label>
                <label>Email:
                    <input
                    type="email"
                    placeholder="Enter Email"
                    value={email}
                    onChange={(e)=>setEmail(e.target.value)}
                    />
                </label><label>Password:
                    <input
                    type="password"
                    placeholder="Enter Password"
                    value={password}
                    onChange={(e)=>setPassword(e.target.value)}
                    />
                </label>
                {res && <div style={{backgroundColor:"green", color:"white"}}>{res}</div>}
                {err && <div style={{backgroundColor:"maroon", color:"white"}}>{err}</div>}
                <button type="submit">Register</button>
                <button type="reset" onClick={()=> navigate("/")}>Login</button>
            </form>
        </div>
    );
};