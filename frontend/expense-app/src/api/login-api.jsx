import { useState } from "react";
import axios from "axios";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000",
    timeout: 10000,
    headers: {
        "Content-Type": "application/json",
    },
});

api.interceptors.request.use((config) => {
    const token = localStorage.getItem("token");

    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }

    return config;
});

api.interceptors.response.use(
    (response) => response,
    (error) => {
        if(error.response?.status === 401 && localStorage.token){
            localStorage.removeItem("token");

            sessionStorage.setItem(
                "authError",
                "Session expired. Please login again."
            );

            window.location.href = "/";
        }
        return Promise.reject(error);
    }
);

export async function LoginAuth(username, password){

    const formData = new URLSearchParams();
    formData.append("username", username);
    formData.append("password", password);

    try{
        const response = await api.post(
            "/login",
            formData,
            {
                headers:{
                    "Content-Type": "application/x-www-form-urlencoded",
                },
            }
        );
        localStorage.setItem(
            "token", 
            response.data.access_token
        );
        
        return response.data;

    } catch (error) {
        throw error;
        console.log("Error: ", error);
        console.log("Status: ", error.response?.status);
        console.log("Data: ", error.response?.data);
    }
}

export async function CreateUser(name, email, password) {

    const formData = new URLSearchParams();
    formData.append("name", name);
    formData.append("email", email);
    formData.append("password", password);

    try{

        const response = await api.post(
            "/register",
            {name, email, password},
        );

        if (response?.status === 200){
            return (true)
        }

    }catch(error){
        throw error;
    }
}

export { api };
